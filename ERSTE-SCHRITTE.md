# Erste Schritte mit Bilder

In etwa einer Viertelstunde läuft die App, Ihr Fotoordner ist eingetragen und – falls Sie
früher Picasa benutzt haben – sind alle dort benannten Personen schon da.

> **Gut zu wissen:** Bilder liest Ihre Fotos **nur**. Es wird nichts verschoben, umbenannt,
> gelöscht oder hochgeladen. Alles bleibt auf Ihrem PC.

## 1. Herunterladen und entpacken

1. Die neueste Version laden: **[Releases](https://github.com/tripledewey-ctrl/bilder-releases/releases)**
   → unter *Assets* auf **`Bilder-….zip`** klicken.
2. Rechtsklick auf die ZIP → **Eigenschaften** → unten bei *Sicherheit* **„Zulassen“**
   anhaken → **OK**.
3. Rechtsklick auf die ZIP → **Alle extrahieren…** → Ziel z. B. `C:\`.
   Es entsteht der Ordner `C:\Bilder`.

Sperrt Edge oder Windows den Download? Die Lösung steht in der
[Anleitung auf der Startseite](README.md#der-download-wird-blockiert).

## 2. Starten

Doppelklick auf **`Bilder.exe`**. Es öffnet sich ein schwarzes Fenster und kurz danach Ihr
Browser mit der App (Adresse `http://127.0.0.1:8000`).

- Meldet Windows *„Der Computer wurde geschützt“*: **Weitere Informationen → Trotzdem ausführen**.
- Das schwarze Fenster **offen lassen** – solange es da ist, läuft die App.
  **Beenden:** das Fenster schließen.
- Browser-Tab aus Versehen geschlossen? Einfach noch einmal auf `Bilder.exe` doppelklicken –
  die App startet nicht doppelt, es öffnet sich nur wieder der Browser.

Tipp: Rechtsklick auf `Bilder.exe` → **Senden an → Desktop (Verknüpfung erstellen)**.

## 3. Erkennungsmodelle laden (nur beim ersten Mal)

Oben auf **Config & Scans** → Abschnitt **2 · Voraussetzungen**.

Fehlen die Modelle für die Gesichtserkennung, auf **Modelle herunterladen (~275 MB)** klicken
und warten, bis oben rechts „fertig“ steht. Danach sollte überall **OK** stehen.

## 4. Fotoordner eintragen

**Config & Scans → 1 · Bildordner → Ordner hinzufügen**

1. Auf **Durchsuchen …** klicken, zu Ihrem Fotoordner gehen und **Diesen Ordner wählen**
   (oder den Pfad eintippen, z. B. `C:\Users\<Name>\Pictures`).
2. **Prüfen** – die App zählt Bilder und zeigt, ob es Picasa-Daten gibt, z. B.
   `6284 Bilder in 18 Ordnern · 52 Gesichter auf 39 Bildern` und darunter die Namen aus Picasa.
3. **Hinzufügen.**

Unterordner werden automatisch mit durchsucht. Weitere Ordner (zweite Festplatte, USB-Platte,
NAS) fügen Sie genauso hinzu.

## 5. Bilder einlesen

**Config & Scans → 3 · Scans ausführen**

| Sie haben früher Picasa benutzt | Sie haben kein Picasa |
| --- | --- |
| Zuerst **⚡ Picasa schnell** – übernimmt in wenigen Minuten alle Personen, die Sie in Picasa benannt haben. Danach **▶ Alles ausführen**. | Gleich **▶ Alles ausführen**. |

**▶ Alles ausführen** sieht sich jedes Bild an und sucht Gesichter. Das dauert etwa
**2 Sekunden pro Bild** – bei 6000 Bildern also einige Stunden. Am besten abends starten und
über Nacht laufen lassen.

- Den Fortschritt sehen Sie oben rechts auf jeder Seite.
- Sie können währenddessen ganz normal in der App weiterarbeiten.
- **■ Stoppen** hält an. Beim nächsten Start macht die App dort weiter, wo sie aufgehört hat.

## 6. Personen benennen

Jetzt beginnt der schöne Teil.

1. Oben auf **Gesichter** → Reiter **Unbekannt**.
2. Ein Gesicht anhaken, oben den Namen eintippen (z. B. `Erika Mustermann`) → **Zuordnen**.
   Gibt es die Person noch nicht, wird sie automatisch angelegt.
3. Mit **≈** an einem Gesicht zeigt die App die **ähnlichsten** Gesichter. Die passenden
   anhaken, Namen eintragen, **Zuordnen** – so benennen Sie Dutzende Fotos auf einmal.
4. Danach unter **Config & Scans → Personen zuordnen** starten: Die App macht jetzt selbst
   Vorschläge für alle übrigen Fotos.
5. Unter **Personen** → Name → **Vorschläge** prüfen: **✓** passt, **✗** passt nicht.
   Was Sie ablehnen, schlägt die App für dieses Gesicht nie wieder vor.

Jeder Name, den Sie vergeben, macht die nächsten Vorschläge besser.

## 7. Stöbern

- **Personen** – alle Personen mit ihren Fotos; ein Klick zeigt alle Bilder dieser Person.
- **Bilder** – suchen nach Ordner oder Dateiname, filtern nach Person, WhatsApp-Bildern
  oder Picasa-Markierung, sortieren nach Datum.
- Ein Klick auf ein Bild zeigt die erkannten Gesichter, Aufnahmedatum, Kamera und Ort –
  und **Original öffnen** zeigt das Foto in voller Größe.
- **Duplikate** – findet doppelte Fotos (z. B. Original und WhatsApp-Kopie). Es wird nichts
  gelöscht, Sie sehen nur, wo die Doppel liegen.

## 8. Ihre Arbeit sichern

Alles, was Sie in der App benannt und eingestellt haben, steht im Ordner **`Data`** neben
`Bilder.exe`.

- **Diesen Ordner nie löschen.**
- Ab und zu sichern: **App schließen** (schwarzes Fenster zu), dann den ganzen Ordner `Data`
  auf einen USB-Stick oder eine externe Festplatte kopieren.
- Ihre Fotos selbst sichern Sie wie bisher – die App verändert sie nicht.

## Häufige Fragen

**Die App findet eine Person nicht zuverlässig.**
Benennen Sie ein paar Gesichter dieser Person von Hand – am besten aus verschiedenen Jahren.
Gerade bei Kindern hilft das sehr. Kleine Gesichter (z. B. aus WhatsApp) sind schwieriger;
die stehen in einem eigenen Reiter **Gesichter → Klein (WhatsApp)**.

**Die App schlägt oft falsche Personen vor.**
Unter **Config & Scans → 4 · Einstellungen** die **Schwelle** etwas erhöhen (z. B. von
`0,45` auf `0,55`) und **Speichern & neu zuordnen**.

**Dieselbe Person steht zweimal da** (z. B. „Erika“ und „Erika M.“).
**Personen** → eine davon öffnen → **Umbenennen / zusammenführen** → den anderen Namen
eintragen. Beide werden zu einer Person.

**Meine Fotos liegen jetzt auf einem anderen Laufwerk.**
**Config & Scans → Bildordner**: in der Ordnerzeile den Pfad ändern → **Prüfen** →
**Speichern**. Namen und Gesichter bleiben erhalten, nichts muss neu eingelesen werden.

**Wie aktualisiere ich auf eine neue Version?**
Siehe [Aktualisieren](README.md#aktualisieren) – kurz: App schließen, `Data` sichern, nur
`Bilder.exe` austauschen.

**Etwas klappt nicht oder Sie haben einen Wunsch?**
→ [Anliegen melden](https://github.com/tripledewey-ctrl/bilder-releases/issues/new/choose).
Bitte keine echten Namen, Fotos oder Dateinamen aus Ihrer Sammlung hineinschreiben –
Anliegen sind öffentlich sichtbar.
