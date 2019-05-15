# Linux_Enfusion
A python program for infusing images in Linux at particular directories
The first phase is related to development of tool which will take parameters which will allow settings made on the set of images and tell
the tool how to handle that set using command line tool. The source files will be uploaded into directories and this tool should be
listening for the files and process in FIFO sets of 3, with error checking for the wrong sets.
Like for every photoshoot to be done, there would be a specific folder with date as its name would be made and all of these photos would be
saved in that specified folder.
Next would be related to uploading of photos in their specified folders. As each user would be given access to his specified directory so 
he would be able to upload images in its specified directory. 
Next step would be that the tool would use first in first out and would make sets of 3 images, align them together and make one final image.
Final step would be the source files are either Canon RAW or DNEG or Nikon NEF RAW and need to be converted to a file format that infuse will work.
