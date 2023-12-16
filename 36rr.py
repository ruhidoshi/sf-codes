class Process:
    def __init__(self, name, arrival_time, burst_time):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time

def round_robin_scheduling(processes, time_quantum):
    current_time = 0
    waiting_time = 0
    turnaround_time = 0
    completed_processes = []

    while processes:
        for process in processes:
            # Check if the process has arrived and has remaining time
            if process.arrival_time <= current_time and process.remaining_time > 0:
                # Update waiting time and current time
                waiting_time += current_time - process.arrival_time
                current_time += min(time_quantum, process.remaining_time)

                # Update turnaround time
                turnaround_time += current_time - process.arrival_time

                # Reduce the remaining time of the selected process
                process.remaining_time -= min(time_quantum, process.remaining_time)

                # If the process is completed, add it to the completed processes list
                if process.remaining_time == 0:
                    processes.remove(process)
                    completed_processes.append(process)
                break
            else:
                # If the process hasn't arrived yet, increment the current time
                current_time += 1

    # Calculate the number of completed processes
    num_processes = len(completed_processes)

    # Calculate average waiting time and average turnaround time
    average_waiting_time = waiting_time / num_processes
    average_turnaround_time = turnaround_time / num_processes

    # Print the results with comments
    print("Average Waiting Time:   ", round(average_waiting_time, 2))
    print("Total Waiting Time:     ", waiting_time)
    print("Average Turnaround Time:", round(average_turnaround_time, 2))
    print("Total Turnaround Time:  ", turnaround_time)


# Example usage:
processes = [
    Process("P1", 0, 7),
    Process("P2", 2, 5),
    Process("P3", 4, 3),
    Process("P4", 6, 1),
    Process("P5", 8, 2),
    Process("P6", 10, 1),
]

time_quantum = 2
round_robin_scheduling(processes, time_quantum)
