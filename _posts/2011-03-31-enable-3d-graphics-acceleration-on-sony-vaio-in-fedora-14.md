---
title: Enable 3D graphics acceleration on Sony Vaio in Fedora 14
author: Amarnath
layout: post
permalink: /2011/03/enable-3d-graphics-acceleration-on-sony-vaio-in-fedora-14/
jabber_published:
  - 1301563848
email_notification:
  - 1301563849
superawesome:
  - 'false'
sp_post_metabox:
  - 'a:4:{s:5:"title";s:0:"";s:11:"description";s:0:"";s:8:"keywords";s:0:"";s:7:"noindex";s:0:"";}'
categories:
  - Free software explorations
  - General
---
<p id="top" />
I have been using Fedora 14 ever since I bought my Sony Vaio E series in May 2010. I have never cared to get my graphics card driver installed until one of my friends insisted to get his ATI card driver installed on his Dell Studio 15 laptop. I had to google deep into the internet to find a easy solution to the problem. Let me share it with you guys.</p> 

First of all get RPM fusion repos included in your repos lists. Then login as root and run
</p>

<p style="padding-left:30px;">
  <code> yum upgrade </code>
</p>

We need have an updated OS running to install the graphics driver properly. Now we will install the driver available in RPM fusion repo.

<p style="padding-left:30px;">
  <code> yum install kmod-catalyst </code>
</p>

Once this is done, we need to run the following code to initialise the ATI card while booting up.

<p style="padding-left:30px;">
  <code> aticonfig --initial -f </code><br /> <code> catalyst-config-display enable </code>
</p>

If the second command gives an error, we can infer the installation of the driver was not successful. If the installation was successful, reboot your system to enjoy full graphical entertainment.

Note: In case there is a failure in installing the driver and its unable to boot into Fedora, please follow the steps given below. Its required to remove the packages installed. In case its not possible to log in to Fedora desktop environment, the single user mode has to be made use. While booting up in GRUB, edit the boot parameters by pressing &#8216;e&#8217;  and add &#8216;single&#8217; at the end of kernel boot info. This enables single user mode and helps in rescue of the system. Once you drop into the root shell just remove the installed package by using the following command.

<p style="padding-left:30px;">
  <code> yum remove kmod-catalyst* </code>
</p>