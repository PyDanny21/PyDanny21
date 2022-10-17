#This is a dictionary that responds to normal conversation in python
#So this is how everything will be done
#i will create a dictionary to keep every single questions i have ever heard and their responses
my_dictionary={
    'Hello':'hi sir,how are you?',
    'Hi':'hello sir,how are you?',
    'How are you':'I am as fit as fiddle and you',
    'I am good':'Thank God',
    'I am fine and you':'I am also doing great sir!!',
    'Who are you':'I am Py-Assist',
    'How old are you':'I am nearly a year old',
    'Who created you':'I was created by PyDanny whose real name is Daniel Quansah',
    'Who is PyDanny':'PyDanny is a young talented self taught python developer,web developer and many more',
    'What can you do':'I can open and close programs and softwares,search for anything from google,youtube,wikipedia,stackoverflow,et cetera.Play music, movies,make note,create keylogger,give you random advice and jokes.',
    'How can you help me': 'I can open and close programs and softwares,search for anything from google,youtube,wikipedia,stackoverflow,et cetera.Play music, movies,make note,create keylogger,give you random advice and jokes.',
    'Whats on':'Nothing much, sir!',
    'How was your day':'It was cool, sir and yours',
    'I am sad':'Oooh sir, please what happened',
    'Tell me more about yourself':'I am Py-Assist,a personal assistant program programmed by my creator PyDanny in pure Python',
    'Will you marry me':'No sir, I am only programmed to help you with some tasks',
    'Can you marry me': 'No sir, I am only programmed to help you with some tasks',

}
while(True):
    word=input('USER SAID:')
    actual_word=word.capitalize()
    if actual_word in my_dictionary:
        print(my_dictionary[actual_word])
