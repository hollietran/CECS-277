class check_input:
    #Make sure to error check all user input: Main menu: 1-7, Year: 2000-2100, Month: 1-12, Day: 1-31, Hour: 0-23, Minute: 0-59
    
    @staticmethod
    def get_date():
        # Prompts the user to input a valid date in MM/DD/YYYY format
        while True:
            try:
                # Get and validate month
                month = int(input("Enter month (1-12): "))
                if not (1 <= month <= 12):
                    print("Invalid month. Please try again.")
                    continue

                # Get and validate day
                day = int(input("Enter day (1-31): "))
                if not (1 <= day <= 31):
                    print("Invalid day. Please try again.")
                    continue

                # Get and validate year
                year = int(input("Enter year (2000 - 2100): "))
                if not (2000 <= year <= 2100):
                    print("Invalid year. Please try again.")
                    continue

                # Return formatted date if all inputs are valid
                return f"{month:02}/{day:02}/{year}"

            except ValueError:
                print("Invalid input. Please enter numbers only.")

    @staticmethod
    def get_time():
        # Prompts the user to input a valid time in HH:MM format
        while True:
            try:
                # Get and validate hour
                hour = int(input("Enter hour (0-23): "))
                if not (0 <= hour <= 23):
                    print("Invalid hour. Please try again.")
                    continue

                # Get and validate minute
                minute = int(input("Enter minute (0-59): "))
                if not (0 <= minute <= 59):
                    print("Invalid minute. Please try again.")
                    continue

                # Return formatted time if valid
                return f"{hour:02}:{minute:02}"

            except ValueError:
                print("Invalid input. Please enter numbers only.")
