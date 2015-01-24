---
title: 'Basic OpenCV Programming &#8211; Negative of an Image'
author: Amarnath
layout: post
permalink: /2010/09/basic-opencv-programming-negative-of-an-image/
jabber_published:
  - 1283690377
sp_post_metabox:
  - 'a:4:{s:5:"title";s:0:"";s:11:"description";s:0:"";s:8:"keywords";s:0:"";s:7:"noindex";s:0:"";}'
categories:
  - OpenCV
---
<p id="top" />
For starting with image processing using OpenCV, I would suggest to start working on problems and try to write the code for its solution. This can give you real experience in coding and learning syntax can be done as and when its required.</p> 

Lets see the code to obtain the negative of an image.  


<pre class="brush: cpp">#include&lt;stdio.h&gt;
#include&lt;highgui.h&gt;
#include&lt;cv.h&gt;
#include&lt;math.h&gt;
#include&lt;stdlib.h&gt;

int main(int argc, char **argv)
{
//reading the input image
const char* imagename = argc &gt; 1 ? argv[1] : "lena.jpg";
IplImage* img = 0;
int h, w, step, channels, i, j, k;
uchar *data;
img = cvLoadImage(imagename, CV_LOAD_IMAGE_UNCHANGED);
if(!img)
printf("Could not load image file: %sn", imagename);
//obtaining the image parameters
h = img-&gt;height;
w = img-&gt;width;
step = img-&gt;widthStep;
channels = img-&gt;nChannels;
data = (uchar *)img-&gt;imageData;
//transforming to negative
for(i=0; i&lt;h; i++)
for(j=0; j&lt;w; j++)
for(k=0; k&lt;channels; k++)
data[i*step+j*channels+k] = 255 - data[i*step+j*channels+k];
//displaying the negative
cvNamedWindow("OpenCV", CV_WINDOW_AUTOSIZE);
cvShowImage("OpenCV", img);
cvWaitKey(0);
cvReleaseImage(&img);
return 0;
}</pre>

  
&nbsp;
</p>

In this code we have read an image and converted it to its negative. The details of the functions used are given below:

`cvLoadImage()` Loads the required image.

`cvNamedWindow()` Creates a window with the name and window size as specified.

`cvShowImage()` Outputs the image to the window created earlier.

`cvWaitKey()` Waits till the user interrupts.

For more detailed understanding of these functions, I would recommend to read the <a href="http://opencv.willowgarage.com/documentation/c/index.html" target="_blank">OpenCV documentation</a>.