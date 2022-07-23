array = []
num = None

#Uncomment for Test data
#array = [2, 3, 1, 4, 6, 5, 9, -50, 8, 7, 13, 2222, 20, 25, 46, 123, 146, 20]
#num = 4

#Copy/Paste test data
#2 3 1 4 6 5 9 -50 8 7 13 2222 20 25 46 123 146 20

#Error printouts
def printError(error):
    print('Wrong input data. Use numbers only. Error:')
    print(error)
    print(type(error))

#Check for int type in array
while not array:
    try:
        array = list(map(int, input("Input a sequence of numbers with spaces: ").split()))
    except ValueError as error:
        printError(error)

#Check for int type for reference number
while num is None:
    try:
        num = int(input('Input reference number: '))
    except ValueError as error:
        printError(error)

#Sort array
def sort_paste(array):
    for i in range(1, len(array)):
        temp = array[i]
        index = i
        while index > 0 and temp < array[index-1]:
            array[index] = array[index-1]
            index -= 1
        array[index] = temp
    return array

def binary_search(array, num, left = 0, right = len(array)-2):
    if left > right:
        return "No element in array matching condition: element < reference num <= element.next"
    middle = (left+right)//2
    if array[middle] < num <= array[middle + 1]:
        return middle
    elif num <= array[middle]:
        return binary_search(array, num, left, middle-1)
    else:
        return binary_search(array, num, middle+1, right)

print('Sorted array:', sort_paste(array))
print('The position is:', binary_search(array, num))

#Uncomment to go through Test data
# for num in array:
#     print('The position is:', binary_search(array, num))
