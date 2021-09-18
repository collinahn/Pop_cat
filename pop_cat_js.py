
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL) # ctrl + c로 종료

import pyautogui
import time
import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from threading import Thread

THREADS_NUMBER = 1
INPUT_LIMIT = int( 10000 / THREADS_NUMBER )

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument('--incognito')


POP_CNT = 0
TIME_EXEC = time.time()

JS_SCRIPT = \
'''var event = new KeyboardEvent('keydown',{
    key:'..',
    ctrlKey:true,
});
undefined
setInterval(function(){
    for(i=0;i<1000;i++){
        document.dispatchEvent(event);
    }
},2000);
'''

while True:
    TIME_EXEC_ONCE = time.time()
    try:
        browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_option)
        browser.get('https://popcat.click/')

        time.sleep(1000)

        pyautogui.press("f12")
        time.sleep(1)

        pyautogui.write(JS_SCRIPT, interval=0.0)

        pyautogui.press("enter")

        time.sleep(100)



    finally:
        browser.quit()
        time.sleep(10)


    print("\n\n\n-------------INFO-------------")
    TIME_NOW = time.time()
    print("Time Executed: " + str(TIME_NOW - TIME_EXEC_ONCE))
    POP_CNT += INPUT_LIMIT * THREADS_NUMBER
    print("TOTAL POP COUNT is " + str(POP_CNT))
    print("Program Executed: " + str(datetime.timedelta(seconds=TIME_NOW - TIME_EXEC)))
    print("=============INFO=============\n\n\n")