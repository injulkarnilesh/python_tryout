from wordcloud import WordCloud, STOPWORDS
import numpy as npy
import random as random
from PIL import Image

def randomize(str):
    str = str.split(' ')
    random.shuffle(str)
    str = ' '.join(str)
    return str

dataset = open("alt.txt", "r").read()
dataset = randomize(dataset)
maskArray = npy.array(Image.open("india.jpg"))
customstopwords = {'in', 'on', 'as', 'from', 'video', 'viral', 'shared', 'claim', 'fake', 'image', 'old', 'new', 'false', 'falsely'}
customstopwords |= STOPWORDS
cloud = WordCloud(background_color = "white", width = 800, height = 400, mask = maskArray, max_words = 200, stopwords = set(customstopwords))
cloud.generate(dataset)
cloud.to_file("wordcloud-india.png")
