import csv
import requests
import os
from dotenv import load_dotenv

load_dotenv('.env')

Key = os.getenv('API')

URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=IBM&interval=1min&slice=year1month1&apikey={}'.format(Key)

with requests.Session() as s:
    downloaded = s.get(URL)
    decoded_content = downloaded.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    for row in my_list:
        print(row)