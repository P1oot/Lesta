# from lesta.celery import app
from .models import File
from django.shortcuts import get_object_or_404
import string
import nltk
from time import sleep

nltk.download('punkt')


# @app.task
def file_processing(id):
    curent_file = get_object_or_404(File, id=id)
    f = open('media/' + curent_file.file.name, 'r', encoding="utf-8")
    text = f.read()
    text = text.lower()
    spec_chars = string.punctuation + '\n\xa0«»\t—…'
    text = "".join([ch for ch in text if ch not in spec_chars])
    text_tokens = nltk.word_tokenize(text)
    text = nltk.Text(text_tokens)
    fdist = nltk.probability.FreqDist(text)
    # sleep(3)
    curent_file.words_list = fdist.most_common(50)
    curent_file.processed = True
    curent_file.save()
