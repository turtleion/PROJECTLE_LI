from colorama import init,Fore,Back,Style
import datetime,time,os
class File:
    # todo = operation to do (write, read, append write)
    TODO_OPERATION = ["w","r","a"]
    # <-- EXIT STATUS -->
    ERR_UNKNOWN = 0
    ERR_FILEREADFAILED = 1
    ERR_UNKNOWNOPTIONTODO = 2
    ERR_FILENOTFOUND = 3
    ERR_FAILWRITEFILE = 4
    ERR_FAILWRITEAPPND = 4.5
    ERR_PERMISSIONFAIL = 5
    ERR_BUFFEMPTY = 6
    init()
    
    
    
    def __init__(self, file, todo):
        if not os.path.isfile(file) and todo == "r" or os.path.isdir(file) and todo == "r":
            self.exitStatusSet(self.ERR_FILENOTFOUND)
            
        if todo not in self.TODO_OPERATION:
            self.exitStatusSet(self.ERR_UNKNOWNOPTIONTODO)

    def exitStatusSet(status,p):
        print(Fore.RED, "\nA Error Have Been Occured :", Fore.WHITE, " Error Code ERR_CODESTAT_",p,"\n","", datetime.datetime.date(datetime.datetime.now()), " | ", datetime.datetime.time(datetime.datetime.now()))
        
    def read(line):
        f = open(self.file)
        if line == 1 and not line < 1:
            return f.readline()
        elif line < 1:
            returns = []
            for i in range(line):
                returns.append(f.readlines[i])
            return returns
        else:
            self.exitStatusSet(self.ERR_FILEREADFAIL)
            
            
     
    def write(buffer):
        timer = time.perf_counter()
        f = open(self.file,self.todo)
         if buffer == "" or buffer == None:
            self.exitStatusSet(ERR_BUFFEMPTY)
         
         f.write(buffer)
         if(os.path.isfile(self.file)):
            strs = self.read(file)
            if strs == "" or strs == None:
                return ExitStatusSet(ERR_FAILWRITEFILE)
                
          timer2 = time.perf_counter()
          print("Successfully Writing a File in ", timer - timer2)
            

try:
    import os
    import sys
    import time
    from tqdm import tqdm
    import level as lelo
    print("Hello World!")
    f = File("eleanor.r","w")
    f.write("This is mins")
except KeyboardInterrupt:
    print("Son of Bitch")