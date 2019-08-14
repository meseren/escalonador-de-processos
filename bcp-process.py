import multiprocessing
import os

def worker():
    print("Filename corresponding to the  controlling terminal:")
    print(os.ctermid())
    
    print("ID do processo:")
    print(os.getppid())
    
    print("ID of the current process group:")
    print(os.getpgrp())
    
    print("Old Priority:")
    print(os.getpriority(os.PRIO_PROCESS, os.getpid()))
    
    os.setpriority(os.PRIO_PROCESS, os.getpid(), 2)
    
    print("New Priority:")
    print(os.getpriority(os.PRIO_PROCESS, os.getpid()))
    
    print("Information identifying the current operating system:")
    print(os.uname())
    
    print("The round-robin quantum in seconds for the process with PID pid")
    print(os.sched_rr_get_interval(0))
    
    return

if __name__ == '__main__':
    jobs = []
    for i in range(1):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()


