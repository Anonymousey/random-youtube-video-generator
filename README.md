# Random YouTube Video Generator (live)
<p>Supports live streams instead of videos.</p>
Random YouTube live stream generator script using YouTube Data API v3 written in Python. <br />

**Default Search Query:** `Prefix ('live', 'webcam', 'test', 'stream')` <br /><br />
You can change its parameter to whatever you want. <br />

## Prerequisites
**Google Developer Key for YouTube** <br />
`DEVELOPER_KEY = 'YOUR_DEVELOPER_KEY'` <br />
Sign up and change with your own developer key: https://console.developers.google.com <br /><br />
**Google APIs Client Library** <br />
`pip3 install --upgrade google-api-python-client`

## Example Usage
`> random-youtube-video-live.py` <br />
`> 0CGyCMzi1l8` <br /><br />
Now you can use this video ID as "https://www.youtube.com/watch?v=0CGyCMzi1l8" <br />
Change the ID parameter with your output: "https://www.youtube.com/watch?v=ID" <br /> 
