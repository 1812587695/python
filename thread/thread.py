import threading
import time


def get_detail_html(url):
    print("get_detail_html start" , url)
    time.sleep(2)
    print("get_detail_html end" , url)

def get_detail_url(url):
    print("get_detail_url start" , url)
    time.sleep(4)
    print("get_detail_url end" , url)

if __name__ == "__main__":
    thread1 = threading.Thread(target=get_detail_html, args=("1",))
    thread2 = threading.Thread(target=get_detail_url, args=("2",))

    # thread1.setDaemon(True) # 守护进程，只有当其他进程结束他才会结束，不管他本身是否在执行，虽然他执行需要2秒，依然要等待get_detail_url函数4秒时间执行完成才结束
    # thread2.setDaemon(True) # 守护进程，只有当其他进程结束他才会结束，不管他本身是否在执行，虽然他执行需要4秒，但是get_detail_url函数2秒时间执行完成就结束，不会继续执行他自己了

    start_time = time.time()

    thread1.start() # 线程开始
    thread2.start()

    thread1.join() # 线程阻塞
    thread2.join()

    print("主线程 {}" . format(time.time() - start_time))












