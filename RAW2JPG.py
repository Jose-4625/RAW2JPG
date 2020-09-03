class RAW2JPG(object):

  def __init__(self):
    """
    Initialize RAW2JPG object and import all necessary libraries
    Dependencies:
        NumPy
        os
        time
        Image from PIL
        raw from rawkit
    Attributes:
        self.queue => []
        self.raw_type => '.CR2'
        self.jpgDir => None
        self.listdir => os.listdir
        self.mkdir => os.mkdir
        self.path => os.path
        self.utime => os.utime
        self.array => np.array
        self.Raw => raw.Raw
        self.time => time.time
        self.frombytes => Image.frombytes
    """
    import numpy as np
    import os
    import time
    from PIL import Image
    try:
      from rawkit import raw
    except (ImportError, ModuleNotFoundError):
      raise Exception("rawkit is not installed or not all dependencies were found, try: pip3 install rawkit AND apt-get install libraw-dev")

    self.queue = []
    self.raw_type = '.CR2'
    self.jpgDir = None
    self.listdir = os.listdir
    self.mkdir = os.mkdir
    self.path = os.path
    self.utime = os.utime
    self.array = np.array
    self.Raw = raw.Raw
    self.time = time.time
    self.frombytes = Image.frombytes

  def test(self):
      print("checking dependencies...")
      try:
        import numpy as np
      except (ImportError, ModuleNotFoundError):
        raise Exception("NumPy is not installed or not all dependencies were found, try: pip3 install numpy")
      try:
        from rawkit import raw
      except (ImportError, ModuleNotFoundError):
        raise Exception("rawkit is not installed or not all dependencies were found, try: pip3 install rawkit AND apt-get install libraw-dev")
      try:
        from PIL import Image
      except (ImportError, ModuleNotFoundError):
        raise Exception("PIL is not installed or not all dependencies were found, try: pip3 install pillow")
      print("RAW2JPG is ready to be used!")

  def _Parse_File(self, file):
    """
    Parse the input RAW filename
    Input:
        file
    Output:
        (fileName, fileWithoutExt, fileTimestamp)
    """
    fileName = self.path.basename(file)
    fileWithoutExt = self.path.splitext(fileName)[0]
    fileTimestamp = self.path.getmtime(file)
    return (fileName, fileWithoutExt, fileTimestamp)

  def _Parse_RAW(self, file):
    """
    Parse the input RAW image data
    Input:
        file
    Output:
        (rawImageProcess, bufferedImage)
    """
    rawImageProcess = self.Raw(file)
    bufferedImage = self.array(rawImageProcess.to_buffer())
    return (rawImageProcess, bufferedImage)

  def _Parse_Orientation(self, rawImageProcess):
    """
    Parse the input RAW orientation data
    Input:
        rawImageProcess
    Output:
        (jpgImageHeight, jpgImageWidth)
    """
    if rawImageProcess.metadata.orientation == 0:
        jpgImageHeight = rawImageProcess.metadata.height
        jpgImageWidth = rawImageProcess.metadata.width
    else:
        jpgImageHeight = rawImageProcess.metadata.width
        jpgImageWidth = rawImageProcess.metadata.height
    return (jpgImageHeight, jpgImageWidth)
  def _Parse_dir(self):
    """
    Parse output directory path
    Input:
        None
    Output:
        self._FS_JPG() OR self.jpgDir
    """
    if not self.jpgDir:
      return self._FS_JPG()
    else:
      return self.jpgDir

  def _Parse_JPG(self, jpgImageHeight, jpgImageWidth, bufferedImage):
    """
    Parse the output JPEG metadata
    Input:
        jpgImageHeight, jpgImageWidth, bufferedImage
    Output:
        (jpgImageLocation, jpgImage)
    """
    jpgImageLocation = self._Parse_dir() + fileWithoutExt + '.jpg'
    jpgImage = self.frombytes('RGB', (jpgImageWidth, jpgImageHeight), bufferedImage)
    jpgImage.save(jpgImageLocation, format="jpeg")
    return (jpgImageLocation, jpgImage)
  def _Process(self, file):
    """
    Parse the onput JPG metadata
    Input:
        file
    Output:
        None
    """
    print("Converting the following raw image: " + file + " to JPG")
    start = self.time()
    # file vars
    fileName, fileWithoutExt, fileTimestamp = self._Parse_File(file)

    # parse CR2 image
    rawImageProcess, bufferedImage = self._Parse_RAW(file)

    # check orientation due to PIL image stretch issue
    jpgImageHeight, jpgImageWidth = self._Parse_Orientation(rawImageProcess)

    # prep JPG details
    jpgImageLocation, jpgImage = self._Parse_JPG(jpgImageHeight, jpgImageWidth, bufferedImage)

    # update JPG file timestamp to match CR2
    os.utime(jpgImageLocation, (fileTimestamp,fileTimestamp))

    # close to prevent too many open files error
    jpgImage.close()
    rawImageProcess.close()
    delta = self.time() - start
    print("Process finished, Elapsed time: ", delta)

  def addRawFile(self, file_path):
    """
    Add a SINGLE, RAW file path to the internal queue
    Input:
        file_path
    Output:
        None
    """
    self.queue.append(file)

  def addRawFolder(self, folder_path):
    """
    Add a SINGLE, RAW folder path to the internal queue
    Input:
        folder_path
    Output:
        None
    """
    for file in self.listdir(folder_path):
      self.addRawFile(file)

  def addOutputPath(self, folder_path):
    """
    Define the SINGLE, JPEG output folder path
    Input:
        folder_path
    Output:
        None
    """
    if self.listdir(folder_path):
      self.jpgDir = folder_path

  def _FS_CR2(self):
    """
    Create CR2 folder
    Input:
        None
    Output:
        'CR2' (String)
    """
    if 'CR2' not in self.listdir('.'):
      self.mkdir('CR2')
      return 'CR2'
    else:
      return 'CR2'
  def _FS_JPG(self):
    """
    Create JPG folder
    Input:
        None
    Output:
        'JPG' (String)
    """
    if 'JPG' not in self.listdir('.'):
      self.mkdir('JPG')
      return 'JPG'
    else:
      return 'JPG'
  def createFileSystem(self):
    """
    Create CR2/JPG folder system for easy Input/Output
    Input:
        None
    Output:
        True (Bool)
    """
    self._FS_CR2()
    self._FS_JPG()
    return True

  def convertImages(self):
    """
    Initiate CR2 to JPG conversion
    Input:
        None
    Output:
        None
    """
    if 'CR2' not in self.listdir('.'):
      for file in self.queue:
        self._Process(file)
    else:
      for i in self.listdir('CR2'):
        self.addRawFile(i)
      for file in self.queue:
        self._Process(file)
