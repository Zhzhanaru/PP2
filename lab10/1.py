import psycopg2 as pg

try:
    conn = pg.connect(
        host='localhost',
        database='Pg2Py',
        port=5432,
        user='postgres',
        password='*********'
    )

    cursor = conn.cursor()
    print("Connection established.")

except Exception as err:
    print("Something went wrong.")
    print(err)
    
def fetch_data():
    cursor.execute('''SELECT * FROM players''')
    data = cursor.fetchall()
    return data

details = fetch_data()
for row in details:
    print(row)
    
def create_entry():
    cursor.execute('''INSERT INTO players (id, name, age) 
                    VALUES (%s, %s, %s)''', (4, 'My Ex', 22))

    add_data = cursor.fetchone()
    conn.commit()
    return add_data

data = create_entry()
print(data)