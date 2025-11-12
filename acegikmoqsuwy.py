import requests

def skyblock(skyblock):
    response = requests.get(f"https://api.hypixel.net/v2/skyblock/bazaar")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    data = response.json()
    lastUpdated=skyblock
    print(data)
    c=0
    for b in data:
        for h in data[c]["lastUpdated"]["products"]:
            y=0
            for i in data[c]["lastUpdated"]["products"][y]:
                return{
                    data["lastUpdated"][y]["quick_status"]
                }
            y+=1
        c+=1

skyblock(5757575756)