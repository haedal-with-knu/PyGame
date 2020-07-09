#함수 객체지향 메서드
'''def add(a,b):
    c = a+b
    return c

def main():
    x = 3
    y = 5
    z = add(x,y)
    print(z)

if __name__ == "__main__":
    main()'''

'''def main():
    total = 0
    for index in range(100):
        total += index
    print(index)
    print(total)

if __name__ == "__main__":
    main()'''

'''message = "Hello"

def say():
    print("say: message="+message)

def main():
    say()
    print("main:message="+message)

if __name__ == "__main__":
    main()'''

'''message = "Hello"

def say():
    print("say:message ="+message)
    obj_id = id(message)
    print("say:id(message) ={0:d}".format(obj_id))

def main():
    say()
    print("main:message="+message)
    obj_id = id(message)
    print("say:id(message) ={0:d}".format(obj_id))
if __name__ == "__main__":
    main()'''

'''class Person:
    def __init__(self,name):
        self.name = name

he = Person("smith")
she = Person("alice")

print(he.name)
print(she.name)'''

'''class Pen:
    def __init__(self, length, color):
        self.length = length
        self.color = color

pen1 = Pen(5,"red")
pen2 = Pen(5,"black")

print(pen1.length, pen1.color)
pen1.length = 4.8
print(pen1.length, pen1.color)'''

'''import pygame
class MyRect(pygame.Rect):
    def flip(self):
        self.width, self.height = (self.height,self.width)

r = MyRect(30,20,20,20)
print(r.size)
r.flip()
print(r.size)'''

class Audio:
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
obj.set_volume(10)