import datetime

now=datetime.datetime.today()
print(str(now.replace(microsecond=0)))

week_ago=now-datetime.timedelta(days=7)
print(str(week_ago.replace(microsecond=0)))

print(str(now.day))
