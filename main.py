from fastapi import FastAPI
from pydantic import BaseModel
from yt_dlp import YoutubeDL

app = FastAPI()

class Link(BaseModel):
    url: str

@app.post("/download")
def download(link: Link):
    ydl_opts = {
        "quiet": True,
        "format": "best"
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(link.url, download=False)

    return {
        "title": info.get("title"),
        "download_url": info.get("url")
    }
