#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 00:25:08 2024

@author: suriya
"""
import streamlit as st

import pandas as pd
def main_page():
    st.markdown("# write")
    st.sidebar.markdown("# write 🎈")
    st.write("hi suriya")
    from datetime import date

    from datetime import datetime
    from dateutil.relativedelta import relativedelta
    
    
    # Today's date
    today = datetime.today()
    
    # Target date
    target_date = datetime(2025, 1, 1)
    
    # Calculate time difference
    time_difference = target_date - today
    
    # Extract days, hours, minutes, and seconds
    days = time_difference.days
    remaining_minutes = time_difference.total_seconds() // 60
    remaining_seconds = time_difference.total_seconds()
    
    # Display results
    st.write("Today's date:", today)
    st.write(f"Days until January 1, 2025: {days}")
    st.write(f"Remaining minutes: {remaining_minutes} minutes")
    st.write(f"Remaining seconds: {remaining_seconds} seconds")

    
    import pandas as pd
    import re
    import pymongo
    client = pymongo.MongoClient("mongodb+srv://suriya315:12345678s@cluster0.kbh9v.mongodb.net/?retryWrites=true&w=majority")
    db = client.log
    pc=db.val
    mind=st.text_input("enter whati in your mind")
    heart=st.text_input("enter whati your heart tell dopamine")
    place=st.text_input("place")
    why=st.text_input("why")
    if st.button("submit"):
        current_date_time = datetime.now()
        data = {
        "mind": mind,
        "heart": heart,
        "place": place,
        "why": why,
        "date_time": current_date_time
        }
        pc.insert_one(data)
    
def page2():
    st.markdown("# analize ❄️")
    st.sidebar.markdown("# search ❄️")
    import pandas as pd
    import re
    import pymongo
    client = pymongo.MongoClient("mongodb+srv://suriya315:12345678s@cluster0.kbh9v.mongodb.net/?retryWrites=true&w=majority")
    db = client.log
    pc=db.val
    cursor = pc.find()

    # Convert the cursor to a list of dictionaries
    data_list = list(cursor)
    
    # Convert the list of dictionaries to a Pandas DataFrame
    df = pd.DataFrame(data_list)
    
    # Display the DataFrame
    st.write(df)
page_names_to_funcs = {
    "write": main_page,
    "analize": page2,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()