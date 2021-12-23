from moviepy.editor import *

video1 = VideoFileClip("path_and_name1.mp4")
video2 = VideoFileClip("path_and_name2.mp4")

'''concatenate_videoclips() joins a list of VideoFileClips in the order listed'''
video = concatenate_videoclips([video1, video2])
video.write_videofile("path_and_name.mp4", threads=4)