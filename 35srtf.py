def srtf(processes):
    current_time = 0
    completed_processes = []
    remaining_time = {process["name"]: process["burst_time"] for process in processes}

    while processes:
        available_processes = [p for p in processes if p["arrival_time"] <= current_time]

        if available_processes:
            shortest_process = min(available_processes, key=lambda x: x["burst_time"])

            if remaining_time[shortest_process["name"]] == shortest_process["burst_time"]:
                # Process is starting
                waiting_time = current_time - shortest_process["arrival_time"]
                shortest_process["waiting_time"] = waiting_time

            remaining_time[shortest_process["name"]] -= 1
            current_time += 1

            if remaining_time[shortest_process["name"]] == 0:
                # Process is completed
                turnaround_time = current_time - shortest_process["arrival_time"]
                shortest_process["turnaround_time"] = turnaround_time
                completed_processes.append(shortest_process)
                processes.remove(shortest_process)
        else:
            current_time += 1

    return completed_processes

# Example usage:
processes_srtf = [
    {"name": "P1", "arrival_time": 0, "burst_time": 7},
    {"name": "P2", "arrival_time": 0, "burst_time": 5},
    {"name": "P3", "arrival_time": 0, "burst_time": 3},
    {"name": "P4", "arrival_time": 0, "burst_time": 1},
    {"name": "P5", "arrival_time": 0, "burst_time": 2},
    {"name": "P6", "arrival_time": 0, "burst_time": 1},
]

completed_processes_srtf = srtf(processes_srtf)

# Print the results with comments
print("SRTF Scheduling:")
print("Process\tWaiting Time\tTurnaround Time")
for process in completed_processes_srtf:
    print(f"{process['name']}\t{process['waiting_time']}\t\t{process['turnaround_time']}")
