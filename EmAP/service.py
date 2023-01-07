import os 
from modules.datapipeline.data_extraction import DataCollection
from modules.datapipeline.data_preperation import load_data , create_dataset
# must be run in python 3.9.7 


# """
# Section 1: Data Collection
# """
# input_dir = r"data\input"
# output_dir = r"data\processed_data"
# #delete everything in the output directory
# #check if the output directory is empty
# if os.listdir(output_dir):
#     #if not empty, delete everything in the output directory
#     for root, dirs, files in os.walk(output_dir, topdown=False):
#         for name in files:
#             os.remove(os.path.join(root, name))
#         for name in dirs:
#             os.rmdir(os.path.join(root, name))
# file_name = os.listdir(input_dir)
# splitval = "5"
# new_dir, splitframessrc, splitaudiosrc, splitvideosrc = DataCollection().process_video(input_dir, output_dir, file_name[0] ,splitval)

"""
Section 2: Data Transformation and Preprocessing
"""

values = {"new_dir": "data\\processed_data\\jebintest", "splitframessrc": "data\\processed_data\\jebintest\\splitframes", "splitaudiosrc": "data\\processed_data\\jebintest\\splitaudio", "splitvideosrc": "data\\processed_data\\jebintest\\splitvideo"}
#audio_to_Text = DataCollection().extract_entire_text(values["splitaudiosrc"])
audio_to_Text = "high there this is a sample audio text and iam really going tell you that this is not the way that we have to behave"
print(audio_to_Text)
#audio_to_Text = DataCollection().extract_entire_text(splitaudiosrc)

datasetname = "test2"
data_frame , dataset_path = create_dataset(datasetname)
print(data_frame)

#append filename to "filename" column
data_frame["filename"] = file_name[0]

#save the dataframe to a csv file
data_frame.to_csv(dataset_path, index=False)





# save new_dir , splitframessrc, splitaudiosrc, splitvideosrc to json 
# import json
# with open('data/moduleOutputs/service_data.json', 'w') as outfile:
#     json.dump({'new_dir':new_dir, 'splitframessrc':splitframessrc, 'splitaudiosrc':splitaudiosrc, 'splitvideosrc':splitvideosrc}, outfile)


