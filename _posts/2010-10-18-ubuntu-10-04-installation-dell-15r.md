---
title: Ubuntu 10.04 Installation – Dell 15R
author: Amarnath
layout: post
permalink: /2010/10/ubuntu-10-04-installation-dell-15r/
jabber_published:
  - 1287414305
email_notification:
  - 1287414306
superawesome:
  - 'false'
sp_post_metabox:
  - 'a:4:{s:5:"title";s:0:"";s:11:"description";s:0:"";s:8:"keywords";s:0:"";s:7:"noindex";s:0:"";}'
categories:
  - Free software explorations
  - Ubuntu
---
<p id="top" />
The new Dell 15R wipes out your GRUB2 when you boot into Windows after the installation of Ubuntu 10.04. This issue can be solved by uninstalling Dell Data Safe in Windows before the installation of GNU/Linux OS. But, if you really want to keep the Dell Data Safe installed, the solution would be to  downgrade GRUB2 to GRUB1.</p> 

*Step 1:* In case you already wiped out MBR, boot using a live USB/CD and reinstall GRUB2. If you have not booted onto Windows after Ubuntu installation, please goto step 2.  
`<br />
sudo -i<br />
mount /dev/sdax /mnt      #x partition where / and y partition where /boot is installed<br />
mount /dev/sday /mnt/boot  #skip this one if not have a separate /boot partition<br />
grub-install --root-directory=/mnt/ /dev/sda<br />
`
</p>

*Step 2: *Downgrading to GRUB1  
Backup GRUB2 files.  
`<br />
sudo cp /etc/default/grub /etc/default/grub.old<br />
sudo cp -R /etc/grub.d /etc/grub.d.old<br />
sudo cp -R /boot/grub /boot/grub.old<br />
`  
Then, remove GRUB2.  
`<br />
sudo apt-get purge grub2 grub-pc<br />
`  
Install GRUB 0.97  
`<br />
sudo apt-get install grub<br />
`  
Next, we need to generate the GRUB1 files using the following commands.  
`<br />
sudo update-grub<br />
sudo grub-install /dev/sdX<br />
`  
Choose X as the partition where /boot is installed. We need to also ensure that synaptic does not update this GRUB automatically to GRUB2.  
`<br />
echo "grub hold" | sudo dpkg --set-selections<br />
`  
Now reboot and enjoy the freedom.