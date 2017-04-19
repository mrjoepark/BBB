from xml.dom import minidom
import urllib2
from time import sleep 

#get gamday URL
#gameday=raw_input("Please paste the URL of the game you wish to track:  ")
#str(gameday)


#define GPIO on/off functions here
def score():
    print str_home_team, int_home_score
    print str_away_team, int_away_score

def topOrBottom():
    if top_bottom=='Y':
        print 'top on'
    else:
        print 'bottom on' 
    
def inning():
    #turn inning lights on or off from bin_current_inning_list 
    if bin_current_inning[0]== '1':
        print ' first on'
    else:
        print ' first off'
    if bin_current_inning[1]== '1':
        print ' second on'
    else:
        print ' second off'
    if bin_current_inning[2]== '1':
        print ' third on'
    else:
        print ' third off'
    if bin_current_inning[3]== '1':
        print ' fourth on'
    else:
        print ' fourt off'
        
#loop 
while True:
    #get the xml  Use boxscore.xml or linescore.xml 
    html=urllib2.urlopen('http://gd2.mlb.com/components/game/mlb/year_2017/month_04/day_18/gid_2017_04_18_sfnmlb_kcamlb_1/linescore.xml')

    #parse the xml
    xmldoc=minidom.parse(html)

    #get the xml tag and access it using dictionary syntax
    game=xmldoc.getElementsByTagName('game')

    #can access element hierarchy using dictionary index
    game_index=game[0]

    #access xml attribute using dictionary syntax
    current_inning=game_index.attributes['inning']
    top_bottom=game_index.attributes['top_inning']
    home_score=game_index.attributes['home_team_runs']
    away_score=game_index.attributes['away_team_runs']
    home_team=game_index.attributes['home_team_name']
    away_team=game_index.attributes['away_team_name']
    #get values and turn the attirbutes into a int and use format to convert to binary
    int_current_inning=int(current_inning.value)
    int_home_score=int(home_score.value)
    int_away_score=int(away_score.value)
    str_home_team=home_team.value
    str_away_team=away_team.value 
    
    #format(value, '04' lead spaces, b=binary
    bin_current_inning=format(int_current_inning, '04b')
    print bin_current_inning
    bin_current_inning=list(bin_current_inning)
    print int_current_inning 

    #GPIO functions
    score()
    topOrBottom()
    inning()
    
    sleep(60)
    del html
