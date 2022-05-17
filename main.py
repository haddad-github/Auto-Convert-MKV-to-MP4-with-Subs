import os
import subprocess
import shutil

directory = "./mkv"
final_directory = "./mp4"
problematic_directory = "./problematic"

#Get all file names (including extension) in a list
def getFiles(directory):
    return os.listdir(directory)

#Remove leading zeros (001 --> 1)
def removeLeadingZeros(num):
    while str(num)[0] == "0":
        num = num[1:]
    return num

#Rename episodes
#Customize based on file naming format
def renameFiles(all_files_in_dir):
    try:
        for file in all_files_in_dir:
            num = file.split(' - ')[1]
            num = removeLeadingZeros(num)
            os.rename(f'{directory}/{file}', f'{directory}/{num}.mkv')
    except:
        print("Already renamed, skipping")

#Convert to MP4
#Case-specific; customize based on what's needed and file format
#If subtitle index is not found, resort to default of subtitle index = 0
def convertToMP4(audio_index, subtitle_index):
    for mkv in all_mkvs:
        name = mkv.split('.')[0]
        try:
            subprocess.check_call(
            f'ffmpeg -i {directory}/{mkv} -map 0:v:0 -map 0:a:{audio_index} -vf "subtitles=\'{directory}/{mkv}\':si={subtitle_index}" -c:v libx264 -c:a copy {final_directory}/{name}.mp4 -y'
            )
            print(mkv, "1") #for debugging purposes
        except:
            try:
                subprocess.check_call(
                f'ffmpeg -i {directory}/{mkv} -map 0:v:0 -map 0:a:{audio_index} -vf "subtitles=\'{directory}/{mkv}\':si=0" -c:v libx264 -c:a copy {final_directory}/{name}.mp4 -y'
                )
                print(mkv, "0") #for debugging purposes
            except:
                shutil.move(f'{directory}/{mkv}', f'{problematic_directory}/{mkv}')

#Sort by name (case-specific)
all_mkvs = sorted(getFiles(directory), key=len)

#Convert
convertToMP4(audio_index=1, subtitle_index=1)