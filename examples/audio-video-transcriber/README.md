# Audio & Video Transcriber (Whisper) - MP3/MP4 to Text, SRT, VTT

Transcribe audio and video URLs to text, SRT and VTT with Whisper.

- Apify Store: [apify.com/tinyrex/audio-video-transcriber](https://apify.com/tinyrex/audio-video-transcriber)
- Guide: [step-by-step tutorial](https://emirmrkaljevic.github.io/tinyrex-data-tools/transcribe-audio-video-to-text-srt-whisper-api/)

## Input used in this example

```json
{
  "mediaUrls": [
    "https://upload.wikimedia.org/wikipedia/commons/3/3c/Pope_Simplicius_Spoken_Version.ogg"
  ]
}
```

## Run it

Python 3.10+ (`pip install apify-client`):

```bash
export APIFY_TOKEN=your_token
python run.py
```

Node.js 18+ (`npm install apify-client`):

```bash
export APIFY_TOKEN=your_token
node run.mjs
```

No SDK, just HTTP (waits for the run and returns the dataset items):

```bash
curl -s -X POST "https://api.apify.com/v2/acts/tinyrex~audio-video-transcriber/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' -d @input.json
```

Pricing, the full input reference and output fields are on the [Store page](https://apify.com/tinyrex/audio-video-transcriber).
