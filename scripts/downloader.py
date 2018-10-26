import requests
from bs4 import BeautifulSoup # We'll be using this to scrape through HTML documents


#Main
#NOTE THIS SAVES THE IMAGES TO WHEREVER THE PYTHON FILE IS LOCATED
if __name__ == "__main__":

    count = 0
    for i in range(0, 30): #pulls from first 30 pages of gettyImages
        html_doc = requests.get('https://www.gettyimages.in/photos/yellow-card?autocorrect=none&embeddable=true&mediatype=photography&page=' + str(i) +'&phrase=yellow%20card&sort=mostpopular').text
        print(html_doc)
        soup = BeautifulSoup(html_doc, "html5lib")
        tags = soup.findAll('img') #Finds all the image tags
        for tag in tags:
            string = "IMG" + str(count) + ".jpg" #labels the images properly
            print("Image String:  " + string) # outputs file name for debugging
            with open(string, 'wb') as f: # sets up the file on disk


                try:
                    print()
                    print(tag['src'] + " downloading...") # output to terminal
                    f.write(requests.get(tag['src']).content) #saves image to jpg on disk
                    count += 1 #incremnent the id
                except:
                    print("Image is not a jpg or there is img tag")
                    pass


    print("DONE DOWNLOADING")