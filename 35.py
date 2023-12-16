processes = [
    {"name": "P1", "arrival_time": 0, "burst_time": 7},
    {"name": "P2", "arrival_time": 0, "burst_time": 5},
    {"name": "P3", "arrival_time": 0, "burst_time": 3},
    {"name": "P4", "arrival_time": 0, "burst_time": 1},
    {"name": "P5", "arrival_time": 0, "burst_time": 2},
    {"name": "P6", "arrival_time": 0, "burst_time": 1},
]

current_time = 0
waiting_time = 0
turnaround_time = 0
completed_processes = []

while processes:
    # Filter processes that have arrived by the current time
    available_processes = [p for p in processes if p["arrival_time"] <= current_time]

    if available_processes:
        # Find the process with the shortest burst time among the available processes
        shortest_process = min(available_processes, key=lambda x: x["burst_time"])

        # Update waiting time and current time
        waiting_time += current_time - shortest_process["arrival_time"]
        current_time += shortest_process["burst_time"]

        # Update turnaround time
        turnaround_time += current_time - shortest_process["arrival_time"]

        # Add the completed process to the list
        completed_processes.append(shortest_process)

        # Remove the completed process from the list of processes
        processes.remove(shortest_process)
    else:
        # If no processes are available, increment the current time
        current_time += 1

# Calculate the number of completed processes
num_processes = len(completed_processes)

# Calculate average waiting time and average turnaround time
average_waiting_time = waiting_time / num_processes
average_turnaround_time = turnaround_time / num_processes

# Print the results with comments
print("Average Waiting Time:", round(average_waiting_time, 2))
print("Total Waiting Time:", waiting_time)
print("Average Turnaround Time:", round(average_turnaround_time, 2))
print("Total Turnaround Time:", turnaround_time)
