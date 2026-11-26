
import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 설정
st.set_page_config(
    page_title="기모노 무늬와 색상 분석",
    page_icon="🎎",
    layout="wide"
)

# 제목
st.title("🎎 기모노 무늬와 색상 분석")
st.write("기모노의 무늬와 색상별 득표수를 비교해 보는 그래프입니다.")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv(
        "kimono_pattern_color_ranking.csv",
        encoding="utf-8"
    )
    return df

df = load_data()

# 무늬와 색상 데이터 분리
pattern_df = df[df["구분"] == "무늬"].copy()
color_df = df[df["구분"] == "색상"].copy()

# 득표수 기준 내림차순 정렬
pattern_df = pattern_df.sort_values(
    "득표수", ascending=False
)

color_df = color_df.sort_values(
    "득표수", ascending=False
)

# 그래프 생성 함수
def draw_chart(data, title):

    fig = px.bar(
        data,
        x="항목",
        y="득표수",
        text="득표수",
        title=title
    )

    fig.update_traces(
        textposition="outside",
        cliponaxis=False
    )

    fig.update_layout(
        xaxis_title="무늬 이름 / 색상 이름",
        yaxis_title="득표수",
        xaxis={
            "categoryorder": "total descending",
            "tickangle": -45
        },
        yaxis={
            "rangemode": "tozero"
        },
        height=600,
        showlegend=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# 무늬 그래프
st.subheader("① 무늬별 득표수")
draw_chart(pattern_df, "기모노 무늬별 득표수")

st.divider()

# 색상 그래프
st.subheader("② 색상별 득표수")
draw_chart(color_df, "기모노 색상별 득표수")

st.divider()

# 데이터 표
st.subheader("📊 원본 데이터")

tab1, tab2 = st.tabs(["무늬 데이터", "색상 데이터"])

with tab1:
    st.dataframe(
        pattern_df,
        use_container_width=True,
        hide_index=True
    )

with tab2:
    st.dataframe(
        color_df,
        use_container_width=True,
        hide_index=True
    )
