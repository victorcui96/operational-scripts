import os
dir = os.path.expanduser("~/Downloads")
list_of_files = os.listdir(dir)
file_extensions = ['.dmg']
for f in list_of_files:
  for extension in file_extensions:
    if f.endswith(extension):
      print 'removing: ' + f
      os.remove(dir + "/" + f)
      
