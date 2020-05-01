
def getFormattedString(x:int, y:str, z) -> str:
    return f"{x}時の{y}は{z}"

if __name__ == "__main__":
    print(getFormattedString(12, "気温", 22.4))