import os 
from modules import data_extraction

input_dir = "data/input"
output_dir = "data/processed_data"
file_name = os.listdir(input_dir)[0]
splitval = "5"
data_extraction.process_video(input_dir, output_dir, file_name ,splitval)