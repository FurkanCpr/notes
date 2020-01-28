import threading
"""
Locks are usually used when you have many threads trying to access same variable usually a global variable 
and they're trying to make changes to the shared global variable. So what can happen is when two threads
are making changes to variable at the same time instead of these changes stacking up we might only get one 
change to the original value
"""
x = 0
COUNT = 100000
lock = threading.Lock()
def adding_2 ():
    global x 
    with lock:
        for i in range(COUNT):
            x+= 2

def adding_3 ():
    global x
    with lock:
        for i in range(COUNT):
            x+= 3

def subtracting_4 ():
    global x
    with lock:
        for i in range(COUNT):
            x-= 4

def subtracting_1 ():
    global x
    with lock: 
        for i in range(COUNT):
            x-= 1  

t = threading.Thread(target= adding_2,)
t2 = threading.Thread(target= subtracting_4,)
t3 = threading.Thread(target= adding_3,)
t4 = threading.Thread(target= subtracting_1,)

t.start()
t3.start()
t2.start()
t4.start()

t.join()
t2.join()
t3.join()
t4.join()


print(x)