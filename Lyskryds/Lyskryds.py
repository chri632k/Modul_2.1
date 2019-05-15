from random import random
from gpiozero import LED
from time import sleep

led1=LED(21) #Red
led2=LED(20) #Yellow
led3=LED(16) #Green

led7=LED(7) #Red
led8=LED(25) #Green

led4=LED(13) #Red
led5=LED(6) #Yellow
led6=LED(5) #Green

led9=LED(26) #Red
led10=LED(19) #Green

led11=LED(8) #Not in use



#def o-3=16-20-21
#def 4-7=17-27-22

def state0():
    print('\033[1;31;41m') #red
    led1.on()
    led4.on()
    led7.on()
    led9.on()
    sleep(2)
    led7.off()
    return state1()

def state1():
    print('\033[1;33;43m') #red+yellow
    led2.on()
    led8.on()
    sleep(2)
    led1.off()
    led2.off()
    return state2()

def state2():
    print('\033[1;32;42m') #green
    led3.on()
    sleep(2)
    led3.off()
    return state3()

def state3():
    print('\033[1;33;43m') #yellow
    led2.on()
    sleep(2)
    led2.off()
    led8.off()
    return state4()
#2.lys
def state4():
    print('\033[1;31;41m') #red
    led4.on()
    led1.on()
    led7.on()
    sleep(2)
    return state5()

def state5():
    print('\033[1;33;43m') #red+yellow
    led5.on()
    led9.off()
    led10.on()
    sleep(2)
    led4.off()
    led5.off()
    return state6()

def state6():
    print('\033[1;32;42m') #green
    led6.on()
    sleep(2)
    led6.off()
    return state7()

def state7():
    print('\033[1;33;43m') #yellow
    led5.on()
    sleep(2)
    led5.off()
    led10.off()
    led9.on()
    return state0()

    

state=state0()  #initial state
while state: state=state()  #launch state mashine
print('Done with state')
