def loadGBText():
    from section3.loadjson import loadJson
    json = loadJson()
    return json["イギリス"]["text"]

if __name__ == "__main__":
    print(loadGBText())
