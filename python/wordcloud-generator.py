import wordcloud
from wordcloud import STOPWORDS
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

text = open("C://Users//gamer//Desktop//outputword.txt", mode="r", encoding="utf-8").read()
stopwords = set(wordcloud.STOPWORDS)

custom_mask = np.array(Image.open("C://Users//gamer//Desktop//Stuff//Files//code//cloud.png"))
wc = wordcloud.WordCloud(background_color="white",
               stopwords=stopwords,
               mask = custom_mask,
              )
wc.generate(text)
image_colors = wordcloud.ImageColorGenerator(custom_mask)
wc.recolor(color_func = image_colors)

plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()