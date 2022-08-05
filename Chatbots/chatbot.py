from flask import Flask, render_template, request
# pip install chatterbot==1.0.4
# pip install --upgrade chatterbot
# or
# https://stackoverflow.com/questions/44925395/error-while-installing-chatterbot
# https://stackoverflow.com/questions/44925395/error-while-installing-chatterbot#:~:text=0-,You%27ll,-need%20to%20install
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)
english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")

app.route("/")
def home ():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))

if __name__ == "__main__":
    app.run()