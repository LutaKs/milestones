import requests
import sys
from typing import Dict, List

months = {1: "january", 2 : "february", 3: "march", 4: "april", 5: "may", 6 : "june",
          7: "july", 8: "august", 9: "september", 10: "october", 11: "november", 12: "december"}

def get_birthdays(month: str, dep: str) -> List[Dict[str, str]]:
    result = []
    url = f"http://127.0.0.1:5000/birthdays?month={month}&department={dep}"
    resp = requests.get(url)
    json_resp = resp.json()
    result = json_resp if resp.status_code == 200 else {}
    return result

def get_anniversaries(month: str, dep: str) -> List[Dict[str, str]]:
    result = []
    url = f"http://127.0.0.1:5000/anniversaries?month={month}&department={dep}"
    resp = requests.get(url)
    json_resp = resp.json()
    
    result = json_resp if resp.status_code == 200 else {}
    return result


month = sys.argv[1]
dep = sys.argv[2]
api = sys.argv[3]


if api == "birthday":
    result = get_birthdays(month, dep)
elif api == "anniversary":
    result = get_anniversaries(month, dep)

res = f"Report for Engineering department for {month} fetched\n"
res += f"Total: {len(result)}\n"
res += "Employees:\n"
for employee in result:
    res += " - " + (employee[2] if api == "birthday" else employee[3]) + ", " + employee[1] + "\n"
print(res)