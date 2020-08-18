# 동영상편집 사이트(https://ezgif.com/video-to-gif)
import random
a = input("1. 연금복권   2. 로또복권")
if a == '1':
    Lotto = []
    for j in range(5):
        c= random.randint(1,5)
        for i in range(6):
            b= random.randint(0,9)
            Lotto.append(b)
        print(c,Lotto)
        del Lotto[:]

elif a == '2':
    Lotto = []
    for i in range(5):
        while len(Lotto) < 6:
            b = random.randint(1,45)
            if b not in Lotto:
                Lotto.append(b)
            else:
                continue
        print(sorted(Lotto))
        del Lotto[:]