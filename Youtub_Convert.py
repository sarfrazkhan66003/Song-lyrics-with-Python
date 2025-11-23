import yt_dlp
import os

def download_youtube(url, choice):
    """
    Download YouTube video as MP3 or HD Video
    
    Args:
        url: YouTube video URL
        choice: '1' for MP3, '2' for HD Video
    """
    
    try:
        if choice == '1':
            # MP3 Audio Download Options with Thumbnail Embedding
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [
                    {
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    },
                    {
                        'key': 'EmbedThumbnail',
                        'already_have_thumbnail': False,
                    },
                    {
                        'key': 'FFmpegMetadata',
                        'add_metadata': True,
                    }
                ],
                'writethumbnail': True,
                'outtmpl': '%(title)s.%(ext)s',
                'quiet': False,
            }
            print("\n🎵 Downloading as MP3 Audio with Album Art...")
            
        elif choice == '2':
            # HD Video Download Options - Fixed for better compatibility
            ydl_opts = {
                'format': 'bestvideo[ext=mp4][height<=1080]+bestaudio[ext=m4a]/bestvideo[height<=1080]+bestaudio/best[height<=1080]',
                'merge_output_format': 'mp4',
                'postprocessors': [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4',
                }],
                'outtmpl': '%(title)s.%(ext)s',
                'quiet': False,
                'prefer_ffmpeg': True,
            }
            print("\n🎬 Downloading as HD Video...")
            
        else:
            print("❌ Invalid choice! Please select 1 or 2.")
            return
        
        # Download with yt-dlp
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"\n📥 Starting download from: {url}")
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            
            if choice == '1':
                filename = filename.rsplit('.', 1)[0] + '.mp3'
                print("\n🖼️ Album art (thumbnail) has been embedded in the MP3 file!")
            
            print(f"\n✅ Download completed successfully!")
            print(f"📁 Saved as: {filename}")
            
    except Exception as e:
        print(f"\n❌ Error occurred: {str(e)}")
        print("\nMake sure you have:")
        print("1. yt-dlp installed: pip install yt-dlp")
        print("2. ffmpeg installed (required for audio conversion)")

def main():
    print("=" * 50)
    print("🎥 YOUTUBE DOWNLOADER 🎵")
    print("=" * 50)
    
    # Get YouTube URL
    url = input("\n📎 Enter YouTube URL: ").strip()
    
    if not url:
        print("❌ No URL provided!")
        return
    
    # Display options
    print("\n📋 Choose download format:")
    print("1️⃣  MP3 Audio (192kbps) with Album Art 🖼️")
    print("2️⃣  HD Video (1080p)")
    
    # Get user choice
    choice = input("\n👉 Enter your choice (1 or 2): ").strip()
    
    # Download
    download_youtube(url, choice)

if __name__ == "__main__":
    main()
    
    # Ask if user wants to download another
    while True:
        again = input("\n🔄 Download another? (y/n): ").strip().lower()
        if again == 'y':
            main()
        else:
            print("\n👋 Thanks for using YouTube Downloader! Goodbye!")
            break