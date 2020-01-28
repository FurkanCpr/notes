# FIFO: first in first out, LIFO: last in first out, Priority: is just priority

# import the libraries 
import queue
import threading
import time
"""
#FIRST EXAMPLE

#Create an instance of queue. This is FIFO queue. Default type of queue.
q = queue.Queue()

 # If you initialize the queue now we want to put items or actions into this queue.
 # So we have put things into a queue
q.put(5)
q.put(4)
q.put('ali')

#Çift parantez atılırsa parantez içerisindeki bütün argümanları alır.
q.put((8,4-3,'veli'))

# q.get() aksiyonu q'daki itemleri toplar. Eğer 4 kere q.put() işlemi ve 3 kere q.get() yaparsak q.empty() = False çıkar.
# Nedeni ise 4. q.put() işlemi q.get() komutu ile alınmadığı için q boş olmaz. True olması için q.put() kadar q.get() olmalı. 
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.empty())
"""
"""
#SECOND EXAMPLE

# First in first out means the first item put in will be the first item we get.
q1 = queue.Queue()
for i in range(5):
    q1.put(i)

# İlk 5 itemi q1.put() dan alır ve döngüyü bitirir.
# The reason for use empty(), if we try to use q.get() and q is empty our program will block
while not q1.empty():
    print(q1.get(), end = '   ')
"""

"""
#THIRD EXAMPLE

# We'll all this function putting_thread because we're going to be putting items into the queue and this function has q parameter.


q3 = queue.Queue()
q3.put(1000)

print(q3.get())
print('first item gotten')

# Never hit the print finished because out program sort of freezes that print q.get() this is known as blocking now.
# Bunu tetikleyen ise q.get() 2.item olmadığından item alamıyor ve blocking operasyonu gerçekleşiyor.
# What happens is, usually we have a different thread putting items into queue and another thread pulling out items.
# So that how it's usually resolved we have another thread sort of putting in items and another thread sort of pulling our items.
# So it keeps that balance but here we're not using any thread so this will indefinitely(süresiz) freeze.
print(q3.get())
print('finished')
"""

"""
#FOURTH EXAMPLE

# So how we can sort of take care of freeze problem using threads and so how we can actually prevent this problem from happening?
# putting_thread fonksiyonu q4 argumanını almalı.
def putting_thread(q4): 
    while True:
        print('starting thread')
        time.sleep(10)
        q4.put(2)
        print('put something')

q4 = queue.Queue()
t = threading.Thread(target=putting_thread, args=(q4,), daemon=True).start()

q4.put(2)

print(q4.get())
print('first item gotten')

# İlk item main threadden alındıktan sonra diğer threadde stucklanır ve 10 saniye bekler. Sonra diğer item de alınır ve kod sonlanır.
print(q4.get())
print('finished')
"""