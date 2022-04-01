import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google API 계정 인증
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('flash-arbor-345908-52dc2cf28500.json', scope)
gc = gspread.authorize(credentials)

# Open WorkSheet
worksheet = gc.open('[PublicAI] FLC_AI 연구소 학생별 수업 참석점검표').worksheet('인공지능의 비밀(달려라 딥레이서)')

# 과목별 이름을 가져옵니다.
subjects = worksheet.row_values(2)[2:]
students = worksheet.col_values(1)[2:]


