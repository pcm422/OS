# 내 파이썬 프로그램의 이름을 알아보자
# 모든 프로세스를 조회한뒤 이 파일의 id가 같을시 출력하는 코드
import os
import psutil

for proc in psutil.process_iter():

    ps_name = proc.name()
    ps_id = proc.pid

    if ps_id == os.getpid():
        print(ps_name, ps_id)