import sys

import pandas as pd

spotify_data = pd.read_csv('docs/data/spotify-2023.csv', encoding='ISO-8859-1')

# Descobrindo as 10 músicas mais tocadas do Spotify com base em presença em playlists e paradas.
top_songs_spotify = spotify_data[['track_name', 'artist(s)_name', 'in_spotify_playlists', 'in_spotify_charts']].copy()
top_songs_spotify['spotify_total'] = top_songs_spotify['in_spotify_playlists'] + top_songs_spotify['in_spotify_charts']
top_songs_spotify = top_songs_spotify.sort_values(by='spotify_total', ascending=False).head(10)

top_songs_spotify.to_csv(sys.stdout, header=True, index=False)
