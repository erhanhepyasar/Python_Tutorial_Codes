from time import sleep
from threading import Thread

def tekrarla(ne, bekleme):
    while True:
        print(ne)
        sleep(bekleme)

if __name__ == '__main__':
    dum = Thread(target = tekrarla, args = ("*********",1))
    tis = Thread(target = tekrarla, args = ("........",0.5))
    ah = Thread(target = tekrarla, args = ("/////////",3))

    dum.start()
    tis.start()
    ah.start()