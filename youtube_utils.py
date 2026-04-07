import urllib.parse as urlparse
from youtube_transcript_api import YouTubeTranscriptApi

def extract_video_id(url):
    """Extracts the YouTube video ID from a standard URL."""
    parsed_url = urlparse.urlparse(url)
    if parsed_url.hostname in ['www.youtube.com', 'youtube.com']:
        return urlparse.parse_qs(parsed_url.query).get('v', [None])[0]
    elif parsed_url.hostname in ['youtu.be']:
        return parsed_url.path[1:]
    return None

def get_transcript(video_id):
    """Fetches the transcript using the latest YouTube Transcript API."""
    try:
        # 1. Initialize the API
        ytt_api = YouTubeTranscriptApi()
        
        # 2. Fetch the transcript
        fetched_transcript = ytt_api.fetch(video_id)
        
        # 3. Convert the fetched object to raw data (a list of dictionaries)
        transcript_data = fetched_transcript.to_raw_data()
        
        # 4. Extract and join the text
        transcript = " ".join([item['text'] for item in transcript_data])
        
        return transcript, None
    except Exception as e:
        return None, str(e)