import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        print(f"\nIterasi Ke-{i+1}:")
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            print(arr)
        if not swapped:
            break
    return arr

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        print(f"Iterasi {i+1}: {arr}")
    return arr

# Menghasilkan array acak untuk diurutkan
random.seed(42)
arr = random.sample(range(1, 100), 10)
print("Tugas 3 PAA II - Membandingkan Bubble Sort dan Insertion Sort")
print("-------------------------------------------------------------")
print("Array Awal:", arr)
print("-------------------------------------------------------------")

# Bubble Sort (Tidak Optimal)
print("\t\t\t\t\t\t BUBBLE SORT\n")
print("Proses : ")
start_time = time.perf_counter()
sorted_arr_bubble = bubble_sort(arr)
end_time = time.perf_counter()
print("\nHasil Bubble Sort:", sorted_arr_bubble)
print("Runtime Bubble Sort:", end_time - start_time, "detik")
print("-------------------------------------------------------------")

# Insertion Sort (Optimal)
print("\t\t\t\t\t INSERTION SORT\n")
print("Proses: ")
start_time = time.perf_counter()
sorted_arr_insertion = insertion_sort(arr.copy())
end_time = time.perf_counter()
print("\nHasil Insertion Sort:", sorted_arr_insertion)
print("Runtime Insertion Sort:", end_time - start_time, "detik")
print("-------------------------------------------------------------")
