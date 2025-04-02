import streamlit as st
import requests
import pandas as pd

# Streamlit app title
st.title("Honda Opportunity Map - Eventbrite Integration")

# Your Eventbrite API Token (Replace with your actual token)
EVENTBRITE_TOKEN = "DXZNIUENDEQXXR47X4UD"

# Streamlit inputs for searching events
keyword = st.text_input("Enter a keyword (e.g., art, movies, music):", "art")
location = st.text_input("Enter a location (e.g., Los Angeles):", "Los Angeles")

if st.button("Search Events"):
    # Properly formatted URL with URL encoding for spaces
    url = f"https://www.eventbriteapi.com/v3/events/search/?q={keyword}&location.address={location}"
    
    headers = {
        "Authorization": f"Bearer {EVENTBRITE_TOKEN}"
    }
    
    # Make the API request
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        events = data.get("events", [])

        if len(events) > 0:
            event_list = []
            for event in events[:10]:  # Displaying top 10 results
                event_list.append({
                    "Name": event['name']['text'],
                    "Description": event['description']['text'] if event['description'] else "No description available",
                    "Start Date": event['start']['local'],
                    "Event URL": event['url']
                })
            
            # Displaying results as a DataFrame
            df = pd.DataFrame(event_list)
            st.write(df)
        else:
            st.write("No events found. Try another keyword or location.")
    else:
        st.write(f"Error fetching data. Status Code: {response.status_code}")
        st.write(response.json())  # Show detailed error message
