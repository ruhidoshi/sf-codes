from array import array
from multiprocessing import Process, current_process

def sort_descending(arr):
    # Convert array to a list, sort the list, and convert it back to an array
    arr_list = list(arr)
    arr_list.sort(reverse=True)
    arr.fromlist(arr_list)
    print(f"Parent Process ({current_process().pid}) - Sorted Descending: {arr}")

def sort_ascending(arr):
    # Convert array to a list, sort the list, and convert it back to an array
    arr_list = list(arr)
    arr_list.sort()
    arr.fromlist(arr_list)
    print(f"Child Process ({current_process().pid}) - Sorted Ascending: {arr}")

def main():
    # Shared array between parent and child processes
    arr = array('i', [7, 2, 5, 1, 8, 6])

    # Create a process for each sorting function
    parent_process = Process(target=sort_descending, args=(arr,))
    child_process = Process(target=sort_ascending, args=(arr,))

    # Start both processes
    parent_process.start()
    child_process.start()

    # Wait for both processes to finish
    parent_process.join()
    child_process.join()

if __name__ == "__main__":
    main()
