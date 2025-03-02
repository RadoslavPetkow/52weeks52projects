#!/usr/bin/env python3

import os
import subprocess
import sys


def main():
    print("==== YouTube Downloader (yt-dlp) ====\n")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    default_output_folder = os.path.join(script_dir, "downloads")

    if not os.path.isdir(default_output_folder):
        print(f"Creating default folder: '{default_output_folder}'...")
        os.makedirs(default_output_folder, exist_ok=True)

    print("Enter YouTube URLs, one per line. Then press Enter on an empty line to finish:")
    urls = []
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break
        urls.append(line)

    if not urls:
        print("No URLs provided. Exiting.")
        sys.exit(1)

    while True:
        download_format = input("Choose format: 'mp4' for video or 'mp3' for audio: ").strip().lower()
        if download_format in ["mp4", "mp3"]:
            break
        print("Invalid choice. Please type 'mp4' or 'mp3'.")

    print(f"\nAll downloads will be saved to: {default_output_folder}")

    print(f"\nStarting downloads in: {default_output_folder}")
    for url in urls:
        print(f"\nDownloading: {url}")

        if download_format == 'mp4':
            cmd = [
                "yt-dlp",
                "-f", "mp4",
                "--merge-output-format", "mp4",
                "-o", os.path.join(default_output_folder, "%(title)s.%(ext)s"),
                url
            ]
        else:
            cmd = [
                "yt-dlp",
                "-x", "--audio-format", "mp3",
                "-o", os.path.join(default_output_folder, "%(title)s.%(ext)s"),
                url
            ]

        subprocess.run(cmd, check=False)

    print("\nAll downloads completed!")


if __name__ == "__main__":
    main()
