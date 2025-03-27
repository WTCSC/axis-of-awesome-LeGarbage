import pandas as pd
import matplotlib.pyplot as plt

# Import the data from the csv
df = pd.read_csv("florida_man.csv")

# Filter the data so only titles containing "florida man" are included
df = df[df["title"].map(lambda title: ("florida" in title.lower()) and "man" in title.lower() and not title.startswith("[FloridaMan]"))]

# Drop any duplicate titles and sort by date
df = df.drop_duplicates(subset=["title"]).sort_values(["created_at", "url"])

# Get a list of the most common words
with open("words.txt") as words:
    common_words = [line.replace("\n", "").lower() for line in words.readlines()]

# Count the most used words in the data
punctuation = str.maketrans({".": "", ",": "", "'": "", '"': "", "!": "", "?": "",})
word_counts = pd.Series(' '.join(df["title"].str.lower().str.translate(punctuation)).split(), name="words").value_counts().reset_index()
word_counts = word_counts[word_counts["words"].map(lambda word: (word.lower() not in common_words) and word.isalpha())].head(25)

# A bar chart with the 25 most common words and how often they occur
plt.bar(word_counts["words"], word_counts["count"])
plt.tight_layout()
plt.show()

# A list of words to count
words = sorted(["alligator", "naked", "rob", "drunk", "drug", "arrested", "car", "steal"])
heights = [df.loc[df["title"].map(lambda title: word in title.lower()), ["title"]].size for word in words]

# # A bar chart with all the words in the list and how often they appear in the data
# plt.bar([word.title() for word in words], heights)
plt.tight_layout()
# plt.show()

# # A line chart that shows the score of each headline over time
# plt.plot(df["created_at"], df["score"])
# plt.show()