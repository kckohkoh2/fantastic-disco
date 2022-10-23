import datetime
today=datetime.datetime().today()
print(today)
print("오늘은 %d년 %d월 %d일입니디"%(today.year,today.month,today.day))
print("지금은 %d시 %d분 %d초입니다"%(today.hour,today.minute,today.second))