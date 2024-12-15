# multi threading
from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(10):
            print('Hello')
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(10):
            print('Hi')
            sleep(1)



t1 = Hello()
t2 = Hi()
t1.start()
sleep(0.2)
t2.start()
t1.join()
t2.join()

print(current_thread())
print('end')



def start_counting():
    for i in range(1,11):
        print(i)
        sleep(1)

def remain_counting():
    for i in range(90,101):
        print(i)
        sleep(1)


t1 = Thread(target=start_counting)
t2 = Thread(target=remain_counting)
t1.start()
t2.start()

# multi threading end