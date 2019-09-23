# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 11:12:09 2019

@author: abhigyan
"""
import webbrowser
from bs4 import BeautifulSoup
from requests import get

def main(emotion): 
	
    if(emotion == "Sad" or emotion == "1"): 
        url = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'

	
    elif(emotion == "Disgust" or emotion == "2"): 
        url = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'

	
    elif(emotion == "Anger" or emotion == "3"): 
        url = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'

	
    elif(emotion == "Anticipation" or emotion == "4"): 
        url = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'

    elif(emotion == "Fear" or emotion == "5"): 
        url = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'

    elif(emotion == "Enjoyment" or emotion == "6"): 
        url = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'

    elif(emotion == "Trust" or emotion == "7"): 
        url = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'

    elif(emotion == "Surprise" or emotion == "8"): 
        url = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'
        
    return url

def webscrap(url):
    
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'lxml')
    movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')
    names = []
    imdb_ratings = []
    for container in movie_containers:
        if container.find('div', class_ = 'ratings-metascore') is not None:
            name = container.h3.a.text
            names.append(name)
            imdb = float(container.strong.text)
            imdb_ratings.append(imdb)
            
    slno=[]
    #x=len(names)
    x=5
    for i in range (x):
        q=i+1
        slno.append(q)
        
    wholetab=dict((z[0],list(z[1:])) for z in zip(slno,names,imdb_ratings))
    
    print("\n\nYou should watch these Popular movies:")
    print ("\n{:<8} {:<40} {:<8}\n".format('Sl.No.','MOVIES','IMDb Ratings'))
    for slno, v in wholetab.items():
        names, imdb_ratings = v
        print ("{:<8} {:<40} {:<8}".format(slno,names,imdb_ratings))
        
    cc=int(input("Enter the Serial No. of the Movie you want to watch now:"))
    vv=wholetab[cc]
    xx=vv[0]
    return xx

def webbrowse(xx):
    term = xx
    #url1 = "https://www.netflix.com/search?q={}".format(term)
    #url2 = "https://www.google.co.in/search?q={}".format(term)
    url3 = "https://www6.fmovies.pub/search?keyword={}".format(term)

    webbrowser.open_new_tab(url3)
    #webbrowser.open_new_tab(url1)
    


            
emotion = input("How Are You Feeling? \n1. Sad\n2. Disgust\n3. Anger\n4. Anticipation\n5. Fear\n6. Enjoyment\n7. Trust\n8. Surprise\nType Emotion or Enter Option: ") 
a = main(emotion)
b=webscrap(a)
c=webbrowse(b)

            
        
            
            
