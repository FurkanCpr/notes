"""
def run(self):
    try:
        if self._target:
            self._target(*self._args, **self._kwargs)

    finally:
        del self._target, self._args, self._kwargs

import time
import threading

class MyThread(threading.Thread):
    def run(self):
        print('{} has started!'.format(self.getName()))
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)

        finally:
            del self._target, self._args, self._kwargs

        print('{} has finished!'.format(self.getName()))

def sleeper (n, name):
    print('Hi, I am {}. Going to sleep to 5 seconds\n'.format(name))
    
    time.sleep(n)
    print('{}. has woken up from sleep \n'.format(name))

for i in range(4):
    t = MyThread(target=sleeper, name = 'thread {}'.format(i+1), args= (3, 'thread {}'.format(i+1)))

    t.start()
"""

import time
import threading

class MyThread(threading.Thread):   
    def __init__(self, number, func, args):
        threading.Thread.__init__(self)
        self.number = number  
        self.func = func
        self.args = args

    def run(self):
        print('thread {} has started'.format(self.number))
        self.func(*self.args)
        print('thread {} has finished'.format(self.number))


def double(number, cycles):
    for i in range(cycles):
        number += number
    print(number)

threading_list = []
 
for i in range(50):
    t = MyThread(number = i +1, func = double, args = [i, 3])

    threading_list.append(t)
    t.start()

for t in threading_list:
    t.join()