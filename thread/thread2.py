import threading, time


def run(n):
    # 获得信号量，信号量减一
    semaphore.acquire()
    time.sleep(1)
    print("run the thread: %s" % n)

    # 释放信号量，信号量加一
    semaphore.release()
    #semaphore.release()    # 可以多次释放信号量，每次释放计数器+1
    #semaphore.release()    # 可以多次释放信号量，每次释放计数器+1


if __name__ == '__main__':

    num = 0
    semaphore = threading.Semaphore(10)  # 最多允许2个线程同时运行(即计数器值)；在多次释放信号量后，计数器值增加后每次可以运行的线程数也会增加
    for i in range(20):
        t = threading.Thread(target=run, args=(i,))
        t.start()
# print(threading.active_count() ,"------------")
while threading.active_count() != 1:
    pass  # print threading.active_count()
else:
    print('----all threads done---')
    print(num)