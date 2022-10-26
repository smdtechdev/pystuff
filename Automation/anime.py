import json

filename = "Automation\\files\\sample.txt"

with open(filename) as f:
    mylist = f.read().splitlines() 
print(mylist)

myDict = {}

for i in range(len(mylist)):
    
    if len(myDict) > 0:
        tmpDict = {f'{mylist[i]}':{"addPaused":"null", "affectedFeeds": ["https://subsplease.org/rss/?r=1080"], "assignedCategory": "", "enabled": "true", 
                   "episodeFilter": "", "ignoreDays": 0,"lastMatch": "","mustContain": f"{mylist[i]}","mustNotContain": "","previouslyMatchedEpisodes": [],
                   "savePath": f"/home/macbot/Downloads/Zone/anime/{mylist[i]}","smartFilter": "false","torrentContentLayout": "null","useRegex": "false" }}
        myDict.update(tmpDict)
    else:
        myDict = {f'{mylist[i]}':{"addPaused":"null", "affectedFeeds": ["https://subsplease.org/rss/?r=1080"], "assignedCategory": "", "enabled": "true", 
                   "episodeFilter": "", "ignoreDays": 0,"lastMatch": "","mustContain": f"{mylist[i]}","mustNotContain": "","previouslyMatchedEpisodes": [],
                   "savePath": f"/home/macbot/Downloads/Zone/anime/{mylist[i]}","smartFilter": "false","torrentContentLayout": "null","useRegex": "false" }}
    
print(json.dumps(myDict))

with open('json_data.json', 'w') as outfile:
    json.dump(myDict, outfile, indent=4)
