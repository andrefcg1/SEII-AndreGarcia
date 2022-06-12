#1
""" import time

start = time.perf_counter()


def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')


do_something()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')

#2
import time
import multiprocessing

start = time.perf_counter()


def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')


p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)

p1.start()
p2.start()

p1.join()
p2.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')

#3
import time
import multiprocessing

start = time.perf_counter()


def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

processes = []

for _ in range(10):
    p = multiprocessing.Process(target=do_something)
    p.start()
    processes.append(p)

for process in processes:
    process.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)') 

#4
import time
import multiprocessing

start = time.perf_counter()


def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

processes = []

def main():
    for _ in range(10):
        p = multiprocessing.Process(target=do_something)
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')

if __name__ == '__main__':
    test()

#5
from lib2to3.pytree import _Results
import time
import multiprocessing

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ProcessPoolExecutor() as executor:
        f1 = executor.submit(do_something, 1)
        f2 = executor.submit(do_something, 1)
        print(f1.result())
        print(f2.result())

# processes = []

# for _ in range(10):
#     p = multiprocessing.Process(target=do_something)
#     p.start()
#     processes.append(p)

# for process in processes:
#     process.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)') 

#6
import time
import multiprocessing

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ProcessPoolExecutor() as executor:
    results = [executor.submit(do_something, 1) for _ in range(10)]

    for f in concurrent.futures.as_completed(results):
        print(f.result())


finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')

#7
import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = [executor.submit(do_something, sec) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result()) """

#8
import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something, secs)

        # for result in results:
        #     print(result)

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')

if __name__ == '__main__': 
    main()












