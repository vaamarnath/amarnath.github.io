---
title: Switch over to LibreOffice!
author: Amarnath
layout: post
permalink: /2010/10/switch-over-to-libreoffice/
jabber_published:
  - 1286296140
sp_post_metabox:
  - 'a:4:{s:5:"title";s:0:"";s:11:"description";s:0:"";s:8:"keywords";s:0:"";s:7:"noindex";s:0:"";}'
categories:
  - 'Free &amp; Open Source'
---
<p id="top" />
Many of you must be aware of the formation of &#8216;The Document Foundation&#8217; to be free from Oracle once it acquired Sun. OOo is now re-branded as &#8216;LibreOffice&#8217;. This is really good news for open source community.</p> 

Lets see how LibreOffice can be installed in Ubuntu and Debian based systems. Currently only beta versions of EN_US builds are available.
</p>

<!--more-->

`echo 'deb http://download.tuxfamily.org/gericom/libreoffice /' | sudo tee -a /etc/apt/sources.list`

`sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 890E7A26`

`sudo apt-get update`

`sudo apt-get install libreoffice3`

<!--more-->

**Screenshot**

<p style="text-align:center;">
  <img class="aligncenter" title="Screenshot LibreOffice" src="http://vaamarnath.co.in/wp-blog/wp-content/uploads/2011/02/lo_startcenter1.png?w=300" alt="" width="450" height="360" />
</p>

<p style="text-align:left;">
  Thanks to <a href="http://www.mydailytechtips.com/2010/10/how-to-install-libreoffice-in-ubuntu.html" target="_blank">mydailytechtips</a>.
</p>