
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64

st.set_page_config(
    page_title="Happy Birthday Abiha ❤️",
    page_icon="🎂",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent

# Find HTML file
html_path = BASE_DIR / "Abiha_Birthday_Scrapbook_Photo_Path_Fixed.html"

if not html_path.exists():
    st.error(f"HTML file not found: {html_path}")
    st.stop()

html = html_path.read_text(encoding="utf-8")

# Find music
music_files = list(BASE_DIR.rglob("*.mp3"))

if music_files:
    music_data = base64.b64encode(
        music_files[0].read_bytes()
    ).decode("utf-8")

    html = html.replace(
        'var MUSIC_SRC="abiha_website_v2/leberch-romantic-584475.mp3";',
        f'var MUSIC_SRC="data:audio/mpeg;base64,{music_data}";'
    )

# Find photos folder beside app.py
photos_dir = BASE_DIR / "static" / "photos"

if not photos_dir.exists():
    st.error(f"Photos folder not found: {photos_dir}")
    st.write("Folders available:", [p.name for p in BASE_DIR.iterdir()])
    st.stop()

# Display actual uploaded filenames for debugging
photo_files = [
    p.name for p in photos_dir.iterdir()
    if p.suffix.lower() in [".jpg", ".jpeg", ".png", ".webp"]
]

if not photo_files:
    st.error("No image files found inside static/photos.")
    st.stop()

# Change the image URL prefix to Streamlit's absolute static URL
html = html.replace(
    "abiha_website_v2/photos/",
    "/app/static/photos/"
)

st.caption(f"Photos detected: {len(photo_files)}")

components.html(
    html,
    height=950,
    scrolling=True
)
