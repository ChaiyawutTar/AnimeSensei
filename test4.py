import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Read your anime data into a pandas DataFrame
df = pd.read_csv('/Users/tar/Documents/sem 2 final/project sem2 animesensei/Anime-3.csv')

# Extract the tags or genres from your DataFrame
tags = ' '.join(df['Type'])

# Create a WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(tags)

# Plot the WordCloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Anime Tags Word Cloud')

# Display the WordCloud
plt.show()