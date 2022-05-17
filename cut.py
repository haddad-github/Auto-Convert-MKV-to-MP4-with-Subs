import subprocess

directory = "./mp4"
new_directory = "./cut_videos"

#Cut video based on timestamp; order here is important, otherwise causes various issues
def cutVideo(episode, start, end):
    subprocess.check_call(f'ffmpeg -i {directory}/{episode}.mp4 -ss {start} -to {end} {new_directory}/{episode}_cut.mp4 -y')

cutVideo(episode=30, start="0:50", end="1:13")