import csv
import os

from tabulate import tabulate
from Notepad.note import HEADERS, Note

class NotesService:
    def __init__(self, file_path="notes.csv"):
        self.file_path = file_path

    def load_notes(self):
        notes = []
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding='utf-8') as file:
                reader = csv.DictReader(file, delimiter=";")
                for row in reader:
                    note = Note(row["Title"], row["Body"])
                    note.set_id(int(row["ID"]))
                    note.date_time = row["Date/Time"]
                    notes.append(note)
        return notes

    def save_notes(self, notes):
        with open(self.file_path, "w", newline="", encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=HEADERS, delimiter=";")
            writer.writeheader()
            for note in notes:
                writer.writerow({
                    "ID": note.id,
                    "Title": note.title,
                    "Body": note.body,
                    "Date/Time": note.date_time
                })

    def display_one_note(self, note):
        try:
            data = {"ID": note.id, "Title": note.title, "Body": note.body, "Date/Time": note.date_time}
            headers = "keys"
            table = tabulate([data], headers=headers, tablefmt="grid")
            print(table)
            tabulate_done = True
        except Exception as e:
            print(f"Ошибка при отображении с использованием tabulate. Установите tabulate и повторите попытку: {e}")
            tabulate_done = False

        if not tabulate_done:
            print("ID: {:>10}".format(note.id))
            print("Title: {:>10}".format(note.title))
            print("Body: {:>10}".format(note.body))
            print("Date/Time: {:>10}".format(note.date_time))
            print("-" * 20)
   
    def display_notes(self, notes):
        if isinstance(notes, list):
            for note in notes:
                self.display_one_note(note)
        else:
            self.display_one_note(notes)
            
