import pandas as pd 



def load_data(path):
    df = pd.read_csv(path)
    return df

#function to create an empty dataframe and save it to a csv file
def create_dataset(dataset_name):
    df = pd.DataFrame()
    #create columns such as filename , text, audio_emotion , video_emotion , text_emotion , result
    df["filename"] = ""
    df["text"] = ""
    df["audio_emotion"] = ""
    df["video_emotion"] = ""
    df["text_emotion"] = ""
    df["result"] = ""

    path = "data/dataset/" + dataset_name + ".csv"
    df.to_csv(path, index=False)
    return df , path