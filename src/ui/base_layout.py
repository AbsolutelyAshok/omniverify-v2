import streamlit as st

#F0F2F6 ,5865F2

def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    background: #F0F2F6 !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color:#E0E3FF !important;
                    padding:2.5rem !important;
                    border-radius: 5rem !important;
                    }

                .stApp div[data-testid="stColumn"] h2 {
                    color:#20243A !important;
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background: #E0E3FF !important;
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    

    

def style_base_layout():
# asdasd
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

        :root {
            --app-font-family: 'Outfit', system-ui, -apple-system, BlinkMacSystemFont,
                'Segoe UI', Roboto, Arial, sans-serif;
        }

        body,
        .stApp,
        .stApp button,
        .stApp input,
        .stApp textarea,
        .stApp select,
        .stApp label {
            font-family: var(--app-font-family) !important;
        }

                
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top:1.5rem !important;    
            }

            h1 {
                font-family: var(--app-font-family) !important;
                font-size: clamp(2rem, 5vw, 3rem) !important;
                font-weight: 700 !important;
                line-height: 1.15 !important;
                margin-bottom: 0 !important;
                color:#20243A !important;
            }
                

            h2 {
                font-family: var(--app-font-family) !important;
                font-size: clamp(1.5rem, 3.4vw, 2rem) !important;
                font-weight: 650 !important;
                line-height: 1.2 !important;
                margin-bottom: 0 !important;
                color:#20243A !important;
            }
                
            h3, h4, p {
                font-family: var(--app-font-family) !important;
            }

            h3, h4 {
                color:#20243A !important;
                font-weight: 600 !important;
            }

            h3 {
                font-size: clamp(1.2rem, 2.5vw, 1.5rem) !important;
            }

            [data-testid="stWidgetLabel"] p,
            [data-testid="stImageCaption"] p {
                color:#20243A !important;
            }
                

            button{
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button:hover{
                transform :scale(1.05)}
        </style>  

                """
            ,unsafe_allow_html=True)
