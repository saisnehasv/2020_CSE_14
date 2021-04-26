from keras.optimizers import Adam
import ffmpeg
from keras import backend as K
import numpy as np
import sys
import os

np.random.seed(55)

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

PREDICT_GREEDY      = False
PREDICT_BEAM_WIDTH  = 200

def predict(weight_path, video_path, absolute_max_string_len=32, output_size=28):
    print ("\nLoading data from disk...")
    if os.path.isfile(video_path):
        video.from_video(video_path)
    else:
        video.from_frames(video_path)
    print ("Data loaded.\n")

    if K.image_data_format() == 'channels_first':
        img_c, frames_n, img_w, img_h = video.data.shape
    else:
        frames_n, img_w, img_h, img_c = video.data.shape

    adam = Adam(lr=0.0001, beta_1=0.9, beta_2=0.999, epsilon=1e-08)

    X_data       = np.array([video.data]).astype(np.float32) / 255
    input_length = np.array([len(video.data)])


if __name__ == '__main__':
    if len(sys.argv) == 3:
        video, result = predict(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 4:
        video, result = predict(sys.argv[1], sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 5:
        video, result = predict(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        video, result = None, ""

    if video is not None:
        show_video_subtitle(video.face, result)

    stripe = "-" * len(result)
    
    print ("             --{}- ".format(stripe))
    print ("[ DECODED ] |> {} |".format(result))
    print ("             --{}- ".format(stripe))
