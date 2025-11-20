import requests

def puzzle():
    response = requests.get("https://lichess.org/api/puzzle/daily")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    data = response.json()
    return{
        "Gamemode": data["game"]["perf"]["name"],
        "Clock": data["game"]["clock"],
        "Solution": data["puzzle"]["solution"],
        "PGN": data["game"]["pgn"]
    }
print(puzzle())