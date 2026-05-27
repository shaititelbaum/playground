# Todo List Application

tasks = []

def add_task(task_name):
    tasks.append(task_name)
    return f"Task '{task_name}' added successfully!"

def get_tasks():
    return tasks

if __name__ == "__main__":
    # Test our code
    print(add_task("Buy groceries"))
    print(add_task("Walk Chip"))
    print(f"Current tasks: {get_tasks()}")
