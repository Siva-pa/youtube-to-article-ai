import streamlit as st
from youtube_utils import extract_video_id, get_transcript
from ai_utils import generate_article
from pdf_utils import create_pdf

# --- 1. SETUP & PAGE CONFIG ---
st.set_page_config(
    page_title="Vid2Article AI", 
    page_icon="✨", 
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- 2. CUSTOM CSS (The Secret Sauce for Attractiveness) ---
st.markdown("""
    <style>
    /* Gradient Main Button */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #FF4B4B 0%, #FF8F8F 100%);
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        letter-spacing: 0.5px;
        padding: 0.5rem 1rem;
        transition: all 0.3s ease;
        width: 100%;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(255, 75, 75, 0.2);
    }
    
    /* Sleeker Text Inputs */
    div[data-baseweb="input"] > div {
        border-radius: 8px;
        border: 1px solid #E0E0E0;
    }
    
    /* Download Button Specific Styling */
    div[data-testid="stDownloadButton"] > button {
        background: linear-gradient(90deg, #4CAF50 0%, #81C784 100%);
    }
    div[data-testid="stDownloadButton"] > button:hover {
        box-shadow: 0 6px 12px rgba(76, 175, 80, 0.2);
    }
    
    /* Clean up the header space */
    .block-container {
        padding-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4180/4180439.png", width=60) # A little AI icon
    st.title("⚙️ Setup")
    st.markdown("Before you begin, connect your AI brain.")
    
    api_key = st.text_input("Google Gemini API Key", type="password", placeholder="Paste key here...")
    
    st.markdown("---")
    st.caption("Don't have an API key? Get one for free from [Google AI Studio](https://aistudio.google.com/app/apikey).")

# --- 4. HERO SECTION ---
# Using columns to center the header nicely
col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    st.markdown("<h1 style='text-align: center; color: #1E1E1E;'>🎥 Vid2Article AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666; font-size: 1.1rem; margin-bottom: 2rem;'>Transform any YouTube video into a beautifully formatted, downloadable PDF article in seconds.</p>", unsafe_allow_html=True)

# --- 5. MAIN INPUT AREA ---
st.markdown("### 🔗 Target Video")
youtube_url = st.text_input("Paste the YouTube URL here:", placeholder="https://www.youtube.com/watch?v=...")

# Wrap the button in empty columns to make it look prominent but not stretched across the whole screen
_, btn_col, _ = st.columns([1, 2, 1])

with btn_col:
    generate_btn = st.button("✨ Generate Article & PDF", use_container_width=True)

# --- 6. EXECUTION LOGIC ---
if generate_btn:
    if not api_key:
        st.error("⚠️ Please enter your Gemini API Key in the sidebar to continue.")
    elif not youtube_url:
        st.warning("⚠️ Please paste a YouTube URL first.")
    else:
        video_id = extract_video_id(youtube_url)
        
        if not video_id:
            st.error("❌ Invalid YouTube URL. Please check and try again.")
        else:
            # We use an empty placeholder to update status dynamically
            status_container = st.empty()
            
            with status_container.container():
                with st.status("🚀 Processing your video...", expanded=True) as status:
                    # 1. Extract
                    st.write("📥 Extracting transcript...")
                    transcript, error = get_transcript(video_id)
                    
                    if error:
                        status.update(label="Extraction failed!", state="error", expanded=True)
                        st.error(f"Make sure the video has closed captions. Details: {error}")
                        st.stop()
                        
                    # 2. Generate
                    st.write("🧠 AI is writing the article...")
                    article_text, ai_error = generate_article(transcript, api_key)
                    
                    if ai_error:
                        status.update(label="AI Generation failed!", state="error", expanded=True)
                        st.error(f"Details: {ai_error}")
                        st.stop()
                        
                    # 3. PDF Formatting
                    st.write("🎨 Formatting your PDF...")
                    pdf_bytes, pdf_error = create_pdf(article_text)
                    
                    if pdf_error:
                        status.update(label="PDF Formatting failed!", state="error", expanded=True)
                        st.error(f"Details: {pdf_error}")
                        st.stop()
                        
                    status.update(label="All done!", state="complete", expanded=False)
            
            # --- 7. SUCCESS UI ---
            st.balloons()
            st.success("🎉 Your article is ready!")
            
            # Use an expander for the preview so it doesn't take up the whole screen
            with st.expander("👀 Preview Article Text"):
                st.markdown(article_text)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Prominent Download Button
            _, down_col, _ = st.columns([1, 2, 1])
            with down_col:
                st.download_button(
                    label="📥 Download High-Quality PDF",
                    data=pdf_bytes,
                    file_name="Insightful_Article.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )