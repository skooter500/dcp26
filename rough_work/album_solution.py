# Irish Music Albums Lab - SOLUTIONS
# Instructor Answer Key

import pandas as pd

# Setup
albums_df = pd.read_csv("data/album.csv")
tracks_df = pd.read_csv("data/albumtracktune.csv")

print("=" * 80)
print("PART 1: EXPLORE THE ALBUMS")
print("=" * 80)

# Task 1.1: Load and Inspect Albums
print("\n--- Task 1.1: Load and Inspect ---")
print(f"Number of albums: {len(albums_df)}")
print(f"Shape: {albums_df.shape}")
print(f"\nColumn names: {list(albums_df.columns)}")

print("\nFirst 5 albums:")
print(albums_df.head())

print("\nLast 5 albums:")
print(albums_df.tail())

# Task 1.2: Data Types
print("\n--- Task 1.2: Data Types ---")
print(albums_df.info())
print("\nMissing values per column:")
print(albums_df.isnull().sum())

# Task 1.3: Unique Values
print("\n--- Task 1.3: Unique Values ---")
print(f"Number of unique artists: {albums_df['artist'].nunique()}")
print(f"\nAll artists:")
print(albums_df['artist'].unique())
print("\nArtist counts:")
print(albums_df['artist'].value_counts())

print("\n" + "=" * 80)
print("PART 2: EXPLORE THE TRACKS")
print("=" * 80)

# Task 2.1: Load and Inspect Tracks
print("\n--- Task 2.1: Load and Inspect ---")
print(f"Number of tracks: {len(tracks_df)}")
print(f"Shape: {tracks_df.shape}")
print(f"\nColumns: {list(tracks_df.columns)}")
print("\nFirst few tracks:")
print(tracks_df.head())
print("\nRelationship: album_id in tracks_df refers to id in albums_df")

# Task 2.2: Track Numbers
print("\n--- Task 2.2: Track Numbers ---")
print(f"Highest track number: {tracks_df['track_num'].max()}")
print(f"Highest tune number: {tracks_df['tune_num'].max()}")
print(f"\nDistribution of tune_num:")
print(tracks_df['tune_num'].value_counts().sort_index())

# Task 2.3: Common Tune Titles
print("\n--- Task 2.3: Common Tune Titles ---")
print("Top 10 most frequent tune titles:")
print(tracks_df['title'].value_counts().head(10))

print("\n" + "=" * 80)
print("PART 3: FILTERING AND COUNTING")
print("=" * 80)

# Task 3.1: Albums by Artist
print("\n--- Task 3.1: Albums by Artist ---")

altan = albums_df[albums_df['artist'] == 'Altan']
print(f"\nAltan albums: {len(altan)}")
print(altan)

martin_hayes = albums_df[albums_df['artist'] == 'Martin Hayes']
print(f"\nMartin Hayes albums: {len(martin_hayes)}")
print(martin_hayes)

bothy_band = albums_df[albums_df['artist'] == 'The Bothy Band']
print(f"\nThe Bothy Band albums: {len(bothy_band)}")
print(bothy_band)

# Task 3.2: Tracks on Specific Albums
print("\n--- Task 3.2: Tracks on Album 1 ---")
album_1_tracks = tracks_df[tracks_df['album_id'] == 1]
print(f"Number of tracks on album 1: {album_1_tracks['track_num'].nunique()}")
print(f"Total tunes on album 1: {len(album_1_tracks)}")
print("\nAll tracks on album 1:")
print(album_1_tracks)

# Task 3.3: Multi-Tune Tracks
print("\n--- Task 3.3: Multi-Tune Tracks ---")
multi_tune = tracks_df[tracks_df['tune_num'] > 1]
print(f"Number of tracks with multiple tunes: {len(multi_tune)}")
print("\nFirst few multi-tune tracks:")
print(multi_tune.head(10))

print("\n" + "=" * 80)
print("PART 4: GROUPING AND AGGREGATING")
print("=" * 80)

# Task 4.1: Tracks per Album
print("\n--- Task 4.1: Tracks per Album ---")
tracks_per_album = tracks_df.groupby('album_id')['track_num'].nunique()
print("Tracks per album:")
print(tracks_per_album)
print(f"\nAlbum with most tracks: Album {tracks_per_album.idxmax()} with {tracks_per_album.max()} tracks")

# Task 4.2: Tunes per Album
print("\n--- Task 4.2: Tunes per Album ---")
tunes_per_album = tracks_df.groupby('album_id').size()
print("Total tunes per album:")
print(tunes_per_album)
print(f"\nAlbum with most tunes: Album {tunes_per_album.idxmax()} with {tunes_per_album.max()} tunes")

# Task 4.3: Average Tunes per Track
print("\n--- Task 4.3: Average Tunes per Track ---")
avg_tunes_per_track = tracks_df.groupby('album_id')['tune_num'].mean()
print("Average tune_num per album (indicates multi-tune tracks):")
print(avg_tunes_per_track.sort_values(ascending=False))

print("\n" + "=" * 80)
print("PART 5: SORTING")
print("=" * 80)

# Task 5.1: Sort Albums
print("\n--- Task 5.1: Sort Albums ---")

print("\nAlphabetically by title:")
print(albums_df.sort_values('title').head())

print("\nAlphabetically by artist:")
print(albums_df.sort_values('artist').head())

print("\nBy ID descending:")
print(albums_df.sort_values('id', ascending=False).head())

# Task 5.2: Sort Tracks
print("\n--- Task 5.2: Sort Tracks ---")

print("\nBy album_id then track_num:")
print(tracks_df.sort_values(['album_id', 'track_num']).head(15))

print("\nBy title alphabetically:")
print(tracks_df.sort_values('title').head())

print("\n" + "=" * 80)
print("PART 6: MERGING THE DATASETS")
print("=" * 80)

# Task 6.1: Simple Merge
print("\n--- Task 6.1: Simple Merge ---")
merged_df = pd.merge(tracks_df, albums_df, left_on='album_id', right_on='id')
print(f"Merged dataframe shape: {merged_df.shape}")
print("\nMerged columns:")
print(list(merged_df.columns))

# Task 6.2: Explore Merged Data
print("\n--- Task 6.2: Explore Merged Data ---")
print(f"Rows in merged dataframe: {len(merged_df)}")
print("\nFirst 10 rows of merged data:")
print(merged_df[['title_x', 'track_num', 'tune_num', 'title_y', 'artist']].head(10))

# Task 6.3: Questions with Merged Data
print("\n--- Task 6.3: Questions with Merged Data ---")

# Martin Hayes tracks
martin_hayes_tracks = merged_df[merged_df['artist'] == 'Martin Hayes']
print(f"\nMartin Hayes has {len(martin_hayes_tracks)} tune entries across his albums")

# Altan tunes
altan_tunes = merged_df[merged_df['artist'] == 'Altan']
print(f"\nAltan has {len(altan_tunes)} tune entries")
print("Sample of Altan tunes:")
print(altan_tunes[['title_x', 'title_y']].head(10))

# Artist with most tunes
tunes_by_artist = merged_df.groupby('artist').size().sort_values(ascending=False)
print("\nTune entries by artist:")
print(tunes_by_artist)
print(f"\nArtist with most tune entries: {tunes_by_artist.idxmax()} with {tunes_by_artist.max()} tunes")

print("\n" + "=" * 80)
print("PART 7: ADVANCED EXPLORATION")
print("=" * 80)

# Task 7.1: Most Prolific Artists
print("\n--- Task 7.1: Most Prolific Artists ---")
artist_summary = merged_df.groupby('artist').agg({
    'album_id': 'nunique',  # Number of unique albums
    'track_num': 'count',   # Total tracks (counts all rows)
    'tune_num': 'count'     # Total tunes (same as above for this dataset)
}).rename(columns={
    'album_id': 'num_albums',
    'track_num': 'total_tracks',
    'tune_num': 'total_tunes'
})
print(artist_summary.sort_values('total_tunes', ascending=False))

# Task 7.2: Find Repeated Tunes
print("\n--- Task 7.2: Find Repeated Tunes ---")
tune_counts = merged_df['title_x'].value_counts()
print("\nMost frequently appearing tunes:")
print(tune_counts.head(10))

most_common_tune = tune_counts.index[0]
print(f"\nMost common tune: '{most_common_tune}' appears {tune_counts.iloc[0]} times")

artists_with_tune = merged_df[merged_df['title_x'] == most_common_tune]['artist'].unique()
print(f"Artists who recorded '{most_common_tune}':")
print(artists_with_tune)

# Task 7.3: Album Completeness
print("\n--- Task 7.3: Album Completeness ---")

album_track_info = tracks_df.groupby('album_id').agg({
    'track_num': ['min', 'max', 'count', 'nunique']
})
album_track_info.columns = ['min_track', 'max_track', 'total_entries', 'unique_tracks']

# Add album info
album_info = pd.merge(album_track_info, albums_df, left_on='album_id', right_on='id')

# Check if sequential (max track number should equal number of unique tracks)
album_info['is_sequential'] = album_info['max_track'] == album_info['unique_tracks']

print("\nAlbum completeness:")
print(album_info[['title', 'artist', 'unique_tracks', 'total_entries', 'is_sequential']])

print("\n" + "=" * 80)
print("BONUS CHALLENGES")
print("=" * 80)

# Bonus 1: Custom Print Function
print("\n--- Bonus 1: Custom Print Function ---")

def print_album_info(album_id):
    """Print nicely formatted album information"""
    album = albums_df[albums_df['id'] == album_id].iloc[0]
    album_tracks = tracks_df[tracks_df['album_id'] == album_id]
    
    print(f"\nAlbum: {album['title']}")
    print(f"Artist: {album['artist']}")
    print(f"Tracks: {album_tracks['track_num'].nunique()}")
    print(f"Tunes: {len(album_tracks)}")

print_album_info(1)
print_album_info(4)

# Bonus 2: Track Listings
print("\n--- Bonus 2: Track Listings ---")

def print_track_listing(album_id):
    """Print complete track listing for an album"""
    album = albums_df[albums_df['id'] == album_id].iloc[0]
    album_tracks = tracks_df[tracks_df['album_id'] == album_id].sort_values(['track_num', 'tune_num'])
    
    print(f"\nAlbum: {album['title']} by {album['artist']}\n")
    
    current_track = None
    for _, row in album_tracks.iterrows():
        if row['track_num'] != current_track:
            current_track = row['track_num']
            print(f"\nTrack {current_track}:")
        print(f"  {row['tune_num']}. {row['title']}")

print_track_listing(1)

# Bonus 3: Artist Comparison
print("\n--- Bonus 3: Artist Comparison ---")

def compare_artists(artist1, artist2):
    """Compare two artists"""
    
    # Get data for each artist
    artist1_data = merged_df[merged_df['artist'] == artist1]
    artist2_data = merged_df[merged_df['artist'] == artist2]
    
    print(f"\n{'='*60}")
    print(f"Comparing {artist1} vs {artist2}")
    print(f"{'='*60}")
    
    print(f"\n{artist1}:")
    print(f"  Albums: {artist1_data['album_id'].nunique()}")
    print(f"  Total tune entries: {len(artist1_data)}")
    
    print(f"\n{artist2}:")
    print(f"  Albums: {artist2_data['album_id'].nunique()}")
    print(f"  Total tune entries: {len(artist2_data)}")
    
    # Shared tunes
    artist1_tunes = set(artist1_data['title_x'].unique())
    artist2_tunes = set(artist2_data['title_x'].unique())
    shared_tunes = artist1_tunes.intersection(artist2_tunes)
    
    print(f"\nShared tune titles: {len(shared_tunes)}")
    if len(shared_tunes) > 0:
        print("Examples:")
        for tune in list(shared_tunes)[:5]:
            print(f"  - {tune}")

compare_artists('Altan', 'Martin Hayes')
compare_artists('Altan', 'The Bothy Band')

print("\n" + "=" * 80)
print("SUMMARY STATISTICS")
print("=" * 80)

print(f"\nTotal albums: {len(albums_df)}")
print(f"Total tune entries: {len(tracks_df)}")
print(f"Total unique artists: {albums_df['artist'].nunique()}")
print(f"Average tunes per album: {len(tracks_df) / len(albums_df):.1f}")
print(f"Albums with most tunes: {tunes_per_album.max()}")
print(f"Albums with fewest tunes: {tunes_per_album.min()}")