
import threading
import time
"""
*Thread bir fonksiyonla çalışır.
*Threading task(görev) ları eş zamanlı olarak çalıştırma yöntemidir.
*Programın tamamı main threaddir. t ise seperate threaddir.
*Thread bir yemek yaparken bütün malzeleri sırasına göre değil de birden boca etmektir
yani bazı işlemleri beklemez en hızlı şekilde diğer işlemleri yapar fakat bu durum manipüle 
edilebilir.
"""

def sleeper (n, name):
    print('Hi, I am {}. Going to sleep to 5 seconds\n'.format(name) )
    
    time.sleep(n)
    print('{}. has woken up from sleep \n'.format(name))

threads_list = []

start = time.time()
for i in range(5):
    t = threading.Thread(target=sleeper, name = 'thread{}'.format(i), args= (5, 'thread{}'.format(i)))
    threads_list.append(t)
    t.start()
    print('{} has started'.format(t.name))

for t in threads_list:
    t.join()


end = time.time() 
print('time taken: {}'.format(end-start))

print('All five threads have finished their jobs')

"""
def sleeper (n, name):
    print('Hi, I am {}. Going to sleep to 5 seconds\n'.format(name) )
    
    time.sleep(n)
    print('{}. has woken up from sleep \n'.format(name))

start = time.time()
for i in range(5):
    print('iteration {} has started'.format(i))
    sleeper(5, i)

end = time.time() 
print('time taken: {}'.format(end-start))
"""