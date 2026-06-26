import streamlit as st
from datetime import datetime

st.set_page_config(page_title="WaraCal", page_icon="🗓", layout="centered")

# =====================
# ヘッダー
# =====================
st.title("WaraCal 🗓")
st.caption("芸人スケジュールを、カレンダーに。")

st.divider()

# =====================
# 検索
# =====================
query = st.text_input("芸人名を入力", placeholder="例：三遊間")

search = st.button("検索")

# =====================
# ダミーデータ（後で差し替え）
# =====================
dummy_data = {
    "三遊間": [
        {
            "date": "2026/06/26",
            "title": "よしもとライブ東京",
            "time": "19:00",
            "place": "ルミネtheよしもと"
        },
        {
            "date": "2026/06/27",
            "title": "単独ライブ",
            "time": "18:30",
            "place": "なんばグランド花月"
        }
    ],
    "default": [
        {
            "date": "2026/06/26",
            "title": "サンプルライブ",
            "time": "19:00",
            "place": "○○劇場"
        }
    ]
}

# =====================
# 検索結果表示
# =====================
if search:
    data = dummy_data.get(query, dummy_data["default"])

    st.subheader("📅 出演スケジュール")

    # 日付ごとにまとめる
    grouped = {}
    for item in data:
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
