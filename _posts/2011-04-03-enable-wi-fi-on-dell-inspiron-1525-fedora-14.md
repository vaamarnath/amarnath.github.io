---
title: 'Enable Wi-Fi on Dell Inspiron 1525 &#8211; Fedora 14'
author: Amarnath
layout: post
permalink: /2011/04/enable-wi-fi-on-dell-inspiron-1525-fedora-14/
superawesome:
  - 'false'
jabber_published:
  - 1301792252
email_notification:
  - 1301792253
sp_post_metabox:
  - 'a:4:{s:5:"title";s:0:"";s:11:"description";s:0:"";s:8:"keywords";s:0:"";s:7:"noindex";s:0:"";}'
categories:
  - Free software explorations
  - General
---
<p id="top" />
I was just upgrading F12 to F14 in my friend&#8217;s Dell Inspiron 1525. Everything was fine, except when the WiFi is switched on, its not detected by F14. I had to do some amount of googling to get it right. I thought I could just share it here.</p> 

First of see that you have [RPM fusion repos][1] added to your repos list. Then just install kmod-wl package after updating you system.
</p>

<p style="padding-left:30px;">
  <code>yum upgrade</code>
</p>

<p style="padding-left:30px;">
  <code>yum install kmod-wl </code>
</p>

<p style="padding-left:30px;">
  <code>reboot</code>
</p>

Now just reboot your system and use the hardware switch to turn on WiFi. Everything should be working now.

<h6 class="zemanta-related-title" style="font-size:1em;">
  Related Articles
</h6>

<ul class="zemanta-article-ul">
  <li class="zemanta-article-ul-li">
    <a href="http://vaamarnath.wordpress.com/2011/03/31/enable-3d-graphics-acceleration-on-sony-vaio-in-fedora-14/">Enable 3D graphics acceleration on Sony Vaio in Fedora 14</a> (vaamarnath.wordpress.com)
  </li>
</ul>

 [1]: http://rpmfusion.org/