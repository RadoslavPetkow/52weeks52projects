# YouTube Downloader (yt-dlp)

A simple Python script for downloading videos or audio from YouTube using the `yt-dlp` tool.

## Features

- Download multiple YouTube videos or audio tracks at once.
- Automatically saves downloads in a `downloads` folder located in the same directory as the script.
- Supports downloading in either `mp4` (video) or `mp3` (audio) formats.

## Prerequisites

1. **Python 3.x**:
   - Ensure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/).

2. **yt-dlp**:
   - Install the `yt-dlp` tool using pip:
     ```bash
     pip install yt-dlp
     ```

3. **FFmpeg** (required for audio extraction):
   - Install FFmpeg for your platform:
     - **Linux**: Install via your package manager (e.g., `sudo apt install ffmpeg`).
     - **MacOS**: Install via Homebrew (`brew install ffmpeg`).
     - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/).

## Installation

1. Clone the repository or download the script:
   ```bash
   git clone https://github.com/yourusername/youtube-downloader.git
   cd youtube-downloader

	2.	Ensure the script is executable:

chmod +x youtube_downloader.py



Usage
	1.	Run the script:

./youtube_downloader.py


	2.	Input YouTube URLs (one per line):

https://www.youtube.com/watch?v=example1
https://www.youtube.com/watch?v=example2

Press Enter on an empty line to finish input.

	3.	Choose the format:
	•	Type mp4 for video.
	•	Type mp3 for audio.
	4.	The script will download all files into the downloads folder.

Example Output

When the script runs, it will display the following:

==== YouTube Downloader (yt-dlp) ====

Enter YouTube URLs, one per line. Then press Enter on an empty line to finish:
https://www.youtube.com/watch?v=example1
https://www.youtube.com/watch?v=example2

Choose format: 'mp4' for video or 'mp3' for audio: mp3

Starting downloads in: /path/to/script/downloads

Downloading: https://www.youtube.com/watch?v=example1
Downloading: https://www.youtube.com/watch?v=example2

All downloads completed!

Notes
	•	The script automatically creates a downloads folder if it doesn’t already exist.
	•	Invalid URLs will not be downloaded.
	•	For issues with audio or video, ensure FFmpeg is correctly installed.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Happy downloading! 🎥🎶

You can customize the `git clone` URL or any other project-specific details as needed!
