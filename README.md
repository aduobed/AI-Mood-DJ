# AI Mood DJ

## Project Overview
**AI Mood DJ** is an interactive web application that uses artificial intelligence to detect your facial emotion from a webcam snapshot and then generates and plays music that matches your mood. The app provides a seamless experience: simply start your camera, capture your image, and let the AI do the rest!

---

## AI Tools Used

- **DeepFace**: For real-time facial emotion detection from images.
- **Streamlit**: For building the interactive web interface and handling webcam input.
- **Spotify API**: For fetching and playing mood-based tracks from Spotify.

---

## How to Run

### Local Setup

1. **Clone the repository and navigate to the project folder:**
   ```bash
   git clone https://github.com/yourusername/ai_mood_dj.git
   cd ai_mood_dj
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API keys:**
   - Replace `"YOUR_SPOTIFY_API_KEY"` in `music_generator.py` with your actual Spotify API key.
   - Set up Spotify API credentials if using Spotify integration by creating an account on spotify.
   - Get started with spotify application creation [here](https://developer.spotify.com/documentation/web-api/tutorials/getting-started)

4. **Run the app:**
   ```bash
   streamlit run app.py
   ```

5. **Usage:**
   - Click "Start Camera" to enable your webcam.
   - Click "Capture Image" to take a snapshot.
   - The app will analyze your mood and play music that matches your emotion using spotify app.

---

## Key Features

- **Live webcam feed and image capture**
- **Automatic emotion detection using DeepFace**
- **Mood-based music generation and playback**
- **Spotify integration for real tracks**
- **User-friendly, modern web interface**

---

## Demo

1. Start camera → Capture image
2. AI detects your emotion
3. Enjoy music tailored to your mood!

---

## License

MIT License

---

## Contact

For questions or contributions, please open an issue or submit a pull request on GitHub.