import sys

import pandas as pd

spotify_data = pd.read_csv('docs/data/spotify-2023.csv', encoding='ISO-8859-1')


def remover_virgula(string):
    if isinstance(string, str):
        string = float(string.replace(",", ""))
    return string


spotify_data['in_deezer_playlists'] = spotify_data['in_deezer_playlists'].apply(remover_virgula)

# Descobrindo as 10 músicas mais tocadas do Deezer com base em presença em playlists e paradas.
top_songs_deezer = spotify_data[['track_name', 'artist(s)_name', 'in_deezer_playlists', 'in_deezer_charts']].copy()
top_songs_deezer['deezer_total'] = top_songs_deezer['in_deezer_playlists'] + top_songs_deezer['in_deezer_charts']
top_songs_deezer = top_songs_deezer.sort_values(by='deezer_total', ascending=False).head(10)

top_songs_deezer.to_csv(sys.stdout, header=True, index=False)
