# Betrieb: Kunden-Repo ↔ Entwicklung

Dieses öffentliche Repo ist die Kundenseite der Bilder-App. Entwickelt wird im privaten Repo
`tripledewey-ctrl/bilder`. Beide sind über Workflows und einen Token verbunden.

## Ablauf

```text
Kunde: Anliegen #7 (bilder-releases)
  └─ anliegen.yml ──► internes Issue #23 (bilder) mit Zeile "Kunden-Issue: …#7", Label "kunde"
                        └─ issue-branch.yml ──► Branch fix/23-… bzw. feature/23-…
Entwickler: Push auf den Branch
  └─ ci.yml: Tests → exe → Job "Testversion für Kunden"
        └─ Release "test-issue-7" (Pre-release, Datei wird bei jedem Push ersetzt)
        └─ Kommentar mit Download in #7, Label "bitte-testen"
Kunde: "/ok" oder "/fehler"
  └─ rueckmeldung.yml ──► Label + Kommentar im internen Issue #23
Pull Request "Closes #23" → Squash and merge
  └─ kunden-status.yml ──► #7 bekommt "behoben" + Hinweis
Release-Lauf (bilder, Kanal rc/stable)
  └─ release.yml ──► gleiches Release hier (rc = Pre-release, stable = Latest)
        stable: alle offenen "behoben"-Anliegen bekommen Download-Link und werden geschlossen
```

Feature-Vorabversionen und CI-Builds bleiben intern. Ein Branch ohne Kunden-Issue erzeugt
hier nichts.

Ein eigenes internes Issue nachträglich einem Kunden-Anliegen zuordnen: in seine Beschreibung
(oder in die des Pull Requests) die Zeile `Kunden-Issue: #7` schreiben.

## Windows-Build hier (kostenlose Minuten)

Die exe wird **hier** gebaut (`.github/workflows/build.yml`), weil Actions-Minuten für
öffentliche Repos nichts kosten. Das private Repo testet nur unter Linux und stößt den Build
per `repository_dispatch` an:

```text
privat ci.yml/release.yml ──"bauen"──► build.yml: privaten Stand holen (KUNDEN_TOKEN),
  exe bauen + starten, Artefakt (14 bzw. 30 Tage) ─► Testversion / Releases ─"exe-gebaut"─► privat
```

- Auslösen kann ihn nur, wer Schreibrechte hat – also nur das private Repo.
- Lauf-Logs und exe-Artefakte sind öffentlich bzw. für angemeldete Nutzer sichtbar; der
  Quellcode wird nicht veröffentlicht.
- Läufe: *Actions → Windows-Build*, Titel `Bilder <Version> · <Commit>`.

## Einrichtung (einmalig)

### 1. Token anlegen

GitHub → *Settings → Developer settings → Fine-grained personal access tokens → Generate new token*

| Feld | Wert |
| --- | --- |
| Name | `bilder-kunden` |
| Expiration | 1 Jahr (Erinnerung setzen!) |
| Repository access | *Only select repositories*: `bilder` **und** `bilder-releases` |
| Permissions → Contents | Read and write (Quellcode holen, Releases, Build anstoßen) |
| Permissions → Issues | Read and write |

### 2. Token in **beiden** Repos hinterlegen

*Settings → Secrets and variables → Actions → New repository secret*

- Name: `KUNDEN_TOKEN`, Wert: der Token
- einmal in `bilder`, einmal in `bilder-releases`

Ohne Token läuft alles weiter wie bisher, nur ohne Brücke (die Läufe melden einen Hinweis).

### 3. Optional: nur bestimmte Kunden

In `bilder-releases` unter *Settings → Secrets and variables → Actions → Variables*:

| Variable | Wert | Wirkung |
| --- | --- | --- |
| `KUNDEN` | `kunde1,kunde2` (GitHub-Namen) | nur deren Anliegen werden sofort aufgenommen; alle anderen bekommen `pruefen`. Label `aufnehmen` übernimmt ein solches Anliegen nachträglich. |
| `INTERN_REPO` | `tripledewey-ctrl/bilder` | nur nötig, wenn das private Repo umzieht |

In `bilder` entsprechend `KUNDEN_REPO`, falls dieses Repo umzieht.

### 4. Empfohlene Einstellungen hier

- *Settings → General → Features*: **Issues** an, Wiki/Projects/Discussions nach Bedarf aus.
- *Settings → Moderation options → Interaction limits*: bei Spam vorübergehend auf
  „Prior contributors“ begrenzen.
- Benachrichtigungen: oben **Watch → All Activity**, damit Sie jede Kundenantwort sehen.

## Aufräumen

Die Releases `test-issue-<nr>` bleiben nach dem Schließen eines Anliegens stehen. Ab und zu
unter *Releases* löschen (Release **und** Tag), wenn das Anliegen erledigt ist.
