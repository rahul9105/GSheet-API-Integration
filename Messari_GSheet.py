from googleapiclient.discovery import build
from google.oauth2 import service_account
import requests
import pandas as pd
from time import sleep

def update():
    # Requesting Data from Website
    r = requests.get(r'https://data.messari.io/api/v1/assets?fields=id,name,slug,symbol,metrics&limit=805')
    # Converting data to json
    data = r.json()

    # Extracting data into python dictionary
    value_dic = {
        'Name':[],
        'Symbol':[],
        'Sector':[],
        'Price USD':[],
    }
    for i in range(len(data['data'])):
        value_dic['Name'].append(data['data'][i]['name'])
        value_dic['Symbol'].append(data['data'][i]['symbol'])
        if data['data'][i]['metrics']['misc_data']['sectors'] is not None:
            value_dic['Sector'].append(data['data'][i]['metrics']['misc_data']['sectors'][0])
        else:
            value_dic['Sector'].append('NA')
        value_dic['Price USD'].append(data['data'][i]['metrics']['market_data']['price_usd'])
    
    # creating a Pandas dataframe
    df = pd.DataFrame(value_dic)

    # Filling missing values
    df.fillna('NA',inplace=True)

    # Data format conversion for GSheet Upload
    l = []
    l.append(df.columns.tolist())
    for i in range(len(df)):
        l.append(df.iloc[i,:].values.tolist())

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
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sheet1!A1",valueInputOption="USER_ENTERED", body={'values':l})
    request.execute()
    print('Sheet Updated')

# Looping for live update.
while True:
    update()
    sleep(90)