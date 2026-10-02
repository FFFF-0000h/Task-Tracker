import os
import json

FILENAME = "tasks.json"

data = {}

def load_tasks():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w") as tasks:
             json.dump(data, tasks)
        return data
    else:
        with open(FILENAME, "r") as tasks:
            task = json.load(tasks)
        return task

def save_tasks(data):
    if data == {}:
        print("\nThere are no tasks to be saved!\nPlease add tasks.\n")
    else:
        with open(FILENAME, "w") as tasks:
            json.dump(data, tasks, indent=4)
            print("\nTasks saved successfully!\n")
