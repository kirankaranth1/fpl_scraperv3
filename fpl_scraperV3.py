from __future__ import print_function
import re
import requests
from lxml import html
from StringIO import StringIO
import sys
from msvcrt import getch
import os
import json
import math
  
  
  
def calcresult(n):
    score=(int(math.floor(n / 10.0)) * 10)/10+1
    return score
def get_score(id) :
    url="http://fantasy.premierleague.com/entry/"+str(id)+"/event-history/"+str(gw)+"/"
    while True:
        try:
            page = requests.get(url)
        except requests.ConnectionError:
            continue
        break
    tree = html.parse(StringIO(page.text)).getroot()
    xpath_1=".//*[@id='ism']/section[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div/div[1]/div/div/text()"
    t_points=int(re.findall('\d+', tree.xpath(xpath_1)[0].strip(' \t\n\r'))[0])
    xpath_2=".//*[@id='ism']/section[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div/div[2]/dl/dd[2]/text()"
    xpath_3=".//*[@id='ism']/section[2]/h1/text()"
    name=str(tree.xpath(xpath_3)[0].strip(' \t\n\r'))
    try:
        transfers=int(re.findall('\d+', tree.xpath(xpath_2)[0].strip(' \t\n\r'))[1])
    except IndexError,e :
        transfers=0;
    t_score=t_points-transfers
    return (t_score,name)
    
def get_team(team,gw):
    scores=[0,0,0,0,0]
    names=["","","","",""]
    print("Parsing scores of "+team[5])
    print("",file=f)
    print(team[5]+" Gameweek "+str(gw),file=f)
    for i in range(0,5):
        scores[i],names[i]=get_score(team[i])
    print("1. "+names[1]+" "+str(scores[1])+", "+names[2]+" "+str(scores[2])+", "+names[3]+" "+str(scores[3])+", "+names[4]+" "+str(scores[4])+" = "+str(scores[1]+scores[2]+scores[3]+scores[4]),file=f)
    print("2. "+names[0]+" "+str(scores[0])+"*2 = "+str(scores[0]*2),file=f)
    ha=0
    if checkifhome(team[6],team[5],gw):
        
        ha=max(scores)*0.2
        print("3. Home advantage= "+"0.2*"+str(max(scores))+"="+str(ha),file=f)
    else:
        print("3. No home advantage",file=f)
    total=scores[1]+scores[2]+scores[3]+scores[4]+scores[0]*2+ha
    print("Total="+str(total)+" ~"+str(round(total)),file=f)
    print("",file=f)
    return round(total)
def checkifhome(teamid,teamname,gw):
    #print(teamid,teamname,gw)
    r = requests.get("http://www.football-data.org/teams/"+str(teamid)+"/fixtures")
    #print(r)
    result = json.loads(r.text)
    #print(result)
    if teamname in result['fixtures'][gw-1]['homeTeam']:
        #print(result[gw+1])
        return True
    else:
        return False
def getfix(gw):
    res = requests.get("http://www.football-data.org/soccerseasons/354/fixtures?matchday="+str(gw))
    result=json.loads(res.text)
    return result
    

print("LFC India Fantasy League FPL Score scraper")
print("--------------------------------------------------")
print("Author: Kiran Karanth")
print("facebook.com/kirankaranth1")
print("")
dict={"Manchester United FC":0,"Swansea City":0,"Leicester City":0,"Everton FC":0,"West Ham United FC":0,"Tottenham Hotspur FC":0,"West Bromwich Albion":0,"Sunderland AFC":0,"Stoke City FC":0,"Aston Villa FC":0,"Queens Park Rangers":0,"Hull City FC":0,"FC Arsenal London":0,"Crystal Palace":0,"Liverpool FC":0,"FC Southampton":0,"Newcastle United":0,"Manchester City FC":0,"FC Burnley":0,"Chelsea FC":0}
gw=input("Enter Gameweek number:  ")
if(gw>=17 and gw<=24):
    
    fn="Gameweek_"+str(gw)+"v3.txt"
    f = open(fn,'a')
    print("All teams scores Gameweek "+str(gw),file=f)
    hull=[235293,1149861,192687,1677986,282609,"Hull City FC",322,"h","h","a","a","h","a","h","a","a","h","a","h","a","h"]
    arsenal=[2147614,1187227,454989,106383,1874374,"FC Arsenal London",57,"h","a","h","a","h","a","h","a","h","a","h","a","h",""]
    villa=[286331,870575,1511244,1793894,1245460,"Aston Villa FC",58,"a","h","a","a","h","a","h","a","a","h","a","h","a","h"]
    burnley=[333912,325056,108067,684282,136183,"FC Burnley",328,"a","a","h","h","a","h","a","h","h","a","h","a","h",""]
    chelsea=[386880,1657614,79759,2365314,320451,"Chelsea FC",61,"h","h","a","a","h","a","h","a","h","a","h","a","h",""]
    palace=[72711,192858,297679,344694,1594177,"Crystal Palace",354,"h","a","h","a","h","a","h","a","h","a","h","a","h",""]
    everton=[1375942,193410,1251421,995844,451136,"Everton FC",62,"a","a","h","a","h","a","h","a","h","a","h","a","h",""]
    leicester=[1318470,41975,286373,2093448,257328,"Leicester City",338,"a","h","a","a","h","a","h","a","h","a","h","a","h",""]
    liverpool=[400106,833373,541519,468192,194237,"Liverpool FC",64,"h","h","a","h","a","h","a","h","a","h","a","h","a","h"]
    city=[1620596,384500,721763,540855,68930,"Manchester City FC",65,"a","a","h","a","h","a","h","a","a","h","a","h","a","h"]
    scums=[262415,81179,2326261,51092,1461413,"Manchester United FC",66,"h","h","a","h","a","h","a","h","h","a","h","a","h",""]
    newcastle=[1144868,342876,407205,52355,56998,"Newcastle United",67,"a","a","h","a","h","a","h","a","a","h","a","h","a","h"]
    qpr=[1880769,264939,277719,1697834,1599192,"Queens Park Rangers",69,"a","a","h","h","a","h","a","h","a","h","a","h","a","h"]
    saints=[278413,383212,258535,2317698,1173922,"FC Southampton",340,"h","a","h","h","a","h","a","h","a","h","a","h","a","h"]
    stoke=[779871,2062491,376009,366861,451272,"Stoke City FC",70,"h","a","h","a","h","a","h","a","a","h","a","h","a","h"]
    ham=[1485675,654398,2639408,1031829,319332,"West Ham United FC",563,"a","h","a","h","a","h","a","h","a","h","a","h","a","h"]
    sunderland=[86905,129763,15003,385980,1203445,"Sunderland AFC",71,"h","h","a","h","a","h","a","h","h","a","h","a","h",""]
    swans=[82318,506284,1721201,1340663,1276345,"Swansea City",72,"a","h","a","h","a","h","a","h","h","a","h","a","h",""]
    spurs=[103596,1628118,1046402,901455,232054,"Tottenham Hotspur FC",73,"a","h","a","h","a","h","a","h","a","h","a","h","a","h"]
    westbrom=[1392297,310730,166582,68335,276748,"West Bromwich Albion",74,"h","a","h","h","a","h","a","h","h","a","h","a","h",""] 
if(gw>=9 and gw<=16):
    
    fn="Gameweek_"+str(gw)+".txt"
    f = open(fn,'a')
    print("All teams scores Gameweek "+str(gw),file=f)
    hull=[1149861,192687,1677986,282609,235293,"Hull City FC",322,"h","h","a","a","h","a","h","a","a","h","a","h"]
    arsenal=[1187227,454989,2147614,106383,1874374,"FC Arsenal London",57,"h","a","h","a","h","a","h","a","h","a","h","a"]
    villa=[870575,1511244,1793894,1245460,286331,"Aston Villa FC",58,"a","h","a","a","h","a","h","a","a","h","a","h"]
    burnley=[325056,108067,684282,333912,136183,"FC Burnley",328,"a","a","h","h","a","h","a","h","h","a","h","a"]
    chelsea=[1657614,79759,2365314,320451,386880,"Chelsea FC",61,"h","h","a","a","h","a","h","a","h","a","h","a"]
    palace=[192858,297679,344694,72711,1594177,"Crystal Palace",354,"h","a","h","a","h","a","h","a","h","a","h","a"]
    everton=[193410,1251421,1375942,995844,451136,"Everton FC",62,"a","a","h","a","h","a","h","a","h","a","h","a"]
    leicester=[41975,286373,2093448,257328,1318470,"Leicester City",338,"a","h","a","a","h","a","h","a","h","a","h","a"]
    liverpool=[833373,541519,400106,468192,194237,"Liverpool FC",64,"h","h","a","h","a","h","a","h","a","h","a","h"]
    city=[384500,721763,540855,1620596,68930,"Manchester City FC",65,"a","a","h","a","h","a","h","a","a","h","a","h"]
    scums=[81179,2326261,262415,51092,1461413,"Manchester United FC",66,"h","h","a","h","a","h","a","h","h","a","h","a"]
    newcastle=[342876,407205,52355,56998,1144868,"Newcastle United",67,"a","a","h","a","h","a","h","a","a","h","a","h"]
    qpr=[264939,277719,1880769,1697834,1599192,"Queens Park Rangers",69,"a","a","h","h","a","h","a","h","a","h","a","h"]
    saints=[383212,258535,278413,2317698,1173922,"FC Southampton",340,"h","a","h","h","a","h","a","h","a","h","a","h"]
    stoke=[2062491,376009,779871,366861,451272,"Stoke City FC",70,"h","a","h","a","h","a","h","a","a","h","a","h"]
    ham=[2639408,1031829,319332,1485675,654398,"West Ham United FC",563,"a","h","a","h","a","h","a","h","a","h","a","h"]
    sunderland=[129763,15003,86905,385980,1203445,"Sunderland AFC",71,"h","h","a","h","a","h","a","h","h","a","h","a"]
    swans=[506284,1721201,1340663,82318,1276345,"Swansea City",72,"a","h","a","h","a","h","a","h","h","a","h","a"]
    spurs=[1628118,1046402,103596,901455,232054,"Tottenham Hotspur FC",73,"a","h","a","h","a","h","a","h","a","h","a","h"]
    westbrom=[310730,166582,68335,276748,1392297,"West Bromwich Albion",74,"h","a","h","h","a","h","a","h","h","a","h","a"]

dict["FC Arsenal London"]=get_team(arsenal,gw)
dict["Aston Villa FC"]=get_team(villa,gw)
dict["FC Burnley"]=get_team(burnley,gw)
dict["Chelsea FC"]=get_team(chelsea,gw)
dict["Crystal Palace"]=get_team(palace,gw)
dict["Everton FC"]=get_team(everton,gw)
dict["Hull City FC"]=get_team(hull,gw)
dict["Leicester City"]=get_team(leicester,gw)
dict["Liverpool FC"]=get_team(liverpool,gw)
dict["Manchester City FC"]=get_team(city,gw)
dict["Manchester United FC"]=get_team(scums,gw)
dict["Newcastle United"]=get_team(newcastle,gw)
dict["Queens Park Rangers"]=get_team(qpr,gw)
dict["FC Southampton"]=get_team(saints,gw)
dict["Stoke City FC"]=get_team(stoke,gw)
dict["Sunderland AFC"]=get_team(sunderland,gw)
dict["Swansea City"]=get_team(swans,gw)
dict["Tottenham Hotspur FC"]=get_team(spurs,gw)
dict["West Bromwich Albion"]=get_team(westbrom,gw)
dict["West Ham United FC"]=get_team(ham,gw)

print(dict)
fixtures=getfix(gw)

for fix in fixtures:
    hscore=dict[fix['homeTeam']]
    ascore=dict[fix['awayTeam']]
    if(hscore>ascore):
        fix['goalsAwayTeam']=0
        diff=hscore-ascore
        fix['goalsHomeTeam']=calcresult(diff)
    elif(hscore==ascore):
        fix['goalsAwayTeam']=0
        fix['goalsHomeTeam']=0
    else:
        
        diff=ascore-hscore
        fix['goalsAwayTeam']=calcresult(diff)
        fix['goalsHomeTeam']=0
        
    print(str(fix['homeTeam'])+" vs "+str(fix['awayTeam'])+"\n"+str(dict[fix['homeTeam']])+"-"+str(dict[fix['awayTeam']])+"\nDiff="+str(diff)+"\n"+str(fix['goalsHomeTeam'])+"-"+str(fix['goalsAwayTeam']))

        
path=str(os.getcwd())
print("Parsing complete. Parsed scores are logged at "+path+"\\"+"Gameweek_"+str(gw)+".txt")
print("")
print("Press any key to exit.")
x=getch()
    
    
  
    
#except Exception,e1:
#    print("Error: Some shit happened. Please report the below error to author.")
#    print(e1)
#    print("Press any key to exit.")
#    x=getch()
    
