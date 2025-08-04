# 🎵 Spotify-Genius Lyrics Bridge

> **The missing link between Spotify and Genius lyrics - because accurate hip-hop lyrics matter.**

## 🎯 The Problem

Spotify's built-in lyrics feature relies on Musixmatch, which often falls short for hip-hop and rap music. While Musixmatch covers mainstream tracks well, it struggles with:

- **Complex rap verses** with fast-paced delivery
- **Underground hip-hop** and independent artists
- **Accurate transcription** of slang and wordplay
- **Real-time lyrics** for live listening experiences

**Genius**, on the other hand, is the gold standard for hip-hop lyrics with:
- Crowdsourced accuracy from hip-hop communities
- Detailed annotations and explanations
- Coverage of underground and independent artists
- Better handling of complex rap verses

## 💡 The Solution

This automation script bridges the gap by:
- **Real-time monitoring** of your Spotify playback
- **Instant Genius integration** for accurate lyrics
- **Smart user interaction detection** (skips, replays, new songs)
- **Seamless experience** without interrupting your music flow

## ✨ Features

- **Real-time Spotify Monitoring**: Continuously tracks currently playing tracks using Spotify Web API
- **Intelligent Lyrics Retrieval**: Automatically searches and retrieves lyrics from Genius for each new song
- **Smart Ad Detection**: Identifies and handles Spotify advertisements gracefully
- **Dynamic Timing**: Calculates song duration and waits for natural song transitions
- **User Interaction Handling**: Detects track skips, replays, and user controls
- **Secure Authentication**: Implements OAuth 2.0 flow for secure API access
- **Clean Data Processing**: Extracts and formats song metadata efficiently
- **Environment-based Configuration**: Secure credential management using environment variables

## 🛠️ Technologies Used

- **Python 3.11+**
- **Spotipy**: Spotify Web API wrapper
- **LyricsGenius**: Genius API wrapper for lyrics retrieval
- **OAuth 2.0**: Secure authentication protocol

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- Spotify Premium account
- Genius API access

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd lyrics
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install spotipy lyricsgenius
   ```

### Configuration

Set up your environment variables:

```bash
export SPOTIPY_CLIENT_ID="your_spotify_client_id"
export SPOTIPY_CLIENT_SECRET="your_spotify_client_secret"
export SPOTIPY_REDIRECT_URI="your_redirect_uri"
export GENIUS_ACCESS_TOKEN="your_genius_access_token"
```

### Usage

1. **Start playing music on Spotify**
2. **Run the automation script**
   ```bash
   python automate_lyrics.py
   ```
3. **Enjoy accurate lyrics**: The script will automatically:
   - Monitor your Spotify playback
   - Detect when a new song starts
   - Retrieve accurate lyrics from Genius
   - Handle user interactions (skips, replays)
   - Wait for the song to finish before checking for the next track
   - Handle advertisements gracefully

## 📋 API Setup Guide

### Spotify API Setup
1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Create a new application
3. Add your redirect URI (e.g., `http://localhost:8888/callback`)
4. Copy your Client ID and Client Secret

### Genius API Setup
1. Visit [Genius API](https://genius.com/api-clients)
2. Create a new API client
3. Generate your access token

## 🔧 Technical Implementation

The script implements a sophisticated monitoring system:

1. **Authentication Layer**: OAuth 2.0 flow for Spotify API access
2. **Continuous Monitoring**: Infinite loop that tracks playback status
3. **Content Type Detection**: Distinguishes between tracks and advertisements
4. **Dynamic Timing**: Calculates remaining song time for optimal performance
5. **Intelligent Processing**: Extracts artist and song information
6. **Integration Layer**: Searches and retrieves lyrics from Genius
7. **Output Layer**: Displays formatted results

### Key Features Explained

- **Real-time Monitoring**: Uses `currently_playing()` API to continuously check playback status
- **Ad Detection**: Identifies when Spotify plays advertisements (`currently_playing_type == 'ad'`)
- **Smart Waiting**: Calculates remaining song time to avoid unnecessary API calls
- **Graceful Handling**: Manages edge cases like ads, paused music, and API errors
- **User Interaction Detection**: Tracks song ID and progress to detect skips, replays, and new songs

## 🎵 Why Genius Over Musixmatch?

| Feature | Musixmatch | Genius |
|---------|------------|--------|
| **Hip-hop Coverage** | Limited | Extensive |
| **Underground Artists** | Poor | Excellent |
| **Lyrics Accuracy** | Good for mainstream | Superior for hip-hop |
| **Community Input** | Limited | Crowdsourced |
| **Annotations** | None | Rich explanations |
| **Slang Handling** | Basic | Advanced |

## 📊 Project Structure

```
lyrics/
├── automate_lyrics.py    # Main automation script with continuous monitoring
├── README.md            # Project documentation
└── requirements.txt     # Python dependencies
```

## 🤝 Contributing

This project is open for contributions! Feel free to:

- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

*Built for hip-hop heads who demand lyrical accuracy* 🎤
