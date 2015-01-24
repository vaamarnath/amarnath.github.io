---
title: Install Firefox on Debian Squeeze
author: Amarnath
layout: post
permalink: /2011/09/install-firefox-on-debian-squeeze/
sp_post_metabox:
  - 'a:4:{s:5:"title";s:0:"";s:11:"description";s:0:"";s:8:"keywords";s:0:"";s:7:"noindex";s:0:"";}'
categories:
  - 'Free &amp; Open Source'
  - Free software explorations
  - General
---
<p id="top" />
Debian Squeeze comes with Iceweasel when its installed. I have been using Iceweasel for past 5 months and I had upgraded to Iceweasel 4.0 when it was available in sometime in June 2011. I always wanted to install Firefox on my Debian machine. And I just did it today. To speak the truth, actually I had to remove Iceweasel 4.0 due to some dependency issues. It was preventing me from installing OpenCV development libraries. So I had made up my mind to do it finally.</p> 

To start with, I would like to recommend to backup all bookmarks, history and cache associated with Iceweasel. But, this is an optional step. If you do not mind losing them, skip this step.
</p>

<p style="padding-left: 30px;">
  <code>cd ~</code>
</p>

<p style="padding-left: 30px;">
  <code>tar -cjvf mozilla_backup.tar.bz2 ~/.mozilla/</code>
</p>

And we need to get the latest version of [Firefox][1] from Mozilla. Untar the tar.bz2 file to the directory where you to have your Firefox setup, say your home.

<p style="padding-left: 30px;">
  <code>tar -xjvf firefox-x.x.x.tar.bz2 ~/</code>
</p>

That&#8217;s it. You have your Firefox ready to launch. Remove the existing Iceweasel from your machine now.

<p style="padding-left: 30px;">
  <code>su</code>
</p>

<p style="padding-left: 30px;">
  <code>apt-get remove iceweasel</code>
</p>

Now, launch Firefox by running the executable in the firefox directory named &#8216;firefox&#8217;. Check whether all bookmarks, history are still intact in the firefox. If this it the case, you do not need to restore the files from the backup. Else, proceed to the next step.

<p style="padding-left: 30px;">
  <code>cd ~</code>
</p>

<p style="padding-left: 30px;">
  <code>tar -xjvf mozilla_backup.tar.bz2 ~/.mozilla</code>
</p>

Now, everything should be up and running. Hope you have Firefox running now with the latest version.

 [1]: http://getfirefox.com