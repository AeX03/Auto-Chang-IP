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
                                                                                
                                                                                
                                             :: ..                              
                                            r..7r.                              
                                         ::Yrrs.                                
                                        .JrvL:                                  
                                        7r7r.                                   
                                     . :7ri                                     
                                     vr:ri                                      
                                     .i .Lr                                     
                                     .v rPY                                     
                                   .iv ..7QJ                                    
                                 .rr.  Lv IBQJ.                                 
                               .7i    i D  uBBBE:                               
                              vr    ::  .i  KBBBBK.                             
                            .j.   :.   :v i :BBQBBE:                            
                            Y   :.    i:D  . XBQQBBU.                           
                           .L  i    ::   r . vBBQQBQr                           
                           :Y .:  :i   .r : iiBBBQBMr                           
                           .v :. .:   .jQ ::JiQBBBQDr                           
                            u  i s   .i 2. 1XiRMBQBJr                           
                            :Y ..:   r  r .D:vQBDBDr.                           
                             iY ..i  :. v v2:RBBB2r                             
                              .7..i7  . 7ir:LBBDL:                              
                                .isuv:.rJri77vr.                                
        .                      ... .iXv...:r.:....                              
        Lr       .           ...7r .vMg7. .L:  r:.:               .   .L:       
          r. :Y: i7         .s.Jv7vu j522ir..vi:7:rr.        :v  rL  7r         
          iXJ.:v7:r.:j..QUY. :YLrj7 .: .Lvi1  5vs77. :JKs :L...77:.:11:         
      .7.:7g7 r :: ::rI:uv .:i:  .r :i. EB S ir: .:i:  2:rj:.. Y .: Pr7..v      
        .5.::  .r :i v  : i1u. .B  Y.r7 XB..:: rL  i1v. . .: r .r.  J iv        
            ... :i   .i.i:.:  2PB1. 7P :.U.1. i2rU: i. i.r.. ..v. .i            
            :v:   J.:rP.i7 : .Mb..   i q  ..  . rPd : .:i.r:.r:   i7            
              i7:.v:si.7::7S.:2  r:.i i.v ..i :. vJ rv.r:i 7:r7 i7 .            
              :r.:7irr  Ii.. BQi. :   r 2:i :7. .:Bi .:ji .r.Li..7  .           
        .i.Ru  :1r i. 7.iX   S:rI:. U5Z :.i.7 iLr.L7  :r.:i .. Er. .Ei:7        
            .ri:  r..i1::5::r: i:i ..rB:..  vYr::Y.ii.irrr5..Y. .1ri   .        
           ir:iL .P . i r2rL.:v. .r7 :2..: 1:r. .:  U.Yj: v  v5  P:.7.          
           7v  7Pr. .:v :..  7:. :rY  i...::... is::  :.:.U. r:Pv.  u.          
          vQY 7..i  . J: ..: r: :E s: :P7. :i.:. v:: :  :7i .  5 r: ZLr         
            .        i7 S7.  r:..L s:i . .v:.: .1:  : .IL 5         :           
                  i77Q  Li:  r::.u  .    .ii J .: Y::i:Yr .B:U.                 
                7:LU  .. . .7:r .   r:..  :.  .rr 7  .r. .. .X:7:               
                  i  7d  :r. :r.. i7Xi:r  rJ  i ir.:Yi i .5  :.                 
                  i v..iv    .J:  Lig.   i5:i:. i  : . .J. 7:.:                 
                  r7:7      :  I.  r:  ij   :  BX.i:r.    ir:J:                 
                  :   .     :.Kq.  :     v. P1ZX .. ..    :  ..                 
                            ::v:i7      .ir.. v5                                
                             .K  .     iB2:                                     
                            i:7:       i..:.                                    
                                           .                                                       
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