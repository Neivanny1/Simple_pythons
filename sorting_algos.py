# simple sorting algorithmns implementations
import time
import random
# Insertion algorithmn 
   #Steps
   #Initialize the array with dummy data
   #Iterate over the given array.
   #Maintain the index of the minimum element.
   #Iterate from the current element
   #check if current_element < minimum element
   #if current_element < than minimum  replace the index
   #Swap the current element with minimum element
#The time complexity of the selection sort is O(n^2), and the space complexity if O(1)
def insertion_sort(array, n):
    start = time.time_ns()
    for i in range(1,n):
        current_pos = i
        current_element = array[i]
        while current_pos > 0 and current_element < array[current_pos - 1]:
            array[current_pos] = array[current_pos - 1]
            current_pos -= 1
        array[current_pos] = current_element
    print(f"Sorted array: {str(array)}")
    stop = time.time_ns()
    print(f'Time taken is: {stop - start}')

if __name__ == '__main__':
    array = [random.randint(1, 1000) for _ in range(1000)]
    n = len(array)
    insertion_sort(array, n)