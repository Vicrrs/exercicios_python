from threading import Thread

def calculate_sum(numbers, result):
    result.append(sum(numbers))

numbers = range(1, 10001)
result = []
threads = []

for i in range(10):
    thread = Thread(target=calculate_sum, args=(numbers[i*1000:(i+1)*1000], result))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

total_sum = sum(result)
print(total_sum)
