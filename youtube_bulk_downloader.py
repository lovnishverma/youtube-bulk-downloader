from yt_dlp import YoutubeDL
import os


def download_video(url, output_path="downloads"):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title).80s.%(ext)s'),
        'format': 'best',
        'quiet': False,
    }

    try:
        print(f"[+] Downloading: {url}")
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("[✓] Downloaded successfully.\n")
    except Exception as e:
        print(f"[!] Failed to download {url}\nError: {e}")


def download_from_file(file_path, output_path="downloads"):
    try:
        with open(file_path, "r") as file:
            urls = [line.strip() for line in file if line.strip()]

        print(f"Found {len(urls)} URLs. Starting download...\n")

        for url in urls:
            download_video(url, output_path)

    except FileNotFoundError:
        print(f"[!] File not found: {file_path}")
    except Exception as e:
        print(f"[!] Error: {e}")


if __name__ == "__main__":
    input_file = "video_urls.txt"
    output_folder = "downloads"

    download_from_file(input_file, output_folder)
