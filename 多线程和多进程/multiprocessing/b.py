from multiprocessing import Process
import time
import random


class Piao(Process):
    def __init__(self, name):
        self.name = name
        super().__init__()

    def run(self):
        print('%s is piaoing' % self.name)
        time.sleep(random.randrange(1, 3))
        print('%s is piao end' % self.name)


if __name__ == '__main__':
    p = Piao('egon')
    p.start()
    p.join(0.0001)  # 等待p停止,等0.0001秒就不再等了
    print('开始')
