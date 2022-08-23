import os
choice = input('[+] to install (Y) to uninstall (N) >> ')
run = os.system
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 777 autochangip.py')
    run('mkdir /usr/share/aut')
    run('cp autoTOR.py /usr/share/aut/autochangip.py')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/aut/autochangip.py "$@"')
    with open('/usr/bin/aut','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/aut & chmod +x /usr/share/aut/autochangip.py')
    print('''\n\ncongratulation auto Tor Ip Changer is installed successfully \nfrom now just type \x1b[6;30;42maut\x1b[0m in terminal ''')
if str(choice)=='N' or str(choice)=='n':
    run('rm -r /usr/share/aut ')
    run('rm /usr/bin/aut ')
    print('[!] now Auto Tor Ip changer  has been removed successfully')
