# Bilder – Ihre Fotos, Gesichter und Personen

Hier gibt es die **Bilder-App** zum Herunterladen, und hier können Sie uns **Fehler und
Wünsche** melden. Zu jedem Anliegen bekommen Sie eine **Testversion**, die Sie selbst
ausprobieren können, bevor die Änderung in die nächste Version kommt.

**Neu hier?** → **[Erste Schritte](ERSTE-SCHRITTE.md)** – in einer Viertelstunde startklar.

## Was ist Bilder?

**Bilder** bringt Ordnung in große Fotosammlungen: Die App findet auf Ihren Fotos die
Gesichter, lernt, wer wer ist, und zeigt Ihnen auf Knopfdruck alle Bilder einer Person.
Haben Sie früher mit **Picasa** Personen markiert, wird diese Arbeit in wenigen Minuten
übernommen.

Die App läuft komplett **auf Ihrem PC** – ohne Konto, ohne Cloud, ohne Installation.
Sie bedienen sie im Browser, Ihre Fotos werden dabei **nur gelesen** und nie verändert,
verschoben oder hochgeladen.

### Das kann die App

- 🙂 **Gesichtserkennung** – findet alle Gesichter auf Ihren Fotos, auch auf älteren und
  kleinen Bildern.
- 👪 **Personen benennen** – Namen vergeben, einzeln oder viele ähnliche Gesichter auf einmal.
  Jeder Name verbessert die nächsten Vorschläge.
- 💡 **Automatische Vorschläge** – die App erkennt bekannte Personen selbst wieder; Sie
  bestätigen oder lehnen mit einem Klick ab.
- 🗂️ **Picasa-Übernahme** – Personen und Gesichtsmarkierungen aus Picasa werden übernommen,
  Picasa muss dafür nicht mehr installiert sein.
- 🔎 **Suchen und filtern** – nach Person, Ordner, Dateiname, WhatsApp-Bildern; sortiert nach
  Aufnahmedatum.
- 📷 **Bilddetails** – Aufnahmedatum, Kamera und Ort (GPS); auch HEIC-Fotos vom iPhone und
  WhatsApp-Bilder ohne Datum werden richtig eingeordnet.
- 🧩 **Duplikate finden** – zeigt doppelte Fotos (z. B. Original und WhatsApp-Kopie), ohne
  etwas zu löschen.
- 📁 **Mehrere Fotoordner** – lokale Festplatte, USB-Platte oder NAS; zieht ein Ordner um,
  bleiben alle Namen erhalten.
- ⏸️ **Fortsetzbar** – große Sammlungen werden nebenbei eingelesen; Anhalten und später
  weitermachen ist jederzeit möglich.
- 🔒 **Privat** – alles bleibt auf Ihrem PC, Ihre Arbeit steckt im Ordner `Data` neben der App.

## ⬇️ Herunterladen

**[Neueste Version herunterladen](https://github.com/tripledewey-ctrl/bilder-releases/releases/latest)**
→ dort unter *Assets* auf **`Bilder-….zip`** klicken.

Die ZIP enthält dieselbe App wie die `.exe` daneben – sie lässt sich aber auch laden, wenn
Edge oder Windows den Download einer `.exe` sperren.

| Was | Wo | Für wen |
| --- | --- | --- |
| **Version** (z. B. `0.2.0`) | [Releases](https://github.com/tripledewey-ctrl/bilder-releases/releases/latest), Markierung „Latest“ | alle – für den Alltag |
| **Vorabversion** (z. B. `0.2.0-rc.1`) | [Releases](https://github.com/tripledewey-ctrl/bilder-releases/releases), Markierung „Pre-release“ | wer die nächste Version vorab prüfen möchte |
| **Testversion zu einem Anliegen** | als Kommentar direkt in Ihrem [Anliegen](https://github.com/tripledewey-ctrl/bilder-releases/issues) | wer das Anliegen gemeldet hat |

## Erste Installation

1. `Bilder-….zip` herunterladen (siehe oben).
2. Rechtsklick auf die ZIP → **Eigenschaften** → unten bei *Sicherheit* **„Zulassen“** anhaken
   → **OK**. Gibt es das Häkchen nicht, ist nichts zu tun.
3. Rechtsklick auf die ZIP → **Alle extrahieren…** → als Ziel z. B. `C:\` wählen.
   Es entsteht der Ordner `C:\Bilder` mit `Bilder.exe` und `LIESMICH.txt`.
4. Doppelklick auf **`Bilder.exe`**. Der Browser öffnet sich mit der App.
5. Meldet Windows *„Der Computer wurde geschützt“*: **Weitere Informationen → Trotzdem ausführen**.
   Das kommt, weil die Datei neu ist – nicht, weil etwas damit nicht stimmt.

### Der Download wird blockiert?

**Edge** zeigt bei neuen Programmen oft *„… wird nicht häufig heruntergeladen“* oder
*„… wurde blockiert“*:

1. Oben rechts das Download-Fenster öffnen (Pfeil-Symbol oder `Strg`+`J`).
2. Mit der Maus auf die Datei → auf **„…“** (Weitere Aktionen) klicken → **Behalten**.
3. Fragt Edge noch einmal nach: **Mehr anzeigen → Trotzdem behalten**.

**Windows** löscht die Datei gleich wieder oder meldet eine Bedrohung? Dann bitte nicht
selbst den Virenschutz abschalten, sondern ein [Anliegen](https://github.com/tripledewey-ctrl/bilder-releases/issues/new/choose)
melden – wir kümmern uns darum.

Die App legt neben sich einen Ordner **`Data`** an. Dort stehen Ihre Einstellungen und alles,
was Sie benannt haben – **diesen Ordner nie löschen**.

## Aktualisieren

1. App schließen (Konsolenfenster schließen).
2. Sicherheitshalber den Ordner **`Data`** kopieren, z. B. auf einen USB-Stick.
3. Die neue ZIP laden, wie oben **„Zulassen“** anhaken und entpacken. Dann die alte
   `Bilder.exe` durch die neue ersetzen. `Data` bleibt, wo er ist.
4. Starten – oben neben „Bilder“ steht die neue Version.

Zurück zur alten Version: einfach die alte `Bilder.exe` wieder hinlegen. Alle früheren Versionen
gibt es weiter unter [Releases](https://github.com/tripledewey-ctrl/bilder-releases/releases).

## 💬 Fehler oder Wunsch melden

Sie brauchen dafür ein kostenloses [GitHub-Konto](https://github.com/signup).

1. **[Neues Anliegen](https://github.com/tripledewey-ctrl/bilder-releases/issues/new/choose)** öffnen
   und *Etwas funktioniert nicht* oder *Wunsch oder Verbesserung* wählen.
2. Ausfüllen und absenden. Sie bekommen sofort eine Bestätigung.
3. Sobald es eine **Testversion** gibt, erscheint sie im Anliegen als Kommentar mit Download –
   GitHub schickt Ihnen dazu eine E-Mail.
4. **Testversion ausprobieren** – die ZIP am besten in einen **eigenen, leeren Ordner**
   entpacken (z. B. `C:\Bilder-Test`), damit Ihre gewohnte App unberührt bleibt.
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

Neben jeder `.exe` liegt eine `.sha256`-Datei. Sie gilt für die `.exe` – auch für die
`Bilder.exe` aus der ZIP. In PowerShell:

```powershell
Get-FileHash .\Bilder-0.2.0.exe -Algorithm SHA256
```

Der angezeigte Wert muss mit dem in der `.sha256`-Datei übereinstimmen.

---

<sub>Der Quellcode wird privat entwickelt. Dieses Repository enthält nur die fertigen Programme
und die Kundenanliegen. Hinweise für die Betreuung: [BETRIEB.md](BETRIEB.md).</sub>
