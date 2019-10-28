#!/usr/bin/python
#usage: .py target_keyword  replace  newword oldword
#usage: .py target_keyword  delete   newword 
import os,sys
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

    if sys.argv[2]=="replace":
            confirm = input("\nAre you sure to do the \" {0},{1},{2} \" to files above???(Y/N)".format(sys.argv[2],sys.argv[3],sys.argv[4])) 
            if (confirm != "Y"):
                exit()
    elif sys.argv[2]=="delete":
            confirm = input("\nAre you sure to do the \" {0},{1} \" to files above???(Y/N)".format(sys.argv[2],sys.argv[3])) 
            if (confirm != "Y"):
                exit()

    #print(sys.argv[1])
    for each_file in searchFile(sys.argv[1]):
        f = open(each_file,"r+")
        old_text = f.read()        

        f.seek(0) #set point to the head
        f.truncate() #clear f

        new_text=""
        if sys.argv[2]=="replace":
            new_text= old_text.replace(sys.argv[4],sys.argv[3])

        elif sys.argv[2]=="delete":
            new_text=old_text.replace(sys.argv[3],"")
        
        #print(old_text,new_text)
        #fnew= open("new","w")
        f.write(new_text)
        f.close()

    



