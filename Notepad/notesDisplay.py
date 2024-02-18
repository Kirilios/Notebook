from tabulate import tabulate

class NotesDisplay:
    @staticmethod
    def display_notes(notes):
        try:
            data = [{"ID": note.id, "Title": note.title, "Body": note.body, "Date/Time": note.date_time} for note in notes]
            headers = "keys"
            print(tabulate(data, headers=headers, tablefmt="grid"))
        except Exception:
            print("У вас не поддерживается отображение таблицей, поэтому отображение будет в виде списка")
            NotesDisplay.display_notes_as_list(notes)
            
    @staticmethod
    def display_one_note(note):
        try:
            data = {"ID": note.id, "Title": note.title, "Body": note.body, "Date/Time": note.date_time}
            headers = "keys"
            print(tabulate([data], headers=headers, tablefmt="grid"))
        except Exception:
            print("У вас не поддерживается отображение таблицей, поэтому отображение будет в виде списка")
            NotesDisplay.display_one_note_as_list(note)
            
    @staticmethod
    def display_notes_as_list(notes):
        for note in notes:
            print(f"ID: {note.id}")
            print(f"Title: {note.title}")
            print(f"Body: {note.body}")
            print(f"Date/Time: {note.date_time}")
            print("-" * 20)
            
    @staticmethod
    def display_one_note_as_list(note):
        print(f"ID: {note.id}")
        print(f"Title: {note.title}")
        print(f"Body: {note.body}")
        print(f"Date/Time: {note.date_time}")
        print("-" * 20)
    
    @staticmethod
    def display_note_by_id(notes, note_id):
        for note in notes:
            if note.id == note_id:
                NotesDisplay.display_one_note(note)
                return
        print(f"Заметка с ID {note_id} не найдена.")