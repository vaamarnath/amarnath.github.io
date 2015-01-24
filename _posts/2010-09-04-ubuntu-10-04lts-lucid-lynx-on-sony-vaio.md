---
title: Ubuntu 10.04 LTS Lucid Lynx on Sony Vaio
author: Amarnath
layout: post
permalink: /2010/09/ubuntu-10-04lts-lucid-lynx-on-sony-vaio/
jabber_published:
  - 1283590937
email_notification:
  - 1283590939
sp_post_metabox:
  - 'a:4:{s:5:"title";s:0:"";s:11:"description";s:0:"";s:8:"keywords";s:0:"";s:7:"noindex";s:0:"";}'
categories:
  - Free software explorations
  - Ubuntu
---
<p id="top" />
This is a guide to get your hardware configured once you have installed Ubuntu 10.04 on Vaio VPCEB14EN. I had some difficulties in getting my graphics card and sound card detected in 10.04.</p> 

**Graphics card : ATI Radeon 5470**
</p>

> `sudo apt-get install fglrx-amdcccle`

**Sound Card : Intel HD Audio 3400 Series with Realtek ALC269 Codec**

You have to update your alsa to latest version, i.e. 1.0.23. For that please remove the existing alsa drivers. Anyways check the alsa installed in your system by

> `cat /proc/asound/version`

If it shows a lower version, please continue with disabling the alsa to install a newer version.

> `sudo /sbin/alsa-utils stop`

Next we need to install necessary tools to build and install a package. And compile it along with kernel headers.

> `sudo apt-get -y install build-essential ncurses-dev gettext xmlto libasound2-dev ```linux-headers-`uname -r` libncursesw5-dev``

Next, download the latest alsa driver, alsa utils and alsa lib.

> `wget ftp://ftp.alsa-project.org/pub/driver/alsa-driver-1.0.23.tar.bz2<br />
wget ftp://ftp.alsa-project.org/pub/lib/alsa-lib-1.0.23.tar.bz2<br />
wget ftp://ftp.alsa-project.org/pub/utils/alsa-utils-1.0.23.tar.bz2`

Then, we need to compile them. Lets do it in by untarring them into a directory.

> `sudo mkdir -p /usr/src/alsa<br />
cd /usr/src/alsa<br />
sudo tar xjf alsa-driver*<br />
sudo tar xjf alsa-lib*<br />
sudo tar xjf alsa-utils*`

Next, we compile each of these sources by going into its directory and installing them.

> `sudo ./configure<br />
sudo make<br />
sudo make install`

The above steps have to be performed for alsa-driver, alsa-lib and alsa-utils. Now everything is done. The version of alsa can be seen by

> `cat /proc/asound/version`

Reboot the system and enjoy!!!