from bs4 import BeautifulSoup
import requests
import json

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
                    raitings[dataTitle] = td.get_text().strip()
                elif dataTitle == "Team Raiting" :
                    continue
                else:
                    item[dataTitle] = td.get_text().strip()
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
        data.append(item)
        item = {}
# Define the file path where you want to save the JSON file
file_path = "C:/Users/Recep Can/Desktop/teams_data.json"

# Write JSON data to the file
with open(file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)
print("Data saved to:", file_path)
