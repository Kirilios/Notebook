import csv
import os

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
                             
    def delete_all_notes(self):
        with open(self.file_path, "w", newline="", encoding='utf-8') as file:
            file.write("") 

