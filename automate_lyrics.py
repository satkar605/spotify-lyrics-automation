# Lyrics Automation Script
import os
import json
import time
import spotipy
import lyricsgenius as lg

# =============================================================================
# ENVIRONMENT VARIABLES SETUP
# =============================================================================
# Environment variables for API credentials
spotify_client_id = os.getenv("SPOTIPY_CLIENT_ID")
spotify_client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
spotify_redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")
genius_access_token = os.getenv("GENIUS_ACCESS_TOKEN")

scope = 'user-read-currently-playing'

# =============================================================================
# SPOTIFY AUTHENTICATION SETUP
# =============================================================================
oauth_object = spotipy.SpotifyOAuth(client_id=spotify_client_id, 
                                    client_secret=spotify_client_secret, 
                                    redirect_uri=spotify_redirect_uri, 
                                    scope=scope)

print(oauth_object)

token_dict = oauth_object.get_access_token()
token = token_dict['access_token']

# =============================================================================
# API CLIENT INITIALIZATION
# =============================================================================
spotify_object = spotipy.Spotify(auth=token)
genius_object = lg.Genius(genius_access_token)

# =============================================================================
# SONG TRACKING VARIABLES
# =============================================================================
# Track the last processed song to detect changes
last_song_id = None
last_progress = 0

print("Spotify Lyrics Monitor Started")
print("Monitoring for song changes...\n")

# =============================================================================
# MAIN MONITORING LOOP
# =============================================================================
while True:
    try:
        current = spotify_object.currently_playing()
        
        if not current:
            print("No music currently playing...")
            time.sleep(5)
            continue
            
        status = current.get('currently_playing_type')
        
        if status == 'track':
            # =================================================================
            # SONG INFORMATION EXTRACTION
            # =================================================================
            item = current['item']
            artist_name = item['album']['artists'][0]['name']
            song_title = item['name']
            song_id = item['id']
            progress = current.get('progress_ms', 0)
            
            # =================================================================
            # USER INTERACTION DETECTION
            # =================================================================
            # Check if this is a new song or user interaction
            is_new_song = song_id != last_song_id
            is_replay = song_id == last_song_id and progress < last_progress
            is_skip = song_id == last_song_id and progress > last_progress + 10000  # 10 second jump
            
            # =================================================================
            # LYRICS FETCHING AND DISPLAY
            # =================================================================
            if is_new_song or is_replay:
                print(f"\nNow playing: {song_title} by {artist_name}")
                print("=" * 50)
                
                try:
                    song = genius_object.search_song(title=song_title, artist=artist_name)
                    if song:
                        lyrics = song.lyrics
                        print(lyrics)
                    else:
                        print(f"Lyrics not found for '{song_title}' by {artist_name}")
                except Exception as e:
                    print(f"Error fetching lyrics: {str(e)}")
                
                print("=" * 50)
                
                last_song_id = song_id
                last_progress = progress
                
            elif is_skip:
                print(f"\nTrack skipped: {song_title} by {artist_name}")
                last_song_id = song_id
                last_progress = progress
            
            # Update progress for next iteration
            last_progress = progress
            
            # Shorter sleep time for more responsive monitoring
            time.sleep(2)
            
        elif status == 'ad':
            print("Advertisement playing...")
            time.sleep(5)
            
        else:
            print("Music paused or no track playing")
            time.sleep(5)
            
    except Exception as e:
        print(f"Error: {str(e)}")
        time.sleep(5)
        continue