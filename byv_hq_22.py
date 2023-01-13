# При старті додатку запускаються три потоки. Перший 
# потік заповнює список випадковими числами. Два інші потоки 
# очікують на заповнення. Коли перелік заповнений, обидва 
# потоки запускаються. Перший потік знаходить суму елементів 
# списку, другий потік знаходить середнє арифметичне значення 
# у списку. Отриманий список, сума та середнє арифметичне 
# виводяться на екран.

import threading, random
# import time
list_int=[]
lock = threading.Lock()

def app():
    for i in range(0,1000):
        value=random.randint(1,9)
        list_int.append(value)
    print('Stop app finish')
        
def get_sum(list_int: list):
    # sm.acquire()
    print('Start get_sum')
    return sum(list_int)
def get_average(list_int: list):
    # sm.acquire()
    print('Start get_averag')
    return sum(list_int)/len(list_int)
th1 = threading.Thread(target=app)
th2 = threading.Thread(target=get_sum,args=(list_int) )
th3 = threading.Thread(target=get_average, args=(list_int))
# app()


th1.start()
th2.start()
th3.start()


lock.acquire() # Выполнит блокировку данного участка кода
th1.join()

lock.release()
# if sm.acquire():

th2.join()
th3.join()
print(list_int)
print(get_sum(list_int), get_average(list_int))
# t2 = time.time()
# print('time:', t2-t1)

# print(s1+s2+s3+s4)