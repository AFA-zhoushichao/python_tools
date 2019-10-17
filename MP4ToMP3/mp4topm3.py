#-*-coding:utf-8 -*-

#mp4文件转mp3文件
from moviepy.editor import *
video = VideoFileClip('test.mp4')
audio = video.audio
audio.write_audiofile('test.mp3')

#切割mp3文件

from pydub import AudioSegment
song = AudioSegment.from_mp3("说好不哭+七里香.mp3")
ten_seconds = 100 * 1000
first_10_seconds = song[:ten_seconds]
first_10_seconds.export("说好不哭.mp3", format="mp3")
first_10_seconds.export("mashup.mp3", format="mp3", tags={'artist': 'Various artists', 'album': 'Best of 2011', 'comments': 'This album is awesome!'})


if __name__ == "__main__":
   from pydub import AudioSegment
   print('----start----')
   song = AudioSegment.from_mp3("说好不哭+七里香.mp3")
   start_seconds = 229 * 1000
   end_seconds = 436 * 1000
   first_10_seconds = song[start_seconds:end_seconds]
   first_10_seconds.export("告白气球.mp3", format="mp3")
   print('----end----')