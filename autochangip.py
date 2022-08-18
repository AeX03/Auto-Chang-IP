import time
import os
import subprocess




try:
    check_pip3 = subprocess.check_output('dpkg -s python3-pip', shell=True)
    if str('install ok installed') in str(check_pip3):
        pass
except subprocess.CalledProcessError:
    print('[+] pip3 not installed')
    subprocess.check_output('sudo apt update',shell=True)
    subprocess.check_output('sudo apt install python3-pip -y', shell=True)
    print('[!] pip3 installed succesfully')



try:

    import requests
except Exception:
    print('[+] python3 requests is not installed')
    os.system('pip3 install requests')
    os.system('pip3 install requests[socks]')
    print('[!] python3 requests is installed ')
try:

    check_tor = subprocess.check_output('which tor', shell=True)
except subprocess.CalledProcessError:

    print('[+] tor is not installed !')
    subprocess.check_output('sudo apt update',shell=True)
    subprocess.check_output('sudo apt install tor -y',shell=True)
    print('[!] tor is installed succesfully ')

os.system("clear")
def ma_ip():
    url='https://www.myexternalip.com/raw'
    get_ip= requests.get(url,proxies=dict(http='socks5://127.0.0.1:9050',https='socks5://127.0.0.1:9050'))
    return get_ip.text

def change():
    os.system("service tor reload")
    print ('[+] Your IP has been Changed to : '+str(ma_ip()))

print('''\033[1;32;40m \n

@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@&PPG#@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@Y!?G&@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@#P~5&@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@PB5P@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@&#GB&GJPB&@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@&GB#&&&&BY55P#@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@BG&&&&@&#&55P5JG@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@5@#&&&@&#&PJPP57&@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@5&#&&@&###Y?PPY7&@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@BP#B#@#&BP?YPY?G@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@&BP5PGPY7JYYP&@@@@@@@@@@@@@@@@@@
@@@@@#@@&@@@@@@@@@&#BBPPP5PGGB#&@@@@@@@@@&@@#@@@@@
@@@@@&B#####&&&#&#GGGB##BG##BGGG#&#&&&#####B&@@@@@
@@@@&#BB&####BBB#B#BB#BB#GBBBBB#B#BBB&&##&BB#&@@@@
@@@@@@@&B&#B#GBB##BPB#####G###GB####B#B#&B#@@@@@@@
@@@@@@@&&B#BGB#B##GGB#########GG##B#BGB#B&&@@@@@@@
@@@@@&&B#B###B#BG#BBB&BG###BBBB##BBBB###B#B&&@@@@@
@@@@@@&B#BB##B#BB#B##B#BB#BB#&B#BBB###BBB#B&@@@@@@
@@@@@@##&&&@&BBB##B###B&##BBB#B###GBB&@&&&&#@@@@@@
@@@@@@@@@@&BBB&B##GB#&#&@@G##B#B#BB&B#B&@@@@@@@@@@
@@@@@@@@@@@##B#&&&BB&#G&&#G####BB&&#B#B@@@@@@@@@@@
@@@@@@@@@@@&&&@@@#BB&&#@&B#B#B#&&&@@&&&@@@@@@@@@@@
@@@@@@@@@@@@@@@@@&B#&@@@#G#@&&@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@&&&@@@&#@&@@@@@@@@@@@@@@@@@@@@@@@                                                      
''')
print("\033[1;40;31m GitHub : Aex03 \n")

os.system("service tor start")




time.sleep(3)
print("\033[1;32;40m change your  SOCKES to 127.0.0.1:9050 \n")
os.system("service tor start")
x = input("[+] Time to change Ip in Sec [Max=60] >> ")
lin = input("[+] How many time do you want to change your ip ? for infinte ip change type [0] >>")
if int(lin) ==int(0):

	while True:
		try:
			time.sleep(int(x))
			change()
		except KeyboardInterrupt:

		 	print('\nauto tor is closed ')
		 	quit()

else:
	for i in range(int(lin)):
		    time.sleep(int(x))
		    change()
