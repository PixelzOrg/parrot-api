import pyodbc

try:
    conn = pyodbc.connect('Driver={SQL Server};SERVER=DESKTOP-AU3C4CP\SQLEXPRESS;DATABASE=Hourglass')
    cursor = conn.cursor()
except Exception as e:
    print(f'Error connecting to database: {e}')
    raise e
