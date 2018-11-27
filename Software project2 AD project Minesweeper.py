import random
n = int(input("N x N 배열 길이 입력 : "))
boom = int(input("폭탄 갯수 입력 : "))


display = [[0 for col in range(n)] for row in range(n)] # 화면
buttonList = [[i, j] for i in range(n) for j in range(n)] # 버튼 리스트
# sample은 중복을 뽑지 않는 것을 이용하여, 원하는 폭탄 갯수 만큼 중복되지 않는 좌표값을 가져옴
boomList = [random.sample(range(n), 2) for i in range (boom)]

# 디스플레이 미구현
for i in range(len(display)):
    for j in range(len(display)):
        if boomList in buttonList:
            print("X", end='')
        else:
            print("ㅁ", end='')
    print()


print(buttonList)
print(boomList)

# 화면에 지뢰 표시 테스트 (일단 실패)
for i in range(len(boomList)):
    for j in range(len(buttonList)):
        if boomList[i] in buttonList[j]:
            print("X", end='')

        else:
            print("ㅁ", end='')

    print()
print(boomList[0])
'''
import random
n = int(input("버튼 길이 입력 : "))
n2 = int(input("폭탄 개수 입력 : "))

boom = [random.sample(range(n), 2) for i in range (n2)]

print(boom)
'''

'''
# 좌표 리스트 알고리즘...
for i in range(6):
    for j in range(6):
        print("[[{} {}]]".format(i, j), end=', ')
        
list1 = [[(i, j) for i in range(6) for j in range(6)]]
print(list1)
'''

'''
dic = {1 : "김", 2 : "이", 3 : "강", '사' : "구"}

print(dic.get('0'))
'''
'''
t1 = input("영어만 입력하세요. : ")
t2 = ''

for i in t1:
    if i.isalpha():
        if i.islower():
            t2 = i.upper()
            print(t2, end='')
        else:
            print(i, end='')
    else:
        print(i, end='')
'''

'''
print(ord('A'), ord('Z'), ord('a'), ord('z'))
a1 = input(영어 단어 입력 : )
a2 = int(input(시저 암호로 만들 숫자 입력 : ))
a1_list = []

for i in range(0, len(a1)):
    if a1[i].isalpha():
        a3 = chr(ord(a1[i]) + a2)
    else:
        a3 = chr(ord(a1[i]))

    if a1[i].isupper():
        if a3 > chr(ord('Z')):
            a3 = chr(ord(a1[i]) + a2 - 26)
    elif a1[i].islower():
        if a3 > chr(ord('z')):
            a3 = chr(ord(a1[i]) + a2 - 26)

    a1_list.append(a3)

result = ''.join(a1_list)
print(result)
'''



