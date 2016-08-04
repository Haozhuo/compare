#!/bin/python

import locale
import random, sys
from optparse import OptionParser

def print1st(line,option1,option2,option3):
    if not option1:
        sys.stdout.write(line+"\n")

def print2nd(line,option1,option2,option3):
    if not option2:
        if not option1:
            sys.stdout.write("\t"+line+"\n")
        else:
            sys.stdout.write(line+"\n")

def print3rd(line,option1,option2,option3):
    if not option3:
        if not option1 and not option2:
            sys.stdout.write("\t"*2+line+"\n")

        elif not option1 or not option2:
            sys.stdout.write("\t"+line+"\n")

        else:
            sys.stdout.write(line+"\n")


def main():
    version_msg = "%comm 2.0"
    usage_msg = """%comm [-123u] FILE1 FILE2

Compare two files line by line"""

    parser = OptionParser(version=version_msg,
                          usage=usage_msg)
    parser.add_option("-1", "--suppress1",
                      action="store_true", dest="option1", default=False,
                      help="suppress column unique to FILE1")

    parser.add_option("-2", "--suppress2",
                      action="store_true", dest="option2", default=False,
                      help="suppress column unique to FILE2")

    parser.add_option("-3", "--suppress3",
                      action="store_true", dest="option3", default=False,
                      help="suppress column in both files")

    parser.add_option("-u", "--unsorted",
                      action="store_true", dest="optionu", default=False,
                      help="compare unsorted files")

    options, args = parser.parse_args(sys.argv[1:])
   

    if len(args) != 2:
        parser.error("wrong number of operands")
    
    filelist1=[]
    filelist2=[]

    try:
        if args[0] == "-":
            f2=open(args[1], 'r')
            filelist2=f2.read().splitlines()
            filelist1=sys.stdin.read().splitlines()
            f2.close()
        elif args[1] == "-":
            f1=open(args[0], 'r')
            filelist1=f1.read().splitlines()
            filelist2=sys.stdin.read().splitlines()
            f1.close()
        else:
            f1=open(args[0],'r')
            filelist1=f1.read().splitlines()
            f2=open(args[1],'r')
            filelist2=f2.read().splitlines()
            f1.close
            f2.close()
    except IOError as err:
        parser.error("I/O error({0}): {1}".
                     format(errno, strerror))

    
    if not options.optionu:
        last=("",-1)
        curr=()
        curr1=""
        curr2=""
        file1Flag=False
        file2Flag=False
        while True:
            if len(filelist1) == 0 or len(filelist2) == 0:
                break
            
            #curr1=filelist1[0]
           # curr2=filelist2[0]

     #       if locale.strcoll(last[0],curr1) > 0 and last[1]!=2 and file1Flag==False:
      #          sys.stderr.write("comm: file 1 is not in sorted order"+"\n")
       #         file1Flag=True

        #    elif locale.strcoll(last[0],curr2) > 0 and last[1]!=1 and file2Flag==False:
         #       sys.stderr.write("comm: file 2 is not in sorted order"+"\n")
          #      file2Flag=True

            if locale.strcoll(filelist1[0],filelist2[0]) < 0:
                curr=(filelist1[0],1)
                last=(filelist1[0],1)
                print1st(curr[0],options.option1, options.option2, options.option3)
                filelist1.remove(filelist1[0])
                

            elif locale.strcoll(filelist1[0],filelist2[0]) == 0:
                curr=(filelist1[0],3)
                last=(filelist1[0],3)
                print3rd(curr[0],options.option1, options.option2, options.option3)
                filelist1.remove(filelist1[0])
                filelist2.remove(filelist2[0])
                

            else:
                curr=(filelist2[0],2)
                last=(filelist2[0],2)
                print2nd(curr[0],options.option1, options.option2, options.option3)
                filelist2.remove(filelist2[0])
 
        if len(filelist1) == 0:
            for i in filelist2:
                curr=(i,2)
               # if locale.strcoll(last[0] , curr[0])>0 and file2Flag==False:
                #    sys.stderr.write("comm: file 2 is not in sorted order"+"\n")
                 #   file2Flag=True

                print2nd(i,options.option1, options.option2, options.option3)
                last=(i,2)

        elif len(filelist2) == 0:
            for i in filelist1:
                curr=(i,1)
               # if locale.strcoll(last[0] , curr[0])>0 and file1Flag==False:
                #     sys.stderr.write("comm: file 1 is not in sorted order"+"\n")
                 #    file1Flag=True

                print1st(i,options.option1, options.option2, options.option3)
                last=(i,1)
    else:
        tupleList=[]
        for i in range(len(filelist1)):
            if filelist1[i] in filelist2:
                tupleList.append((filelist1[i],3))
                filelist2.remove(filelist1[i])
            
            else:
                tupleList.append((filelist1[i],1))
            
        for i in range(len(filelist2)):
            tupleList.append((filelist2[i],2))
        
        for i in tupleList:
            if i[1] == 1:
                print1st(i[0],options.option1,options.option2,options.option3)
            if i[1] == 2:
                print2nd(i[0],options.option1,options.option2,options.option3)
            if i[1] == 3:
                print3rd(i[0],options.option1,options.option2,options.option3)
    
if __name__ == "__main__":
    main()
