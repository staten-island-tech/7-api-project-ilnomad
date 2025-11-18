import requests

def puzzle(id):
    response = requests.get(f"https://lichess.org/api/puzzle/{id}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    data = response.json()
    return{
        "puzzleid": data["PuzzleId"]
    }
id("00sHx")