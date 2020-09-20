# insertion sort / pg16 / 9.20.2020
import random as rand

arr = []
len = int(rand.random() * 1000)
for i in range(len):
    element = int(rand.random() * 1000)
    arr.append(element)
#----------------create array end------------------------

for j in range(1, len):
    key = arr[j]
    i = j-1
    while(i >= 0 and arr[i] > key):
        arr[i + 1] = arr[i]
        i -= 1
    arr[i+1] = key
#----------------insertion sort algorithm end------------------------

print(arr)
ind = 0
for i in range(len-1):
    if (arr[i] > arr[i+1]):
        ind = 1
        print("sort fail")
if (ind == 0):
    print('sort successful')
#----------------testing end------------------------