import threading
import os

def func():
    print("실험용으로 대충 만든 함수")
    print("프로세스 아이디 :", os.getpid())
    print("스레드 아이디 :", threading.get_native_id())

if __name__ == "__main__":
    print("09.py 프로세스 아이디 :", os.getpid())
    thread1 = threading.Thread(target=func)
    thread1.start()