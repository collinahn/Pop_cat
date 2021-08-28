
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL) # ctrl + c로 종료

import pyautogui
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import multiprocessing as mp

PROCESS_NUMBER = 3
INPUT_LIMIT = int( 10000 / PROCESS_NUMBER )

def click():
    _write = ''.join('.' for _ in range(INPUT_LIMIT))
    pyautogui.write(_write, interval=0.0001)


if __name__ == "__main__":

    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_argument('--incognito')

    while True:
        try:
            lst_process = [
                mp.Process(name="Sub", target=click)
                for _ in range(PROCESS_NUMBER)
            ]

            browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_option)
            browser.get('https://popcat.click/')

            for worker in lst_process:
                worker.start()
                print("pid: " + str(worker.pid))

            time.sleep(0.1)
            
            for worker in lst_process:
                worker.join()


        finally:
            browser.quit()
            time.sleep(0.1)
