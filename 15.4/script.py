alpha = 'abcdefghijklmnopqrstuvwxyz'
song = "soundofsilence.txt"

filename = input("Input filename: ")

with open(filename, encoding='utf8') as tempFile:
    file = tempFile.read().split()

#Drop all non alphabetic symbols e.g. ',!?''
text = list(map(lambda x: ''.join(filter(str.isalpha, x)).lower(), file))

def most_common(text):
    text = (list(filter(lambda x: len(x)>3, text))) #Filter for words longer than 3 symbols
    dict1 = {}
    for i in text:
        dict1[i] = text.count(i) #Create dictionary {word:how_many_times_met_in_text}
    return sorted(dict1.items(), key = lambda x: x[1])[-1][0] #sort dictionary items by value, take the last item's value only

def longest(text):
    list1 = [i for i in text if all(map(lambda x: x in alpha, i))] #create a list with english words only
    return sorted(list1, key = len)[-1] #sort by length, take last

print(f'Most common word with more than 3 symbols is: {most_common(text)}\nThe longest word with english symbols only is: {longest(text)}')