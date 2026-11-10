
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64

st.set_page_config(
    page_title="Happy Birthday Abiha ❤️",
    page_icon="🎂",
    layout="wide"
)

# Read your birthday website
BASE_DIR = Path(__file__).resolve().parent

html_path = BASE_DIR / "Abiha_Birthday_Scrapbook_Photo_Path_Fixed.html"

if not html_path.exists():
    raise FileNotFoundError(
        f"HTML file not found: {html_path}. "
        f"Files in this folder: {[p.name for p in BASE_DIR.iterdir()]}"
    )

html = html_path.read_text(encoding="utf-8")

# Convert music to Base64 so it can play inside the website
# Automatically find the MP3 file
music_files = list(BASE_DIR.rglob("*.mp3"))

if not music_files:
    raise FileNotFoundError(
        "No MP3 file found. Please upload your birthday music "
        "inside the music folder."
    )

music_path = music_files[0]

music_data = base64.b64encode(
    music_path.read_bytes()
).decode("utf-8")

html = html.replace(
    'var MUSIC_SRC="abiha_website_v2/leberch-romantic-584475.mp3";',
    f'var MUSIC_SRC="data:audio/mpeg;base64,{music_data}";'
)

# Change photo paths to Streamlit's static folder
html = html.replace(
    'abiha_website_v2/photos/',
    'app/static/photos/'
)

# Display the website
components.html(
    html,
    height=950,
    scrolling=True
)