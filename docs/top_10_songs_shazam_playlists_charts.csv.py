import sys

import pandas as pd

spotify_data = pd.read_csv('docs/data/spotify-2023.csv', encoding='ISO-8859-1')


def remover_virgula(string):
    if isinstance(string, str):
        string = float(string.replace(",", ""))
    return string


spotify_data['in_shazam_charts'] = spotify_data['in_shazam_charts'].apply(remover_virgula)

# Descobrindo as 10 músicas mais tocadas do Shazam com base em presença em playlists e paradas.
top_songs_shazam = spotify_data[['track_name', 'artist(s)_name', 'in_shazam_charts']].copy()
top_songs_shazam['shazam_total'] = top_songs_shazam['in_shazam_charts']
top_songs_shazam = top_songs_shazam.sort_values(by='shazam_total', ascending=False).head(10)

top_songs_shazam.to_csv(sys.stdout, header=True, index=False)
