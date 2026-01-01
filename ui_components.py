import streamlit as st

def ui_card(title, content):
    st.markdown(
        f"""
        <div style="
            background-color:#0f172a;
            padding:20px;
            border-radius:12px;
            margin-bottom:20px;
        ">
            <h3>{title}</h3>
            <div>{content}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
