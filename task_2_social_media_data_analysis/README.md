# Social Media Data Analysis

View live at [precog-twitter-visualisation.herokuapp.com/](https://precog-twitter-visualisation.herokuapp.com/)

## File Structure

#### Required Scripts
- To get Tweets: [index.py](./index.py)
- To make visualisations: [app.py](./app.py)

#### Miscellaneous Scripts
- To convert CSV to JSON: [csv_to_json.py](./csv_to_json.py)

#### Dumps
- Tweet dump as CSV: [data_final.csv](data_final.csv)
- Tweet dump as JSON: [data_final.json](data_final.json)

## Inferences

### What can we say about the users who tweeted this hashtag?
**Verified users:** From the corpus collected, a whopping **99.89%** of the users were **not verified**

**User Location:** 5,583 tweets from the corpus had their authors' location in the respective profiles. Out of these, about 45% had the word `India` in the profile locations. Please note that this does not mean that the rest (\~55%) don't reside in India as their were cases with locations like *Chandigarh* where the user didn't explicitly mention the country. At present, this graph doesn't give much insight, but can be improved to account for all the places in India.

### Can we comment on the language aspect of the corpus collected?
**Tweet Language:** English, Punjabi and Hindi are the top three languages respectively. Apart from this, there were 114(1.57%) tweets in French.
*Twitter returns language codes for languages*

### Can we draw any insights about their user’s followers and friends?

| Attribute | Minimum | Average | Maximum  |
|-----------|---------|---------|----------|
| Followers | 0       | 510     | 3,76,962 |
| Friends   | 0       | 343     | 37,132   |
| Posts     | 1       | 5251    | 4,05,659 |
| Favorites | 0       | 5855    | 3,57,210 |

**Graphs vs statistics for Friends and Followers:** Looking at the graphs of Followers and Friends in the visualisation dashboard, it was easy to conclude that the friend graph had a higher density as compared to follower graph. One could easily conclude form there that on an averga a person has higher number of friends than followers. This was in a stark contrast with the above statistics where average number of followers is considerably higher than the average number of friends.


**General inference from graphs:** In all the four graphs of the above mentioned attributes, there is a higher density at the start after which there is a seemingly exponential decrease with a few spikes which gradually flatten out as one approaches the max number.



**_Notes_**

*The inferences drawn from the visualisations have also been mentioned with their respective charts.*



*P.S. I didn't notice the `.ipynb` submission format earlier and had completed the Task 2 by that time. As I result, I confirmed with Tanvi Karandikar who assured that submission in this format would be okay*
