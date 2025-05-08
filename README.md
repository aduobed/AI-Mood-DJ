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

### Setting Up a Python Virtual Environment

It is recommended to use a virtual environment to manage dependencies and avoid conflicts. Below are the steps to create and activate a virtual environment using **Python 3.11.4**:

2. **Install Python 3.11.4**

If you don't have Python 3.11.4 installed, you can install it using [pyenv](https://github.com/pyenv/pyenv) or download it from the [official Python website](https://www.python.org/downloads/release/python-3114/).

3. **Create a Virtual Environment**
   ```bash
    python3.11 -m venv venv
   ```

3. **Activate the Virtual Environment**

   ***Macos***
   ```bash
    source venv/bin/activate
   ```

      ***Windows***
   ```bash
    venv\Scripts\activate
   ```

   Once activated, your terminal prompt will show (venv) indicating the environment is active. You can now install dependencies and run the app as described above.



4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up your API keys:**
   - Replace `"YOUR_SPOTIFY_API_KEY"` in `music_generator.py` with your actual Spotify API key.
   - Set up Spotify API credentials if using Spotify integration by creating an account on spotify.
   - Get started with spotify application creation [here](https://developer.spotify.com/documentation/web-api/tutorials/getting-started)

6. **Run the app:**
   ```bash
   streamlit run app.py
   ```

7. **Usage:**
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