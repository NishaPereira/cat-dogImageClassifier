#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Nisha George Pereira
# DATE CREATED:   28/01/2020                           
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
   
    filename_list=listdir(image_dir)
       
    print("\n prints all the  filenames from folder pet_images/")
    for idx in range(0,len(filename_list),1):
        print("{:2d}file: {:>25}".format(idx+1,filename_list[idx]))
            

              
              
    results_dic = {}
    items_in_dic=len(results_dic)
    print("\n empty Dictionary results_dic - n times=",items_in_dic)
    pet_image=[None]*len(filename_list)
    low_pet_image=[None]*len(filename_list)
    word_list_pet_image=[None]*len(filename_list)
    pet_name=[None]*len(filename_list)
    for idx in range(0,len(filename_list),1):
        if filename_list[idx][0] != 0:
            pet_image[idx]=filename_list[idx]
            low_pet_image[idx]=pet_image[idx].lower()
            word_list_pet_image[idx]=low_pet_image[idx].split("_")
            pet_name[idx]=" "
        for word in word_list_pet_image[idx]:
            if word.isalpha():
              pet_name[idx]+=word+" "
                
                
                
                
        pet_name[idx]=pet_name[idx].strip()
        print("\n filename=",pet_image[idx],"label=",pet_name[idx])
        
        
        
        
    for idx in range(0,len(filename_list),1):
        if filename_list[idx] not in results_dic:
           results_dic[filename_list[idx]]=pet_name[idx]
         
        else:
            print("**Warning:key=",filename_list[idx],"alredy exists in result_dic with values=",results_dic[filename_list])
            
            
            
            
    print("\n Printing all key- values pair in dictionary results_dic:")
    for key in results_dic:
        print("filename=",key,"pet label=",results_dic[key])
        
        
        
        
            
    return results_dic
