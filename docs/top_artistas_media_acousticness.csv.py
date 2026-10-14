import sys

import pandas as pd

spotify_data = pd.read_csv('docs/data/spotify-2023.csv', encoding='ISO-8859-1')

# Top 10 artistas por total de streams
spotify_data['streams'] = pd.to_numeric(spotify_data['streams'], errors='coerce')
top_artistas = spotify_data.groupby('artist(s)_name')['streams'].sum().sort_values(ascending=False).head(10).index
top_artistas_data = spotify_data[spotify_data['artist(s)_name'].isin(top_artistas)]

# Média de acousticness_% por artista
artista_caracteristica_media = top_artistas_data.groupby('artist(s)_name')['acousticness_%'].mean().sort_values(ascending=False)

df_artista_caracteristica_media = pd.DataFrame(list(artista_caracteristica_media.items()), columns=['artista', 'media'])
df_artista_caracteristica_media.to_csv(sys.stdout, header=True, index=False)
