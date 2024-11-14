import asyncio
import os
import re
import json
import glob
import random
from typing import Union
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message
from youtubesearchpython.future import VideosSearch
import yt_dlp

class YouTubeAPI:
    def init(self):
        self.base_url = "https://www.youtube.com/watch?v="
        self.cookie_file = self.get_cookie_file()
        self.ytdl_opts = {"quiet": True, "cookiefile": self.cookie_file}

    def get_cookie_file(self):
        folder_path = f"{os.getcwd()}/cookies"
        txt_files = glob.glob(os.path.join(folder_path, '*.txt'))
        if not txt_files:
            raise FileNotFoundError("No .txt files found.")
        return random.choice(txt_files)

    async def fetch_video_details(self, link: str, limit: int = 1):
        results = VideosSearch(link, limit=limit)
        return await results.next()

    async def check_video_existence(self, link: str):
        return bool(re.search(r"(?:youtube\.com|youtu\.be)", link))

    async def download_video(self, link: str, format_id: str = None):
        cmd = [
            "yt-dlp",
            "--cookies", self.cookie_file,
            "-g",
            "-f", format_id if format_id else "best[height<=?720][width<=?1280]",
            link
        ]
        proc = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, _ = await proc.communicate()
        return stdout.decode().strip() if stdout else None

    async def fetch_video_title(self, link: str):
        details = await self.fetch_video_details(link)
        return details["result"][0]["title"] if details["result"] else None

    async def fetch_video_duration(self, link: str):
        details = await self.fetch_video_details(link)
        return details["result"][0]["duration"] if details["result"] else None

    async def fetch_video_thumbnail(self, link: str):
        details = await self.fetch_video_details(link)
        return details["result"][0]["thumbnails"][0]["url"].split("?")[0] if details["result"] else None

# উদাহরণ হিসাবে ফাংশনগুলি কীভাবে ব্যবহার করবেন
async def main():
    yt_api = YouTubeAPI()
    link = "https://www.youtube.com/watch?v=EXAMPLE"
    if await yt_api.check_video_existence(link):
        video_url = await yt_api.download_video(link)
        video_title = await yt_api.fetch_video_title(link)
        video_duration = await yt_api.fetch_video_duration(link)
        video_thumbnail = await yt_api.fetch_video_thumbnail(link)

        print(f"Video URL: {video_url}")
        print(f"Title: {video_title}")
        print(f"Duration: {video_duration}")
        print(f"Thumbnail: {video_thumbnail}")

# প্রধান ফাংশন চালানো
asyncio.run(main())