from datetime import date

def calculate_days_between_dates(date1, date2):
    delta = date2 - date1
    print(f"{delta.days} days")

calculate_days_between_dates(date(2014, 7, 2), date(2014, 7, 11))
