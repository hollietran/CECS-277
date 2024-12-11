class Task:
    def __init__(self, desc, date, time):
        self.description = desc.strip()
        self.date = date.strip()  # MM/DD/YYYY
        self.time = time.strip()  # HH:MM

    def __str__(self):
        return f"{self.description} - Due: {self.date} at {self.time}"
    
    def __repr__(self):
        return f"{self.description}, {self.date}, {self.time}"
    
    def __lt__(self, other):
        '''The __lt__ method should
            sort by year, and if those are the same, it should sort by month, then day, then
            hour, then minute, then if all of those are the same, then sort the description'''
        # Convert dates and times to sortable formats
        self_date = self.date.split("/")
        other_date = other.date.split("/")
        self_time = self.time.split(":")
        other_time = other.time.split(":")
        
        # Convert to (YYYY, MM, DD, HH, MM) for comparison
        self_tuple = (int(self_date[2]), int(self_date[0]), int(self_date[1]), int(self_time[0]), int(self_time[1]))
        other_tuple = (int(other_date[2]), int(other_date[0]), int(other_date[1]), int(other_time[0]), int(other_time[1]))
        
        # Make sure the list is resorted after adding and postponing a task
        return self_tuple < other_tuple
