import os
import sys
import imghdr
import time
import pickle
from distutils.dir_util import copy_tree
import ntpath
import image
from PyQt5 import QtCore, QtGui, QtWidgets

'''
    Input : Path to folder
    Returns : List of image wrapper objects populated with path and the colorhash of the image
'''
def processFolder(path, label = None):
    img_list = []
    size = 0
    for file in os.listdir(path):
        current_file = os.path.join(path, file)
        print(current_file)
        if label is not None:
            x1, y1, w1, h1 = label.frameGeometry().getRect()
            label.setText(f'Processing : {current_file}')
            label.adjustSize()
            x2, y2, w2, h2 = label.frameGeometry().getRect()
            print(x1, y1, w1, h1)
            x2 = x1 - (w2 - w1)/2
            label.setGeometry(QtCore.QRect(x2, y2, w2, h2))
        if (current_file == path):
            continue
        if os.path.isdir(current_file):
            s, l = processFolder(current_file, label)
            size += s*(1024**2)
            img_list += l
            pass
        else:
            if (imghdr.what(current_file) == None):
                continue
            else:
                img_list.append(image.ImageWrapper(current_file, os.stat(current_file).st_size))
                size += os.stat(current_file).st_size

    return (size/1024**2), img_list
        
'''
    Input : ImageWrapper object
    Output : Deletes the image stored in the wrapper object
    Return: None
'''
def deleteImage(img):
    if os.path.exists(img.path):
        os.remove(img.path)
'''
    Input : List of ImageWrapper objects
    Output : Deletes all images in this list
    Return : None
'''
def deleteImageList(img_list):
    for img in img_list:
        deleteImage(img)

'''
    Inputs
        from_path : The path of the directory which is to be copied
        to_path : The path to the directory to which copy must be done
    Return : None 
'''
def copyFolder(from_path, to_path):
    dirName = ntpath.basename(from_path)
    to_path = os.path.join(to_path, dirName)
    i = 0
    while(os.path.exists(to_path)):
        i += 1
        to_path += str(i)
    copy_tree(from_path, to_path)
    return to_path

'''
    Input : root path of database
    Return : If any libraries exists, return ImageLibrary Objects
'''
def loadLibraries(path = ""):
    path = os.path.join(path, '.database')
    if not os.path.exists(path):
        print(f'Program has not been initialised, initialising...')
        os.mkdir(path)
        return []
    else:
        print(f'Loading libraries ...')
        libs = []
        for file in os.listdir(path):
            current_file = os.path.join(path, file)
            with open(current_file, 'rb') as input:
               dirName = ntpath.basename(current_file)              
               try:
                   lib = pickle.load(input)
                   libs.append(lib)
               except Exception:
                   print(f'Something went wrong in reading library {dirName}')
        return libs
        
'''
    Inputs
        lib : ImageLibrary Object
        path : root directory of database
    Outputs:
        Saves the object to file for data persistance
    Return : None
'''
def saveLib(lib, path = ""):
    path = os.path.join(path, '.database')
    if not os.path.exists(path):
        print(f'Program has not been initialised, initialising...')
        os.mkdir(path)
    current_file = os.path.join(path, lib.name + '.data')
    with open(current_file, 'wb') as output:
        pickle.dump(lib, output, pickle.HIGHEST_PROTOCOL)
    return


'''
    Helper function for UI when it is eventually implemented
'''
def takePrompt(size, totalnum, del_size, delnum, del_list, msg = ""):
    print(f'Total size of the folder = {round(size, 2)} MBs')
    print(f'Out of the {totalnum} images, {delnum} were similar.')
    print('Thy are : ')
    for img in del_list:
        print(img)
    print(f'Deleting will save {round(del_size, 2)} MBs, leaving space occupied to {round(size-del_size, 2)} MBs.')
    decision = input(msg)
    if decision.upper() == 'Y' or decision.upper() == 'YES':
        return True
    else:
        return False
    pass


