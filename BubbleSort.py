#Nurul Aliyah Dyah Sakhinah - F55121069

def bubble_sort(arr):
    n = len(arr)
    # Melakukan looping pada seluruh elemen dalam array
    for i in range(n):
        # Elemen-elemen terakhir sebanyak i sudah diurutkan
        for j in range(0, n-i-1):
            # Tukar jika elemen yang ditemukan lebih besar dari elemen berikutnya
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#Input Array
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)
