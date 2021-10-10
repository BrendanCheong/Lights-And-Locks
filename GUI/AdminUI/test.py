import os
import urllib.parse
import json
dct = {
    'Admin ID': 'admin',
    'Name': 'Brendan Cheong Ern Jie'
}
dict1 = urllib.parse.quote(json.dumps(dct))
os.system(f"cd GUI/AdminUI && python main.py {dict1}")
