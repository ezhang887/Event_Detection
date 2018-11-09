import zipfile
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

os.remove("images.zip")
os.remove("labels.zip")
print("files deleted")

