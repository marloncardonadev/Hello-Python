
### Dates ###

from datetime import datetime, time, date, timedelta

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date)
    print(date.timestamp())

now = datetime.now()

print_date(now)

year_2023 = datetime(2023, 1, 1)

print_date(year_2023)

current_time = time(9,15,57)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2023, 9, 22)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year, current_date.month + 1, current_date.day)

print(current_date.month)

diff = year_2023 - now
print(diff)

diff = year_2023.date() - current_date
print(diff)

init_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)

print(end_timedelta - init_timedelta)
print(end_timedelta + init_timedelta)