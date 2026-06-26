import streamlit as st

st.set_page_config(page_title="WaraCal", page_icon="🗓")

# ヘッダー
st.title("WaraCal 🗓")
st.caption("芸人スケジュールをカレンダーにするやつ")

st.divider()

# 検索
query = st.text_input("芸人名を入力（例：三遊間）")

search = st.button("検索")

# ダミーデータ（後で本物に変える）
data = {
    "三遊間": [
        {"date": "2026/06/26", "title": "よしもとライブ東京", "time": "19:00", "place": "ルミネtheよしもと"},
        {"date": "2026/06/27", "title": "単独ライブ", "time": "18:30", "place": "なんばグランド花月"}
    ],
    "default": [
        {"date": "2026/06/26", "title": "サンプルライブ", "time": "19:00", "place": "○○劇場"}
    ]
}

if search:
    result = data.get(query, data["default"])

    st.subheader("📅 出演スケジュール")

    grouped = {}
    for item in result:
        grouped.setdefault(item["date"], []).append(item)

    for date, events in grouped.items():
        st.markdown(f"### 🗓 {date}")

        for e in events:
            st.markdown(
                f"""
**{e['title']}**  
{e['time']} / {e['place']}  
➕ カレンダー追加（仮）
                """
            )
            st.divider()
