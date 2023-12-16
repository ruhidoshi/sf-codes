def non_preemptive_priority(processes):
    # Sort processes based on priority (lower priority value has higher priority)
    processes.sort(key=lambda x: x[2])

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
processes_priority = [(1, 6, 2), (2, 8, 1), (3, 7, 3), (4, 3, 4)]
waiting_time_priority, turnaround_time_priority = non_preemptive_priority(processes_priority)

print("Non-Preemptive Priority Scheduling:")
print("Process\tWaiting Time\tTurnaround Time")
for i in range(len(processes_priority)):
    print(f"{processes_priority[i][0]}\t{waiting_time_priority[i]}\t\t{turnaround_time_priority[i]}")
