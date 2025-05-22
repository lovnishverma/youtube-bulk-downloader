
# 🎥 YouTube Bulk Downloader

A simple and efficient Python script to download multiple YouTube videos in one go using the `yt-dlp` library.

> Developed by [Lovnish Verma](https://github.com/lovnishverma)

---

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

MIT License © [Lovnish Verma](https://github.com/lovnishverma)

```
