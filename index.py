import moviepy
from moviepy import VideoFileClip, TextClip

# Fix filename (remove … and quotes issues)
video = moviepy.VideoFileClip("Jesus… I’m Scared of My Future..mp4")
audio = video.audio
audio.write_audiofile("my_audio.mp3")

# Cleanup
video.close()
audio.close()
print("✅ Done! Check my_audio.mp3")