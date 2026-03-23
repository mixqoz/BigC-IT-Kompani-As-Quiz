import mysql.connector

# Connect to MySQL (adjust credentials as needed)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="your_password",
    database="your_database"
)

cursor = db.cursor()

# Read and execute the SQL file
with open('stillingerDB.sql', 'r', encoding='utf-8') as file:
    sql_script = file.read()

# Split the script into individual statements
statements = sql_script.split(';')

for statement in statements:
    statement = statement.strip()
    if statement:
        try:
            cursor.execute(statement)
            print(f"Executed: {statement[:50]}...")
        except mysql.connector.Error as err:
            print(f"Error executing statement: {err}")

db.commit()
cursor.close()
db.close()

print("Database setup complete!")