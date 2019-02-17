"""Basic script to download lyrics.

Should be abstracted out to something that can dedupe, clean, and save
the songs of a specified artist(s) to a specified directory in a
future PR.
"""
import sys

import lyricsgenius


def download_lyrics(api_key):
    bands = [
        "Iron Maiden",
        "Black Sabbath",
        "Blind Guardian",
        "Judas Priest",
        "Rainbow",
        "Metallica",
        "Motorhead",
        "Megadeth",
        "Manilla Road",
        "Thin Lizzy",
        "Led Zeppelin",
        "Manowar",
        "Dragonforce",
    ]

    genius = lyricsgenius.Genius(api_key)

    for band in bands:
        # We're using nested try/except blocks here for 2 reasons:
        # 1. the song downloading can fail from a connection error
        #    (could use a library like tenacity for retrying logic)
        # 2. song titles with forward slashes on them will not be saved
        #    (we can figure out how to handle this too)
        try:
            songs = genius.search_artist(band, sort="popularity", max_songs=50)
            for song in songs:
                try:
                    song.save_lyrics(extension="txt")
                except Exception:
                    pass
        except Exception:
            pass


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide the API key as a command line argument.")
        sys.exit(1)
    api_key = sys.argv[1]
    download_lyrics(api_key)