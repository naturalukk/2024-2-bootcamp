import datetime

today = datetime.date.today()
real_today = datetime.date.today() + datetime.timedelta(hours=9)
print(real_today)
