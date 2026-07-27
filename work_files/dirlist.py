import shutil

shutil.make_archive('folder_2', 'zip', 'folder_2/')
src = 'test2.txt'
dst = 'folder_2'
shutil.move(src, "folder_2/")
