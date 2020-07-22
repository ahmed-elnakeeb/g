import os
import sys
import getopt
import io
import platform
from google.cloud import vision
from google.cloud.vision import types
from datetime import datetime


system = platform.system()
version = platform.python_version()
if version[0] != '3':
    print("sorry! this only works for python3")
    sys.exit()

def err():
    if system == "Windows":
        print('imtote.exe -h')
    else:
        print('imtote -h')
    sys.exit()

def main(argv):
    ###---        main        ---###
    i_ok=False
    d_ok=False
    image_path=""
    directory=""
    outfile_path=os.path.join( os.getcwd(),'report.txt')
    

    try:
        opts, args = getopt.getopt(argv, "hi:o:d:", ["image_path=", "outfile_path=","directory="])
    except getopt.GetoptError:
        err()

    for opt, arg in opts:
        ####################################
        if opt == '-h':
            print("#-----------------------------------#")
            print("options")
            print("i | image_path         | selected  img path")                        
            print("d | directory          | selected  imgs path")
            print("-------------------------------------")
            print("usage")
            if system == "Windows":
                print("imtote.exe -i <image_path> ")      
            else:
                print("imtote -i <image_path>") 
            sys.exit()
        ####################################
        if opt in ['-i','--image_path']:
            image_path=arg
            i_ok=True
        if opt in ['-d','--']:
            directory=arg
            d_ok=True

    if i_ok :
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'
        client = vision.ImageAnnotatorClient()

        with io.open(image_path, 'rb') as image_file:
            content = image_file.read() 

        image = vision.types.Image(content=content)
        response = client.document_text_detection(image=image)

        docText = response.full_text_annotation.text
        #################################
        image_path=os.path.join( os.getcwd(),image_path)
        base=os.path.basename(image_path)
        report=os.path.splitext(base)[0]
        outfile_path=os.path.join( os.getcwd(),report+'.txt')
        report = open(outfile_path,"w", encoding="utf-8")
        report.write(docText)
        report.close() 
    elif (d_ok):
        dd =os.path.join( os.getcwd(),directory)
        for filename in os.listdir(dd):
            if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
                image_path= os.path.join(dd, filename)
                print(image_path)
                os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'
                client = vision.ImageAnnotatorClient()
                with io.open(image_path, 'rb') as image_file:
                    content = image_file.read() 

                image = vision.types.Image(content=content)
                response = client.document_text_detection(image=image)

                docText = response.full_text_annotation.text
                #################################
                base=os.path.basename(image_path)
                report=os.path.splitext(base)[0]
                outfile_path=os.path.join( dd,report+'.txt')
                report = open(outfile_path,"w", encoding="utf-8")
                report.write(docText)
                report.close()
            else:
                continue
###---        main        ---###


if __name__ == "__main__":
    main(sys.argv[1:])