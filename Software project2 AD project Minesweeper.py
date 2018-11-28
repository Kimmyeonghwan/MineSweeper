
import random
n = int(input("N x N 배열 길이 입력 : "))
boom = int(input("폭탄 갯수 입력 : "))


display = [[0 for col in range(n)] for row in range(n)] # 화면
buttonList = [[i, j] for i in range(n) for j in range(n)] # 버튼 리스트
# sample은 중복을 뽑지 않는 것을 이용하여, 원하는 폭탄 갯수 만큼 중복되지 않는 좌표값을 가져옴
boomList = random.sample(buttonList, boom) # 왜 가끔 중복되는 숫자가 나오지?

# 디스플레이 미구현

for i in range(len(buttonList)):
    for j in range(len(boomList)):
        if boomList in buttonList:
            print("폭", end='')
        else:
            print("빔", end='')
    print()


print(buttonList)
print(boomList)
'''
# 화면에 지뢰 표시 테스트 (일단 실패)
for i in range(len(boomList)):
    for j in range(len(buttonList)):
        if boomList[i] in buttonList[j]:
            print("X", end='')

        else:
            print("ㅁ", end='')

    print()
'''

print(boomList[0])

guessX = int(input("추측할 x 좌표 값 입력 : "))
guessY = int(input("추측할 y 좌표 값 입력 : "))

test1 = [[guessX, guessY]]

# 입력한 좌표 값이 지뢰의 좌표 값과 일치하면 펑
if test1[0] in boomList:
    print("펑")
else:
    # 지뢰가 없는 좌표 값이라면 1, 2, 3 숫자들 만날 때 까지 주변 0을 지우는 코드
    pass

'''

import random
n = int(input("입력 : "))
boom = int(input("폭탄 개수 : "))
buttonList = [[i, j] for i in range(n) for j in range(n)]
list1 = random.sample(buttonList, boom)


list2 = [[i for i in range(2)] for j in range(5) ]
print(list1)
'''
