
from datetime import datetime


HEADERS = ["ID", "Title", "Body", "Date/Time"]

class Note:
    def __init__(self, title, body):
        self.id = None
        self.title = title
        self.body = body
        self.date_time = None
        
    def set_id(self, note_id):
        self.id = note_id

    def set_date_time(self):
        self.date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        
        