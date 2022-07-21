array = []
num = None

#Uncomment this for test data
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7, 13, 20, 25, 46, 123, 146, 2222]
# num = 70

#Copy/Paste test data
#2 3 1 4 6 5 9 8 7 13 20 25 46 123 146 2222

def printError(error):
    print('Wrong input data. Use numbers only. Error:')
    print(error)
    print(type(error))

while not array:
    try:
        array = list(map(int, input("Input a sequence of numbers with spaces: ").split()))
    except ValueError as error:
        printError(error)

while not num:
    try:
        num = int(input('Input reference number: '))
    except ValueError as error:
        printError(error)

def sort_paste(array):
    for i in range(1, len(array)):
        temp = array[i]
        index = i
        while index > 0 and temp < array[index-1]:
            array[index] = array[index-1]
            index -= 1
        array[index] = temp
    return array

print('Sorted array:', sort_paste(array))

def binary_search(array, num, left = 0, right = len(array)-1):
    if left > right:
        return False
    middle = (left+right)//2
    if array[middle] < num <= array[middle + 1]:
        return middle
    elif num < array[middle]:
        return binary_search(array, num, left, middle)
    else:
        return binary_search(array, num, middle+1, right)

print('The position is:', binary_search(array, num))



