---
title: 'OpenCV &#8211; Extracting RGB from a color image'
author: Amarnath
layout: post
permalink: /2010/09/opencv-extracting-rgb-from-a-color-image/
jabber_published:
  - 1283909766
sp_post_metabox:
  - 'a:4:{s:5:"title";s:0:"";s:11:"description";s:0:"";s:8:"keywords";s:0:"";s:7:"noindex";s:0:"";}'
categories:
  - OpenCV
---
<p id="top" />
In this post I would like to go into details of a color image. In opencv, an image is represented as a 1 dimensional entity. From the top left hand corner of the image, each pixel is represented as BGR in an array form. That is. each row of pixels is represented one after another where each pixel information is given completely. An RGB image is a 3 channel image where each pixel is represented by three 8 bit values corresponding to blue, green and red components. Here, I would give an example how to extract only the blue components of an input image.
  


<pre class="brush: cpp">#include&lt;stdio.h&gt;
#include&lt;highgui.h&gt;
#include&lt;cv.h&gt;
#include&lt;math.h&gt;
#include&lt;stdlib.h&gt;

int main(int argc, char **argv)

{
const char* imagename = argc &gt; 1 ? argv[1] : "lena.jpg";
IplImage* img = 0;
int h, w, step, channels, i, j, k;
uchar *data, *trans;
img = cvLoadImage(imagename, CV_LOAD_IMAGE_UNCHANGED);
if(!img)
printf("Could not load image file: %sn", imagename);
h = img-&gt;height;
w = img-&gt;width;
step = img-&gt;widthStep;
channels = img-&gt;nChannels;
data = (uchar *)img-&gt;imageData;

IplImage* RGB = cvCreateImage(cvGetSize(img), 8, 1);
trans = (uchar *)RGB-&gt;imageData;
int trans_step;
trans_step = RGB-&gt;widthStep;

//extracting necessary components
int col = 0;
for(i=0; i&lt;h; i++)
for(j=0; j&lt;w; j++)
trans[i*trans_step+j] = data[i*step+j*channels+col];

cvNamedWindow("OpenCV", CV_WINDOW_AUTOSIZE);
cvShowImage("OpenCV", RGB);
cvWaitKey(0);
cvReleaseImage(&img);
cvReleaseImage(&RGB);

return 0;
}</pre>

  
&nbsp;  
In this example code, we read an image into *img* and extract required component into a single channel image *RGB*. Here, in the code section mentioning extraction features takes the blue components into the image data array *trans* as *col* is set as **. That is we are copying every one first value representing an image, i.e. the blue component into our new image. If we set *col = 1* we can obtain the green sections of the image and similarly *col = 2* gives red components of the image.</p>