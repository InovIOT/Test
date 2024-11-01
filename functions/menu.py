import streamlit as st
import config as c

def update_language():
    # Update session state when the language is changed
    st.session_state['language'] = st.session_state['selected_language']

def menu():
    # Check if language is already in session_state, else initialize it with a default value
    if 'language' not in st.session_state:
        st.session_state['language'] = "Svenska"  # Default language
    
    if 'app_version' not in st.session_state:
        st.session_state['app_version'] = c.app_version
    if 'update_date' not in st.session_state:
        st.session_state['update_date'] = c.update_date

    # Sidebar for language selection
    st.sidebar.selectbox(
        "Språk", 
        ("Svenska", "English"),
        index = ["Svenska", "English"].index(st.session_state['language']),
        key = "selected_language",
        on_change = update_language,
        label_visibility = "collapsed"
    )

    if st.session_state['language'] == "Svenska":
        st.sidebar.markdown("### Meny")

        # Home section
        st.sidebar.page_link("Start.py", label="Start", icon=":material/home:")
        st.sidebar.markdown("###### ")

        # AI Lab section with dropdown
        st.sidebar.markdown("### AI-labbet")
        
        with st.sidebar.expander("💬 Chat & Text", expanded=True):
            st.page_link("pages/chatbot.py", label="Chat", icon=":material/forum:")
            st.page_link("pages/chat_with_document.py", label="Chatta med dina dokument", icon=":material/description:")
            st.page_link("pages/transcribe.py", label="Transkribering", icon=":material/transcribe:")
            
            # Chat History (show last 10)
            if 'chat_history' in st.session_state:
                st.markdown("##### Senaste chattar")
                for chat in list(st.session_state.chat_history)[-10:]:
                    st.markdown(f"- {chat}")

        with st.sidebar.expander("🖼️ Bild", expanded=True):
            st.page_link("pages/image.py", label="Bild", icon=":material/image:")
            st.page_link("pages/image_analysis.py", label="Bildanalys", icon=":material/image:")

        st.sidebar.markdown("# ")
        with st.sidebar.container(border=True):
            st.markdown(f"""__Version:__ {st.session_state["app_version"]}  
            __Uppdaterad:__ {st.session_state["update_date"]}
            """)

    if st.session_state['language'] == "English":
        st.sidebar.markdown("### Menu")

        # Home section
        st.sidebar.page_link("Start.py", label="Start", icon=":material/home:")
        st.sidebar.markdown("###### ")

        # AI Lab section with dropdown
        st.sidebar.markdown("### AI-lab")
        
        with st.sidebar.expander("💬 Chat & Text", expanded=True):
            st.page_link("pages/chatbot.py", label="Chat", icon=":material/forum:")
            st.page_link("pages/chat_with_document.py", label="Chat with your documents", icon=":material/description:")
            st.page_link("pages/transcribe.py", label="Transcribe", icon=":material/transcribe:")
            
            # Chat History (show last 10)
            if 'chat_history' in st.session_state:
                st.markdown("##### Recent Chats")
                for chat in list(st.session_state.chat_history)[-10:]:
                    st.markdown(f"- {chat}")

        with st.sidebar.expander("🖼️ Image", expanded=True):
            st.page_link("pages/image.py", label="Image", icon=":material/image:")
            st.page_link("pages/image_analysis.py", label="Image analysis", icon=":material/image:")

        st.sidebar.markdown("# ")
        with st.sidebar.container(border=True):
            st.markdown(f"""__Version:__ {st.session_state["app_version"]}  
            __Updated:__ {st.session_state["update_date"]}
            """)
