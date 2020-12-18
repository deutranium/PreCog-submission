import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# CONSTANTS

follower_desc = """Distribution of users according to the number of their followers.
    
- **X-axis:**  The numbers 0-100 shown there are the divisions of the sample space where the sample space is the range 0 to the value you select in the slider below.

- **Y-axis:** The number of users with followers in interval $$[x \\cdot \\frac{range}{100}, (x+1) \\cdot \\frac{range}{100})$$"""


def main():
    PAGES = {
        "Introduction": introduction,
        "User Analysis": user_analysis,
        "Tweet Analysis": tweet_analysis
    }

    st.title("Twitter Data Visualisations")
    st.sidebar.header("Contents")
    page = st.sidebar.selectbox("Select section", options=list(PAGES.keys()))
    PAGES[page]()

@st.cache
def load_data():
    data = pd.read_csv('data_final.csv', nrows=11000)
    return data

stuff = load_data()

def plot_area(df, range):
    hist_values = np.histogram(df, bins=100, range=(0,range))[0]
    print(hist_values)
    st.area_chart(hist_values)
    
# User follower count
def user_followers_count():
    st.subheader("User follower count")
    st.markdown(follower_desc)

    # slider to select range
    range = st.slider("Select the upper limit to number of followers", 0, 5000, value=500)
    # getting plot data
    df = pd.DataFrame(stuff, columns=['user_followers_count'])
    # plot
    plot_area(df, range)
    # Explanations
    st.markdown("**Explanation:** Say the selected value *range* from the slider below is *1000* and hovering the cursor at `x=25` says `index: 25`, `value:176`. This means that there are 176 users who have followers in the interval $$\\frac{25 \\cdot 1000}{100} = 250$$ to $$250+10 = 260$$")    

# User following count
def user_following_count():
    st.subheader("User following count")
    st.markdown("""Distribution of users according to the number of people they are following, or "friends" according to twitter lingo.""")

    # slider to select range
    range = st.slider("Select the upper limit to number of people the user is following", 0, 5000, value=500)
    # getting plot data
    df = pd.DataFrame(stuff, columns=['user_friends_count'])
    # plot
    plot_area(df, range)
    # Explanations
    st.markdown("**Explanation:** Same as the previous plot")

# User posts count
def user_posts_count():
    st.subheader("User posts count")
    st.markdown("""Distribution of users according to the number of posts they have created""")

    # slider to select range
    range = st.slider("Select the upper limit to number of posts the user has created", 0, 5000, value=500)
    # getting plot data
    df = pd.DataFrame(stuff, columns=['user_statuses_count'])
    # plot
    plot_area(df, range)
    # Explanations
    st.markdown("**Explanation:** Same as the previous plot")

# User favourites count
def user_favourites_count():
    st.subheader("User favourites count")
    st.markdown("""Distribution of users according to the number of posts they have liked""")

    # slider to select range
    range = st.slider("Select the upper limit to number of posts the user has liked", 0, 5000, value=500)
    # getting plot data
    df = pd.DataFrame(stuff, columns=['user_favourites_count'])
    # plot
    plot_area(df, range)
    # Explanations
    st.markdown("**Explanation:** Same as the previous plot")

# PAGES

# intro page
def introduction():
    st.header("Introduction")

    # What is this
    st.subheader("What is this?")
    st.markdown("""
    This dashboard aims to analyze the tweets with `#FarmersDyingModiEnjoying`, which was the trending hashtag in **New Delhi** region at the time of writing. This portal tends to gain insights into:
    
    1. **User Analysis:**
    Study the properties of user who tweeted, like if they are verified or not, their location, follower count etc.

    2. **Tweet Analysis:**
    Study the properties of tweets, like distribution across dates, language, geo location etc.
    """)

    st.subheader("Data")
    st.write(stuff)


    # How to use
    st.subheader("How to use?")
    st.markdown("""
        You may select the the category for the analysis you would like to view using the sidebar you see at the left and navigate throughout the page using the same.
    """)

    st.subheader("How this works")
    st.markdown("""
        I have used the following tools and libraries to make this project:
        
        - **[Streamlit](https://www.streamlit.io/):** To display the visualisations
        - **[Tweepy](https://www.tweepy.org/):** The Python library to get data
        - **[Streamlit-Echarts](https://github.com/andfanilo/streamlit-echarts):** The streamlit component used to visualise data

        The basic workflow included creating a `csv` file with the data collected using `tweepy`, linking it to `streamlit` and using the `streamlit-echarts` module to display the visualisations
        
        For a detailed explanantion, you may go through the [code](https://github.com/deutranium/PreCog-submission) which has been properly commented for easier understanding.
    """)

    # How can this be improved
    st.subheader("How can this be improved?")
    st.markdown("""
        At present, there is a very primitive analysis which is more of displaying visualisations for the numeric data. For future, we can look into the following:
        
        1. **Network Graphs:**
        We can try creating network graphs and look for possible nodes. These nodes can be news channels, parties affected and/or political figures according to the nature of tweets.

        2. **Relation to other topics:**
        We can look at the hashtags most common apart from the `#FarmersDyingModiEnjoying` and how frequently they appear together. This can give an insight into how this case relates to other topics.

        3. **Geographical Analysis:**
        We can plot the locations of the tweets (which are geo-location enabled) and analyze the certian *hotspots* which might be there along with getting an insight into the international participation.

        4. **Timeline:**
        We can look at how the number of tweets per day with this hashtag have changed. We might see a spike near the days of incident, judgements, investigation etc. and analyze how the curve of participation changes.
    """)

    # Issues faced
    st.subheader("Issues faced")
    st.markdown("""
        One of the major issues I faced was because of the limit set by Twitter API to get only a certain number of tweets every 15 minutes, resulting in numerous `ConnectionRefused` errors, going through tons of pages on StackOverflow, and Twitter API documentation and finally somehow getting it to work xD

        The other issue faced was that some trending hashtags didn't have the required number of tweets at the time of fetching, resulting in checking for hashtags with 10k+ tweets instead of the one top in trending.
    """)

def user_analysis():
    st.header("User Analysis")
    st.subheader("Columns analyzed")
    st.markdown("""
    `user_id`, `user_screen_name`, `user_followers_count`, `user_friends_count`, `user_created_at`, `user_favourites_count`, `user_statuses_count`, `user_lang`, `user_verified`, `user_location`
    """)

    # Charts
    user_followers_count()
    user_following_count()
    user_posts_count()
    user_favourites_count()


def tweet_analysis():
    st.header("Tweet Analysis")
    st.subheader("Columns analyzed")
    st.markdown("""
    `tweet_id`, `tweet_full_text`, `tweet_created_at`, `tweet_lang`, `hashtags`, `tweet_retweet_count`, `tweet_favorite_count`, `tweet_place`
    """)

main()
