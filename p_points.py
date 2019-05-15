"""This module consists of the functions required to calculate the points for the top players"""

def batting(p):
    batscore=0
    batscore+=p['runs']/2
    if p['runs']>=50:
        batscore+=5
    elif p['runs']>=100:
        batscore+=10
    if p['runs']/p['balls']>=80 and p['runs']/p['balls']<=100:
        batscore+=2
    elif p['runs']/p['balls']>100:
        batscore+=6
    batscore+=p['4']
    batscore+=p['6']*2
    batscore+=(p['field']*10)
    ptemp={'score':int(batscore)}
    p.update(ptemp)
    pnew={'name':p['name'],'score':p['score']}
    print(pnew)
    return

def bowling(p):
    bowlscore=0
    bowlscore+=p['wkts']*10
    if p['wkts']>=3:
        bowlscore+=5
    if p['wkts']>=5:
        bowlscore+=10
    if 3.5<=(p['runs']/p['overs']) and (p['runs']/p['overs'])<=4.5:
        bowlscore+=4
    elif 2<=(p['runs']/p['overs']) and (p['runs']/p['overs'])<=3:
        bowlscore+=7
    elif (p['runs']/p['overs'])<2:
        bowlscore+=10
    bowlscore+=p['field']*10
    ptemp={'score':int(bowlscore)}
    p.update(ptemp)
    pnew={'name':p['name'],'score':p['score']}
    print(pnew)
    return

def ba_or_bo(p):
    if p['role']=='bat':
        batting(p)
    else:
        bowling(p)
    return


def top_p(lst):
    maxx=lst[0]['score']
    for i in lst[1:5]:
        if(i['score']>maxx):
            maxx=i['score']
            top=i

    return top
        
        
    


    
