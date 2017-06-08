# coding:utf-8
'''
守护进程与非守护进程
'''
import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',             #level: 设置日志级别，默认为logging.WARNING
                    )
#默认情况下，logging将日志打印到屏幕，日志级别为WARNING
#日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET，当然也可以自己定义日志级别。

def daemon():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join(1)
print 'd.isAlive',d.isAlive()
t.join()
#
# import logging
#
# logging.debug('This is debug message')
# logging.info('This is info message')
# logging.warning('This is warning message')