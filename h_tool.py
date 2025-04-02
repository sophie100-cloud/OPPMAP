import streamlit as st
import requests
import pandas as pd

# Streamlit app title
st.title("Honda Opportunity Map - Eventbrite Integration")

# Your Eventbrite API Token
EVENTBRITE_TOKEN = "DXZNIUENDEQXXR47X4UD"  # Replace with your token

# Streamlit inputs for searching events
keyword = st.text_input("Enter a keyword (e.g., art, movies, music):")
location = st.text_input("Enter a location (e.g., Los Angeles):")

if st.button("Search Events"):
    # Eventbrite API URL
    url = f"https://www.eventbriteapi.com/v3/events/search/?q={keyword}&location.address={location}"
    headers = {"Authorization": f"Bearer {EVENTBRITE_TOKEN}"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        events = data.get("events", [])

        if len(events) > 0:
            event_list = []

            for event in events[:10]:  # Display top 10 events
                event_list.append({
                    "Name": event['name']['text'],
                    "Description": event['description']['text'] if event['description'] else "No description available",
                    "Start Date": event['start']['local'],
                    "Event URL": event['url']
                })
            
            # Displaying results in a DataFrame
            df = pd.DataFrame(event_list)
            st.write(df)
        else:
            st.write("No events found. Try another keyword or location.")
    else:
        st.write("Error fetching data. Make sure your API key is correct.")
