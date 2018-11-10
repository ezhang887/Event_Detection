import zipfile
import shutil
import urllib.request
import os

print('Beginning file download with urllib2...')

images_url = 'http://eventdetection.web.illinois.edu/images.zip'
labels_url = 'http://eventdetection.web.illinois.edu/labels.zip'
urllib.request.urlretrieve(images_url, 'images.zip')
print('Successfully downloaded images.zip')
urllib.request.urlretrieve(labels_url, 'labels.zip')
print('Successfully downloaded labels.zip')

images = zipfile.ZipFile('images.zip', 'r')
for files in images.namelist():
    images.extract(files, 'darknet/images')
print('Successfully extracted images.zip')
labels = zipfile.ZipFile('labels.zip', 'r')
for files in labels.namelist():
    labels.extract(files, 'darknet/images')
print('Successfully extracted labels.zip')
images.close()
labels.close()


#THIS PUTS ALL THE IMAGES AND TEXT FILES IN THE SAME FOLDER
sourceDir = 'darknet/images/labels'
destDir = 'darknet/images/'
files = os.listdir(sourceDir)
for f in files:
    try:
        sourceFile = os.path.join(sourceDir, f)
        directoryFile = os.path.join(destDir, f)
        shutil.move(sourceFile, destDir)
    except:
        pass
sourceDir = 'darknet/images/Photos2'
files = os.listdir(sourceDir)
for f in files:
    try:
        sourceFile = os.path.join(sourceDir, f)
        directoryFile = os.path.join(destDir, f)
        shutil.move(sourceFile, destDir)
    except:
        pass


os.remove("images.zip")
os.remove("labels.zip")
shutil.rmtree("darknet/images/Photos2")
shutil.rmtree("darknet/images/labels")

print("files deleted")

