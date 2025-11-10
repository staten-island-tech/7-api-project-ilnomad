import requests

def skyblock(skyblock):
    response = requests.get(f"https://api.hypixel.net/v2/skyblock/bazaar")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    print(data)
    c=0
    for b in data:
        c+=1
        for h in data[c]["products"]:
            y=0
            for i in data[c]["products"][y]:
                return{
                    "quick_status": data["products"][y]["quick_status"]
        }
            y+=1

skyblock(363463456)