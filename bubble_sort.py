# number = 0
# while number <= 89:
#     if number % 10 == 0:
#         number += 1 + number // 10
#     print("{:02d}".format(number), end='\n' if number == 89 else ", ")
#     number += 1
def bubblesort(array):
    if len(array) != 0:
        for i in range(len(array)):
            for j in range(len(array) - i -1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]


arr = [5, 6, 9, 2, 0, -8, 5,11, 89, 16, 80, 107, 45, 30, 47, -5, 6, 9, 2, 0, -8, 5,11, 89, 16, 80, 107, 45, 30, 47, -56]
print(arr, "Unsorted list!")
bubblesort(arr)
print(arr)

