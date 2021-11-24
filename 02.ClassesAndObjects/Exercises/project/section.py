class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        pass

    def clean_section(self):
        i = 0
        removed_tasks = 0
        while i < len(self.tasks):
            t = self.tasks[i]
            if t.completed:
                self.tasks.remove(t)
                removed_tasks += 1
                i -= 1
            i += 1
        return f"Cleared {removed_tasks} tasks."

    def view_section(self):
        return f"Section {self.name}:\n{chr(10).join(t.details() for t in self.tasks)}"
