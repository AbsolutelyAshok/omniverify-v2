import streamlit as st


from supabase import create_client, Client

supabase_url = st.secrets["SUPABASE_URL"]
supabase_key = st.secrets.get("SUPABASE_SECRET_KEY") or st.secrets.get("SUPABASE_KEY")

if not supabase_key:
    raise KeyError("Add SUPABASE_SECRET_KEY or SUPABASE_KEY to Streamlit secrets.")

supabase: Client = create_client(supabase_url, supabase_key)
