# 운영체제 학습 및 실습 예제

이 저장소는 운영체제의 기본 개념을 이해하고, 다양한 실습 예제를 통해 프로세스, 스레드, 프로세스 간 통신, 동기화, 메모리 관리, 파일 시스템, 숫자 체계, 그리고 CPU 스케줄링 등의 주제를 다루기 위한 예제들을 모아놓은 프로젝트입니다.

## 목차

- [프로세스 관리](#프로세스-관리)
- [스레드](#스레드)
- [프로세스 간 통신](#프로세스-간-통신)
- [동기화](#동기화)
- [메모리 관리](#메모리-관리)
- [파일 시스템](#파일-시스템)
- [숫자 체계](#숫자-체계)
- [CPU 스케줄링](#cpu-스케줄링)
- [사용 기술 및 라이브러리](#사용-기술-및-라이브러리)
- [실행 방법](#실행-방법)

## 프로세스 관리

이 섹션은 프로세스 생성, 프로세스 ID 확인, 시그널 처리, 그리고 부모-자식 프로세스 관계에 관한 예제들을 포함합니다.

- **01.py**: SIGINT(키보드 인터럽트) 시그널을 처리하는 예제  
- **02.py**: 현재 실행 중인 파이썬 프로세스의 ID를 출력하는 예제  
- **03.py**: psutil 라이브러리를 활용해 프로세스 목록 중 특정 프로세스(예, Chrome)를 검색하는 예제  
- **04.py**: 프로세스의 상태, 부모 및 자식 프로세스 정보를 조회하는 예제  
- **05.py, 06.py**: multiprocessing 모듈을 이용한 자식 프로세스 생성 및 부모-자식 관계 확인 예제  
- **07.py**: 서로 다른 함수를 실행하는 여러 자식 프로세스를 생성하여 프로세스 아이디와 부모 아이디를 출력하는 예제  
- **08.py**: 현재 파이썬 프로그램에 해당하는 프로세스의 정보를 출력하는 예제  
- **11.py**: 무한 반복하며 각 프로세스(콜라, 사이다, 쥬스)의 아이디를 출력하고, 키보드 인터럽트로 종료하는 예제

## 스레드

프로세스와 달리 가벼운 실행 단위인 스레드를 활용한 예제들을 다룹니다.

- **09.py**: 스레드를 생성하고, 프로세스와 스레드의 아이디를 확인하는 예제  
- **10.py**: 데몬 스레드를 활용하여 백그라운드 작업을 수행하는 예제

## 프로세스 간 통신

여러 프로세스 간에 데이터를 주고받는 방법을 보여주는 예제입니다.

- **12.py**: Pipe를 사용해 부모와 자식 프로세스 간 데이터를 주고받는 예제  
- **13.py**: 파일을 매개체로 프로세스 간 데이터를 공유하는 예제

## 동기화

여러 프로세스 또는 스레드가 동일한 공유 자원에 접근할 때 발생할 수 있는 경쟁 조건을 방지하는 방법을 설명합니다.

- **14.py**: 공유 변수에 대한 경쟁 상태 발생 예제  
- **15.py**: multiprocessing 환경에서 Lock을 이용해 동기화를 구현한 예제  
- **16.py**: 스레드 환경에서 Lock을 활용해 동기화를 구현한 예제

## 메모리 관리

메모리 사용 및 관리, 그리고 가비지 컬렉션과 관련된 개념들을 다루는 예제입니다.

- **17.py**: 변수의 참조와 복사, 그리고 레퍼런스 카운트의 변화 예제  
- **18.js**: JavaScript에서 객체의 참조와 가비지 컬렉션 과정을 설명하는 예제  
- **19.py**: `memoryview`를 통한 메모리 접근 및 객체 주소 출력 예제  
- **20.py**: psutil 라이브러리를 이용하여 시스템 메모리 사용량을 조회하는 예제  
- **21.py**: tracemalloc 모듈을 사용한 메모리 사용량 추적 예제

## 파일 시스템

파일 입출력, 파일 검색, 경로 처리 등 파일 시스템 관련 작업을 다룹니다.

- **23.py**: 파일 생성, 쓰기, 그리고 glob 모듈을 활용한 파일 목록 조회 예제  
- **24.py**: 파일 읽기 시 발생할 수 있는 예외 처리 예제  
- **25.js**: Node.js를 사용한 파일 읽기 및 쓰기 예제  
- **26.py**: os 모듈을 사용한 디렉토리 탐색 및 파일/디렉토리 여부 확인 예제  
- **27.py**: 재귀적으로 특정 확장자를 가진 파일을 검색하고 내용을 읽는 예제  
- **28.py**: shutil 모듈을 활용한 파일 복사 및 이동 예제  
- **29.py**: pathlib 모듈을 통한 파일 경로 객체 처리 예제

## 숫자 체계

운영체제 공부에 필요한 숫자 체계 관련 변환 예제를 포함합니다.

- **30.py**: 정수를 이진수, 8진수, 16진수로 변환하는 예제

## CPU 스케줄링

CPU 스케줄링 알고리즘을 이해하기 위한 예제들을 제공합니다.

- **31.py**: ProcessPoolExecutor를 사용한 병렬 작업 처리 예제  
- **32.py**: 라운드 로빈 스케줄링 알고리즘을 구현하여 프로세스의 대기 시간과 반환 시간을 계산하는 예제

## 사용 기술 및 라이브러리

- Python (multiprocessing, threading, psutil, tracemalloc 등)
- JavaScript (Node.js)
- 파일 시스템 관련 모듈 (os, glob, pathlib, shutil)

이 저장소의 예제들을 통해 운영체제의 기본 개념을 실습하며, 직접 코드를 실행함으로써 실제 운영체제가 작동하는 원리를 이해하는 데 도움을 받을 수 있습니다.

## 실행 방법

- **Python 실행**  
  - Python 3.x 환경이 필요합니다.  
  - 필요한 라이브러리가 있을 경우, 예를 들어 `psutil`은 아래 명령어로 설치할 수 있습니다:  
    ```
    pip install psutil
    ```  
  - 각 예제 파일이 저장된 디렉토리에서 터미널 또는 명령 프롬프트를 열고 다음과 같이 실행합니다:  
    ```
    python 파일이름.py
    ```

- **JavaScript 실행 (Node.js)**  
  - Node.js가 설치되어 있어야 합니다.  
  - 각 예제 파일이 저장된 디렉토리에서 터미널을 열고 다음과 같이 실행합니다:  
    ```
    node 파일이름.js
    ```

이 저장소의 예제 코드를 직접 실행하여 운영체제의 동작 원리와 관련 기능들을 체험할 수 있습니다.