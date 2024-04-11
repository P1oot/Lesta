# from lesta.celery import app
from .models import File, Words
from django.shortcuts import get_object_or_404
import string
import nltk
import json
# from time import sleep

# nltk.download('punkt')


# @app.task
def file_processing(id):
    curent_file = get_object_or_404(File, id=id)
    f = open('media/' + curent_file.file.name, 'r', encoding="utf-8")
    text = f.read()
    text = text.lower()
    spec_chars = string.punctuation + '\n\xa0«»\t—…–'
    text = "".join([ch for ch in text if ch not in spec_chars])
    text_tokens = nltk.word_tokenize(text)
    text = nltk.Text(text_tokens)
    fdist = nltk.probability.FreqDist(text).most_common(50)
    words_q = len(text_tokens)
    words_dict_list = []
    for t in fdist:
        tf = round((t[1]/words_q*100), 3)
        d = [t[0], t[1], tf]
        words_dict_list.append(d)
    # sleep(3)
    words_json = json.dumps(words_dict_list)
    Words.objects.create(
        file=curent_file,
        quantity=words_q,
        words_list=words_json,
    )
    curent_file.processed = True
    curent_file.save()
