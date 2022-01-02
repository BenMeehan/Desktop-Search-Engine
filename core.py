import os
import pickle 
import re

class IndexSearch:
    def __init__(self) -> None:
        '''Initializing the varibles needed'''
        self.files=0
        self.directories=0 
        self.file_index=[]
        self.dir_index=[]
        self.file_results=[]
        self.dir_results=[]
        self.file_matches=0
        self.dir_matches=0

    def create_index(self,path):
        '''Search through the given path and create an index of files and directories.
            The result is stored on the disk in a pickle file.'''
        self.file_index=[(root,file) for root,dirs,file in os.walk(path) if file]
        self.dir_index=[(root,dirs)for root,dirs,file in os.walk(path) if dirs]
        
        with open("file_index.pkl",'wb') as f:
            pickle.dump(self.file_index,f)
        
        with open("dir_index.pkl",'wb') as f:
            pickle.dump(self.dir_index,f)
        return True
    
    def load_index(self):
        '''Check if an index file is already present in the current directory and load it.
            Set index to empty array if no file is found.'''
        result=True
        try:
            with open("file_index.pkl",'rb') as f:
                self.file_index=pickle.load(f)
        except:
            self.file_index=[]
            result=False
        
        try:
            with open("dir_index.pkl",'rb') as f:
                self.dir_index=pickle.load(f)
        except:
            self.dir_index=[]
            result=False

        return result

    def search_files(self,term,method):
        print(term,method)
        '''Search for the list of file index.

            method = "prefix" | "suffix" | "all" 
            
            The output is written to a file in the same directory called "files.txt"'''
        self.file_results=[]
        self.file_matches=0 
        self.files=0 

        if method=="prefix":
            for path,files in self.file_index:
                for file in files:
                    self.files+=1 
                    if re.search(f"^{term}",file):
                        self.file_results.append(path+"\\"+file)
                        self.file_matches+=1 
        
        elif method=="suffix":
            for path,files in self.file_index:
                for file in files:
                    self.files+=1 
                    if re.search(f"{term}$",file):
                        self.file_results.append(path+"\\"+file)
                        self.file_matches+=1 
        elif method=="all":
            for path,files in self.file_index:
                for file in files:
                    self.files+=1 
                    if re.search(f"{term}",file):
                        self.file_results.append(path+"\\"+file)
                        self.file_matches+=1 

        print(self.file_results)
        with open("files.txt",'w') as f: 
            for result in self.file_results:
                f.write(result+"\n")
        
        os.startfile("files.txt")
    
    def search_dirs(self,term,method):
        '''search for a term in the list of directories index.

            method = "prefix" | "suffix" | "all"
            
            The output is written to a file in the same directory called "directory.txt"'''
        self.dir_results=[]
        self.dir_matches=0 
        self.dir=0 

        if method=="prefix":
            for path,directories in self.dir_index:
                for dir in directories:
                    self.directories+=1 
                    if re.search(f"^{term}",dir):
                        self.dir_results.append(path+"\\"+dir)
                        self.dir_matches+=1 
        elif method=="suffix":
            for path,directories in self.dir_index:
                for dir in directories:
                    self.directories+=1 
                    if re.search(f"{term}$",dir):
                        self.dir_results.append(path+"\\"+dir)
                        self.dir_matches+=1 
        elif method=="all":
            for path,directories in self.dir_index:
                for dir in directories:
                    self.directories+=1 
                    if re.search(f"{term}",dir):
                        self.dir_results.append(path+"\\"+dir)
                        self.dir_matches+=1 

        with open("directories.txt",'w') as f: 
            for result in self.dir_results:
                f.write(result+"\n")

        os.startfile("directories.txt")

