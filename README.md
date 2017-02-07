## 파이썬 설치

#### Windows
- www.python.org에서 다운로드 메뉴 - Python 3.5이상 선택해서 다운로드
- 설치 과정에서 "Add Python 3.5 to Path" 반드시 체크
- 설치 확인
 - 윈도우키 + R을 눌러서 나오는 창에 powershell이라고 치고, 확인을 눌러서 powershell실행
 - powershell화면에서 python이라고 입력해서 오류가 나오지 않으면 설치 성공

#### REPL(Read-Eval-Print-Loop) 도구 
: 코드를 읽어서, 실행하고, 출력하는, 반복 
만약 python이라고만 쳐서 >>>에 갇히게 된다면?
-> `exit()` 라고 하면 빠져나올 수 있다. 

`>>>` 에서 한줄씩 직접결과를 보면서 테스트할 수 있다. 
잘 모르는 함수 등을 테스트할 때 편하다. 

## 파이썬 실행
1. 에디터에서 xx.py 라고 저장한다. 
2. powershell을 실행시켜서 해당 폴더로 간 뒤
`python xx.py`라고 실행시킨다. 

### print('Hello, world!');
화면출력 함수 

### 변수
```
name = '메롱'
number_of_legs = 2
print('Hello,', name, '다리는 ',number_of_legs)
```

### 주석 
```
# 한 줄 주석

"""
긴 주석
"""
```

### 연산
- 거듭제곱 : **
- 문자열 
```
text = '2020'+'1010' 
print(text) # 결과 20201010
```

## Shell 사용법
커맨드라인 쉘 (명령중 쉘) : 파이썬을 쓸 땐 이게 편하다. 
- pwd (print working directory): 현재 경로 나옴 
- ls (list segments): 현재 폴더 리스트 (폴더의 구성물)
- cd 이동할폴더이름 (change directory)
- cd .. : 상위폴더로 이동
- cp 복사할파일 새파일이름 (copy): 파일복사하기
- rm 삭제할파일이름 (remove)(휴지통에 들어가지않고 바로 삭제됨)
- 파일이름을 두글자쓰고 tab키 누르면 자동으로 파일명 생김 

## 조건문
```
if 조건식:
    print('메롱')  # 들여쓰기 꼭 해야 블럭안에 있다고 인식이 된다. 

    if 조건식:
        pritn('위 if블록에 속한 코드')
````

## 조건식 
a < b <br>
a <= b (등호는 반드시 =앞에온다)<br>
a == b (같다)<br>
a != b (같지 않다)<br>
True and True (and는 두 조건이 모두 참인 경우에만 참)<br>
True and False<br>
True or False(or는 두 조건 중 하나라도 참이면 참)<br>
not True(조건을 뒤집음)

### if-else
```
if True:
    pass # 조건이 참일 때 실행
else:
    pass # 조건이 거짓일 때 실행 
```

### elif (else와 if를 합친다.)
```
if xx:
    
else:
    if xx:

```

위와 같은 기능으로 elif를 쓰면 
```
if xx:
    
elif xx:

```

기능은 똑같으나 코드가 눈에 어떻게 보이느냐에 따라 쓸 수 있는 선호의 차이이다. 

## 날짜와 시간 (datetime 라이브러리)

```
>>> import datetime
>>> start_time = datetime.datetime.now()
>>> type(start_time)
<class 'datetime.datetime'> # start_time변수 값은 datetime class인 것을 알 수 있다. 
```

datetime에는 replace라는 메소드가 있다. 
`start_time = start_time.replace(year = 2018, month = 2, day = 1)`

처음부터 내가 원하는 년월일로 바꾸고 싶다면
`start_time = datetime.datetime(2018,1,1)`

오늘부터 지정 날짜까지 얼마나 남았는지 계산해보자. 
```
>>> how_long = start_time - datetime.datetime.now()
>>> type(how_long)
<class 'datetime.timedelta'>
# how_long은 timedelta라는 class인 것을 알 수 있다. 
# timedelta는 days와 seconds로 날짜와 초를 제공해준다. 
```

```
import datetime
start_time = datetime.datetime(2018,1,1)
how_long = start_time - datetime.datetime.now()
print ("내년까지 {}일 {}시간이 남았습니다.".format(how_long.days, how_long.seconds//3600))
```

### datetime과 timedelta class를 사용하여 날짜와 시간을 자유자재로 구해보자. 
```
import datetime

hundred = datetime.timedelta(days = 100)
today = datetime.datetime.now().date()
hundred_days = today + hundred

print("오늘 사귀면 {}일에 우리 100일이야.ㅋㅋ".format(hundred_days))
```

## Function(함수)

```
def functionNmae():
    내용
```

```
def add(a,b): # 매개변수
	#함수 add에서 a와 b를 입력받아서 두 값을 더한 값을 result에 저장하고 출력하도록 만들어 보세요.
	result = a + b
	print( "{} + {} = {}".format(a,b,result) )#print문은 수정하지 마세요.

add(10,5) # 실행인자
```

함수내에서 return을 쓰면 아래코드를 실행하지 않고 끝낸다. 

## 문자열
```
name = "홍님"
color = "하늘"
print('안녕하세요. 제 이름은 {}이고 좋아하는 색상은 {}입니다.'.format(name, color))
```

줄바꿈할때 따옴표 세개를 쓴다. 
따옴표안에 따옴표쓸때도 따옴표 세개 안에 쓰면 간편하다. 
```
string1 = """다스베이더가 말했다.
"내가 니 애비다!"
그 말을 들은 루크는 '깜짝' 놀랐다."""
```

## 정수와 실수(부동소수점)

### 정수
정수끼리 연산할 때. 정확하다. 
나눗셈은 제외 

### 실수
정수와 실수섞으면 실수가 된다. 정확치 않은 값으로 인식한다. 

6 / 5 = 1.2
6 // 5 = 1

```
a = 6
b = 5

print(a == b * (a // b) + (a % b)) # 결과 : True
print(int(5.0)) # 정수로
print(float(5)) # 부동소수점으로
print(5 * 1.0) # 부동소수점으로
```

## 사용자 입력받기 (중요하다)

#### 전통적인 프로그래밍 단계
사용자 입력 -> 자료처리 -> 결과출력

```
print("가위, 바위, 보 가운데 하나를 내 주세요. >", end = " ")
mine = input()
print("Mine:", mine)
```
input : 사용자의 키보드 입력을 return 
end = " " : 줄 바꿈 없앰 

```
mine = input("가위, 바위, 보 가운데 하나를 내 주세요. >")
print("Mine:", mine)
```

input함수에는 print를 할 수 있는 기능이 내장되어 있다. 

input실행시 프로그램이 멈추게 되는데 ctrl+c 를 하게되면 바로 종료 

## list 배열
여러개의 값을 담을 수 있는 변수
```
list1 = ['가위', '바위', '보']

# -1은 뒤에서 첫번째 값
print(list1[-1])  # 보 
```

```
rainbow=['빨강','주황','노랑','초록','파랑','남색','보라']
#rainbow를 이용해서 first_color에 값을 저장하세요
first_color = rainbow[0]
print('무지개의 첫번째 색은 {}이다'.format(first_color) )
```

#### list 값 추가하기 
```
list2 = [1,2,3]
list2.append(4) #[1,2,3,4]
list3 = list2 + [4] #[1,2,3,4]
```

#### list 합치기 
```
list4 = list2 + list3 #[1,2,3,4,1,2,3,4]
```

#### list에 특정 값 있는지 확인 
```
n = 5
check = n in list4
print(check) #false
```

#### 특정 위치 값 삭제
```
del list4[0] # 첫번째 값 지우기

list4.remove(4) #값이 4인 것 중에 처음 나오는 것 삭제 
```

## for in 반복문 
```
patterns = [1,2,3,4,5]
for pattern in patterns:
  print(pattern) # 1 ~ 5까지 출력된다. 
```

in 뒤에 있는 모든 값을 in 앞에 있는 변수에 한번씩 넣어가면서 블럭을 실행한다. 