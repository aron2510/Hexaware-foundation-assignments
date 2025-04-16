import pyodbc
from dao.adoptioneventdao import AdoptionEventDAO
from util.dbconnutil import DBConnUtil

class AdoptionEventDAOImpl(AdoptionEventDAO):
    def __init__(self):
        self.conn = DBConnUtil.get_connection()

    def get_all_events(self):
        cursor = self.conn.cursor()
        cursor.execute("select * from adoption_events")
        rows = cursor.fetchall()
        events = []
        for row in rows:
            events.append({
                "event_id": row.event_id,
                "event_name": row.event_name,
                "event_date": str(row.event_date)
            })
        return events

    def register_participant(self, name, event_id, role):
        cursor = self.conn.cursor()
        cursor.execute(
            "insert into participants (name, event_id, role) values (?, ?, ?)",
            (name, event_id, role)
        )
        self.conn.commit()
        cursor.execute("SELECT * FROM participants")
        participants = cursor.fetchall()
        print("Updated participants table:")
        for row in participants:
            print(row)
