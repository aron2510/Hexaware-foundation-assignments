from util.DBConnUtil import DBConnUtil

def fetch_users():
    conn = DBConnUtil.get_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM Users")
            rows = cursor.fetchall()

            print("✅ Connected to DB. Users:")
            for row in rows:
                print(row)

        except Exception as e:
            print("Failed to fetch users:", e)
        finally:
            conn.close()
    else:
        print("Could not establish connection.")

if __name__ == "__main__":
    fetch_users()
