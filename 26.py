# os 파일 시스템 관련 함수
import os

pwd = "/Users/bakcheolmin/Desktop/oz_08/os"

# 디렉토리 내부 리스트 업
filenames = os.listdir(pwd)
# print(filenames)

# 디렉토리인지 아닌지 여부
print(os.path.isdir(filenames[0]))
print(os.path.isdir(pwd + "/anony"))

# 파일인지 아닌지 여부
print(os.path.isfile(filenames[0]))
print(os.path.isfile(pwd + "/anony"))

# 파일이름과 확장자 분리
filepath = pwd + "/" + filenames[0]
print(filepath)
name, ext = os.path.splitext(filepath)
print(name)
print(ext)
