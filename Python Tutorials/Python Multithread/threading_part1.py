
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

# initialize thread
t = threading.Thread(target=sleeper, name = 'thread1', args = (5, 'thread1'))

# run a thread
t.start()
"""
*Burada main threada dönüldü ve main thread, t threadinin çalışmasını bitirmesini beklemedi.
*Eğer join methodu eklersek, sleeper fonksiyonunundaki taskları gerçekleştiren t threadi,
işlemini bitirmeden başka bir threade(buradaki farklı thread main threaddir.) geçmez.
"""

t.join()
print('hello')
print('hello')