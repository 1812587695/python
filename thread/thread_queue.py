import threading
import time


class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)
    def run(self):
        print("get_detail_html start")
        time.sleep(2)
        print("get_detail_html end")


class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)
    def run(self):
        print("get_detail_url start")
        time.sleep(4)
        print("get_detail_url end")


if  __name__ == "__main__":
    thread1 = GetDetailHtml("get_detail_html")
    thread2 = GetDetailUrl("get_detail_url")
    start_time = time.time()

    thread1.start()  # 线程开始
    thread2.start()

    thread1.join()  # 线程阻塞
    thread2.join()

    print("主线程 {}".format(time.time() - start_time))







