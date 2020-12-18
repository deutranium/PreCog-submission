import streamlit as st

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

def introduction():
    st.title("Introduction")

def user_analysis():
    st.title("User Analysis")

def tweet_analysis():
    st.title("Tweet Analysis")


main()
