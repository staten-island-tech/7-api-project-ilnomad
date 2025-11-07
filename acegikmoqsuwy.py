import requests

def skyblock(skyblock):
    response = requests.get(f"https://api.hypixel.net/?ref=freepublicapis.com#tag/SkyBlock/paths/~1v2~1skyblock~1bazaar/get{poke.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return{
        "sell_summary": data["sell_summary"],
        "buy_summary": data["buy_summary"],
        "quick_status": data["quick_status"],
    }
{
    "success": True,
    "lastUpdated": 1590854517479,
    "products": {
        "INK_SACK:3": {
            "product_id": "INK_SACK:3",
            "sell_summary": [
                {
                    "amount": 20569,
                    "pricePerUnit": 4.2,
                    "orders": 1
                },
                {
                    "amount": 140326,
                    "pricePerUnit": 3.8,
                    "orders": 2
                }
            ],
            "buy_summary": [
                {
                    "amount": 640,
                    "pricePerUnit": 4.8,
                    "orders": 1
                },
                {
                    "amount": 640,
                    "pricePerUnit": 4.9,
                    "orders": 1
                },
                {
                    "amount": 25957,
                    "pricePerUnit": 5,
                    "orders": 3
                }
            ],
            "quick_status": {
                "productId": "INK_SACK:3",
                "sellPrice": 4.2,
                "sellVolume": 409855,
                "sellMovingWeek": 8301075,
                "sellOrders": 11,
                "buyPrice": 4.99260315136572,
                "buyVolume": 1254854,
                "buyMovingWeek": 5830656,
                "buyOrders": 85
            }
        }
    }
}