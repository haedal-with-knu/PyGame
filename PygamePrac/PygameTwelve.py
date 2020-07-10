#함수 객체지향 메서드

'''def add(a,b): #함수정의
    c = a+b
    return c  #반환받는 리턴값

def main():
    x = 3
    y = 5
    z = add(x,y)
    print(z)

if __name__ == "__main__":   #__name__ == "__main__"은 인터프리터에서 직접 실행했을 경우에만 if문 내의 코드르 실행하라
    main()'''

'''def main(): 
    total = 0
    for index in range(100):
        total += index
    print(index)
    print(total)

if __name__ == "__main__":
    main()'''

'''message = "Hello" #전역변수 message를 여러 함수에서 인용하는 구문

def say():
    print("say: message="+message)

def main():
    say()
    print("main:message="+message)

if __name__ == "__main__":
    main()'''

'''message = "Hello" #전역변수 선언

def say():
    print("say:message ="+message) 
    obj_id = id(message) #message 변수의 주소값을 반환한다.
    print("say:id(message) ={0:d}".format(obj_id))

def main():
    say()
    print("main:message="+message)
    obj_id = id(message)
    print("say:id(message) ={0:d}".format(obj_id))
if __name__ == "__main__": #주소값이 서로서로 같은지 확인한다.
    main()'''

'''class Person: #각 이름이 class를 통해 출력되는지 확인한다.
    def __init__(self,name):
        self.name = name

he = Person("smith")
she = Person("alice")

print(he.name)
print(she.name)'''

'''class Pen: #길이와 색을 설정해주는 class
    def __init__(self, length, color):
        self.length = length
        self.color = color

pen1 = Pen(5,"red")
pen2 = Pen(5,"black")

print(pen1.length, pen1.color)
pen1.length = 4.8  # 변수값을 바꿔준다
print(pen1.length, pen1.color)'''

'''import pygame # flip함수에 의해 프린트되는 것을 확인한다.
class MyRect(pygame.Rect):
    def flip(self):
        self.width, self.height = (self.height,self.width)

r = MyRect(30,20,20,20)
print(r.size)
r.flip()
print(r.size)'''

#클래스와 상속에 대해 알아보기

'''
class Audio: #클래스를 지정하고 전역에서 사용하기.
    def __init__(self, power, volume):
        self.power =power
        self.volume = volume

    def switch(self, on_off):
        self.power = on_off

    def set_volume(self,vol):
        self.volume =vol

    def tune(self):
        str = "LaLaLa..." if self.power else "turn it on"
        print(str)

mp3 = Audio(False,8)
mp3.set_volume(12)
mp3.tune()
'''
'''
class TV:
    def __init__(self,power,volume, size):
        self.power = power
        self.volume = volume
        self.size = size

    def switch(self,on_off):
        self.power = on_off
    def set_volume(self,vol):
        self.volume = vol
    def watch(self):
        str = "have fun!" if self.power else "switch on"
        print(str)

obj = TV(True, 14, 40)
obj.switch(True)
obj.watch()
obj.set_volume(10)'''

#부모 클래스를 지정하고 자식클래스에 넣어주기
class AudioVisual:#부모클래스
    def __init__(self,power, volume):
        self.power= power
        self.volume = volume
    def switch(self,on_off):
        self.power =on_off
    def set_volume(self,vol):
        self.volume =vol

class Audio(AudioVisual):#자식클래스
    def __init__(self,power, volume):
        super().__init__(power,volume)
    def tune(self): #자식클래스만의 함수
        str = "La la la..." if self.power else "turn it on"
        print(str)

class TV(AudioVisual):#자식클래스
    def __init__(self,size,volume,power):
        super().__init__(power,volume)
        self.size = size
    def watch(self):#자식클래스만의 함수
        str = "have fun" if self.power else "switch on"
        print(str)

obj1 = TV(False, 12, 40)
obj1.switch(True) # self.power를 공유해서 switch에서 True 가 TV의 power에 True가 들어가게됩니다.
obj1.watch()

obj2 = Audio(True,15)
obj2.set_volume(6)
obj2.tune()