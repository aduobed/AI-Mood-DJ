import requests
import random


def generate_music(emotion):
    base_url = "https://api.spotify.com/v1"
    playlist_url = f"{base_url}/playlists/7GhawGpb43Ctkq3PRP1fOL/tracks?limit=100" if emotion == "happy" else f"{base_url}/playlists/3K1PpxEipASK24SdExJXVa/tracks?limit=20"

    # Replace with your actual API key
    api_key = f"{YOUR_API_KEY}"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.get(playlist_url, headers=headers)

    if response.status_code != 200:
        print(f"Error fetching playlist: {response.status_code}")
        return None

    data = response.json()

    random_index = random.randint(0, len(data["items"]) -1)
    music_uri = data["items"][random_index]["track"]["uri"]
    music_image = data["items"][random_index]["track"]["album"]["images"][0]["url"]

    if not music_uri:
        print("No music URLs found.")
        return None

    return music_uri, music_image
