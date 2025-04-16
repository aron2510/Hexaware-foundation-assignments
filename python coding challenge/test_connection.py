from util.dbconnutil import DBConnUtil

try:
    conn = DBConnUtil.get_connection()
    print("Database connection successful!")

    cursor = conn.cursor()
    cursor.execute("SELECT DB_NAME()")
    db_name = cursor.fetchone()[0]
    print("🔍 Connected to database:", db_name)
    cursor.execute("""
        SELECT TABLE_SCHEMA, TABLE_NAME 
        FROM INFORMATION_SCHEMA.TABLES 
        WHERE TABLE_TYPE = 'BASE TABLE'
    """)
    print("📋 Tables in the database:")
    for row in cursor.fetchall():
        print(f"- {row.TABLE_SCHEMA}.{row.TABLE_NAME}")

    cursor.close()
    conn.close()

except Exception as e:
    print("Database connection failed:", e)
