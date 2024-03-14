import sqlite3

def login(username, password):
    # Connect to the SQLite database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Vulnerable SQL query with string concatenation
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

    # Execute the SQL query
    cursor.execute(query)

    # Fetch the result
    result = cursor.fetchone()

    # Close the database connection
    conn.close()

    if result:
        return "Login successful"
    else:
        return "Invalid username or password"

# Usage example (vulnerable to SQL injection)
username = input("Enter your username: ")
password = input("Enter your password: ")
print(login(username, password))
