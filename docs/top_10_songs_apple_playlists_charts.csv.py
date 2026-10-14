import sys

import pandas as pd

spotify_data = pd.read_csv('docs/data/spotify-2023.csv', encoding='ISO-8859-1')

# Descobrindo as 10 músicas mais tocadas da Apple com base em presença em playlists e paradas.
top_songs_apple = spotify_data[['track_name', 'artist(s)_name', 'in_apple_playlists', 'in_apple_charts']].copy()
top_songs_apple['apple_total'] = top_songs_apple['in_apple_playlists'] + top_songs_apple['in_apple_charts']
top_songs_apple = top_songs_apple.sort_values(by='apple_total', ascending=False).head(10)

top_songs_apple.to_csv(sys.stdout, header=True, index=False)
