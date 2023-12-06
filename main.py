'''To-Do List with File Storage:
   * A to-do list application that allows users to add, remove, and view tasks.
   * And save tasks to a text file so that they persist between program runs.
'''
import json
import pprint

class TaskManager:
    '''Task Class'''
    def __init__(self, file_path):
        self.file_path = file_path
        self.tasks = self.read_tasks_from_file(file_path)

    def read_tasks_from_file(self, file_path):
        '''Read from the file'''
        with open(file_path, 'r', encoding="utf-8") as file:
            tasks = json.load(file)
        return tasks

    def write_tasks_to_file(self):
        '''Write to the file'''
        with open(self.file_path, 'w', encoding="utf-8") as file:
            json.dump(self.tasks, file, indent=2)

    def add_task(self, new_task):
        """
        Add a new task to the task list.

        Parameters:
        - new_task (dict): A dictionary representing the new task.
        """
        self.tasks.append(new_task)
        self.write_tasks_to_file()

    def remove_task(self, task_identifier):
        """
        Remove a task from the task list.

        Parameters:
        - task_identifier : task_name
        """
        self.tasks = [d for d in self.tasks if d['task'] != task_identifier]
        self.write_tasks_to_file()

    def list_tasks(self):
        """
        List all tasks in the To-Do List.
        """
        # Display all tasks along with their details (task name, due date, status)
        if self.tasks:
            print("Your To-Do List:")
            for i, tsk in enumerate(self.tasks, 1):
                print(f"{i}. Task: {tsk['task']}, Due Date: {tsk['due_date']}, Status: {tsk['status']}")
        else:
            print("Your To-Do List is empty.")
        

# Instatiate a TaskManager object
my_task_manager = TaskManager("tasks.json")

# Add Task
task_name = input("Task name: ")
status = input("Status: ")
due_date = input("Due date: ")
task = json.loads(f'{{"task": "{task_name}", "status": "{status}", "due_date": "{due_date}"}}')
my_task_manager.add_task(task)

# View Tasks
pprint.pprint(my_task_manager.read_tasks_from_file("tasks.json"))
my_task_manager.list_tasks()

# Remove Task
task_name_to_del = input('Enter the task name you wanna delete: ')
my_task_manager.remove_task(task_name_to_del)
