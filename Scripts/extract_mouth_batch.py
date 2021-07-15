'''
extract_mouth_batch.py
    This script will extract mouth crop of every single video inside source directory
    while preserving the overall structure of the source directory content.

Usage:
    python extract_mouth_batch.py [source directory] [pattern] [target directory] [face predictor path]

    pattern: *.avi, *.mpg, etc

Example:
    python scripts/extract_mouth_batch.py evaluation/samples/GRID/ *.mpg TARGET/ common/predictors/shape_predictor_68_face_landmarks.dat

    Will make directory TARGET and process everything inside evaluation/samples/GRID/ that match pattern *.mpg.
'''

from lipnet.lipreading.videos import Video
import os, fnmatch, sys, errno
from skimage import io

SOURCE_PATH = sys.argv[1] #path of the script
SOURCE_EXTS = sys.argv[2] #directory of dataset stored
TARGET_PATH = sys.argv[3]#where output will be saved
FACE_PREDICTOR_PATH = sys.argv[4] #dlib facial landmark predictor

def mkdir_p(path): #making target directory
    try:
        os.makedirs(path)#os is used to tranverse through the system files
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):#if path alreadt exists
            pass
        else:
            raise

def find_files(directory, pattern): #find directory which has dataset in it, pattern is mpg
    for root, dirs, files in os.walk(directory): #list of root directories, sub-directories and list of file names in the current directory.
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):#checking if the files in the dataset are videos or not, we have alignment files as well
                filename = os.path.join(root, basename) #creating the pathname to the video file
                yield filename #return the path to the video file

for filepath in find_files(SOURCE_PATH, SOURCE_EXTS):
    print ("Processing: {}".format(filepath))
    video = Video(vtype='face', face_predictor_path=FACE_PREDICTOR_PATH).from_video(filepath)
    #Video is the user defined class name
    #vtype = video type, which means it has a face in it
    #face_predictor_path is the facial landmark predictor
    #from_video is a method in video class to which we're providing the path of each video file

    filepath_wo_ext = os.path.splitext(filepath)[0]#The mouth extract images will have the same name as the original video name so for that we're extracting the file path without extension
    target_dir = os.path.join(TARGET_PATH, filepath_wo_ext) #creating a target directory by target path by user and file path
    mkdir_p(target_dir)

    i = 0
    for frame in video.mouth:#for each frame, we're going to save each frame in png format
    	io.imsave(os.path.join(target_dir, "mouth_{0:03d}.png".format(i)), frame)
    	i += 1
