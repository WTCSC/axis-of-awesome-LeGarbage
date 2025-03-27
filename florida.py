import pandas as pd
import matplotlib.pyplot as plt

# Import the data from the csv
df = pd.read_csv("florida_man.csv")

# Filter the data so only titles containing "florida man" are included
df = df[df["title"].map(lambda title: ("florida" in title.lower()) and "man" in title.lower())]

plt.plot_date(df["created_at"], df["score"])
plt.show()