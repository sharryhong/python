import datetime

hundred = datetime.timedelta(days = 100)
today = datetime.datetime.now().date()
hundred_days = today + hundred

print("오늘 사귀면 {}일에 우리 100일이야.ㅋㅋ".format(hundred_days))


hundred_after = datetime.datetime.now().replace(hour = 9, minute = 0, second = 0) + datetime.timedelta(days = 100)

print("{}/{}/{}".format(hundred_after.year,hundred_after.month, hundred_after.day))