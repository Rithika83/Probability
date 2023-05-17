import os
import random
import pygame

def create_playlist(folder_path,):
    # audio_extensions = [".mp3", ".wav"]  # Supported audio file extensions 
    
    # Get all files in the folder
    audio_files = os.listdir(folder_path)
    
    # Filter audio files
    # audio_files = [file for file in files if os.path.splitext(file)[1] in audio_extensions] 
    
    # if shuffle:
    random.shuffle(audio_files)  # Shuffle the list of audio files
    
    # Create playlist file
    # playlist_file = os.path.join(folder_path, playlist_name + ".m3u")
    
    # with open(playlist_file, "w") as f:
        # Write each audio file path to the playlist file
    print (audio_files)
    for audio_file in audio_files:
        file_path = os.path.join(folder_path, audio_file)
        play_playlist(file_path)
    
    print("Playlist created successfully!")
    
    
    return playlist_file

def play_playlist(playlist_file):
    print(playlist_file)		
    # Initialize the mixer module
    pygame.mixer.init()
    
    # Load the playlist
    pygame.mixer.music.load(playlist_file)
    
    # Start playing the playlist
    pygame.mixer.music.play()
    
    # Wait for the playlist to finish playing
    while pygame.mixer.music.get_busy():
        continue

# Usage example
folder_path = "./songs"
shuffle_option = True  # Set to True for shuffling, False otherwise
playlist_file = create_playlist(folder_path)
play_playlist(playlist_file)

