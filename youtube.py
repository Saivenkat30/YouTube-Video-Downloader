import yt_dlp

url = input("Enter YouTube URL: ")
path = input("Enter destination folder path: ")

ydl_opts = {
    'outtmpl': f'{path}/%(title)s.%(ext)s'
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Download completed ✅")

except Exception as e:
    print("Download failed ❌")
    print("Error:", e)
