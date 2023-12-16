def sjf(processes):
    # Sort processes based on burst time (shortest job first)
    processes.sort(key=lambda x: x[1])

    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Calculate waiting time for each process
    for i in range(1, n):
        waiting_time[i] = waiting_time[i-1] + processes[i-1][1]

    # Calculate turnaround time for each process
    for i in range(n):
        turnaround_time[i] = waiting_time[i] + processes[i][1]

    return waiting_time, turnaround_time

# Example usage:
processes_sjf = [(1, 6), (2, 8), (3, 7), (4, 3)]
waiting_time_sjf, turnaround_time_sjf = sjf(processes_sjf)

print("SJF Scheduling:")
print("Process\tWaiting Time\tTurnaround Time")
for i in range(len(processes_sjf)):
    print(f"{processes_sjf[i][0]}\t{waiting_time_sjf[i]}\t\t{turnaround_time_sjf[i]}")