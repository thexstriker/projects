import sqlite3
from datetime import datetime
from colorama import Fore, Style

# Connect to the SQLite database
conn = sqlite3.connect('todo_list.db')
cursor = conn.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_name TEXT NOT NULL,
        description TEXT,
        status TEXT NOT NULL DEFAULT 'pending',
        date_added TEXT NOT NULL
    )
""")

cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
""")


tables = cursor.fetchall()
print(tables)

conn.commit()

def add_task(task_name, description):
    date_added = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''
                   INSERT INTO tasks (task_name, description, status, date_added)
                   VALUES (?, ?, 'pending', ?)
                   ''', (task_name, description, date_added))
    conn.commit()
    print(Fore.GREEN + f"Task, '{task_name}', added successfully." + Style.RESET_ALL)

def view_tasks():
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    print("\nCurrent Tasks:")
    for task in tasks:
        print(Fore.CYAN + f"ID: {task[0]}, Name: {task[1]}, Status: {task[3]}, Added: {task[4]}" + Style.RESET_ALL)

def update_task_status(task_id, new_status):
    cursor.execute('UPDATE tasks SET status = ? WHERE id = ?', (new_status, task_id))
    conn.commit()
    print(Fore.YELLOW + f"Task ID {task_id} updated to '{new_status}'." + Style.RESET_ALL)

def delete_task(task_id):
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    print(Fore.RED + f"Task ID {task_id} deleted." + Style.RESET_ALL)

# Main loop
while True:
    print("\nOptions: 1) Add Task 2) View Tasks 3) Update Task 4) Delete Task 5) Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        task_name = input("Enter task name: ")
        description = input("Enter task description: ")
        add_task(task_name, description)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        task_id = input("Enter the ID of the task to update: ")
        new_status = input("Enter new status (pending, in-progress, complete): ")
        update_task_status(task_id, new_status)
    elif choice == '4':
        task_id = input("Enter the ID of the task to delete: ")
        delete_task(task_id)
    elif choice == '5':
        break
    else:
        print("Invalid option. Please try again.")

conn.close()