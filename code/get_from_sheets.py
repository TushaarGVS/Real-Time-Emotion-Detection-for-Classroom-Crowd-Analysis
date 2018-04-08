import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open_by_key("1rVQwbYUUOhvvQeXoKHEjn2Mct8uj3fr2_jqizlJpnMM").sheet1

list_of_hashes = sheet.get_all_records()
numRows = len(list_of_hashes)

print sheet.row_values(numRows + 1)
