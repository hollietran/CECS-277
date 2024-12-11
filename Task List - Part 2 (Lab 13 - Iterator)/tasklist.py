from task import Task
class Tasklist:
    # Manages a list of tasks with iterator functionality.
    def __init__(self):
        self.tasklist = []
        self.n = 0
        try:
            with open("tasklist.txt", "r") as file:
                for line in file:
                    # Ensure the line contains exactly three comma-separated values
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        desc, date, time = parts
                        self.add_task(desc.strip(), date.strip(), time.strip())
        except FileNotFoundError:
            pass  # No existing file, start with an empty list


    def add_task(self, desc, date, time):
        task = Task(desc, date, time)
        self.tasklist.append(task)
        self.tasklist.sort()

    def get_current_task(self):
        return self.tasklist[0] if self.tasklist else None
    
    def mark_complete(self):
        return self.tasklist.pop(0) if self.tasklist else None
    
    def postpone_task(self, date, time):
        if not self.tasklist:
            return None
        current_task = self.tasklist.pop(0)
        self.add_task(current_task.description, date, time)

    def save_file(self):
        # Make sure that you write to the file in the same format (ie. comma separated with no spaces after the commas (spaces are ok in the description))
        with open("tasklist.txt", "w") as file:
            for task in self.tasklist:
                file.write(repr(task) + "\n")

    def __len__(self):
        return len(self.tasklist)
    
    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        if self.n >= len(self.tasklist):
            raise StopIteration
        task = self.tasklist[self.n]
        self.n += 1
        return task
