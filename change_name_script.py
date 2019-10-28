#!/usr/bin/python
# -*- coding: UTF-8 -*- 
#usage: .py target_keyword  replace  newword oldword 
#usage: .py target_keyword  delete   newword 
#usage: .py target_keyword  add      newword 
import os,sys,shutil 
if hasattr(__builtins__, 'raw_input'):
    input=raw_input

def searchFile(target):
    os.chdir(os.curdir)
    for each_file in os.listdir(os.curdir):
       if target in each_file:
           yield each_file

if __name__ == "__main__":

    for each_file in searchFile(sys.argv[1]):
        print(each_file)

    confirm = input("\nAre you sure to change names of files above???(Y/N)") 
    
    if (confirm != "Y"):
        exit()

    #print(sys.argv[1])
    for each_file in searchFile(sys.argv[1]):
        new_file=""
        if sys.argv[2]=="replace":
            new_file = each_file.replace(sys.argv[4],sys.argv[3])
        elif sys.argv[2]=="delete":
            new_file = each_file.replace(sys.argv[3],"")
        elif sys.argv[2]=="add":
            new_file = each_file + sys.argv[3]
        print(each_file,">",new_file)
        os.rename(each_file,new_file)