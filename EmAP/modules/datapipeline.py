import os
import subprocess
import threading
# Set the input and output directories
input_dir = "data/input"
output_dir = "data/processed_data"

# Get the file name from the input directory
file_name = os.listdir(input_dir)[0]
# remove extension from file name
destination_folder = file_name.split(".")[0]
# Create a new directory with the file name in the output directory
new_dir = os.path.join(output_dir, destination_folder)
os.makedirs(new_dir)
#create a new folders inside destination folder with splitvideo , splitframes and splitaudio
splitvideosrc = os.path.join(new_dir, "splitvideo")
os.makedirs(splitvideosrc)
splitframessrc = os.path.join(new_dir, "splitframes")
os.makedirs(splitframessrc)
splitaudiosrc = os.path.join(new_dir, "splitaudio")
os.makedirs(splitaudiosrc)

# Set the input and output file paths
video_input_file = os.path.join(input_dir, file_name)
video_output_template = os.path.join(splitvideosrc, "clip" + "_%03d.mp4")
splitval =  "5"
# Split the video into 10 second segments
subprocess.run(["ffmpeg", "-i", video_input_file, "-vcodec", "copy", "-acodec", "copy", "-vsync", "0", "-async", "1", "-segment_time", splitval, "-reset_timestamps", "1", "-f", "segment", video_output_template])

#collect files splitvideo folder and create a list
splitvideolist = os.listdir(splitvideosrc)


def extract_frames(input_file, output_template):
    subprocess.run(["ffmpeg", "-i", input_file, "-vf", "fps=1", output_template])

def extract_audio(input_file, output_file):
    subprocess.run(["ffmpeg", "-i", input_file, "-vn", "-acodec", "libmp3lame", output_file])

for i in splitvideolist:
    #create new folder for each video file
    clipdir = os.path.join(splitframessrc, i.split(".")[0])
    os.makedirs(clipdir)
    #join i and splitvideosrc to get the path of the video file
    inputfile = os.path.join(splitvideosrc, i)
    frame_output_template = os.path.join(clipdir, "frame" + "_%03d.jpg")
    # create a new thread to run the function in parallel
    thread = threading.Thread(target=extract_frames, args=(inputfile, frame_output_template))
    thread.start()

for i in splitvideolist:
    #join i and splitvideosrc to get the path of the video file
    inputfile = os.path.join(splitvideosrc, i)
    # create the output file path
    outputfile = os.path.join(splitaudiosrc, i.split(".")[0] + ".mp3")
    # create a new thread to run the function in parallel
    thread = threading.Thread(target=extract_audio, args=(inputfile, outputfile))
    thread.start()