from googleapiclient.discovery import build
from google.oauth2 import service_account
import requests
import pandas as pd
from time import sleep

def update():
    # Requesting Data from Website and storing them in a list
    data_lst=[]
    for i in range(29):
        r1=requests.get(f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page={i+1}&sparkline=false&price_change_percentage=1h%2C24h%2C7d%2C1y')
        data1=r1.json()
        data_lst.append(data1)
        
    # Initializing a dictionary for storing values.
    value={
        'name': [],
        'symbol': [],
        'current_price': [],
        'market_cap': [],
        'market_cap_rank': [],
        'fully_diluted_valuation': [],
        'total_volume': [],
        'high_24h': [],
        'low_24h': [],
        'price_change_24h': [],
        'price_change_percentage_24h': [],
        'market_cap_change_24h': [],
        'market_cap_change_percentage_24h': [],
        'circulating_supply': [],
        'total_supply': [],
        'max_supply':[],
        'ath': [],
        'ath_change_percentage': [],
        'ath_date': [],
        'atl': [],
        'atl_change_percentage':[],
        'atl_date':[],
        'roi': [],
        'last_updated': [],
        'price_change_percentage_1h_in_currency':[],
        'price_change_percentage_24h_in_currency': [],
        'price_change_percentage_7d_in_currency':[],
        'price_change_percentage_1y_in_currency':[]
    }

    # Storing data in dictionary
    for l in range(29):
        for i in range(len(data_lst[0])):
            value['name'].append(data_lst[l][i]['name'])
            value['symbol'].append(data_lst[l][i]['symbol'])
            value['current_price'].append(data_lst[l][i]['current_price'])
            value['market_cap'].append(data_lst[l][i]['market_cap'])
            value['market_cap_rank'].append(data_lst[l][i]['market_cap_rank'])
            value['fully_diluted_valuation'].append(data_lst[l][i]['fully_diluted_valuation'])
            value['total_volume'].append(data_lst[l][i]['total_volume'])
            value['high_24h'].append(data_lst[l][i]['high_24h'])
            value['low_24h'].append(data_lst[l][i]['low_24h'])
            value['price_change_24h'].append(data_lst[l][i]['price_change_24h'])
            value['price_change_percentage_24h'].append(data_lst[l][i]['price_change_percentage_24h'])
            value['market_cap_change_24h'].append(data_lst[l][i]['market_cap_change_24h'])
            value['market_cap_change_percentage_24h'].append(data_lst[l][i]['market_cap_change_percentage_24h'])
            value['circulating_supply'].append(data_lst[l][i]['circulating_supply'])
            value['total_supply'].append(data_lst[l][i]['total_supply'])
            value['max_supply'].append(data_lst[l][i]['max_supply'])
            value['ath'].append(data_lst[l][i]['ath'])
            value['ath_change_percentage'].append(data_lst[l][i]['ath_change_percentage'])
            value['ath_date'].append(data_lst[l][i]['ath_date'])
            value['atl'].append(data_lst[l][i]['atl'])
            value['atl_change_percentage'].append(data_lst[l][i]['atl_change_percentage'])
            value['atl_date'].append(data_lst[l][i]['atl_date'])
            value['last_updated'].append(data_lst[l][i]['last_updated'])
            value['price_change_percentage_1h_in_currency'].append(data_lst[l][i]['price_change_percentage_1h_in_currency'])
            value['price_change_percentage_24h_in_currency'].append(data_lst[l][i]['price_change_percentage_24h_in_currency'])
            value['price_change_percentage_7d_in_currency'].append(data_lst[l][i]['price_change_percentage_7d_in_currency'])
            value['price_change_percentage_1y_in_currency'].append(data_lst[l][i]['price_change_percentage_1y_in_currency'])
            try:
                value['roi'].append(data_lst[l][i]['roi']['percentage'])
            except TypeError:
                value['roi'].append(None)
    # Converting to dataframe
    df1=pd.DataFrame(value)
    r2=requests.get(f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=30&sparkline=false&price_change_percentage=1h%2C24h%2C7d%2C1y')
    data2=r2.json()
    value1={
        'name': [],
        'symbol': [],
        'current_price': [],
        'market_cap': [],
        'market_cap_rank': [],
        'fully_diluted_valuation': [],
        'total_volume': [],
        'high_24h': [],
        'low_24h': [],
        'price_change_24h': [],
        'price_change_percentage_24h': [],
        'market_cap_change_24h': [],
        'market_cap_change_percentage_24h': [],
        'circulating_supply': [],
        'total_supply': [],
        'max_supply':[],
        'ath': [],
        'ath_change_percentage': [],
        'ath_date': [],
        'atl': [],
        'atl_change_percentage':[],
        'atl_date':[],
        'roi': [],
        'last_updated': [],
        'price_change_percentage_1h_in_currency':[],
        'price_change_percentage_24h_in_currency': [],
        'price_change_percentage_7d_in_currency':[],
        'price_change_percentage_1y_in_currency':[]
    }

    for i in range(len(data2)):
        value1['name'].append(data2[i]['name'])
        value1['symbol'].append(data2[i]['symbol'])
        value1['current_price'].append(data2[i]['current_price'])
        value1['market_cap'].append(data2[i]['market_cap'])
        value1['market_cap_rank'].append(data2[i]['market_cap_rank'])
        value1['fully_diluted_valuation'].append(data2[i]['fully_diluted_valuation'])
        value1['total_volume'].append(data2[i]['total_volume'])
        value1['high_24h'].append(data2[i]['high_24h'])
        value1['low_24h'].append(data2[i]['low_24h'])
        value1['price_change_24h'].append(data2[i]['price_change_24h'])
        value1['price_change_percentage_24h'].append(data2[i]['price_change_percentage_24h'])
        value1['market_cap_change_24h'].append(data2[i]['market_cap_change_24h'])
        value1['market_cap_change_percentage_24h'].append(data2[i]['market_cap_change_percentage_24h'])
        value1['circulating_supply'].append(data2[i]['circulating_supply'])
        value1['total_supply'].append(data2[i]['total_supply'])
        value1['max_supply'].append(data2[i]['max_supply'])
        value1['ath'].append(data2[i]['ath'])
        value1['ath_change_percentage'].append(data2[i]['ath_change_percentage'])
        value1['ath_date'].append(data2[i]['ath_date'])
        value1['atl'].append(data2[i]['atl'])
        value1['atl_change_percentage'].append(data2[i]['atl_change_percentage'])
        value1['atl_date'].append(data2[i]['atl_date'])
        value1['last_updated'].append(data2[i]['last_updated'])
        value1['price_change_percentage_1h_in_currency'].append(data2[i]['price_change_percentage_1h_in_currency'])
        value1['price_change_percentage_24h_in_currency'].append(data2[i]['price_change_percentage_24h_in_currency'])
        value1['price_change_percentage_7d_in_currency'].append(data2[i]['price_change_percentage_7d_in_currency'])
        value1['price_change_percentage_1y_in_currency'].append(data2[i]['price_change_percentage_1y_in_currency'])        
        try:
            value1['roi'].append(data2[i]['roi']['percentage'])
        except TypeError:
            value1['roi'].append(None)
    df2=pd.DataFrame(value1)       
    frames = [df1,df2]
    result = pd.concat(frames,ignore_index=True)
    result.fillna('NA',inplace=True)

    # Data format conversion for GSheet Upload
    l1 = []
    l1.append(result.columns.tolist())
    for i in range(len(result)):
        l1.append(result.iloc[i,:].values.tolist())

    # GSheet Upload settings and config
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SERVICE_ACCOUNT_FILE = r'keys.json'
    creds=None
    creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    SAMPLE_SPREADSHEET_ID = 'Spreadsheet ID to be entered'
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API and upload data
    sheet = service.spreadsheets()
    request2 = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sheet1!A1",valueInputOption="USER_ENTERED", body={'values':l1})
    request2.execute()
    print('Sheet Updated')

# Looping for live update.
while True:
    update()
    sleep(30)