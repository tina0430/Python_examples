import threading, time

def func(id):
    for i in range(1, 6):
        print('id={} --> {}'.format(id, i))
        time.sleep(0.5)

#thread 사용 X -> 순자척
func(1)
func(2)

#thread 사용 O
print('스레드 사용=======')
th1 = threading.Thread(target=func, args=('일'))
th2 = threading.Thread(target=func, args=('이'))
th1.start()
th2.start()
th1.join()
th2.join()