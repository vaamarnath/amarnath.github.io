---
title: 'OpenCV &#8211; Gamma Correction'
author: Amarnath
layout: post
permalink: /2011/02/opencv-gamma-correction/
email_notification:
  - 1298423018
jabber_published:
  - 1298423016
sp_post_metabox:
  - 'a:4:{s:5:"title";s:0:"";s:11:"description";s:0:"";s:8:"keywords";s:0:"";s:7:"noindex";s:0:"";}'
categories:
  - Open Source
  - OpenCV
---
<p id="top" />
Gamma correction (also known as power transformation) is used in image processing in several situations. The classic example where gamma correction is needed is in CRT monitors. In CRTs the amount or intensity of light from the phosphor in the screen is related to voltage as</p> 

<p style="text-align: center;">
  <em>Output = Voltage <sup>crt_gamma</sup></em>
</p>

**Hence if we give a linear or normal image to the CRT, the image would be look much too dark. In order to mitigate this effect, we &#8220;gamma correct&#8221; the image such a way that the image output looks well. All we do is something opposite to what the CRT does.
</p>

<p style="text-align: center;">
  gamma_correc_image = image<sup>(1/crt_gamma)</sup>
</p>

For most CRTs, the crt_gamma is somewhere between 1.0 and 3.0.

Now lets delve into the code. The code given below is just to explicit to understand (I believe).  


<pre class="brush: cpp">#include&lt;stdio.h&gt;
#include&lt;highgui.h&gt;
#include&lt;cv.h&gt;
#include&lt;math.h&gt;
#include&lt;stdlib.h&gt;

int main(int argc, char **argv)

{ const char* imagename = argc &gt; 1 ? argv[1] : "lena.jpg";
IplImage* img = 0;
int h, w, step, channels, i, j, k;
uchar *data;
//read the input image
img = cvLoadImage(imagename, CV_LOAD_IMAGE_UNCHANGED);
if(!img)
printf("Could not load image file: %sn", imagename);
h = img-&gt;height;
w = img-&gt;width;
step = img-&gt;widthStep;
channels = img-&gt;nChannels;
data = (uchar *)img-&gt;imageData;
//assign the gamma inverse value, here 2
int gamma = 2;

//new image with gamma correction
IplImage* trans = cvCreateImage(cvGetSize(img), 8, channels);
int trans_step;
trans_step = trans-&gt;widthStep;
//gamma correction
cvPow(img, trans, gamma);
cvConvertScaleAbs(trans, trans, 1, 0);
cvNamedWindow("OpenCV", CV_WINDOW_AUTOSIZE);
cvShowImage("OpenCV", trans);
cvWaitKey(0);
cvReleaseImage(&img);
cvReleaseImage(&trans);

return 0;
}</pre>

  
&nbsp;