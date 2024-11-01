import streamlit as st
import config as c


def page_config():
    # Set default theme to light
    if 'theme' not in st.session_state:
        st.session_state.theme = 'light'
    
    st.set_page_config(
        page_title = c.page_title,
        layout="centered",
        page_icon=":material/smart_toy:",
        initial_sidebar_state="expanded")

    # Add theme toggle in sidebar
    with st.sidebar:
        st.write("## Theme Settings")
        if st.button("Toggle Dark/Light Mode"):
            st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'
            st.experimental_rerun()


# CSS styling
def styling():
    # Base styles
    base_styles = """
    [data-testid="stChatMessageAvatarUser"], [alt="user avatar"] {
        height: 2.8rem;
        width: 2.8rem;
        border-radius: 8px;    
    }
                
    [data-testid="stChatMessageAvatarAssistant"], [alt="assistant avatar"] {
        height: 2.8rem;
        width: 2.8rem;
        border-radius: 8px;
    }
                
    [aria-label="Chat message from user"] {
        padding: 10px;
        border-radius: 0.5rem;
    }
                
    [aria-label="Chat message from assistant"] {
        padding: 10px;
    }
                
    .block-container {
        padding-top: 3rem;
        padding-bottom: 0rem;
    }
                
    .stPageLink {
        margin-bottom: -12px;
    }
                
    [data-testid="stPageLink-NavLink"] p {
        font-size: 1rem !important;
    }
                
    h6 {
        padding-bottom: 0rem;
    }
                
    p {
        font-size: 1.1rem;
    }
    """

    # Dark mode specific styles
    dark_mode = """
    .stApp {
        background-color: #1a1a1a;
        color: #ffffff;
    }

    .stMarkdown {
        color: #ffffff;
    }

    .stButton button {
        background-color: #2e2e2e;
        color: #ffffff;
        border: 1px solid #404040;
    }

    .stTextInput input {
        background-color: #2e2e2e;
        color: #ffffff;
        border: 1px solid #404040;
    }

    .stSelectbox select {
        background-color: #2e2e2e;
        color: #ffffff;
    }

    [data-testid="stSidebar"] {
        background-color: #262626;
    }

    .stAlert {
        background-color: #2e2e2e;
        color: #ffffff;
    }

    [data-testid="stHeader"] {
        background-color: #1a1a1a;
    }
    """

    # Light mode specific styles
    light_mode = """
    .stApp {
        background-color: #ffffff;
        color: #000000;
    }

    .stMarkdown {
        color: #000000;
    }

    .stButton button {
        background-color: #f0f2f6;
        color: #000000;
        border: 1px solid #e0e0e0;
    }

    .stTextInput input {
        background-color: #ffffff;
        color: #000000;
        border: 1px solid #e0e0e0;
    }
    """

    # Combine styles based on theme
    theme_styles = dark_mode if st.session_state.theme == 'dark' else light_mode
    final_styles = f"""
    <style>
    {base_styles}
    {theme_styles}
    </style>
    """

    st.markdown(final_styles, unsafe_allow_html=True)
