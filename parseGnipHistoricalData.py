import os,json
#place all the json files in this folder
path = "C:\\<folder>\\<subfolder>\\"
filelist=os.listdir(path)

#list of data to be parsed 
header=["displayName","summary","postedTime","body","friendsCount","followersCount","listedCount","statusesCount"
       ,"klout_score","country","countryCode","locality","region","subRegion"]

out=open("gnipFinalOutput5.xls","w")
out.write("\t".join(header))
out.write("\n")
for file1 in filelist:
    data = []
    with open(path+file1) as f:
        for line in f:
            if len(line.replace("\n",""))>0:
                data.append(json.loads(line))
        for row in data:
            try:
                id=row["id"].encode("ascii","ignore")
            except:
                id=""
            try:
                summary=""+row["actor"]["summary"].encode("ascii","ignore")
            except:
                summary=""
            try:
                friendsCount=str(row["actor"]["friendsCount"]).encode("ascii","ignore")
            except:
                friendsCount=""
            try:
                followersCount=str(row["actor"]["followersCount"]).encode("ascii","ignore")
            except:
                followersCount=""
            try:
                listedCount=str(row["actor"]["listedCount"]).encode("ascii","ignore")
            except:
                listedCount=""
            try:
                statusesCount=str(row["actor"]["statusesCount"]).encode("ascii","ignore")
            except:
                statusesCount=""
            try:
                displayName=row["actor"]["displayName"].encode("ascii","ignore")
            except:
                displayName=""
            try:
                postedTime=row["postedTime"].encode("ascii","ignore")
            except:
                postedTime=""
            try:
                body=row["body"].encode("ascii","ignore")
            except:
                body=""
            try:
                actorname=row["actor"]["preferredUsername"].encode("ascii","ignore")
            except:
                actorname=""
            #try:
            #    symbols="%%".join(row["twitter_entities"]["symbols"]).encode("ascii","ignore")
            #except:
            #    symbols=""
            try:
                klout_score=str(row["gnip"]["klout_score"]).encode("ascii","ignore")
            except:
                klout_score=""
            try:
                country=row["gnip"]["profileLocations"][0]["address"]["country"].encode("ascii","ignore")
            except:
                country=""
            try:
                countryCode=row["gnip"]["profileLocations"][0]["address"]["countryCode"].encode("ascii","ignore")
            except:
                countryCode=""
            try:
                locality=row["gnip"]["profileLocations"][0]["address"]["locality"].encode("ascii","ignore")
            except:
                locality=""
            try:
                region=row["gnip"]["profileLocations"][0]["address"]["region"].encode("ascii","ignore")
            except:
                region=""
            try:
                subRegion=row["gnip"]["profileLocations"][0]["address"]["subRegion"].encode("ascii","ignore").encode("ascii","ignore")
            except:
                subRegion=""
            outlist=[eval(i).replace("\n","").replace("\r","").replace("\r\n","").replace("\t","") for i in header]
            #print outlist
            if(len(displayName)>1):
                out.write("\t".join(outlist)+"\n")
    print file1, " converted successfully"
out.close()
