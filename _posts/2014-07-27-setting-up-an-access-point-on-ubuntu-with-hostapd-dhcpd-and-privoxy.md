---
title: 'Setting up an access point  on Ubuntu with hostapd, dhcpd and privoxy'
author: Amarnath
layout: post
permalink: /2014/07/setting-up-an-access-point-on-ubuntu-with-hostapd-dhcpd-and-privoxy/
categories:
  - Free software explorations
  - Ubuntu
---
<p id="top" />
This blog post explains how to share internet to your mobile devices from your laptop/PC running GNU/Linux. I am using Ubuntu 14.04 LTS 32 bit OS in this tutorial. Note: Skip step 4, 5 completely in case you do not need privoxy. I have used privoxy to forward my proxy authentication to the chaining proxy server.</p> 

Step 1. Install hostapd, isc-dhcp-server, privoxy.  
`sudo apt-get install hostapd isc-dhcp-server privoxy`
</p>

Step 2. Configure hostapd to setup your WiFi network. Add the following to your `/etc/hostapd/hostapd.conf`.  
`interface=wlan0<br />
driver=nl80211<br />
ssid=YourWifiSSID<br />
hw_mode=g<br />
channel=1<br />
macaddr_acl=0<br />
auth_algs=1<br />
ignore_broadcast_ssid=0<br />
wpa=3<br />
wpa_passphrase=YourPassPhrase<br />
wpa_key_mgmt=WPA-PSK<br />
wpa_pairwise=TKIP<br />
rsn_pairwise=CCMP`

Step 3. Configure your dhcp server (only if you need your wifi have dynamically allocated IPs). Add the following lines to your `/etc/dhcp/dhcpd.conf`.  
`subnet 10.0.0.0 netmask 255.255.255.0 {<br />
range 10.0.0.2 10.0.0.10;<br />
option domain-name-servers 8.8.4.4, 8.8.8.8;<br />
option routers 10.0.0.1;<br />
}`

Step 4. Configure privoxy (optional: needed if your internet is chained to other proxies with authentication).  
Step 4a. Add the following to `/etc/privoxy/config` `listen-address 10.0.0.1:8118` and comment out `listen-address localhost:8118` to open up privoxy server to devices connecting to your wifi network.  
Step 4b. Insert `forward / chaining-proxy-ip-address:port-num` in order to forward everything to the chaining proxy server.  
Step 5. Configure privoxy&#8217;s actions to add HTTP header for proxy authentication. Add the following to your `/etc/privoxy/match-all.action`&#8216;s rules.

`+add-header{Proxy-Authorization: Basic base64-value-username-password} \`.

The easiest method to figure out your base64 value of username/password is use some tool to analyse headers of outgoing HTTP traffic from your browser and pick the value of &#8220;Proxy-Authentication&#8221; key.

Step 6. Trigger the launch of all services. Use the following shell script to do the same. The script takes param1 as the interface where the internet is being shared and param2 as the interface where internet is connected. This enable the machine to forward packets from one interface to another and uses masquerade to do the same.  
`<br />
/etc/init.d/privoxy restart<br />
nmcli nm wifi off<br />
rfkill unblock wlan<br />
ifconfig $1 up 10.0.0.1 netmask 255.255.255.0<br />
sleep 2<br />
#Enable NAT<br />
iptables --flush<br />
iptables --table nat --flush<br />
iptables --delete-chain<br />
iptables --table nat --delete-chain<br />
iptables --table nat --append POSTROUTING --out-interface $2 -j MASQUERADE<br />
iptables --append FORWARD --in-interface $1 -j ACCEPT<br />
sysctl -w net.ipv4.ip_forward=1`

service hostapd restart  
killall dhcpd  
dhcpd $1