import time
import datetime
import random

def display_current_datetime():
    now = datetime.datetime.now()
    print(f"Year: {now.year}, Month: {now.month}, Day: {now.day}")
    print(f"Hour: {now.hour}, Minute: {now.minute}, Second: {now.second}")

def display_time_since_epoch():
    epoch_time = time.time()
    print(f"Time in seconds since epoch: {epoch_time}")

def format_date_time():
    now = datetime.datetime.now()
    date_ddmmyyyy = now.strftime("%d-%m-%Y")
    date_mmyyyydd = now.strftime("%m/%d/%Y")
    time_24h = now.strftime("%H:%M:%S")
    time_12h = now.strftime("%I:%M:%S %p")
    print(f"Date (DD-MM-YYYY): {date_ddmmyyyy}")
    print(f"Date (MM/DD/YYYY): {date_mmyyyydd}")
    print(f"Time (24-hour): {time_24h}")
    print(f"Time (12-hour): {time_12h}")

def calculate_days_between_dates():
    date1 = datetime.datetime.now()
    date2 = date1 + datetime.timedelta(days=7)
    days_diff = (date2 - date1).days
    print(f"Days between dates: {days_diff}")
    print(f"Date after adding 7 days: {date2.strftime('%Y-%m-%d')}")

def convert_date_string():
    date_str = "2024-01-01"
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    formatted_str = date_obj.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Date object from string: {date_obj}")
    print(f"Formatted string: {formatted_str}")

def measure_execution_time():
    def sample_function():
        time.sleep(1)
    start_time = time.time()
    sample_function()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.2f} seconds")

def display_utc_local_time():
    utc_time = datetime.datetime.utcnow()
    local_time = datetime.datetime.now()
    print(f"UTC Time: {utc_time}")
    print(f"Local Time: {local_time}")

def stopwatch():
    running = False
    start_time = 0
    elapsed = 0
    while True:
        choice = input("Stopwatch - (s)tart/(resume), (p)ause, (r)eset, (q)uit: ").lower()
        if choice == 's' and not running:
            running = True
            start_time = time.time() - elapsed
            print("Stopwatch started...")
            try:
                while running:
                    elapsed = time.time() - start_time
                    print(f"Elapsed: {elapsed:.2f} seconds", end='\r')
                    time.sleep(0.1)
                    # Check for pause, reset, or quit
                    import msvcrt
                    if msvcrt.kbhit():
                        key = msvcrt.getwch().lower()
                        if key == 'p':
                            running = False
                            print(f"\nPaused at: {elapsed:.2f} seconds")
                        elif key == 'r':
                            running = False
                            elapsed = 0
                            print("\nStopwatch reset")
                        elif key == 'q':
                            print("\nExiting stopwatch...")
                            return
            except KeyboardInterrupt:
                print(f"\nPaused at: {elapsed:.2f} seconds")
                running = False
        elif choice == 'p' and running:
            running = False
            elapsed = time.time() - start_time
            print(f"Paused at: {elapsed:.2f} seconds")
        elif choice == 'r':
            running = False
            elapsed = 0
            print("Stopwatch reset")
        elif choice == 'q':
            print("Exiting stopwatch...")
            break

def countdown_timer():
    seconds = int(input("Enter number of seconds to count down: "))
    while seconds > 0:
        print(f"Time remaining: {seconds} seconds")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

def is_leap_year():
    year = int(input("Enter a year to check: "))
    is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    print(f"{year} is{' ' if is_leap else ' not '}a leap year")

def day_of_week():
    date_str = input("Enter date (YYYY-MM-DD): ")
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    day_name = date_obj.strftime("%A")
    print(f"Day of the week: {day_name}")

def schedule_reminder():
    reminder_time = float(input("Enter reminder time in seconds: "))
    print(f"Waiting for {reminder_time} seconds...")
    time.sleep(reminder_time)
    print("Reminder! Time's up!")

def digital_clock():
    print("Digital Clock started. Press Ctrl+C to stop.")
    try:
        while True:
            now = datetime.datetime.now()
            time_str = now.strftime("%H:%M:%S")
            date_str = now.strftime("%A, %d %B %Y")
            print(f"{time_str} | {date_str}", end='\r')
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nDigital Clock stopped.")

# Main menu
while True:
    print("\nMenu:")
    print("1. Display current date and time")
    print("2. Display time since epoch")
    print("3. Format date and time")
    print("4. Calculate days between dates")
    print("5. Convert date string")
    print("6. Measure execution time")
    print("7. Display UTC and local time")
    print("8. Stopwatch")
    print("9. Countdown timer")
    print("10. Check leap year")
    print("11. Day of the week")
    print("12. Schedule reminder")
    print("13. Digital Clock")
    print("0. Exit")
    
    choice = input("Enter your choice (0-13): ")
    
    if choice == '1':
        display_current_datetime()
    elif choice == '2':
        display_time_since_epoch()
    elif choice == '3':
        format_date_time()
    elif choice == '4':
        calculate_days_between_dates()
    elif choice == '5':
        convert_date_string()
    elif choice == '6':
        measure_execution_time()
    elif choice == '7':
        display_utc_local_time()
    elif choice == '8':
        stopwatch()
    elif choice == '9':
        countdown_timer()
    elif choice == '10':
        is_leap_year()
    elif choice == '11':
        day_of_week()
    elif choice == '12':
        schedule_reminder()
    elif choice == '13':
        digital_clock()
    elif choice == '0':
        print("Goodbye!")
        print("Exiting...")
        time.sleep(random.randint(1, 6))
        break
    else:
        print("Invalid choice, please try again.")