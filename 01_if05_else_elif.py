"""
gender의 값을 검사해서 "남자"라면 "남자입니다."라고 출력하고
"여자"라면 "여자입니다."라고 출력하고, 
둘 다 아닐경우 "성별은 남자/여자 둘중에 하나여야 합니다."라고 출력하도록 만들어 보세요.
if, elif, else를 이용해야 합니다.
"""

# gender = "남자"
# #이 아래줄에 if문을 추가하세요
# if gender == "남자":
#     print("남자입니다.")
# #이 아래줄에 elif문을 추가하세요
# else:
#     if gender == "여자":
#         print("여자입니다.")
# # #이 아래줄에 else문을 추가하세요
#     else:
#         print("성별은 남자/여자 둘중에 하나여야 합니다.")

gender = "남자"
#이 아래줄에 if문을 추가하세요
if gender == "남자":
    print("남자입니다.")
#이 아래줄에 elif문을 추가하세요
elif gender == "여자":
        print("여자입니다.")
# #이 아래줄에 else문을 추가하세요
else:
    print("성별은 남자/여자 둘중에 하나여야 합니다.")