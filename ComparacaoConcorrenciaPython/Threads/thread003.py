from threading import Thread, Lock

counter = 0
lock = Lock()

def increment_counter():
    global counter
    with lock:
        for _ in range(10_000):
            counter +=1

threads = [Thread(target=increment_counter) for _ in range(5)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(counter)
