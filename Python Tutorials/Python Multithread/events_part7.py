import threading
import queue
import numpy as np
import time

"""

# Flag = True
event.set()

# Flag = False
event.clear()  

# Flag true olana kadar blocklar. 
event.wait()
"""
def flag():
    time.sleep(3) 
    event.set()
    print('starting countdown')
    time.sleep(7)
    print('event is cleared')

    #Diğer thread blocklanır.
    event.clear()

def start_operations():
    event.wait()
    while event.is_set():
        print('starting random integer task')
        x = np.random.randint(1,30)
        time.sleep(.5)
        if x == 29:
            print("True")
    print('Event has been cleared, random operation stops ')
# t2 threadi hemen başlamıcak çünkü event.wait() den dolayı blocklu şuan. t1 threadindeki event.set() komutunu beklemek zorunda.
event = threading.Event()
t1 = threading.Thread(target=flag)
t2 = threading.Thread(target=start_operations)

t1.start()
t2.start()
