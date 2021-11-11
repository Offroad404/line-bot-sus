import requests
import schedule
import time

url = 'https://notify-api.line.me/api/notify'
token = 'RtZzP1dU0dvMbGoIutHaNR0ETzRYyyTpgrAnRYLTzP4'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

def thai():
    msg = 'ภาษาไทย: https://meet.google.com/ees-nmdo-doz?authuser=0'
    r = requests.post(url, headers=headers, data = {'message':msg})
    print (r.text)

def math_01():
    msg = 'จำนวนและพีชคณิต: https://meet.google.com/zop-oxmh-jjv?authuser=0 '
    r = requests.post(url, headers=headers, data = {'message':msg})
    print (r.text)

def eng_teacher():
    msg = 'อังกฤษท่องเที่ยว teacher: https://meet.google.com/rjo-yhuz-zhf?authuser=0 '
    r = requests.post(url, headers=headers, data = {'message':msg})
    print (r.text)

def sci():
    msg = 'วิทยาศาสตร์: https://meet.google.com/pwx-mgxh-xgv?authuser=0 '
    r = requests.post(url, headers=headers, data = {'message':msg})
    print (r.text)

def internet():
    msg = 'อินเทอร์เน็ต: https://meet.google.com/tgy-bcbr-ahi?authuser=0 '
    r = requests.post(url, headers=headers, data = {'message':msg})
    print (r.text)

def HSK():
    msg = 'ติวHSK: https://meet.google.com/hdh-vnni-rno?authuser=0 '
    r = requests.post(url, headers=headers, data = {'message':msg})
    print (r.text)

def SOC():
    msg = 'สังคมศึกษา: https://meet.google.com/guk-cnqn-abm?authuser=0'
    r = requests.post(url, headers=headers, data = {'message':msg})
    print (r.text)

def free():
    msg = 'คาบว่างๆๆๆ'
    r = requests.post(url, headers=headers, data = {'message':msg})
    print (r.text)

def PE():
    msg = 'พละ: https://meet.google.com/iwz-axie-qyx?authuser=0 '
    r = requests.post(url, headers=headers, data = {'message':msg})
    print (r.text)

def Sub():
    msg = 'ชมรม: ---'
    r = requests.post(url, headers=headers, data = {'message':msg})
    print (r.text)

def Art():
    msg = 'ศิลปะ: https://meet.google.com/uas-yaqr-kkc?authuser=0'
    r = requests.post(url, headers=headers, data = {'message':msg})
    print (r.text)

def math_02():
    msg = 'เรขาคณิตและสถิติ: https://meet.google.com/wwj-fwoe-wgd?authuser=0'
    r = requests.post(url, headers=headers, data = {'message':msg})
    print (r.text)

def design():
    msg = 'ออกแบบ: https://meet.google.com/xbd-vtcc-dec?authuser=0'
    r = requests.post(url, headers=headers, data = {'message':msg})
    print (r.text)

def CHN():
    msg = 'ภาษาจีน: https://meet.google.com/hdh-vnni-rno?authuser=0 '
    r = requests.post(url, headers=headers, data = {'message':msg})
    print (r.text)

def eng():
    msg = 'อังกฤษ: https://meet.google.com/ieq-dgkq-fpb?authuser=0'
    r = requests.post(url, headers=headers, data = {'message':msg})
    print (r.text)

def h_work():
    msg = 'การงาน: https://meet.google.com/yft-vksg-thn?authuser=0'
    r = requests.post(url, headers=headers, data = {'message':msg})
    print (r.text)

def PE_02():
    msg = 'สุขศึกษา: https://meet.google.com/eep-xtew-ruk?authuser=0'
    r = requests.post(url, headers=headers, data = {'message':msg})
    print (r.text)

def history():
    msg = 'ประวัติ: https://meet.google.com/yrq-tjbh-itd?authuser=0'
    r = requests.post(url, headers=headers, data = {'message':msg})
    print (r.text)

def info():
    msg = 'แนะแนว: https://meet.google.com/fpt-qmmu-zfy?authuser=0'
    r = requests.post(url, headers=headers, data = {'message':msg})
    print (r.text)


#monday
schedule.every().monday.at("07:55").do(thai)
schedule.every().monday.at("08:55").do(math_01)
schedule.every().monday.at("09:55").do(eng_teacher)
schedule.every().monday.at("10:55").do(sci)
schedule.every().monday.at("12:55").do(internet)
schedule.every().monday.at("13:55").do(HSK)

#tuesday
schedule.every().tuesday.at("07:55").do(math_01)
schedule.every().tuesday.at("08:55").do(SOC)
schedule.every().tuesday.at("09:55").do(sci)
schedule.every().tuesday.at("10:55").do(free)
schedule.every().tuesday.at("12:55").do(PE)
schedule.every().tuesday.at("13:55").do(Sub)

#wednesday
schedule.every().wednesday.at("07:55").do(Art)
schedule.every().wednesday.at("08:55").do(math_02)
schedule.every().wednesday.at("09:55").do(design)
schedule.every().wednesday.at("10:55").do(CHN)
schedule.every().wednesday.at("12:55").do(eng_teacher)

#thursday
schedule.every().thursday.at("07:55").do(eng)
schedule.every().thursday.at("08:55").do(math_01)
schedule.every().thursday.at("09:55").do(thai)
schedule.every().thursday.at("10:55").do(h_work)
schedule.every().thursday.at("12:55").do(SOC)

#friday
schedule.every().friday.at("07:55").do(math_02)
schedule.every().friday.at("08:55").do(sci)
schedule.every().friday.at("09:55").do(PE_02)
schedule.every().friday.at("10:55").do(history)
schedule.every().friday.at("12:55").do(info)


while True:
    schedule.run_pending()
    time.sleep(1)
