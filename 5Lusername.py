import threading
import webbrowser
import random
import datetime
import sys
import requests,pyfiglet
import os
import webbrowser
import time
from cfonts import render 

Ab='\033[1;92m'
aB='\033[1;91m'
AB='\033[1;96m'
aBbs='\033[1;93m'
AbBs='\033[1;95m'
A_bSa = '\033[1;31m'
a_bSa = '\033[1;32m'
faB_s = '\033[2;32m'
a_aB_s = '\033[2;39m'
Ba_bS = '\033[2;36m'
Ya_Bs = '\033[1;34m'
S_aBs = '\033[1;33m'
R = "\033[1;31m"
G = "\033[1;32m"
B = "\033[0;94m"
Y = "\033[1;33m" 
NIKZ = render('{5L User}', colors=['yellow', 'cyan'], align='center')
print(NIKZ)
print ("\033[1;32m Pass Reset Tool By : NikzPy \n JOIN TG - https://t.me/nikzffx        ")
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
F = '\033[1;32m'  # Ø§Ø®Ø¶Ø±
B = "\033[1;30m"  # Black
R = "\033[1;31m"  # Red
G = "\033[1;32m"  # Green
Y = "\033[1;33m"  # Yellow
Bl = "\033[1;34m"  # Blue
P = "\033[1;35m"  # Purple
C = "\033[1;36m"  # Cyan
W = "\033[1;37m"  # White
PN = "\033[1;35m"  # PINK

def to(s):
    for char in s + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(500.0 / 8000)

to(
    f"This Tool Is 5L Username Finder")
print('')
id=input(f"{F} CHAT 𝗜𝗗 ➥ {C}")
token=input(f"{F} 𝗧𝗼𝗸𝗲𝗻 ➥ {C}")
print('\033[32;m')
#------------By @NiKzPy----------------------------------------------
def instaa(SDM):
    url = requests.post('https://www.instagram.com/accounts/web_create_ajax/attempt/', headers={
        'Host': 'www.instagram.com',
        'content-length': '85',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'sec-ch-ua-mobile': '?0',
        'x-instagram-ajax': '81f3a3c9dfe2',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'x-requested-with': 'XMLHttpRequest',
        'x-asbd-id': '198387',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36',
        'x-csrftoken': 'jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
        'sec-ch-ua-platform': '"Linux"',
        'origin': 'https://www.instagram.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.instagram.com/accounts/emailsignup/',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-IQ,en;q=0.9',
        'cookie': 'csrftoken=jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
        'cookie': 'mid=YtsQ1gABAAEszHB5wT9VqccwQIUL',
        'cookie': 'ig_did=227CCCC2-3675-4A04-8DA5-BA3195B46425',
        'cookie': 'ig_nrcb=1' }, data=f'email=aakmnnsjskksmsnsn%40gmail.com&username={SDM}&first_name=&opt_into_one_tap=false')
    if '{"message":"feedback_required","spam":true,"feedback_title":"Try Again Later","feedback_message":"We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.","feedback_url":"repute/report_problem/scraping/","feedback_appeal_label":"Tell us","feedback_ignore_label":"OK","feedback_action":"report_problem","status":"fail"}' in url.text:
        print(W + f' {X} ＥＲＯＲＲ ＵＳＥＲ➳ {X}{SDM}')
    elif '"errors": {"username":' in url.text or '"code": "username_is_taken"' in url.text:
        pass
    else:
        email = 0
        print(W + f''' [+]{F}  Good User :{C} {SDM} ''')
        email += 1
        god=f"""⋘─────━━─────⋙

 USERNAME>> {SDM}


 Join >> @nikzffx
⋘─────━━─────⋙
 𝐁𝐘 :  @NikzPy"""
        requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={god}')
def SDMs():
    ran1 = '1234567890..__qwertyuiopasdfghjklzxvcbnm__..'
    v1 = ''.join(random.choice(insta) for _ in range(1))
    v2 = ''.join(random.choice(insta) for _ in range(1))
    v3 = ''.join(random.choice(insta) for _ in range(1))
    v4 = ''.join(random.choice(insta) for _ in range(1))
    v5 = ''.join(random.choice(all) for _ in range(1))
    SDM1 = v5 + v1 + v2 + v3 + v4
    SDM2 = v1 + v5 + v2 + v3 + v4
    SDM3 = v1 + v2 + v5 + v3 + v4
    SDM4 = v1 + v2 + v3 + v5 + v4
    hamo010 = (SDM1, SDM2, SDM3, SDM4)
    SDM = random.choice(hamo010)
    instaa(SDM)

SDMs()

Threads = []
for t in range(100000000000000):
    x = threading.Thread(target=SDMs)
    x.start()
    Threads.append(x)
for Th in Threads:
    Th.join()
