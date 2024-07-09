import requests
import json

api_key = "RGAPI-16c91d72-6e97-4403-84b2-63d3eca4df02"

def main():
    region = getRegion()
    tagLine = str(gettagline())
    gameName = getgameName()
    url = f"https://{region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}?api_key=RGAPI-16c91d72-6e97-4403-84b2-63d3eca4df02"
    r = requests.get(url)
    print(r.json())


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

if __name__ == "__main__":
    main()