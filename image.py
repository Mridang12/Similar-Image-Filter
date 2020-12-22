from PIL import Image
import os
import sys
import imghdr
import numpy
import scipy.fftpack
import time
import pickle
from distutils.dir_util import copy_tree
import ntpath
from file_io import *



'''
    Given a list of image wrapper objects, gives back the list of similar images, removing them from img_list
    Optional : reference. Passed if want to compare with another list of images instead of with itself
    Return : list of images that are similar
'''
def processImages(img_list, reference = []):
    img_list = img_list[:]

    if not reference:
        i = 0
        size_del = 0
        del_list = dict()
        while (i < len(img_list)):
            j = i+1
            while (j < len(img_list)):
                if (img_list[i].similarity_test(img_list[j])):
                    size_del += img_list[j].size
                    del_list[img_list[i]] = del_list.get(img_list[i], []) + [img_list.pop(j)]
                else:
                    j += 1
            i += 1
        return size_del, del_list
    else:
        size_del = 0
        del_list = dict()
        
        for ref in reference:
            i = 0
            while (i < len(img_list)):
                if ref.similarity_test(img_list[i]):
                    size_del += img_list[i].size
                    del_list[ref] = del_list.get(ref, []) + [img_lost.pop(i)]
                else:
                    i +=1

        return size_del, del_list


'''
    Class to wrap images with their path and colorhashes.
'''
class ImageWrapper:
    def __init__(self, path, size):
        self.path = path
        self.size = (size/1024**2)
        self.hash = self.calc_phash()

    def similarity_test(self, img, cutoff = 8):
        return numpy.count_nonzero(self.hash.flatten() != img.hash.flatten()) <= cutoff

    
    '''
        Calculates a difference hash
    '''
    def calc_dhash(self, size = 8):
        img = Image.open(self.path)
        img = img.convert('L')
        img = img.resize((size + 1, size))
        img = numpy.asarray(img)
        diff = img[: , 1:] > img[:, :-1]
        return diff

    '''
        Calculates a perceptual hash
    '''
    def calc_phash(self, size = 8, highfreq = 4):
        img = Image.open(self.path)
        img = img.convert('L') #CONVERT TO GRAYSCALE
        img = img.resize((size * highfreq, size * highfreq), Image.ANTIALIAS) #RESIZE TO 32 by 32
        img = numpy.asarray(img)
        DTC = scipy.fftpack.dct(img, axis=0) 
        DTC = scipy.fftpack.dct(DTC, axis=1) #CALC DTC
        lowfreq = DTC[:size, :size] #ONLY KEEP THE TOP LEFT PORTION (LOW FREQ)
        median = numpy.median(lowfreq)
        diff = lowfreq > median
        return diff

    def __str__(self):
        return self.path

'''
    Class to manage an image library.
'''
class ImageLibrary:
    def __init__(self, name, path, size=None, img_list=[]):
        self.path = path
        self.name = name
        if (not img_list):
            self.img_list = []
            self.initialise()
        else:
            self.img_list = img_list
            self.size = size

    def scan(self):
        size, img_list = processFolder(self.path)
        self.size = size
        self.img_list = img_list

    def process(self):
        return processImages(self.img_list)

    def initialise(self):
        self.scan()
        del_size, del_list = self.process()
        if len(del_list) == 0:
            print(f"All {len(self.img_list)} images in library \"{self.name}\" found to be unique!")
            pass
        else:
            if (takePrompt(self.size, len(del_list) + len(self.img_list), del_size, len(del_list),del_list, msg = f"For library \"{self.name}\", Do you want to delete or keep similar duplicates ?\n\t Enter yes to delete : ")):
                self.size -= del_size
                deleteImageList(del_list)
            else:
                self.img_list += del_list
            

    def addFolder(self, path):
        folderPath = copyFolder(to_path = self.path, from_path = path)
        size, img_list = processFolder(folderPath)

        del_size_inside, del_list_inside = processImages(img_list)
        if takePrompt(size, len(img_list) + len(del_list_inside), del_size_inside, len(del_list_inside),del_list_inside, msg = f"Inside this folder, Do you want to delete or keep similar duplicates ?\n\t Enter yes to delete : ") :
            size -= del_size_inside
            deleteImageList(del_list_inside)
        else:
            img_list += del_list_inside

        del_size, del_list = processImages(img_list, reference = self.img_list)        
        if takePrompt(size, len(img_list) + len(del_list), del_size, len(del_list),del_list, msg = f"In the newly added folder to library \"{self.name}\ , Do you want to delete or keep similar duplicates ?\n\t Enter yes to delete : "):
            size -= del_size
            deleteImageList(del_list)
        else:
            img_list += del_list
        
        self.img_list += img_list
        self.size += size

    def __str__(self):
        string = f'Library \"{self.name}\" currently tracking the following images :'
        for img in self.img_list:
            string += '\n' + str(img)
        return string

        
    