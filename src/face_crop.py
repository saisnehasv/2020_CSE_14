import cv2
import os
//using a built in haar cascade classifier file for the face region in OpenCV 
classifier = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")

/*mouth_cascade= cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_mcs_mouth.xml")
Throwing an error 
*/

dirFace = 'cropped_face'

# Create if there is no cropped_face directory
if not os.path.exists(dirFace):
    os.mkdir(dirFace)
    print("Directory " , dirFace ,  " Created ")
else:    
    print("Directory " , dirFace ,  " has found.")

def face_crop(file):

        video = cv2.VideoCapture(file) 
        while (True):
             
            (f, im) = video.read() # reading frames from video 

            if f != True:
               break

            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) #grayscale conversion

            # detectfaces 
            faces = classifier.detectMultiScale(
                gray, # video
                scaleFactor=1.10, 
                minNeighbors=20, 
                minSize=(30, 30) # min image detection size
                ) 

            # Draw rectangles around each face
            for (x, y, w, h) in faces:

                cv2.rectangle(im, (x, y), (x + w, y + h),(0,0,255),thickness=2)
                # saving faces according to detected coordinates 
                sub_face = im[y:y+h, x:x+w]
                FaceFileName = "cropped_face/face_" + str(y+x) + ".jpg" # folder path and random name image
                cv2.imwrite(FaceFileName, sub_face)

            # Video Window
            cv2.imshow('Face Detected Video ',im)
            key = cv2.waitKey(1) & 0xFF
            # q for exit
            if key == ord('q'): 
                break

for filename in os.listdir("C:/Users/neetu/Desktop/Scripts/GRID"):# video path

    if filename.endswith("mpg"): 
          file=os.path.join("C:/Users/neetu/Desktop/Scripts/GRID/", filename)
          face_crop(file)
          continue
    else:
        continue
