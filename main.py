from xml.dom import minidom
import urllib2
from time import sleep 

#get gamday URL
gameday=raw_input("Please paste the URL of the game you wish to track")
str(gameday)

while True:
    
    #get the xml  Use boxscore.xml or linescore.xml 
    html = urllib2.urlopen(gameday)

    #parse the xml
    xmldoc=minidom.parse(html)

    #get the xml tag and access it using dictionary syntax
    game=xmldoc.getElementsByTagName('game')
    

    #can access element hierarchy using dictionary index
    game_index=game[0]

    #access xml attribute using dictionary syntax
    current_inning=game_index.attributes['inning']
    
    print str(current_inning.value)

    sleep(60)
    del html





