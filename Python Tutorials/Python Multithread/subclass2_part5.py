import time
import threading

class MyThread(threading.Thread):
    def __init__(self, number, style, *args, **kwargs):
        #super() ifadesi, temel sınıfta tanımlanan bir fonksiyonun içeriğine ekleme yapmaya yarar.Yani temel sınıftaki fonksiyonun çalışmasını sağlar.
        super(MyThread, self).__init__(*args, **kwargs)
        self.number = number
        self.style = style


    def run(self,*args, **kwargs):
        print('thread starting')
        super(MyThread, self).run(*args, **kwargs)
        print('thread has ended')

def sleeper(num,style):
    print('we are sleeping for {} seconds as {}'.format(num, style))
    time.sleep(num)

t = MyThread(number = 3, style = 'yellow', target = sleeper, args = [3, 'yellow'])

t.start()

print(t.style)
print(t.number)