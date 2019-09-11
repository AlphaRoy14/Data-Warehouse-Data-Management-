import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

myUrl = "https://www.last.fm/charts"

client = urlopen(myUrl)
page = client.read()
client.close()
f=open("TopSongs","w")
headers = "Rank, Song Name, Artist\n"
f.write(headers)

page_soup = soup(page,"html.parser")

charts = page_soup.findAll("tbody")

#finds all the songs 
songs = charts[0].findAll("tr")

for song in songs:
    try:
        position = song.td.text.strip()
        song_name = song.findAll("td",{"class":"globalchart-name"})[0].a.text
        artist_name = song.findAll("td",{"class":"globalchart-track-artist-name"})[0].a.text

        f.write(position + "," + song_name.replace(",","|") + "," + artist_name + "\n")
        print("Rank: ------ ",position)
        print("Song Name: -----", song_name)
        print("artist_name: -----", artist_name)
        print("\n\n\n")
    except IndexError:
        continue





