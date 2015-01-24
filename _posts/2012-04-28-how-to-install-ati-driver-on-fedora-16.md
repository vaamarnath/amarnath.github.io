---
title: How to install ATI driver on Fedora 16
author: Amarnath
layout: post
permalink: /2012/04/how-to-install-ati-driver-on-fedora-16/
categories:
  - Fedora
  - Free software explorations
---
<p id="top" />
As usual I had some bad time trying to figure out how to get my laptop cool down after my fresh install of Fedora 16 last week. The free graphics driver was not helping a bit. Finally after several hours of duckduckgoing, ended up on a right tutorial how to get this done.</p> 

First step I would recommend is get your system updated.
</p>

<pre>yum update</pre>

Next step, install the kernel development packages.

<pre>yum install kernel-devel</pre>

The following <a href="http://wiki.cchtml.com/index.php/Fedora_16_Installation_Guide#Requirements" target="_blank">steps</a> needs to taken care of next. See to it that you do the necessary changes depending on the architecture you have got.

<pre>su - yum reinstall mes-libGL</pre>

See that you have added rpm fusion repos to your repo list. If not use the next command.

<pre>su -rpm -Uvh http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-stable.noarch.rpm  http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-stable.noarch.rpm</pre>

And here goes the installation step finally!

As usual I had some bad time trying to figure out how to get my laptop cool down after my fresh install of Fedora 16 last week. The free graphics driver was not helping a bit. Finally after several hours of duckduckgoing, ended up on a right tutorial how to get this done.

First step I would recommend is get your system updated.

<pre>yum update</pre>

Next step, install the kernel development packages.

<pre>yum install kernel-devel</pre>

The following <a href="http://wiki.cchtml.com/index.php/Fedora_16_Installation_Guide#Requirements" target="_blank">steps</a> needs to taken care of next. See to it that you do the necessary changes depending on the architecture you have got.

<pre>su - yum reinstall mes-libGL</pre>

See that you have added rpm fusion repos to your repo list. If not use the next command.

<pre>su -rpm -Uvh http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-stable.noarch.rpm  http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-stable.noarch.rpm</pre>

And here goes the installation step finally!

<pre>su -c yum install akmod-catalyst xorg-x11-drv-catalyst xorg-x11-drv-catalyst-libs</pre>

Note: This is a simplified tutorial to the howto given <a href="http://wiki.cchtml.com/index.php/Fedora_16_Installation_Guide" target="_blank">here</a> for x64 Fedora 16 machines with ATI Radeon graphics card.