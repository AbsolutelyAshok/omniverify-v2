import streamlit as st
import base64
from pathlib import Path


LOGO_PATH = Path(__file__).resolve().parents[2] / "assets" / "logo.png.png"


@st.cache_data
def _logo_data_uri():
    encoded_logo = base64.b64encode(LOGO_PATH.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{encoded_logo}"


def header_home():

    logo_url = _logo_data_uri()
    
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            <img src='{logo_url}' style='height:100px;' />
            <h1 style='text-align:center; color:#20243A'>OmniVerify</h1>
        </div>   
                
                """, unsafe_allow_html=True)


def header_dashboard():

    logo_url = _logo_data_uri()
    
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src='{logo_url}' style='height:85px;' />
            <h2 style='text-align:left; color:#5865F2; white-space:nowrap; flex-shrink:0;'>OmniVerify</h2>
        </div>   
                
                """, unsafe_allow_html=True)
