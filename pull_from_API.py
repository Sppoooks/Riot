import requests
import json

api_key = "RGAPI-2262acdd-a433-4f1c-87d2-3393910671bc"


def getMatchInfo(MatchNumber = 0):
    LoadMatches = getMatchHistory()
    MatchID = LoadMatches[MatchNumber]
    print(MatchID)
    url = f"{api_endpoint}/lol/match/v5/matches/{MatchID}?api_key={api_key}"
    response = requests.get(url)
    MatchData = json.load(response.json())
    file = open("MatchInfo.json", "w+")
    file.write(MatchData)

def getMatchHistory(start = 0, count = 20):
    puuid = getPUUID()
    url = f"{api_endpoint}/lol/match/v5/matches/by-puuid/{puuid}/ids?start={start}&count={count}&api_key={api_key}"
    MatchHistory = requests.get(url)
    return MatchHistory.json()
    

def getPUUID():
    tagLine = str(gettagline())
    gameName = getgameName()
    url = f"{api_endpoint}/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}?api_key={api_key}"
    r = requests.get(url)
    puuid = r.json().get("puuid")
    print(f"PUUID: {puuid}")
    return puuid


def getRegion():
    r = input("Select region: \n1. Americas\n2. Asia\n3. Europe\n")
    match r:
        case "1":
            return "americas"
        case "2":
            return "asia"
        case "3":
            return "europe"

def gettagline():
    return input("Tagline: ")

def getgameName():
    return input("gameName: ")

region = getRegion()
api_endpoint = f"https://{region}.api.riotgames.com"


if __name__ == "__main__":
    getMatchInfo()