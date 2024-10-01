import datetime #datetime 받아오는 모듈

real_today = datetime.date.today() + datetime.timedelta(hours=9) # 오늘 날짜에다가 timedelta 명령어 써서 9시간 더하기
print(real_today)
