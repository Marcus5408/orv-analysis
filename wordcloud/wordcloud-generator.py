from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

text = open("wordcloud\words-only.txt", mode="r", encoding="utf-8").read()
stopwords = set(STOPWORDS)

custom_mask = np.array(Image.open("wordcloud\mask.png"))
wc = WordCloud(background_color="white",
               stopwords=stopwords,
               mask = custom_mask,
              )
wc.generate(text)
image_colors = ImageColorGenerator(custom_mask)
wc.recolor(color_func = image_colors)

plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
