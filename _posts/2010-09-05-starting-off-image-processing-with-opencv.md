---
title: Starting off Image Processing with OpenCV
author: Amarnath
layout: post
permalink: /2010/09/starting-off-image-processing-with-opencv/
jabber_published:
  - 1283679131
sp_post_metabox:
  - 'a:4:{s:5:"title";s:0:"";s:11:"description";s:0:"";s:8:"keywords";s:0:"";s:7:"noindex";s:0:"";}'
categories:
  - OpenCV
---
<p id="top" />

<img class="alignleft" style="margin-top:5px;margin-bottom:5px;" title="OpenCv Logo" src="http://www.aishack.in/wp-content/uploads/2010/03/opencv_logo.gif" alt="" width="224" height="207" /></p> 

Image processing is an important field where a lot of signal processing concepts learned is applied. Image processing maybe done with any programming language. I think Matlab and C are the most commonly used and the latter being more popular due to the user friendly interface. But, C gives you more power and flexibility to solve image processing problems. OpenCV is a image &#8211; video processing library developed by Intel and released under BSD license. It can serve as a great tool for image manipulation and transformations in C programming.

I am using GCC to compile my C programs in my Ubuntu machine. You may use any other C compilers and please note to include the CV libraries in your include path.

> `gcc program.c -o program -I /usr/include/opencv/ -L /usr/local/lib/ -lcv -lhighgui -lcvaux -lm`

The above command is used for compiling the programs. Please see that you have installed libcv-dev, libcvaux and libhighgui-dev packages installed from the repository in case of linux distributions. Other users please check <a href="http://opencv.willowgarage.com/" target="_blank">http://opencv.willowgarage.com/</a>.

To run the program after compilation,

> `./program argumentsifany`

In the following posts I would include sample programs and explanations for some of the library functions in OpenCV.