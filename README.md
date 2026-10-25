# Bilder – Ihre Fotos, Gesichter und Personen

Hier gibt es die **Bilder-App** zum Herunterladen, und hier können Sie uns **Fehler und
Wünsche** melden. Zu jedem Anliegen bekommen Sie eine **Testversion**, die Sie selbst
ausprobieren können, bevor die Änderung in die nächste Version kommt.

## ⬇️ Herunterladen

**[Neueste Version herunterladen](https://github.com/tripledewey-ctrl/bilder-releases/releases/latest)**
→ dort unter *Assets* auf `Bilder-….exe` klicken.

| Was | Wo | Für wen |
| --- | --- | --- |
| **Version** (z. B. `0.2.0`) | [Releases](https://github.com/tripledewey-ctrl/bilder-releases/releases/latest), Markierung „Latest“ | alle – für den Alltag |
| **Vorabversion** (z. B. `0.2.0-rc.1`) | [Releases](https://github.com/tripledewey-ctrl/bilder-releases/releases), Markierung „Pre-release“ | wer die nächste Version vorab prüfen möchte |
| **Testversion zu einem Anliegen** | als Kommentar direkt in Ihrem [Anliegen](https://github.com/tripledewey-ctrl/bilder-releases/issues) | wer das Anliegen gemeldet hat |

## Erste Installation

1. Einen Ordner anlegen, z. B. `C:\Bilder-App`.
2. Die heruntergeladene `Bilder-….exe` hineinlegen (gern in `Bilder.exe` umbenennen).
3. Doppelklick zum Starten. Der Browser öffnet sich mit der App.
4. Meldet Windows *„Der Computer wurde geschützt“*: **Weitere Informationen → Trotzdem ausführen**.
   Das kommt, weil die Datei neu ist – nicht, weil etwas damit nicht stimmt.

Die App legt neben sich einen Ordner **`Data`** an. Dort stehen Ihre Einstellungen und alles,
was Sie benannt haben – **diesen Ordner nie löschen**.

## Aktualisieren

1. App schließen (Konsolenfenster schließen).
2. Sicherheitshalber den Ordner **`Data`** kopieren, z. B. auf einen USB-Stick.
3. Die alte `Bilder.exe` durch die neue ersetzen. `Data` bleibt, wo er ist.
4. Starten – oben neben „Bilder“ steht die neue Version.

Zurück zur alten Version: einfach die alte `.exe` wieder hinlegen. Alle früheren Versionen
gibt es weiter unter [Releases](https://github.com/tripledewey-ctrl/bilder-releases/releases).

## 💬 Fehler oder Wunsch melden

Sie brauchen dafür ein kostenloses [GitHub-Konto](https://github.com/signup).

1. **[Neues Anliegen](https://github.com/tripledewey-ctrl/bilder-releases/issues/new/choose)** öffnen
   und *Etwas funktioniert nicht* oder *Wunsch oder Verbesserung* wählen.
2. Ausfüllen und absenden. Sie bekommen sofort eine Bestätigung.
3. Sobald es eine **Testversion** gibt, erscheint sie im Anliegen als Kommentar mit Download –
   GitHub schickt Ihnen dazu eine E-Mail.
4. **Testversion ausprobieren** – am besten in einem **eigenen, leeren Ordner** (z. B.
   `C:\Bilder-Test`), damit Ihre gewohnte App unberührt bleibt.
5. **Antworten Sie im Anliegen** mit
   - `/ok` – funktioniert so, wie gewünscht, oder
   - `/fehler` – stimmt noch nicht (gern mit ein paar Sätzen dazu).
6. Ist alles fertig, kommt die Änderung in die nächste Version. Dann melden wir uns ein letztes
   Mal im Anliegen und schließen es.

> **Bitte beachten:** Anliegen sind **öffentlich sichtbar**. Schreiben Sie keine echten Namen,
> keine Fotos von Personen und keine Dateinamen aus Ihrer Sammlung hinein – Platzhalter wie
> „Erika Mustermann“ reichen.

### Was die Markierungen bedeuten

| Markierung | Bedeutung |
| --- | --- |
| `in-arbeit` | angekommen, wir kümmern uns |
| `bitte-testen` | eine Testversion wartet auf Ihre Rückmeldung |
| `getestet-ok` / `getestet-fehler` | Ihre Rückmeldung |
| `behoben` | fertig, kommt mit der nächsten Version |
| `nicht-geplant` | wird vorerst nicht umgesetzt |

## Prüfsumme (für Vorsichtige)

Neben jeder `.exe` liegt eine `.sha256`-Datei. In PowerShell:

```powershell
Get-FileHash .\Bilder-0.2.0.exe -Algorithm SHA256
```

Der angezeigte Wert muss mit dem in der `.sha256`-Datei übereinstimmen.

---

<sub>Der Quellcode wird privat entwickelt. Dieses Repository enthält nur die fertigen Programme
und die Kundenanliegen. Hinweise für die Betreuung: [BETRIEB.md](BETRIEB.md).</sub>
