import pyodbc

def SQLConnect():
    conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-MVOVAQ6;"
                      "Database=PaymentDetailDB;"
                      "Trusted_Connection=yes;")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Diseases')
    cur = cursor.fetchall()
    for row in cur:
        print (row)

def SQLInsert():
    conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-MVOVAQ6;"
                      "Database=PaymentDetailDB;"
                      "Trusted_Connection=yes;")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Diseases (DiseaseName, Code, Description) VALUES ('Corona', 'CO', 'COVID19')")
    conn.commit()

SQLConnect()
SQLInsert()