import streamlit as st
from pytubefix import YouTube
import io

st.title('Quackery Convert 🪿')

yt_url = st.text_input("URL: ", value="")

if st.button("Convert to MP3"):
  vid = YouTube(yt_url)
  audio_download = vid.streams.get_audio_only()
  entry = YouTube(yt_url).title

  st.write(f"\nVideo found: {entry}\n")
  st.write("Downloading Audio...")

  # Save the audio as an in-memory file
  audio_buffer = io.BytesIO()
  audio_download.stream_to_buffer(audio_buffer)
  audio_buffer.seek(0)  # Move the cursor to the start of the file

  st.write("Download complete.")

  # Use st.download_button to prompt the download of the MP3
  st.download_button(
      label="Download MP3",
      data=audio_buffer,
      file_name=f"{entry}.mp3",
      mime="audio/mpeg"
  )



