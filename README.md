<p align="center">
<img src="https://github.com/AeX03/Auto-Chang-IP/blob/main/picture/Auto-Chang-IP.png" width="200"/>


# Auto-Chang-IP
🌐 - Change your IP address with the Tor gateway

[![license](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://github.com/AeX03/Auto-Chang-IP)
[![version](https://img.shields.io/badge/version-1.0-blue.svg)](https://github.com/AeX03/Auto-Chang-IP)
[![Discord](https://img.shields.io/discord/979349329909264414?label=Discord&logo=Discord)](http://discord.gg/xpaxKBEx9t)
<br>
[![eLys](https://img.shields.io/badge/Site-eLys-pink.svg)](https://eLysiane.eu/)
[![Tornado](https://img.shields.io/badge/NOVA-Tornado%20Cash-brightgreen.svg)](https://img.shields.io/badge/-available%20/09/2022-lightgrey)
<p align="center">

## Tested on
- [x] Kali Linux 2022
- [x] Ubuntu 2022

### Installation Using Sudo SU
  <table width="100%" style="width:100%; display:table;">
 <thead>
  <tr>
   <th width="50%" style="width:50%;">Linux ROOT</th>
      </tr>
 </thead>
 <tbody style="vertical-align: bottom;">
  <tr>
   <td>
     <div class="highlight highlight-source-shell"><pre># Update & Upgrade
sudo apt update -y && sudo apt upgrade -y
     <div class="highlight highlight-source-shell"><pre># Get the Auto Chang IP
git clone https://github.com/aex03/auto-chang-ip</pre></div>
     <div class="highlight highlight-source-shell"><pre># Install tor
sudo apt-get install tor</pre></div>
<div class="highlight highlight-source-shell"><pre># Start the Auto Chang IP
Python3 autochangip.py</pre></div>
        </td>
  </tr>
 </tbody>
</table>

# Change your SOCKS5 !

<b>Firefox<b> 
go to settings > general > (all down) network setting > manual proxy configuration > (socks host) 127.0.0.1 > (port) 9050 > (enable) socksv5 > (enable) proxy dns socksv5
<br>
<b>Chrome, Edge Etc...<b> 
go to settings > (search bar and type "Proxy") > (select) Open your computer’s proxy settings > manual proxy configuration > (enable) Use a proxy server > (socks host "Address") 127.0.0.1 > (port) 9050 > (use a proxy server "write") *.local > (enable) don't use the proxy server for local

