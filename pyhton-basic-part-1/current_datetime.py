from datetime import datetime

def display_current_datetime():
    now = datetime.now()
    print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))

display_current_datetime()
