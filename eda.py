import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

df = pd.read_csv("data/job_listings.csv")
df.dropna(inplace=True)

df['Job Title'].value_counts().head(10).plot(kind='barh', title='Top Job Titles')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("output/top_job_titles.png")
plt.close()

df['Location'].value_counts().head(10).plot(kind='bar', title='Top Locations')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/top_locations.png")
plt.close()

text = " ".join(df['Summary'])
wc = WordCloud(width=800, height=400, background_color='white').generate(text)
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.title("Common Words in Job Summaries")
plt.tight_layout()
plt.savefig("output/wordcloud.png")
plt.close()
