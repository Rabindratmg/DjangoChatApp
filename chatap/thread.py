import threading
import time

class ThreadExample(threading.Thread):

    def run(self):
        try:
            print("thread has been executed")
            for i in range(0,10):
                print(i)
                time.sleep(1)

        except Exception as e:
            print(e)
