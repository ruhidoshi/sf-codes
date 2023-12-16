def fifo(page_ref, frame_size):
    # Initialize variables to track page faults and frames in memory
    page_faults = 0
    frames = []

    # Iterate through the page references
    for page in page_ref:
        # Check if the page is not in the frames (page fault)
        if page not in frames:
            # If there is space in the frames, add the page
            if len(frames) < frame_size:
                frames.append(page)
            else:
                # If the frames are full, remove the oldest page (FIFO) and add the new page
                frames.pop(0)
                frames.append(page)
            # Increment page_faults counter
            page_faults += 1

    # Return the total number of page faults
    return page_faults

# Example usage
page_ref_fifo = [1, 3, 5, 3, 2, 6, 6, 3, 1]
frame_size_fifo = 3

# Call the fifo function with the example page references and frame size
page_faults_fifo = fifo(page_ref_fifo, frame_size_fifo)

# Print the result
print(f"Page faults: {page_faults_fifo}")
