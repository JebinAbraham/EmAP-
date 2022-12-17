from deepface import DeepFace
import os 
image_path = "D:\Data\Documents\Images\Dp Compressed.jpg"
image = DeepFace.load_image(image_path)

# Use the DeepFace library to detect the emotions in the image
emotions = DeepFace.analyze(image, actions=['emotion'])

# Extract the list of emotions from the results
emotions_list = emotions['emotion']
print(emotions_list
)