
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL) # ctrl + c로 종료

import pyautogui
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from threading import Thread

THREADS_NUMBER = 1
INPUT_LIMIT = int( 10000 / THREADS_NUMBER )

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument('--incognito')

_write = ''.join('.' for _ in range(INPUT_LIMIT))

while True:
    try:
        lst_threads = [
            Thread(target=(lambda x: pyautogui.write(x, interval=0.001)), args=(_write, ))
            for _ in range(THREADS_NUMBER)
        ]

        browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_option)
        browser.get('https://popcat.click/')

        for worker in lst_threads:
            worker.start()
            print("thread start")

        time.sleep(0.1)

        for worker in lst_threads:
            worker.join()

    finally:
        browser.quit()
        time.sleep(0.1)
