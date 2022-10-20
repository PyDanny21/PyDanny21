#pip install chatterbot
#pip install chatterbot_corpus
#python -m spacy.download('en')
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#create chatbot
chatbot=ChatBot('bot')

trainer=ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

while(True):
    query=str(input('>>'))
    print(chatbot.get_response(query))
    if 'exit' in query:
        break