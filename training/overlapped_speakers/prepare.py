import os
import glob
import subprocess
import sys

'''
This script prepare training folder and its dataset for each speaker.
- Folder s{i}/datasets/train would contain original DATASET_VIDEO - s{i} with 0 <= i < VAL_SAMPLES
- Folder s{i}/datasets/val would contain s{i} >= VAL_SAMPLES
- Folder s{i}/datasets/align would contain all your *.align

Usage: 
$ python prepare.py [Path to video dataset] [Path to align dataset] [Number of samples]

Notes:
- [Path to video dataset] should be a folder with structure: /s{i}/[video]
- [Path to align dataset] should be a folder with structure: /[align].align
- [Number of samples] should be less than or equal to min(len(ls '/s{i}/*'))
'''
#defining paths of both video and align folder, number of samples is to specify the validation/testing. 

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
DATASET_VIDEO_PATH = sys.argv[1]
DATASET_ALIGN_PATH = sys.argv[2]

VAL_SAMPLES = int(sys.argv[3])


for speaker_path in glob.glob(os.path.join(DATASET_VIDEO_PATH, '*')):#it lists the files in the directory
    speaker_id = os.path.splitext(speaker_path)[0].split('\\')[-1]#it makes s1,s2,s3... folders 
    print(speaker_id)#only the folder that is being considered is printed 
    subprocess.check_output("mkdir {}".format(os.path.join(CURRENT_PATH, speaker_id, 'datasets', 'train')), shell=True) #current path of prepare.py, creates a /s1/datasets/train
    for s_path in glob.glob(os.path.join(DATASET_VIDEO_PATH, '*')):#lists the file in the path
        s_id = os.path.splitext(s_path)[0].split('\\')[-1]#same as above

        if s_path == speaker_path:#to check if the first and second for loop is in sync, if yes
            subprocess.check_output("mkdir {}".format(os.path.join(CURRENT_PATH, speaker_id, 'datasets', 'train', s_id)), shell=True)#dataset/train/s*
            subprocess.check_output("mkdir {}".format(os.path.join(CURRENT_PATH, speaker_id, 'datasets', 'val', s_id)), shell=True)#dataset/val/s*
            n = 0
            for video_path in glob.glob(os.path.join(DATASET_VIDEO_PATH, speaker_id, '*')):#to check how many files are listed in s1, 2, 3...
                video_id = os.path.basename(video_path)#name of the file.mpg
                if n < VAL_SAMPLES:#val_samples is the number of samples, eg. 350
                    subprocess.check_output("mklink {} {}".format(os.path.join(CURRENT_PATH, speaker_id, 'datasets', 'val', s_id, video_id), video_path), shell=True)#first 350 is for validation
                else:
                    subprocess.check_output("mklink {} {}".format(os.path.join(CURRENT_PATH, speaker_id, 'datasets', 'train', s_id, video_id), video_path), shell=True)#remaining for training
                n += 1
        else:
            subprocess.check_output("mklink /D {} {}".format( os.path.join(CURRENT_PATH, speaker_id, 'datasets', 'train', s_id), s_path), shell=True)#all files will be taken for training
    subprocess.check_output("mklink /D {} {}".format(os.path.join(CURRENT_PATH, speaker_id, 'datasets', 'align'), DATASET_ALIGN_PATH), shell=True)#creating dataset/align