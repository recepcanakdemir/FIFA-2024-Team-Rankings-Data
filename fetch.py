from bs4 import BeautifulSoup
import requests
import json
import re

# this functions replaces unsupported characters with their real value
def replace_unsupported_characters(input_string):
    sequences = [
        ['\ucc98', 'ó'],
        ['\u00fc', 'ú'],
        ['\u00e9', 'ė'],
        ['\uccb4', 'ü'],
        ['\u00e7', 'ç'],
        ['\u00f6', 'ö'],
        ['\u00f9', 'ù'],
        ['\u00fa', 'ú'],
        ['\u00fa', 'ú'],
        ['\u00fb', 'û'],
        ['\u00fd', 'ý'],
        ['\u00f8', 'ø'],
        ['\u00ec', 'ì'],
        ['\u00ed', 'í'],
        ['\u00ef', 'î'],
        ['\u00df', 'ß']
]
    modified_string = input_string
    for seq in sequences:
        if seq[0] in input_string:
            modified_string = input_string.replace(seq[0], seq[1])
    return modified_string

site_url = 'https://www.fifaindex.com/teams/'
links = []
links.append(site_url)
# get all pages in a links list
for page in range (1,24):
    if page != 1:
        link = site_url + '?page='+str(page)
        links.append(link)

# data is the final json 
data = []

# loop tru all of the links (pages)
for url in links:
    response = requests.get(url)
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    trItems = soup.find_all('tr')

    # loop tru each tr element
    for tr in trItems:
        item = {} # for every item inside of data 
        raitings = {} # for a raitings inside of every team item

        # get td elements
        tdTags = tr.find_all('td')

        # loop tru each td element (each team)
        for td in tdTags:
            dataTitle = td.get('data-title')

            # get teams' other properties
            if dataTitle is None:
                # get image urls
                imageEl = td.find_all('img')
                if len(imageEl):
                    imageUrl = imageEl[0].get('src')
                    item['image'] = imageUrl
            else:
                ranks = ['ATT', 'MID','DEF', 'OVR']
                if dataTitle in ranks:
                    dT = td.get_text().strip()
                    raitings[dataTitle] = dT
                elif dataTitle == "Team Raiting" :
                    continue
                else:
                    dT = replace_unsupported_characters(td.get_text().strip())
                    item[dataTitle] = dT
                item["team_Ratings"] = raitings

            # get stars (if number is 10 it means star is full, 
            # if it is 5, star is half filled, number is 0, then it is empty)

            Itags = td.find_all('i')
            stars = []
            for itag in Itags:
                classesOfITags = itag.get('class')
                star = 10
                if  'far' in classesOfITags:
                    star = 0
                elif 'fa-star-half-alt' in classesOfITags:
                    star = 5
                stars.append(star)
            data_title = dataTitle
            item['stars'] = stars
        #print("this is an item : " + str(item))
        if item and item is not {} and item['stars']:
            data.append(item)

file_path = "C:/Users/Recep Can/Desktop/FIFA Kura Çekme/Data/teams_data.json"

# write JSON data to the file
with open(file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)
print("Data saved to:", file_path)
