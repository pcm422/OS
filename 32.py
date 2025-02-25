def roundrobin(processes, burst_time, time_quantum):
    n = len(processes)
    remaining_time = list(burst_time)
    turnaround_time = [0] * n
    waiting_time = [0] * n

    queue = []
    time = 0

    while True:
        all_completed = True # 모든 프로세스 종료시 반복문 종료를 위한 플래그

        for i in range(n):
            if remaining_time[i] > 0:
                all_completed = False

                if remaining_time[i] > time_quantum:
                    time += time_quantum
                    remaining_time[i] -= time_quantum
                    queue.append(i)
                else:
                    time += remaining_time[i]
                    turnaround_time[i] = time
                    waiting_time[i] = turnaround_time[i] - burst_time[i]
                    remaining_time[i] = 0

        if all_completed:
            break

    print("Process\tTurnaround Time\tWaiting Time")
    for i in range(n):
        print(f"P{i+1}\t\t{turnaround_time[i]}\t\t{waiting_time[i]}")

# 함수 호출해 기능 확인하기
processes = [1, 2, 3]
burst_time = [10, 5, 18]
time_slice = 2

roundrobin(processes, burst_time, time_slice)