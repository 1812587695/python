from multiprocessing import Process
import time


def work(name, age):
    print('task <%s> is runing <%s>' % (name, age))
    time.sleep(2)
    print('task <%s> is done <%s>' % (name, age))


if __name__ == '__main__':
    # Process(target=work,kwargs={'name':'egon'})
    p1 = Process(target=work, args=('egon', "4",))
    p2 = Process(target=work, args=('alex', "3",))
    p1.start()
    p2.start()
print('主')
