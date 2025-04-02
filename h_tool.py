import streamlit as st
import requests

# App title
st.title("Honda Opportunity Map")

# Enter keywords for searching events
keyword = st.text_input("Enter a keyword (e.g., art, movies, music):")
location = st.text_input("Enter a location (e.g., Los Angeles):")

if st.button("Search Events"):
    # Fetch data from Eventbrite API
    url = f"https://www.eventbriteapi.com/v3/events/search/?q={keyword}&location.address={location}"
    headers = {"Authorization": "Bearer YOUR_EVENTBRITE_API_KEY"}  # Replace with your Eventbrite API Key
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        events = data.get("events", [])

        if len(events) > 0:
            for event in events[:5]:  # Display top 5 events
                st.write(f"### {event['name']['text']}")
                st.write(event['description']['text'])
                st.write(f"**Start Date:** {event['start']['local']}")
                st.write(f"[More Info]({event['url']})")
                st.write("---")
        else:
            st.write("No events found.")
    else:
        st.write("Error fetching data. Make sure your API key is correct.")
