"""
다음 코드는 mine과 yours의 값에 따라 가위바위보의 승패를 판정하고 있습니다.
mine의 값이 "가위", "바위", "보"일때를 처리하는 부분이 점점 더 깊은 블록으로 들어가고 있어서 코드를 파악하기가 쉽지 않은데요.
elif를 사용해서 코드를 정리해 보세요.
"""

mine = "가위"
yours = "바위"

if mine == yours:
    print("비김")
else:
    if mine == "가위":
        if yours == "보":
            print("이겼다")
        else:
            print("졌다")
    elif mine == "바위":
        if yours == "가위":
            print("이겼다")
        else:
            print("졌다")
    elif mine == "보":
        if yours == "바위":
            print("이겼다")
        else:
            print("졌다")
