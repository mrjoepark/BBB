from xml.dom import minidom
import urllib2
from time import sleep 

while True:

    #get the xml  Use boxscore.xml or linescore.xml 
    html = urllib2.urlopen('http://gd2.mlb.com/components/game/mlb/year_2017/month_04/day_05/gid_2017_04_05_miamlb_wasmlb_1/linescore.xml')

    #parse the xml
    xmldoc=minidom.parse(html)

    #get the xml tag and access it using dictionary syntax
    game=xmldoc.getElementsByTagName('game')
    

    #can access element hierarchy using dictionary index
    game_index=game[0]

    #access xml attribute using dictionary syntax
    pbp=game_index.attributes['venue']
    current_inning=game_index.attributes['inning']
   

    print str(current_inning.value)
    print str(pbp.value)

    sleep(60)
    del html





