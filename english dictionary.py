#install PyDictionary
from PyDictionary import PyDictionary
dictionary=PyDictionary()


while True:
    word=input('Enter word:')
    if word=='':
        print('You did not enter any word')
    print(dictionary.meaning(word))
#multiple words
'''    
dictionary=PyDictionary('hear','wisdom','oop')
print(dictionary.printMeaning())
print(dictionary.getMeaning())'''