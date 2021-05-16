import datetime
import pytz;
today=datetime.date.today();
print(today)

birthday=datetime.date(2000,3,3)
print(birthday)

day_since_birthday=(today-birthday).days
print(day_since_birthday)
print(today.day)
print(today.weekday())

print(datetime.time(7,2,20,15))

plus_time=datetime.timedelta(days=10,hours=12)
print(datetime.datetime.now()+plus_time)
print(datetime.datetime.now(tz=pytz.UTC))
datetime_today=datetime.datetime.now(tz=pytz.UTC)
datetime_pacific=datetime_today.astimezone(pytz.timezone('US/Pacific'))
print(datetime_pacific)
for tz in pytz.all_timezones:
    print(tz)
print(datetime_pacific.strftime('%B %d %Y'))