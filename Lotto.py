# 로또 번호 생성
'''
import random
a = int(input("얼마치사실껀가요?"))

Lotto_List = []
for i in range(a):
    for j in range(6):
        b = random.randint(1,45)
        if b not in Lotto_List:
            Lotto_List.append(b)

    print(sorted(Lotto_List))
    Lotto_List = []
'''
import random

Lotto = []
for i in range(6):
    b = random.randint(0,9)
    Lotto.append(b)
print(Lotto)
c = random.randint(1,5)
print(c)

