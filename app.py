import time
import psutil

def display_usage(cpu_usage, mem_usage, bars=50):
    cpu_percent = cpu_usage / 100
    cpu_bar = '█' * int(cpu_percent * bars) + '-' * int(bars - int(cpu_percent * bars))

    mem_percent = mem_usage / 100
    mem_bar = '█' * int(mem_percent * bars) + '-' * int(bars - int(mem_percent * bars))

    print(f"\rCPU Usage: |{cpu_bar}| {cpu_usage:.2f}% ", end='')
    print(f"MEM Usage: |{mem_bar}| {mem_usage:.2f}% ", end='\r')



while True:
    display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent, 30)
    time.sleep(0.5)