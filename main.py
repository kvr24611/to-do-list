# To-Do List with File Storage:
# A to-do list application that allows users to add, remove, and view tasks.
# And save tasks to a text file so that they persist between program runs.

import json

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



# Instatiate a TaskManager object
my_task_manager = TaskManager("tasks.json")


task_name = input("Task name: ")
status = input("Status: ")
due_date = input("Due date: ")
task = json.loads(f'{{"task": "{task_name}", "status": "{status}", "due_date": "{due_date}"}}')

my_task_manager.add_task(task)
