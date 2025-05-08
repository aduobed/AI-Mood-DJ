import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
import av
import webbrowser
from emotion_detection import detect_emotion
from music_generator import generate_music

EMOJI_MAP = {
    "happy": "😄",
    "sad": "😢",
    "angry": "😠",
    "surprise": "😲",
    "fear": "😨",
    "neutral": "😐"
}

st.set_page_config(page_title="AI Mood DJ", layout="centered")
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<div class="title">🎧 AI Mood DJ</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Let AI play music based on your mood!</div>',
            unsafe_allow_html=True)

# Session state for camera and last frame
if "last_frame" not in st.session_state:
    st.session_state["last_frame"] = None
if "camera_active" not in st.session_state:
    st.session_state["camera_active"] = False

# Start camera button only toggles camera
if st.button("▶️ Start Camera"):
    st.session_state["camera_active"] = True
    st.session_state["last_frame"] = None  # Reset last frame

# Show live feed if camera is active
if st.session_state["camera_active"]:
    class VideoProcessor(VideoProcessorBase):
        def __init__(self):
            self.frame = None

        def recv(self, frame):
            img = frame.to_ndarray(format="bgr24")
            self.frame = img
            return av.VideoFrame.from_ndarray(img, format="bgr24")

    ctx = webrtc_streamer(
        key="mood-dj",
        video_processor_factory=VideoProcessor,
        media_stream_constraints={"video": True, "audio": False},
        async_processing=True,
    )

    # Only process when Capture Image is clicked
    if ctx.video_processor and st.button("📸 Capture Image"):
        st.session_state["last_frame"] = ctx.video_processor.frame
        st.session_state["camera_active"] = False
        st.rerun()

# Only process and show results if an image has been captured
if st.session_state["last_frame"] is not None:
    st.image(st.session_state["last_frame"],
             channels="BGR", caption="Captured Image")
    with st.spinner("Analyzing your expression..."):
        emotion = detect_emotion(st.session_state["last_frame"])
        emoji = EMOJI_MAP.get(emotion.lower(), "😐")
        st.success(f"Detected emotion: **{emotion.capitalize()} {emoji}**")

    with st.spinner("Finding the perfect track..."):
        try:
            music_url, music_image = generate_music(emotion)
            if music_url is None:
                st.error("No music found for this emotion.")
            else:
                st.markdown(
                    "🎶 **Now playing music for your mood on spotify...**")
                st.image(f"{music_image}", caption="Album Art",
                         use_container_width=True)
                # Convert spotify:track:... to https://open.spotify.com/track/...
                if music_url.startswith("spotify:track:"):
                    web_url = "https://open.spotify.com/track/" + \
                        music_url.split(":")[-1]
                else:
                    web_url = music_url
                if st.button("Open in Spotify"):
                    webbrowser.open(music_url)
        except Exception as e:
            st.error(f"Failed to play music: {e}")

st.markdown("</div>", unsafe_allow_html=True)
