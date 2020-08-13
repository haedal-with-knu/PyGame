import random
Lotto = []
for j in range(5):
    c= random.randint(1,5)
    for i in range(6):
        b= random.randint(0,9)
        Lotto.append(b)
    print(c,Lotto)
    del Lotto[:]


    #동영상편집 사이트(https://ezgif.com/video-to-gif)