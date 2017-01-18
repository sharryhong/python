import datetime

# datetime내에는 datetime이라는 class가 있다. 
# datetime.datetime.now() # now 메소드 
# 결과 : datetime.datetime(2017, 1, 18, 14, 18, 58, 124544)
# 년 월 일 시 분 초 마이크로초(백만분의 일초)

start_time = datetime.datetime(2018,1,1)

how_long = start_time - datetime.datetime.now()

print ("내년까지 {}일 {}시간이 남았습니다.".format(how_long.days, how_long.seconds//3600))