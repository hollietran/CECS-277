#Names: Min, Hollie
"""
Description: A program that maintains a task list for the user.
The user should be able to view the current task, mark the task complete,
postpone the current task, ror add a new task. The program will read the 
list from a file ('tasklist.txt') when the program begins and then stores 
the updated list by overwriting the old contents when the user quits 
the program.
"""
def main_menu():
    # Displays the main menu and returns the user's valid input.

def read_file():
    # Opens the file ('tasklist.txt') and read each of the tasks.
    # Construct a task object from each line adn add it to a list.
    # Return the filled task list.
    
def write_file(tasklist):
    # Passes in the list of tasks that will be written to the file
    # ('tasklist.txt'). Iterate through the list of tasks and write each
    # one to the file using the Task's repr() method

def get_date():
    # Prompt the user to input a month, day, and year
    # Valid: year (2000 - 2100), month (1 - 12), day (1 - 31)
    # Return the date in the format: MM/DD/YYYY
    # If the inputted month or day is less than 10, add a leading 0 to format it correctly

def get_time():
    # Prompts the user to enter the hour (Military time) and minute.
    # Valid: hours (0 - 23), minutes (0-59)
    # Return date in format: MM/DD/YYYY
    # If the inputted hour or minute is less than 10, add a leading 0 to format it correctly

def main():
    