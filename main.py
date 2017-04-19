from xml.dom import minidom
import urllib2
from time import sleep 

#get gamday URL
#gameday=raw_input("Please paste the URL of the game you wish to track:  ")
#str(gameday)

#define GPIO on/off functions here
#figure out runner on base status pattern
''' 0=no one on 
    1-first base
    2=second base
    3=third base
    4=? maybe 1/2
    5=? maybe 2/3
    6=? maybe 1/3
    7=bases loaded'''
def base_runners():
    if int_base==0:
        print 'no one on'
    if int_base==1:
        print 'runner on first'
    #else:
    if int_base==2:
        print 'runner on second'
    #else:
    if int_base==3:
        print 'runner on third'
    #else:
    if int_base==4:
        print 'base 4'
    #else:
    if int_base==5:
        print 'base 5'
    #else:
    if int_base==6:
        print 'base 6'
    #else:
    if int_base==7:
        print 'bases loaded'        

def score():
    print str_away_team, int_away_score
    print str_home_team, int_home_score

def topOrBottom():
    print str_top_bottom 
    if str_top_bottom=='Top':
        print 'top on'
    else:
        print 'bottom on' 
    
def inning():
    print int_current_inning 
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
        print ' fourth off'

def GPIO_home_score():
    print 'home score binary'
    #turn score lights on or off from bin_home_score 
    if bin_home_score[0]== '1':
        print ' first on'
    else:
        print ' first off'
    if bin_home_score[1]== '1':
        print ' second on'
    else:
        print ' second off'
    if bin_home_score[2]== '1':
        print ' third on'
    else:
        print ' third off'
    if bin_home_score[3]=='1':
        print ' fourth on'
    else:
        print ' fourt off'
    if bin_home_score[4]=='1':
        print ' fifth on'
    else:
        print ' fifth off'

def GPIO_away_score():
    print 'away score binary'
    #turn score lights on or off from bin_away_score 
    if bin_away_score[0]== '1':
        print ' first on'
    else:
        print ' first off'
    if bin_away_score[1]== '1':
        print ' second on'
    else:
        print ' second off'
    if bin_away_score[2]== '1':
        print ' third on'
    else:
        print ' third off'
    if bin_away_score[3]=='1':
        print ' fourth on'
    else:
        print ' fourt off'
    if bin_away_score[4]=='1':
        print ' fifth on'
    else:
        print ' fifth off'
        
#loop 
while True:
    #get the xml. Use linescore.xml 
    html=urllib2.urlopen('http://gd2.mlb.com/components/game/mlb/year_2017/month_04/day_19/gid_2017_04_19_pitmlb_slnmlb_1/linescore.xml')
    #parse the xml
    xmldoc=minidom.parse(html)
    #get the xml tag and access it using dictionary syntax
    game=xmldoc.getElementsByTagName('game')
    #can access element hierarchy using dictionary index
    game_index=game[0]

    #access xml attribute using dictionary syntax
    current_inning=game_index.attributes['inning']
    top_bottom=game_index.attributes['inning_state']
    home_score=game_index.attributes['home_team_runs']
    away_score=game_index.attributes['away_team_runs']
    home_team=game_index.attributes['home_team_name']
    away_team=game_index.attributes['away_team_name']
    base=game_index.attributes['runner_on_base_status']
    #get values and turn the attirbutes into a int, str
    int_current_inning=int(current_inning.value)
    str_top_bottom=str(top_bottom.value)
    int_home_score=int(home_score.value)
    int_away_score=int(away_score.value)
    str_home_team=home_team.value
    str_away_team=away_team.value
    int_base=int(base.value)

    #format binary(value, '04' lead spaces, b=binary)
    bin_current_inning=format(int_current_inning, '04b')
    bin_home_score=format(int_home_score, '05b')
    bin_away_score=format(int_away_score, '05b')
    print bin_current_inning
    print bin_home_score
    print bin_away_score 
    bin_current_inning=list(bin_current_inning)
    bin_home_score=list(bin_home_score)
    bin_away_score=list(bin_away_score)

     
    #GPIO functions
    
    score()
    topOrBottom()
    inning()
    base_runners()
    GPIO_home_score()
    GPIO_away_score()
    
    sleep(60)
    print '\n'
    del html
     
