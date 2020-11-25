from os import path
from wordcloud_fa import WordCloudFa
from random import choice
import pandas as pd
import arabic_reshaper as ar
import re
import sys

args = sys.argv
if len(args) < 2:
	print("Specify CSV file!")
	exit()

csv_address = args[1]
username = path.splitext(csv_address)[0]

columns = ["artist", "album", "track", "date"]
data = pd.read_csv(csv_address, header=None, names=columns)
top_series = data["artist"].value_counts()[:50]
top = dict(zip(top_series.index, top_series))

colormaps = ['viridis', 'plasma', 'inferno', 'magma', 'cividis', 'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink', 'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia', 'hot', 'afmhot', 'gist_heat', 'copper']

colormap = choice(colormaps)
print(f"Colormap: {colormap}")

wordcloud = WordCloudFa(
	prefer_horizontal=1,
	background_color="white",
	colormap=colormap,
	width=2048,
	height=2048
).generate_from_frequencies(top)

image = wordcloud.to_image()
image.save(f"{username}.png")