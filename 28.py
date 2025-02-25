# 파일 복사 또는 이동
import os
import shutil
from fileinput import filename

pwd = "/Users/bakcheolmin/Desktop/oz_08/os"
filenames = os.listdir(pwd)

for filename in filenames:
    if "tokyo" in filename:
        origin = os.path.join(pwd, filename)
        print(origin)
        # shutil.copy(origin, os.path.join(pwd, "copy.txt"))
        shutil.move(origin, os.path.join(pwd, "anony"))