from moviepy import *

'''subclip(start, end) argument can be float values in seconds or a string in the format "hh:mm:ss" to define the start and end of the video cut'''
video = VideoFileClip("path_and_name.mp4").subclip(0,30)

'''concatenate_videoclips() joins a list of VideoFileClips in the order listed'''
video.write_videofile("path_and_name_cut.mp4", threads=4)