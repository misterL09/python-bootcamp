from concurrent.futures import ThreadPoolExecutor
import time
def process(number):
    time.sleep(number)
    # value = number * 1_000_000 ** 100
    print('Finished computation')
    
if __name__=='__main__':
    start_time = time.time()

    with ThreadPoolExecutor() as executor:
        x = executor.submit(process, 3)
        y = executor.submit(input, 'Enter number: ')

    end_time = time.time()

    print("Execute time:",end_time - start_time)