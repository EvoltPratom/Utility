help_strings = {
    "organize": '''
    Organize a folder according to a configuration file.

    Usage: python Utility organize [--path <folder_path>] [--config <config_file>]

    Examples:
      python Utility organize --path \path\to\folder\ --config "my_config.json"
      (if you want to organize current folder) python Utility organize
    Options:
      --path    Folder path to be organized (default: current working directory).
      --config  Configuration file to use (default: config.json).
    ''',

    "flatten": '''
    Flatten a folder and its contents.

    Usage: python Utility flatten [--path <folder_path>]

    Examples:
      python Utility flatten --path \path\to\folder
      (if you want to organize current folder) python Utility flatten
    Options:
      --path  Folder path to be flattened (default: current working directory).
    ''',

    "img2pdf": '''
    Convert images from a folder to a PDF.

    Usage: python Utility img2pdf [--path <folder_path>] [--output <output_PDF>] [--dimg]

    Examples:
      python Utility img2pdf --path \path\to\images --output output.pdf --dimg 1
    Options:
      --path    Folder path containing images (default: current working directory).
      --output  Output PDF file (default: None).
      --dimg    Delete source images after conversion (default: False).
    ''',

    "pdf2img": '''
    Convert a PDF to images.

    Usage: python Utility pdf2img <pdf_path> [--output <output_path>]

    Examples:
      python Utility pdf2img \path\to\my_document.pdf --output /output/folder
    Arguments:
      pdf_path  Path to the PDF file to be converted to images.

    Options:
      --output  Output path for the images (default: current working directory).
    ''',

    "convert_music": '''
    Bulk convert videos or audio to audio format.

    Usage: python Utility convert_music [--path <audio_folder>] [--format <output_format>] [--daudio]

    Examples:
      python Utility convert_music --path \path\to\audio_files --format mp3 --daudio 1
    Options:
      --path     Folder containing audio or video files (default: None).
      --format   Output audio format (default: None).
      --daudio   Delete original files after conversion (default: False).
    ''',

    "combine_music": '''
    Bulk combine  audio

    Usage: python Utility combine_music [--path <audio_folder>]

    Examples:
      python Utility combine_music --path \path\to\audio_files
    Options:
      --path     Folder containing audio or video files (default: None).
    ''',

    "ytmp3": '''
    Download a YouTube video and convert it to MP3 format.

    Usage: python Utility ytmp3 <youtube_uri> [--title <output_title>]

    Examples:
      python Utility ytmp3 https://www.youtube.com/watch?v=your_video_id --title "my_audio"
    Arguments:
      youtube_uri  YouTube video URL.
      title       Output title in MP3 format (default: None).

    Options:
      --title  Specify the output title in MP3 format (default: None).
    ''',

    "mp4tomp3": '''
    Convert a single video to audio (MP3 format).

    Usage: python Utility mp4tomp3 <video_path>

    Examples:
      python Utility mp4tomp3 path\\to\\video.mp4
    Arguments:
      video_path  Path to the video file to be converted to audio.
    ''',

    "test1": '''
    A test function.

    Usage: python Utility test1 [--path <test_path>]
    Options:
      --path  Test path (default: "sd").
    ''',

    "yt_playlist_mp3": '''
    Download a YouTube playlist and convert its videos to MP3 format.\n

    Usage: python Utility yt_playlist_mp3 <playlist_url>

    Examples:
      python Utility yt_playlist_mp3 https://www.youtube.com/playlist?list=XXXXXXXX
    Arguments:
      playlist_url  URL of the YouTube playlist to download.
    ''',
}
