import gzip
import json
from typing import Dict
def loadJson() ->  Dict[str, Dict[str, str]]:
    ans = {}
    with gzip.open("jawiki-country.json.gz") as f:
        for l in f:
            js = json.loads(l)
            title = js["title"]
            ans[title] = js
    return ans
