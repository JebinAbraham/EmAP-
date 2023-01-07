from modules.datapipeline.speech_to_text import speech_to_text
import os 

import threading

# def extract_entire_text(splitaudiosrc):
#     """
#     splitaudiosrc: path
#     """
#     # extract all audio files and put them in a list called audio_files
#     audio_files = os.listdir(splitaudiosrc)

#     # create a list to store the output of the threads
#     thread_output = []

#     # create a list of threads
#     threads = []

#     for audio in audio_files:
#         audio = os.path.join(splitaudiosrc, audio)

#         # create a thread for each audio file
#         t = threading.Thread(target=speech_to_text, args=(audio,))
#         threads.append(t)

#     # start all threads
#     for t in threads:
#         t.start()

#     # wait for all threads to finish
#     for t in threads:
#         t.join()

#         # retrieve the output of the thread and append it to the list
#         text = t.get()
#         thread_output.append(text)

#     # combine all the text in the list into one string
#     entire_text = " ".join(thread_output)
#     return entire_text




def extract_entire_text(splitaudiosrc):
    """
    splitaudiosrc: path
    """
    #extract al audio files and put them in a list called audio_files
    audio_files = os.listdir(splitaudiosrc)
    print(audio_files)
    entire_text = []
    for audio in audio_files:
        audio = os.path.join(splitaudiosrc, audio)
        text = speech_to_text(audio)
        entire_text.append(text)

    #combine all the text in the list into one string
    entire_text = " ".join(entire_text)
    return entire_text

entire_text = extract_entire_text(r"data\\processed_data\\jebintest\\splitaudio")
# # save entire_text to json
import json
with open('test_data.json', 'w') as outfile:
    json.dump({'text':entire_text}, outfile)