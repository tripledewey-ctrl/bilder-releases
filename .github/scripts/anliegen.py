"""Kunden-Anliegen im öffentlichen Repo verarbeiten (Workflows anliegen.yml, rueckmeldung.yml).

    python anliegen.py aufnehmen     neues Issue -> internes Issue im privaten Entwicklungs-Repo
                                     (dort entsteht automatisch der Branch, jeder Push darauf
                                     liefert eine Testversion zurück in dieses Issue)
    python anliegen.py rueckmeldung  Kommentar "/ok" oder "/fehler" -> Label setzen und das
                                     interne Issue benachrichtigen

Umgebung: GITHUB_TOKEN (dieses Repo), KUNDEN_TOKEN (Token mit Zugriff auf das private Repo;
fehlt er, wird nur hier kommentiert), INTERN_REPO, KUNDEN (Komma-Liste erlaubter
GitHub-Namen; leer = alle), GITHUB_REPOSITORY, ISSUE_NUMBER, ISSUE_TITLE, ISSUE_BODY,
ISSUE_AUTHOR, ISSUE_LABELS, REPO_OWNER, COMMENT_BODY, COMMENT_AUTHOR, COMMENT_URL.
Alle Nutzertexte kommen über Umgebungsvariablen und werden nie als Befehl ausgeführt.

Nur Standardbibliothek.
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.github.com"
DEFAULT_INTERN = "tripledewey-ctrl/bilder"
MARKER = "<!-- bilder-intern:{n} -->"
MARKER_RE = re.compile(r"<!-- bilder-intern:(\d+) -->")
LABEL_INTERN = {"fehler": "bug", "wunsch": "enhancement"}
MAX_BODY = 60000


def env(key: str, default: str = "") -> str:
    return os.environ.get(key) or default


def summary(text: str) -> None:
    print(text)
    if path := env("GITHUB_STEP_SUMMARY"):
        with open(path, "a", encoding="utf-8") as fh:
            fh.write(text + "\n")


def call(token: str, method: str, path: str, data=None):
    req = urllib.request.Request(
        API + path, method=method,
        data=None if data is None else json.dumps(data).encode(),
        headers={"Authorization": f"Bearer {token}",
                 "Accept": "application/vnd.github+json",
                 "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        out = r.read()
        return json.loads(out) if out else None


def comments(token: str, repo: str, n: int) -> list[dict]:
    return call(token, "GET", f"/repos/{repo}/issues/{n}/comments?per_page=100")


def intern_nummer(token: str, repo: str, n: int) -> int | None:
    for c in comments(token, repo, n):
        if m := MARKER_RE.search(c.get("body") or ""):
            return int(m.group(1))
    return None


def erlaubt(user: str) -> bool:
    liste = {x.strip().lower() for x in env("KUNDEN").split(",") if x.strip()}
    return not liste or user.lower() in liste or user.lower() == env("REPO_OWNER").lower()


def cmd_aufnehmen() -> int:
    gh, pat = env("GITHUB_TOKEN"), env("KUNDEN_TOKEN")
    repo, intern = env("GITHUB_REPOSITORY"), env("INTERN_REPO", DEFAULT_INTERN)
    n, autor = int(env("ISSUE_NUMBER")), env("ISSUE_AUTHOR")
    labels = {x.strip().lower() for x in env("ISSUE_LABELS").split(",") if x.strip()}

    if intern_nummer(gh, repo, n):
        print("Schon aufgenommen.")
        return 0
    if "aufnehmen" not in labels and not erlaubt(autor):
        call(gh, "POST", f"/repos/{repo}/issues/{n}/comments", {"body": (
            "Vielen Dank für Ihre Nachricht! Wir schauen sie uns an und melden uns hier.")})
        call(gh, "POST", f"/repos/{repo}/issues/{n}/labels", {"labels": ["pruefen"]})
        summary(f"#{n} von @{autor}: nicht in der Kundenliste – Label `pruefen`.")
        return 0
    if not pat:
        print("::warning::Secret KUNDEN_TOKEN fehlt – Anliegen wird nicht weitergegeben.")
        return 0

    url = f"{env('GITHUB_SERVER_URL', 'https://github.com')}/{repo}/issues/{n}"
    body = (f"Kunden-Issue: {repo}#{n}\n"
            f"Gemeldet von @{autor} · {url}\n\n---\n\n" + env("ISSUE_BODY"))[:MAX_BODY]
    neu = call(pat, "POST", f"/repos/{intern}/issues", {
        "title": env("ISSUE_TITLE")[:200] or f"Kunden-Anliegen #{n}",
        "body": body,
        "labels": sorted({LABEL_INTERN[x] for x in labels if x in LABEL_INTERN} | {"kunde"}),
    })
    text = (
        MARKER.format(n=neu["number"]) + "\n"
        "Vielen Dank! Ihr Anliegen ist bei uns angekommen und in Arbeit.\n\n"
        "Sobald es eine **Testversion** gibt, erscheint sie hier als Kommentar mit "
        "Download-Link. Sie bekommen dazu eine Benachrichtigung von GitHub."
    )
    call(gh, "POST", f"/repos/{repo}/issues/{n}/comments", {"body": text})
    call(gh, "POST", f"/repos/{repo}/issues/{n}/labels", {"labels": ["in-arbeit"]})
    try:
        call(gh, "DELETE", f"/repos/{repo}/issues/{n}/labels/pruefen")
    except urllib.error.HTTPError:
        pass
    summary(f"#{n} aufgenommen als {intern}#{neu['number']}.")
    return 0


def cmd_rueckmeldung() -> int:
    gh, pat = env("GITHUB_TOKEN"), env("KUNDEN_TOKEN")
    repo, intern = env("GITHUB_REPOSITORY"), env("INTERN_REPO", DEFAULT_INTERN)
    n = int(env("ISSUE_NUMBER"))
    wer, text = env("COMMENT_AUTHOR"), env("COMMENT_BODY").strip()
    erste = text.splitlines()[0].strip().lower() if text else ""

    if wer.lower() not in {env("ISSUE_AUTHOR").lower(), env("REPO_OWNER").lower()}:
        print("Rückmeldung zählt nur vom Verfasser des Anliegens.")
        return 0
    if erste.startswith("/ok"):
        neu, alt, wort = "getestet-ok", "getestet-fehler", "✅ funktioniert"
    elif erste.startswith("/fehler"):
        neu, alt, wort = "getestet-fehler", "getestet-ok", "❌ stimmt noch nicht"
    else:
        print("Kein /ok oder /fehler – nichts zu tun.")
        return 0

    call(gh, "POST", f"/repos/{repo}/issues/{n}/labels", {"labels": [neu]})
    for name in (alt, "bitte-testen"):
        try:
            call(gh, "DELETE", f"/repos/{repo}/issues/{n}/labels/{urllib.parse.quote(name)}")
        except urllib.error.HTTPError:
            pass
    call(gh, "POST", f"/repos/{repo}/issues/{n}/comments",
         {"body": "Danke für die Rückmeldung! 👍" if neu == "getestet-ok" else
          "Danke – wir schauen uns das an und melden uns mit einer neuen Testversion."})

    nr = intern_nummer(gh, repo, n)
    if pat and nr:
        call(pat, "POST", f"/repos/{intern}/issues/{nr}/comments", {"body": (
            f"**Kunde:** {wort} – [Rückmeldung]({env('COMMENT_URL')})")})
    summary(f"#{n}: Label `{neu}`" + (f", {intern}#{nr} benachrichtigt" if pat and nr else ""))
    return 0


if __name__ == "__main__":
    match sys.argv[1:]:
        case ["aufnehmen"]:
            sys.exit(cmd_aufnehmen())
        case ["rueckmeldung"]:
            sys.exit(cmd_rueckmeldung())
    print(__doc__)
    sys.exit(1)
