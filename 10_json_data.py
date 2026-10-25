"""
Working with JSON Data using the json Module
============================================
Corey Schafer - Python Tutorial

The four functions to remember (the trailing "s" means "string"):

    json.loads(str)  -> Python object   (parse a JSON STRING)
    json.load(file)  -> Python object   (parse a JSON FILE)
    json.dumps(obj)  -> str             (serialise to a JSON STRING)
    json.dump(obj, f)                   (serialise to a JSON FILE)

JSON -> Python type mapping:
    object -> dict      array -> list      string -> str
    number -> int/float true/false -> True/False    null -> None

Covers:
    * Parsing a JSON string and navigating the resulting dict/list
    * Pretty-printing with indent= and sort_keys=
    * Reading a JSON file, modifying the data, writing a new file
    * Fetching live JSON from a web API with urllib

Input:   data/states.json
Output:  output/new_states.json  (area codes removed)

Run:
    python 10_json_data.py
"""

import json
from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

# ---------------------------------------------------------------------------
# 1. JSON string -> Python object  (json.loads)
# ---------------------------------------------------------------------------
people_string = """
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7165",
            "emails": ["js@gmail.com", "jswork@work-place.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "650-555-7165",
            "emails": null,
            "has_license": true
        }
    ]
}
"""

data = json.loads(people_string)
print(data)
print(type(data))  # <class 'dict'>  - the top-level {} became a dict
print(type(data["people"]))  # <class 'list'>  - the [] became a list

for person in data["people"]:
    print(person["name"])

# ---------------------------------------------------------------------------
# 2. Python object -> JSON string  (json.dumps)
# ---------------------------------------------------------------------------
# Strip the phone numbers, then serialise. indent= pretty-prints and
# sort_keys= orders keys alphabetically for a stable, readable output.
for person in data["people"]:
    del person["phone"]

new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)

# ---------------------------------------------------------------------------
# 3. JSON file -> Python object  (json.load)
# ---------------------------------------------------------------------------
with open(DATA_DIR / "states.json") as f:
    data = json.load(f)

for state in data["states"]:
    print(state)

for state in data["states"]:
    print(state["name"], state["abbreviation"])

# ---------------------------------------------------------------------------
# 4. Python object -> JSON file  (json.dump)
# ---------------------------------------------------------------------------
for state in data["states"]:
    del state["area_codes"]

with open(OUTPUT_DIR / "new_states.json", "w") as f:
    json.dump(data, f, indent=2)

# ---------------------------------------------------------------------------
# 5. JSON from a web API
# ---------------------------------------------------------------------------
# Frankfurter is a free exchange-rate API. The v2 endpoint returns a LIST of
# records like {"date": "...", "base": "USD", "quote": "INR", "rate": 83.1}.
url = "https://api.frankfurter.dev/v2/rates?base=USD"

# Some servers reject requests without a browser-like User-Agent header.
request = Request(
    url,
    headers={
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
    },
)

try:
    # urlopen() returns a file-like object, so json.load() works on it directly.
    with urlopen(request, timeout=20) as response:
        data = json.load(response)
except URLError as e:
    # No network, DNS failure, timeout, etc. Don't crash the whole lesson.
    print(f"Could not reach {url}: {e}")
else:
    # print(json.dumps(data, indent=2))   # uncomment to see the raw payload

    print(len(data))  # number of currency pairs returned

    # Build a lookup like {"USDINR": 83.1, "USDEUR": 0.92, ...}
    usd_rates = {}

    for item in data:
        date = item["date"]
        rate = item["rate"]
        base = item["base"]
        quote = item["quote"]
        print(date, rate)
        usd_rates[base + quote] = rate

    print(usd_rates["USDINR"])

    # Convert 50 USD into INR and EUR.
    print(50 * float(usd_rates["USDINR"]))
    print(50 * float(usd_rates["USDEUR"]))


"""
Expected output (abridged - live rates will differ)
---------------------------------------------------
{'people': [{'name': 'John Smith', 'phone': '615-555-7165', 'emails': [...], 'has_license': False}, {...}]}
<class 'dict'>
<class 'list'>
John Smith
Jane Doe
{
  "people": [
    {
      "emails": [
        "js@gmail.com",
        "jswork@work-place.com"
      ],
      "has_license": false,
      "name": "John Smith"
    },
    {
      "emails": null,
      "has_license": true,
      "name": "Jane Doe"
    }
  ]
}
{'name': 'Alabama', 'abbreviation': 'AL', 'area_codes': ['205', '251', '256', '334', '938']}
...
Alabama AL
Alaska AK
...
165
2026-10-25 3.6725
...
94.76
4738.0
44.5565
"""
