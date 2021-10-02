import os
import urllib.parse
import json
dct = {
    'Customer ID': 'Brendan',
    'Name': 'Brendan Cheong Ern Jie'
}
dict1 = urllib.parse.quote(json.dumps(dct))
os.system(f"cd GUI/MainUI && python main.py {dict1}")
