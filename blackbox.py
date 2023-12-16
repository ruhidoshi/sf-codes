def look_disk_scheduling(requests, head_position):
    # Sort the requests
    sorted_requests = sorted(requests)

    # Split requests into two parts: those below and above the head position
    lower_requests = [r for r in sorted_requests if r < head_position]
    upper_requests = [r for r in sorted_requests if r >= head_position]

    # Reverse the lower requests for LOOK
    lower_requests.reverse()

    # Combine the two parts
    ordered_sequence = lower_requests + upper_requests

    # Calculate the total number of disk seeks
    total_seeks = sum(abs(ordered_sequence[i] - ordered_sequence[i+1]) for i in range(len(ordered_sequence)-1))

    return total_seeks, ordered_sequence

# Example usage
requests = [98, 183, 37, 122, 14, 124, 65, 67]
head_position = 50
count, optimal_order = look_disk_scheduling(requests, head_position)
print(f"Total number of disk seeks: {count}")
print(f"Optimal order of requests: {optimal_order}")
