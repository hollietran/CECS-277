'''Names: Min Hein, Hollie Tran
Update Lab 5 to use an iterator to display the contents of the task list. The user should be able to
do everything that they were able to do before, plus the added ability to search by date. Use the
following UML diagram to update your program:
'''

from tasklist import Tasklist
from check_input import check_input

def main_menu():
    print("-Tasklist-\n1. Display all tasks\n2. Display current task\n3. Add new task\n4. Mark current task complete\n5. Postpone current task\n6. Search tasks by date\n7. Save and quit")
    return input("Enter choice: ")

def main():
    tasklist = Tasklist()

    while True:
        # Make sure that you display the total number of tasks to complete
        print(f"You have {len(tasklist)} tasks.")
        choice = main_menu()

        if choice == "1":
            # Make sure that it displays all the tasks in sorted order and uses the iterator
            print("Task to complete:")
            for i, task in enumerate(tasklist, start=1):
                print(f"{i}. {task}")

        elif choice == "2":
            # Make sure that the current task is the soonest due date and time
            current = tasklist.get_current_task()
            print(f"Current task: {current}" if current else "No tasks left.")
        
        elif choice == "3":
            desc = input("Enter task description: ")
            date = check_input.get_date()
            time = check_input.get_time()
            tasklist.add_task(desc, date, time)
            print("Task added.")

        elif choice == "4":
            # Make sure that the current task is removed when marking it complete
            completed = tasklist.mark_complete()
            if completed:
                print(f"Completed task: {completed}")
            
            else:
                print("No tasks to complete.")

        elif choice == "5":
            current = tasklist.get_current_task()
            if current:
                print(f"Postponing task: {current}")
                date = check_input.get_date()
                time = check_input.get_time()
                tasklist.postpone_task(date, time)
                print("Task postponed.")
            
            else:
                print("No tasks to postpone")
            
        elif choice == "6":
            # Make sure that the search finds all matching tasks.
            search_date = check_input.get_date()
            matches = [task for task in tasklist if task.date == search_date]
            if matches:
                for i, task in enumerate(matches, start = 1):
                    print(f"{i}. {task}")
            
            else:
                print("No task found for that date.")
            
        elif choice == "7":
            tasklist.save_file()
            print("Saving list...")
            break

        else:
            print("invalid choice. Try again.")

main()