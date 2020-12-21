import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from streamlit_echarts import st_echarts

# CONSTANTS
intro_what = """This dashboard aims to analyze the tweets with `#FarmersDyingModiEnjoying`, which was the trending hashtag in **New Delhi** region at the time of writing. This portal tends to gain insights into:
    
1. **User Analysis:**
Study the properties of user who tweeted, like if they are verified or not, their location, follower count etc.

2. **Tweet Analysis:**
Study the properties of tweets, like distribution across dates, language, geo location etc."""
intro_how_use = """Select the the category for the analysis you would like to view using the left sidebar."""
intro_how_works = """Tools used:
        
- **[Streamlit](https://www.streamlit.io/):** To display the visualisations
- **[Tweepy](https://www.tweepy.org/):** Python library to get Twitter data
- **[Streamlit-Echarts](https://github.com/andfanilo/streamlit-echarts):** Streamlit component used to help visualise data

The basic workflow included creating a `csv` file with the data collected using `tweepy`, linking it to `streamlit` and using the `streamlit-echarts` module to display the visualisations

For a detailed explanantion, you may go through the [code](https://github.com/deutranium/PreCog-submission)."""
intro_how_improve = """At present, the analysis is more of displaying visualisations for the direct numeric data. For the future, we can look into the following:
        
1. **Network Graphs:**
Creating network graphs for users and look for possible nodes. These nodes can possibly be news channels, parties affected and/or political figures according to the nature of tweets.

2. **Relation to other topics:**
Look at the hashtags most common apart from the `#FarmersDyingModiEnjoying` and how frequently they appear together. This can give an insight into how this case relates to other topics.

3. **Geographical Analysis:**
Plot the locations of the tweets (which are geo-location enabled) and analyze the certian *hotspots* which might be there along with getting an insight into the international participation.

4. **Timeline:**
Look at how the number of tweets per day with this hashtag have changed. We might see a spike near the days of incident, judgements, investigation etc. and analyze how the curve of participation changes."""
intro_issues = """One of the major issues I faced was because of the limit set by Twitter API to get only a certain number of tweets every 15 minutes, resulting in numerous `ConnectionRefused` errors, going through tons of pages on StackOverflow, and Twitter API documentation and finally somehow getting it to work xD

The other hiccup on the way was some trending hashtags not having the required number of tweets(~10k) at the time of fetching, resulting in checking for hashtags with 10k+ tweets too instead of directly picking the top trending one."""
insights_user = """- It was observed that almost all the **11,000** users from the given corpus are not verified with only **12** having the verification tags.

**Can we draw any insights about the users' followers and friends?**

- Moreover, looking at the area charts below, the number of users decreases as we go towards higher number of friends/followers, and there is a significantly higher concentration of users with followers < 300 and friends < 1000.

- One other conclusion can be the higher number of friends than followers for an average user from the corpus which can be clearly seen from the density of **Friends graph** being more than that of **Followers graph**."""
follower_desc = """Distribution of users according to the number of their followers.
    
- **X-axis:**  The numbers 0-100 shown there are the divisions of the sample space where the sample space is the range 0 to the value you select in the slider below.

- **Y-axis:** The number of users with followers in `x%` to `(x+1)%` of the **upper limit**"""
follower_explanation = "**Explanation:** Say the selected value *range* from the slider below is *1000* and hovering the cursor at `x=25` says `index: 25`, `value:176`. This means that there are 176 users who have followers in the interval $$25\% \ of \ 1000 = 250$$ to $$26\% \ of \ 1000 = 260$$"
tweet_insights = """We can clearly see from the pie chart below that **English**, **Punjabi** and **Hindi** are the first, second and third most common languages respectively which is very well justified looking at the nature of the hashtag `#FarmersDyingModiEnjoying` which has the most participation from the population of Delhi-NCR, Haryana and Punjab.
    
One surprising thing I noticed was the presence of a significant number of tweets in languages like **French** (for `fr`) which are not so common in India"""
language_codes = {'en': 'English', 'ar': 'Arabic', 'bn': 'Bengali', 'cs': 'Czech', 'da': 'Danish', 'de': 'German', 'el': 'Greek', 'es': 'Spanish', 'fa': 'Persian', 'fi': 'Finnish', 'fil': 'Filipino', 'fr': 'French', 'he': 'Hebrew', 'hi': 'Hindi', 'hu': 'Hungarian', 'id': 'Indonesian', 'it': 'Italian', 'ja': 'Japanese', 'ko': 'Korean', 'msa': 'Malay', 'nl': 'Dutch', 'no': 'Norwegian', 'pl': 'Polish', 'pt': 'Portuguese', 'ro': 'Romanian', 'ru': 'Russian', 'sv': 'Swedish', 'th': 'Thai', 'tr': 'Turkish', 'uk': 'Ukrainian', 'ur': 'Urdu', 'vi': 'Vietnamese', 'zh-cn': 'Chinese', 'zh-tw': 'Chinese'}

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
    data = pd.read_csv('task_2_social_media_data_analysis/data_final.csv')
    return data

stuff = load_data()
stuff_df = pd.DataFrame(stuff)

# Plot area graph from the given data
def plot_area(df, range):
    hist_values = np.histogram(df, bins=100, range=(0,range))[0]
    st.area_chart(hist_values)
    
# User follower count
def user_followers_count():
    st.subheader("User follower count")
    st.markdown(follower_desc)

    # getting plot data
    df = stuff_df['user_followers_count']
    max_val = int(df.max())
    min_val = int(df.min())
    # slider to select range
    range = st.slider("Select the upper limit to number of followers", 0, 20000, value=1000)
    
    
    # plot
    plot_area(df, range)
    # Explanations
    st.markdown(f"**Maximum number of followers:** {max_val}")
    st.markdown(f"**Minimum number of followers:** {min_val}")
    st.markdown(follower_explanation)    

# User following count
def user_following_count():
    st.subheader("User following count")
    st.markdown("""Distribution of users according to the number of people they are following, or "friends" according to twitter lingo.""")

    # getting plot data
    df = stuff_df['user_friends_count']
    max_val = int(df.max())
    min_val = int(df.min())

    # slider to select range
    range = st.slider("Select the upper limit to number of people the user is following", 0, 20000, value=1000)
    
    # plot
    plot_area(df, range)
    # Explanations
    st.markdown(f"**Maximum number of friends:** {max_val}")
    st.markdown(f"**Minimum number of friends:** {min_val}")
    st.markdown("**Explanation:** Same as the previous plot")

# User posts count
def user_posts_count():
    st.subheader("User posts count")
    st.markdown("""Distribution of users according to the number of posts they have created""")

    # getting plot data
    df = stuff_df['user_statuses_count']
    max_val = int(df.max())
    min_val = int(df.min())

    # slider to select range
    range = st.slider("Select the upper limit to number of posts the user has created", 0, 20000, value=1000)
    
    # plot
    plot_area(df, range)
    # Explanations
    st.markdown(f"**Maximum number of posts by a user:** {max_val}")
    st.markdown(f"**Minimum number of posts by a user:** {min_val}")
    st.markdown("**Explanation:** Same as the previous plot")

# User favourites count
def user_favourites_count():
    st.subheader("User favourites count")
    st.markdown("""Distribution of users according to the number of posts they have liked""")
    
    # getting plot data
    df = stuff_df['user_favourites_count']
    max_val = int(df.max())
    min_val = int(df.min())

    # slider to select range
    range = st.slider("Select the upper limit to number of posts the user has liked", 0, 20000, value=1000)
    # plot
    plot_area(df, range)
    # Explanations
    st.markdown(f"**Maximum number of friends:** {max_val}")
    st.markdown(f"**Minimum number of friends:** {min_val}")
    st.markdown("**Explanation:** Same as the previous plot")

# User location distribution
def user_loc():
    st.subheader("Users with 'India' in location")
    total_locations = int(stuff_df['user_location'].count())
    with_India = int(stuff_df['user_location'].str.contains("India").sum())
    info = f"P.S. This does not mean that only the users with term 'India' reside in India. Out of 11,000 users, {(total_locations - with_India):,} didn't have any location specified. Apart from this, there were also cases with locations like `Chandigarh` where the user didn't explicitly mention `India`"
    st.markdown(info)

    pie_options = {
        "backgroundColor": "#2c343c",
        "title": {
            "text": "Users with India in location",
            "left": "center",
            "top": 20,
            "textStyle": {"color": "#ccc"},
        },
        "tooltip": {"trigger": "item", "formatter": "{a} <br/>{b} : {c} ({d}%)"},
        "visualMap": {
            "show": False,
            "min": 0,
            "max": 600,
            "inRange": {"colorLightness": [0.1, 0.6]},
        },
        "series": [
            {
                "name": "Users with India in location",
                "type": "pie",
                "radius": "55%",
                "center": ["50%", "50%"],
                "data": [
                    {"value": (total_locations - with_India), "name": "Without India"},
                    {"value": with_India, "name": "With India"},
                ],
                "roseType": "radius",
                "label": {"color": "rgba(255, 255, 255, 0.3)"},
                "labelLine": {
                    "lineStyle": {"color": "rgba(255, 255, 255, 0.3)"},
                    "smooth": 0.2,
                    "length": 10,
                    "length2": 20,
                },
                "itemStyle": {
                    "color": "#c23531",
                    "shadowBlur": 200,
                    "shadowColor": "rgba(0, 0, 0, 0.5)",
                },
                "animationType": "scale",
                "animationEasing": "elasticOut",
            }
        ],
    }
    st_echarts(options=pie_options)

# User verification distribution
def user_verified():
    st.subheader("User Verification")
    st.markdown("""Distribution of users based on their Twitter verification. Here you can clearly see that almost all the users from this corpus are not verified.""")

    num_false = int((stuff_df['user_verified'].values == False).sum())
    num_true = int((stuff_df['user_verified'].values == True).sum())
    pie_options = {
        "backgroundColor": "#2c343c",
        "title": {
            "text": "Ratio of verified and unverified users",
            "left": "center",
            "top": 20,
            "textStyle": {"color": "#ccc"},
        },
        "tooltip": {"trigger": "item", "formatter": "{a} <br/>{b} : {c} ({d}%)"},
        "visualMap": {
            "show": False,
            "min": 80,
            "max": 600,
            "inRange": {"colorLightness": [0.3, 0.7]},
        },
        "series": [
            {
                "name": "Number of verified users",
                "type": "pie",
                "radius": "55%",
                "center": ["50%", "50%"],
                "data": [
                    {"value": num_false, "name": "Not Verified"},
                    {"value": num_true, "name": "Verified"},
                ],
                "roseType": "radius",
                "label": {"color": "rgba(255, 255, 255, 0.3)"},
                "labelLine": {
                    "lineStyle": {"color": "rgba(255, 255, 255, 0.3)"},
                    "smooth": 0.2,
                    "length": 10,
                    "length2": 20,
                },
                "itemStyle": {
                    "color": "#c23531",
                    "shadowBlur": 200,
                    "shadowColor": "rgba(200, 0, 0, 0.5)",
                },
                "animationType": "scale",
                "animationEasing": "elasticOut",
            }
        ],
    }
    st_echarts(options=pie_options)

def tweet_lang():
    st.subheader("Tweet Language")
    st.markdown("""Distribution of tweets among languages. By hovering over a section of the pie chart, you can see the BCP47 language tag of the language concerned.""")
    st.markdown("""One of the issues of concern here are the language codes. For example, for `in` code, there isn't an entry in `BCP47 language codes` and manually looking at the tweets with this language classification resulted in tweets from Hindi, English and Punjabi. I believe this classification can be improved by using an external library to classify the tweets.""")

    a = stuff_df['tweet_lang'].value_counts()
    lang_data = []
    for i,v in a.items():
        lang_data.append({"value": v, "name": i})

    pie_options = {
        "backgroundColor": "#2c343c",
        "title": {
            "text": "Top 10 languages",
            "left": "center",
            "top": 20,
            "textStyle": {"color": "#ccc"},
        },
        "tooltip": {"trigger": "item", "formatter": "{a} <br/>{b} : {c} ({d}%)"},
        "visualMap": {
            # "show": False,
            # "min": 80,
            # "max": 600,
            # "inRange": {"colorLightness": [0.2, 0.6]},
        },
        "series": [
            {
                "name": "Distribution among languages",
                "type": "pie",
                "radius": "55%",
                "center": ["50%", "50%"],
                "data": lang_data[1:10],
                # "roseType": "radius",
                "label": {"color": "rgba(255, 255, 255, 0.3)"},
                "labelLine": {
                    "lineStyle": {"color": "rgba(255, 255, 255, 0.3)"},
                    "smooth": 0.2,
                    "length": 10,
                    "length2": 20,
                },
                "itemStyle": {
                    "color": "#c23531",
                    "shadowBlur": 200,
                    "shadowColor": "rgba(200, 0, 0, 0.5)",
                },
                "animationType": "scale",
                "animationEasing": "elasticOut",
            }
        ],
    }
    st_echarts(options=pie_options)

    st.markdown("----")
    st.markdown("*The dashboard is obviously incomplete as I planned to add some more visualisations including ones with geo-location etc. I'm not sure if I'll be able to do it right now because of time constraints, but I'll definitely give it a shot later*")


# --------------------------------------------
# PAGES

# intro page
def introduction():
    st.header("Introduction")

    # What is this
    st.subheader("What is this?")
    st.markdown(intro_what)
    st.subheader("Data")
    st.write(stuff)
    st.markdown("-----")

    # How to use
    st.subheader("How to use?")
    st.markdown(intro_how_use)

    st.subheader("How this works")
    st.markdown(intro_how_works)
    st.markdown("-----")

    # How can this be improved
    st.subheader("How can this be improved?")
    st.markdown(intro_how_improve)
    st.markdown("-----")

    # Issues faced
    st.subheader("Issues faced")
    st.markdown(intro_issues)

def user_analysis():
    st.header("User Analysis")

    # Columns
    st.subheader("Columns analyzed")
    st.markdown("""
    `user_id`, `user_screen_name`, `user_followers_count`, `user_friends_count`, `user_created_at`, `user_favourites_count`, `user_statuses_count`, `user_lang`, `user_verified`, `user_location`
    """)
    st.markdown("-----")

    # Insights
    st.subheader("Insights (What can we say about the users who tweeted this hashtag?)")
    st.markdown(insights_user)
    st.markdown("-----")

    # Charts
    user_followers_count()
    st.markdown("-----")
    user_following_count()
    st.markdown("-----")
    user_verified()
    st.markdown("-----")
    user_posts_count()
    st.markdown("-----")
    user_favourites_count()
    st.markdown("-----")
    user_loc()


def tweet_analysis():
    st.header("Tweet Analysis")
    st.subheader("Columns analyzed")
    st.markdown("""
    `tweet_id`, `tweet_full_text`, `tweet_created_at`, `tweet_lang`, `hashtags`, `tweet_retweet_count`, `tweet_favorite_count`, `tweet_place`
    """)

    st.subheader("Insights")
    st.markdown(tweet_insights)

    st.markdown("----")
    tweet_lang()

main()
