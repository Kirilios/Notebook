
from Notepad.note import Note
from Notepad.notesDisplay import NotesDisplay
from Notepad.notesService import NotesService



class NotesApp:
      def __init__(self):
            self.notesService = NotesService()
            self.display = NotesDisplay()
      
      def add_note(self, title, body):
            notes = self.notesService.load_notes()
            new_note = Note(title, body)
            new_note.set_id(len(notes) +1)
            new_note.set_date_time()
            notes.append(new_note)
            self.notesService.save_notes(notes)
            print("Новая заметка добавлена.")
            self.display.display_notes([new_note])
      
      def edit_notes(self, note_id, title, body):
            notes = self.notesService.load_notes()
            for note in notes:
                  if note.id == note_id:
                        note.title = title
                        note.body = body
                        note.set_date_time()
                        break
            self.notesService.save_notes(notes)
            print(f"Заметка {note_id} изменена")
            self.display.display_note_by_id(notes, note_id)
      
      def delete_notes(self, note_id):
            notes = self.notesService.load_notes()
            for note in notes:
                if note.id == note_id:
                    notes = [n for n in notes if n.id != note_id]
                    self.notesService.save_notes(notes)
                    print(f"Заметка {note_id} удалена")
                    self.display.display_notes(notes)
                    return
            print(f"Заметка с ID {note_id} не найдена.")
            
      def delete_everything(self):
            self.notesService.delete_all_notes()
            print("Все заметки удалены.")
            self.display.display_notes([]) 
            
      def show_notes(self, filter_date=None):
            notes = self.notesService.load_notes()
            if filter_date:
                  filtered_notes = [note for note in notes if note.date_time.startswith(filter_date)]
                  self.display.display_notes(filtered_notes)
            else:
                  self.display.display_notes(notes)
                  
      def show_selected_note_by_id(self, note_id):
            notes = self.notesService.load_notes()
            self.display.display_note_by_id(notes, note_id)
      
      def run(self): 
          
        while True:
            print("\nМеню:")
            print("1. Показать заметки")
            print("2. Добавить заметку")
            print("3. Отредактировать заметку")
            print("4. Удалить заметку")
            print("5. Показать заметки с фильтром")
            print("6. Очистить все заметки")
            print("7. Показать одну заметку по ID")
            print("8. Выход")

            choice = input("Введите число (1-8): ")

            if choice == "1":
                self.show_notes()
            elif choice == "2":
                title = input("Введите название заметки ")
                body = input("Введите содержимое заметки ")
                self.add_note(title, body)
            elif choice == "3":
                note_id = int(input("Введите ID заметки "))
                title = input("Введите название заметки ")
                body = input("Введите содержимое заметки ")
                self.edit_notes(note_id, title, body)
            elif choice == "4":
                note_id = int(input("Введите ID заметки для удаления: "))
                self.delete_notes(note_id)
            elif choice == "5":
                filter_date = input("Введите данные по модели для сортировки по дате (DD-MM-YYYY): ")
                self.show_notes(filter_date)
            elif choice == "6":
                self.delete_everything()
            elif choice == "7":
                note_id = int(input("Введите ID заметки для поиска совпадений: "))
                self.display.display_note_by_id(self.notesService.load_notes(), note_id)
            elif choice == "8":
                print("Выход произведен успешно.")
                break
            else:
                print("Ошибка ввода. Введите числа от 1 до 6")
      
if __name__ == "__main__":
    app = NotesApp()
    app.run()

            
            
            
            