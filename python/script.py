import json


text_file = open("data.txt", "r", encoding="utf8")
r = text_file.read()
text_file.close()

r = json.loads(r) 

u = 0
while r[u].get("zoneName") != "Gironde":
    u+=1

#print(type(r[0]),len(r[0]),r[3].get("zoneName"))
#T = []

text_file = open("names.txt", "w")
rank = 0
URL = ["https://matchmaking.trackmania.nadeo.club/api/matchmaking/2/leaderboard/players?"]
o = 0
u=0
for i in range(len(r[0].get('players'))):
    u+=1
    #["Pseudo", "AccountID", "points""]
    #T += [[r[u].get('players')[i].get('nameOnPlatform'), r[u].get('players')[i].get('accountId'), r[u].get('players')[i].get('points')]]
    rank += 1 
    data = ["Pseudo :",r[0].get('players')[i].get('nameOnPlatform'),"AccountID :", r[0].get('players')[i].get('accountId'),"Total points :", r[0].get('players')[i].get('points'),"Rank :", rank]
    #print(type(URL[o]),rank)
    URL[o] = str(URL[o]+"&players[]="+str(data[3]))

    if u>=150:
        o += 1
        URL.append("https://matchmaking.trackmania.nadeo.club/api/matchmaking/2/leaderboard/players?")
        u=0
    
    n = text_file.write(str(data))
    n = text_file.write("\n")

for l in range(len(URL)):
    n = text_file.write(str(URL[l]))
    n = text_file.write("\n""\n")
    
text_file.close()


    
#for i in range(len(r[0].get('players'))):
    
    #print("Pseudo :",r[u].get('players')[i].get('nameOnPlatform'),"AccountID :", r[u].get('players')[i].get('accountId'),"Total points :", r[u].get('players')[i].get('points'))

    
#print(T)
