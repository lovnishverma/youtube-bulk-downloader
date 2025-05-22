
# 🎥 YouTube Bulk Downloader

A simple and efficient Python script to download multiple YouTube videos in one go using the `yt-dlp` library.

> Developed by [Lovnish Verma](https://github.com/lovnishverma)

---

![image](https://github.com/user-attachments/assets/167479c7-39d3-432c-8222-e52cf3dc693c)


## 🚀 Features

- 📥 Download multiple YouTube videos from a list  
- 🧠 Uses `yt-dlp` for high-quality, reliable downloads  
- 📁 Automatically saves videos to a `downloads/` folder  
- 🛡️ Skips already downloaded videos  
- ✅ Simple CLI-based usage

---

## 🧰 Requirements

- Python 3.7+
- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp)

Install dependencies:

```bash
pip install yt-dlp
````

---

## 📦 Usage

1. Clone the repo:

```bash
git clone https://github.com/lovnishverma/youtube-bulk-downloader.git
cd youtube-bulk-downloader
```

2. Add video URLs to `video_urls.txt` (one per line):

```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
https://www.youtube.com/watch?v=3JZ_D3ELwOQ
https://www.youtube.com/watch?v=DLzxrzFCyOs
```

3. Run the script:

```bash
python youtube_bulk_downloader.py
```

Videos will be downloaded to the `downloads/` folder.

---

## 🗃️ Project Structure

```
youtube-bulk-downloader/
├── downloads/                  # Downloaded videos go here (auto-created)
├── video_urls.txt              # Your list of YouTube URLs
├── youtube_bulk_downloader.py # The main script
├── README.md                   # This file
└── .gitignore                  # Ignores __pycache__, downloads, etc.
```

---

## 🧠 How It Works

The script:

* Reads URLs from `video_urls.txt`
* Uses `yt-dlp`'s Python API to download each video
* Handles exceptions gracefully
* Saves all videos in a local `downloads/` folder

---

## 📝 .gitignore

```
__pycache__/
*.pyc
downloads/
```

---

## 📄 License

```bash
MIT License © [Lovnish Verma](https://github.com/lovnishverma)

Copyright (c) 2025 Lovnish Verma

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
