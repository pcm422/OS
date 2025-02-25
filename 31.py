import concurrent.futures
import time

def task(name):
    time.sleep(0.5)
    return f"{name} 작업 완료"

if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        future_name = {
            executor.submit(task, f"task-{i}"): f"task-{i}" for i in range(5)
        }

        # 작업이 완료된 순서대로 결과 출력
        for future in concurrent.futures.as_completed(future_name):
            name = future_name[future]
            try:
                result = future.result()
                print(f"{name} : {result}")
            except Exception as e:
                print(e)