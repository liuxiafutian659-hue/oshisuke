import streamlit as st
import requests
import re

st.title("🎭 推しスケ")

name = st.text_input("芸人名")

if st.button("検索"):

    events = []
    offset = 0

    while True:

        r = requests.get(
            "https://ticket.fany.lol/search/event_more",
            params={
                "keywords": name,
                "search_type": "search_string",
                "offset": offset
            }
        )

        data = r.json()["performances"]

        if len(data) == 0:
            break

        events.extend(data)

        offset += len(data)

    st.success(f"{len(events)}件見つかりました！")

    for e in events:

        date = re.sub("<.*?>", "", e["performance_date"])

        st.write("📅", date)
        st.write("🎪", e["name"])
        st.write("📍", e["venue_name"])
        st.write("---")
