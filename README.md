# RAW2JPG
## Inherts from:
* builtins.object

## Module
* RAW2JPG



Methods defined here:
RAW2JPG
object
Dependencies: 
NumPy  
os  
time 
Image from PIL 
raw from rawkit 
Attributes: 
self. queue  => [] 
self. raw_type  => '.CR2' 
self. jpgDir  => None 
self. listdir  => os.listdir 
self. mkdir  => os.mkdir 
self. path  => os.path 
self. utime  => os.utime 
self. array  => np.array 
self. Raw  => raw.Raw 
self. time  => time.time 
self. frombytes  => Image.frombytes   

  <a name="RAW2JPG-addOutputPath" addOutputPath  (self, folder_path)   Define theSINGLE,JPEG
 output
 folderpath 
Input: 
folder_path 
Output: 
None   

  <a name="RAW2JPG-addRawFile"> addRawFile  (self, file_path)   Add a SINGLE, RAW file path to the internal queue 
Input: 
    file_path 
Output: 
    None   

  <a name="RAW2JPG-addRawFolder"> addRawFolder  (self, folder_path)   Add a SINGLE, RAW folder path to the internal queue 
Input: 
    folder_path 
Output: 
    None   

  <a name="RAW2JPG-convertImages"> convertImages  (self)   Initiate CR2 to JPG conversion 
Input: 
    None 
Output: 
    None   

  <a name="RAW2JPG-createFileSystem"> createFileSystem  (self)   Create CR2/JPG folder system for easy Input/Output 
Input: 
    None 
Output: 
    True (Bool)   

 
Data descriptors defined here: 
   __dict__  
  dictionary for instance variables (if defined)  
 
   __weakref__  
  list of weak references to the object (if defined)  
 
      
  
