#######################################################
# this is the first release of our graduation project
# pyhthon 3.8.2
# dependencies {}
# made by 
# 1- ahmedelnakeeb2016@outlook.com
# 2-
# 3-
# 4-
# 5-
# 6-
# released in 30/03/2020
# project name: xamcorrection
# project description :
#######################################################

import os
import sys
import getopt
import io
import platform
from operations import Operations
from context import context
from myOCR import myOCR
from compare import compare
from nltk_tool_kit import nltkToolKit
from new_tool_kit import newToolKit
from google.cloud import vision
from google.cloud.vision import types
import pandas as pd



system = platform.system()
version = platform.python_version()
if version[0] != '3':
    print("sorry! this only works for python3")
    sys.exit()

def err():
    if system == "Windows":
        print('python xamcorrection.py -h')
    else:
        print('python3 xamcorrection.py -h')
    sys.exit()

def main(argv):
    ###---        main        ---###
    i_ok=False
    t_ok=False
    m_ok=False
    image_path=""
    textfile_path=""
    ocr_mode="t1"
    correction_mode="g"
    model_answer_path=""
    outfile_path=os.path.join( os.getcwd(),'report.txt')
    

    try:
        opts, args = getopt.getopt(argv, "hi:t:r:c:m:o:", ["image_path=", "textfile_path=", "outfile_path=", "model_answer_path="])
    except getopt.GetoptError:
        err()

    for opt, arg in opts:
        ####################################
        if opt == '-h':
            print("#-----------------------------------#")
            print("options")
            print("i | image_path         | selected  img path")
            print("t | textfile_path      | exam as text file")
            print("r | ocr_mode           | which ocr to use")
            print("c | correction_mode    | comaresion algorism")
            print("m | model_answer_path  | mentors answer as text file")
            print("o | outfile_path       | the report location")
            print("-------------------------------------")
            print("args")
            print("ocr_mode")
            print("g - google api")
            print("t - tessreact ocr")
            print("c - custom ocr")
            print()
            print("correction_mode")
            print("t1 - key words")
            print("t2 - context")
            print("#-----------------------------------#")
            print("usage")
            if system == "Windows":
                print("python xamcorrection.py -i <image_path> -m <model_answer_path> -o <outfile_path>")      
            else:
                print("python3 xamcorrection.py -i <image_path> -m <model_answer_path> -o <outfile_path>") 
            sys.exit()
        ####################################
        if opt in ['-i','--image_path']:
            image_path=arg
            i_ok=True
        ####################################
        if opt in ['-t','--textfile_path']:
            textfile_path=arg
            t_ok=True
        ####################################
        if opt in ['-r','--ocr_mode']:
            if arg in['g','t','c']:
                ocr_mode=arg
            else:
                err()
        ####################################
        if opt in ['-c','--correction_mode']:
            if arg in['t1','t2']:
                correction_mode=arg
            else:
                err()
        ####################################
        if opt in ['-m','--model_answer_path']:
            model_answer_path=arg
            m_ok=True
        ####################################
        if opt in ['-o','--outfile_path']:
            outfile_path=arg
        ####################################
    #start  
    if m_ok:    
        nlp=nltkToolKit()
        new =newToolKit(nlp)
        c=context(nlp,new)
        comp=compare()
    else:
        print("provide model answer please")

    if i_ok :
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'
        client = vision.ImageAnnotatorClient()

        with io.open(image_path, 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)
        response = client.document_text_detection(image=image)

        docText = response.full_text_annotation.text
        #################################
        fixed=c.Context_sensitive_spellchecker(docText)
        report = open(outfile_path,"w")
        report.write( str(comp.compare(fixed,model_answer_path)))
        report.close()
    elif t_ok:
        pass


        
    ###---        main        ---###


if __name__ == "__main__":
    main(sys.argv[1:])