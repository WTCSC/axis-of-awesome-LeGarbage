[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18894961)
# Florida Man Does Data Analysis on Florida Man Headlines

And you can too

## The data

The Florida Man data set is a collection of over 40,000 Florida Man headlines collected from the r/FloridaMan subreddit. These headlines were collected from January 1st, 2014 to April 30th, 2022. In addition to the headlines, the data also inclues the post id, date and time posted, the score of the post, the user who posted it, and the url of the source article.

**This data set is not filtered directly in the file, only in the python code**

## Filtering

Due to the nature of the collection of the data, not all of the headlines are relevant. Some are ads and posts about the subreddit itself. The best way that I found to filter the data was to only allow headlines that include "florida" and "man", as well as manually adding some exceptions to exclude ads that inclue "florida" or "man". There are also many duplicate headlines, which are removed by dropping any duplicate titles or urls.

## Usage

Just run the `florida.py` file

Upon running, 3 graphs should pop up and look like this:

![A line graph showing upvotes over time](imgs/Florida1.png)

![A bar graph showing some hand selected words and their frequency in the headlines](imgs/Florida2.png)

![A bar graph showing the 25 most common uncommon words in the hedlines](imgs/Florida3.png)

The `florida_man.csv` file is also included for your convenience

## Source

This dataset was obtained from [here](https://www.kaggle.com/datasets/bcruise/reddit-rfloridaman).
