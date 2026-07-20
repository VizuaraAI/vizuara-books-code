"""
Python for Data Science - shared context from earlier chapters.

Several chapters continue a thread started earlier in the book: chapter 30
keeps using the MediaPipe detector built in chapter 28, chapter 33 parses the
response fetched in chapter 32, and chapter 34 walks the soup built in
chapter 33. Extracted per-chapter, those files reference names that were
defined pages earlier.

This module holds those carry-over definitions, COPIED VERBATIM from the
earlier chapter's own code, so the later chapters can say
`from context import <name>`.

Nothing here is invented. Each section cites the chapter it came from, and
only the lines needed to define the carried-over name are included.

NOTE: these are real side-effecting setup lines from the book - importing this
module opens a webcam (chapter 28) and makes a live HTTP request (chapter 32),
exactly as running those chapters would. That is the honest carry-over; it is
not meant to be imported on a machine without a camera or a network.
"""

# ---------------------------------------------------------------------------
# From chapter 28: Hand Tracking with MediaPipe
# https://books.vizuara.ai/read/python-for-data-science/hand-tracking-with-mediapipe
# Provides: hands  (used by chapter 30)
# ---------------------------------------------------------------------------
import mediapipe as mp

mp_hands = mp.solutions.hands

# Create the detector ONCE, outside the loop.
hands = mp_hands.Hands(
    max_num_hands=2,                 # detect up to two hands
    min_detection_confidence=0.5,    # how sure before it reports a hand
    min_tracking_confidence=0.5,     # how sure before it keeps tracking one
)

# ---------------------------------------------------------------------------
# From chapter 32: Fetching Pages with requests
# https://books.vizuara.ai/read/python-for-data-science/fetching-pages-with-requests
# Provides: resp  (used by chapter 33)
# ---------------------------------------------------------------------------
import requests

url = "https://example.com"
resp = requests.get(url)      # send an HTTP GET request

# ---------------------------------------------------------------------------
# From chapter 33: Parsing HTML with BeautifulSoup
# https://books.vizuara.ai/read/python-for-data-science/parsing-html-with-beautifulsoup
# Provides: soup  (used by chapter 34)
# ---------------------------------------------------------------------------
from bs4 import BeautifulSoup

soup = BeautifulSoup(resp.text, "html.parser")
