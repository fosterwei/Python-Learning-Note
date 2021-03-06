#添加多线程
import threading
def thread_job():
  print 'This is an added Thread,number is %s' % threading.current_thread #线程的名称
  
def main():
  added_thread=threading.Thread(target=thread_job) #定义一个新的thread
  add_thread.start()#开始运行thread
  print threading.active_count()#线程数量
  print threading.enumerate()#哪两个线程
  print threading.current_thread()#现在正在运行的线程
  
if __name__=='__main__'
  main()

#2  join功能 要等T1全部运行完才开始其他的  所有线程一步一步的实行

import threading
import time
def thread_job():
  print 'T1 start\n'
  for i in range(10):
    time.sleep(0.1)
    print "T1 finish\n"
def T2_job():
  print 'T2 start\n'
  print 'T2 finish\n'
def main():
  add_thread=threading.Thread(target=thread_job,name='T1')#定义一个新的thread
  thread2=threading.Thread(target=T2_job,name='T2')
  add_thread.start()#开始运行thread
  thread2.start()
  added_thread.join()#要等T1执行完才开始all done\n
  thread2.join()      #要等T2执行完才开始all done\n
  print 'all done\n'
if __name__=='__main__'
  main()
#实例例证
#coding:utf-8
from time import sleep,ctime
import threading

def super_player(file,time):
  for i in range(2):
    print 'Start play:%s! %s' %(file,ctime())
    sleep(time)

list={'love story.mp3':3,'avatar.mp4':5,'you and me.mp3':4}

thread=[]
files=range(len(lsit))

for file,time in list.items():  #items后数据变成[('love story.mp3',3)]字典转成列表
  t=threading.Thread(target=super_player,args=(file,time))
  threads.append(t)
  
if __name__=='__main__':
  for i in files:
    threads[i].start()
  for i in files:
    threads[i].join()
  print 'end:%s' %ctime()
  
#锁
import threading

def job1():
  global A,lock
  lock.acquire()
  for i in range(10):
    A+=1
    print job1,a
  lock.release()
def job2():
  global A,lock
  lock.acquire()
  for i in range(10):
    A+=10
    print job2,A
  lock.release()
    
if __name__=='__main__'
  lock=Threading.Lock()
  A=0
  t1=threading.Thread(target=job1)
  t2=threading.Thread(target=job2)
  t1.start()
  t2.start()
  t1.join()
  t2.join()
  
