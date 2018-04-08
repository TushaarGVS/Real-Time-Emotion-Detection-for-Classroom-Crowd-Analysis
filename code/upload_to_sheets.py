import gspread
from oauth2client.service_account import ServiceAccountCredentials
import main as m

def recommend(OEV):
    if OEV < 0:
        if OEV > -25:
            return "Go with Interactive Teaching!"
        elif OEV > -50:
            return "A break would go a long way!"
        elif OEV > -75:
            return "It's time to conclude the class!"
        else:
            return "Change the teaching strategy!"
    else:
        if OEV < 25:
            return "Go with Question-Answering strategy!"
        elif OEV < 50:
            return "Class is going fine, so continue!"
        elif OEV < 75:
            return "Class is highly motivated, keep going!"
        else:
            return "The current strategy works best!"

classification, overall_emotion_value, time = m.run()
recommendation = recommend(overall_emotion_value)

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open_by_key("1rVQwbYUUOhvvQeXoKHEjn2Mct8uj3fr2_jqizlJpnMM").sheet1
list_of_hashes = sheet.get_all_records()
lastRow = len(list_of_hashes) + 2
# time, fear, anger, contempt, sadness, disgust, neutral, happy, surprise, Overall Emotion Value, Recommendation
row = [time, classification['fear'], classification['anger'], classification['contempt'], classification['sadness'], classification['disgust'], classification['neutral'], classification['happy'], classification['surprise'], overall_emotion_value, recommendation]

sheet.insert_row(row, lastRow)
