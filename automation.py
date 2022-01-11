import cv2
import dropobox
import time
import random

start_time=time.time()

def take_snapshot():
    number=random.randit(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    print("snapshot taken")

    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token="bhzwEfzJj40AAAAAAAAAAXHHIo49yqKLTQ9JknpuZsPmyk2N9685wCObm8zM0M4p"
    file=img_name
    file_from=file
    file_to="/test"+(img_name)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")
    
def main():
    while(True):
        if(time.time()-start_time>=10):
            name=take_snapshot()
            upload_file(name)
    
main()