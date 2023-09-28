# Readme

## Installation

* **Downloads:**
  * Python 3.11: [Python 3.11 Download](https://www.python.org/downloads/)
  * Visual Studio Code: [Visual Studio Code Download](https://code.visualstudio.com/)

* **Installation:**
  * Folgen Sie den Anweisungen des Python Installers.
  * Laden Sie in VS Code unter _Extentions_ die _Python_ Extension von Microsoft herunter, indem Sie `⇧` + `⌘` + `X` oder `STRG` + `⇧` + `X` drücken.
 
* **Installation der Python-Bibliotheken und mehr:**
    * **Virtuelle Umgebung erstellen:**
      ```shell
      python3 -m venv db
      ```
      Hier ist "db" der Name der virtuellen Umgebung.

    * **Aktiviere die virtuelle Umgebung:**
        * **Windows:** 
            ```shell 
            .db\Scripts\activate
            ```

        * **MacOS / Linux:** 
            ```shell
            source db/bin/activate
            ```

    * **Bibliotheken installieren:**
      ```shell
      pip install mysql-connector-python
      ```

    * **Virtuelle Umgebung auswählen:**
      Klicken Sie auf die [Python-Version (z.B. 3.11.5)] → Klicken Sie auf [Python [Version (z.B. 3.11.5)] (64-bit) ('AI': venv)].


## Methoden

 * **Funktionen:**
   
   | Methode               | Beschreibung                                           |
   |-----------------------|--------------------------------------------------------|
   | `connect`             | Verbinden mit der Datenbank                            |
   | `close`               | Verbindung schließen                                   |
   | `execute`             | Befehl ausführen                                       |
   | `fetch_all`           | Alle Zeilen aus dem Ergebnis einer SQL-Abfrage abrufen |
   | `fetch_many`          | Eine bestimmte Anzahl von Zeilen ausgeben              |
   | `create_table`        | Eine Tabelle erstellen                                 |
   | `drop_table`          | Tabelle löschen                                        |
   | `insert_data`         | Daten einfügen                                         |
   | `update_data`         | Tabelle aktualisieren                                  |
   | `delete_data`         | Daten löschen                                          |
   | `get_column_names`    | Spaltennamen ausgeben                                  |
   | `count_rows`          | Anzahl der Zeilen ausgeben                             |
   | `execute_script`      | SQL-Skript ausführen                                   |
   | `create_index`        | Eigenständige Datenstruktur erstellen                  |
   | `create_unique_index` | Eindeutige Datenstruktur erstellen                     |
   | `add_column`          | Spalte hinzufügen                                      |




    
