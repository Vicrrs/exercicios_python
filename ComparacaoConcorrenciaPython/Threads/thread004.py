from threading import Thread

def process_lines(start_line, end_line, filename):
    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            if start_line <= i < end_line:
                print(f"Processing line {i}: {line.strip()}")

filename = 'example.txt'
thread_count = 4
lines_per_thread = 25
threads = []

for i in range(thread_count):
    start_line = i * lines_per_thread
    end_line = start_line + lines_per_thread
    thread = Thread(target=process_lines, args=(start_line, end_line, filename))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
