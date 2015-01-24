---
title: 'OpenCV &#8211; Image Resize (Pixel Replication)'
author: Amarnath
layout: post
permalink: /2010/10/opencv-image-resize-pixel-replication/
jabber_published:
  - 1286365057
sp_post_metabox:
  - 'a:4:{s:5:"title";s:0:"";s:11:"description";s:0:"";s:8:"keywords";s:0:"";s:7:"noindex";s:0:"";}'
categories:
  - Open Source
  - OpenCV
---
<p id="top" />
Image resizing is an important function for 
<a class="zem_slink" title="Image processing" href="http://en.wikipedia.org/wiki/Image_processing" rel="wikipedia">image processing</a> applications. Its really important that the information content is not lost during zooming or shrinking of an image. In <a class="zem_slink" title="OpenCV" href="http://en.wikipedia.org/wiki/OpenCV" rel="wikipedia">OpenCV</a>, we have a library function `cvResize` that can be used for image resizing. Here, I am implementing *pixel replication* algorithm for zooming of images.</p> 

<pre class="brush: cpp">#include&lt;stdio.h&gt;
#include&lt;highgui.h&gt;
#include&lt;cv.h&gt;
#include&lt;math.h&gt;
#include&lt;stdlib.h&gt;

int main(int argc, char **argv)

{ const char* imagename = argc &gt; 1 ? argv[1] : "lena128.png";
IplImage* img = 0;
int h, w, step, zstep, channels, i, j, k, px, py;
uchar *data, *newdata;
//reading image, by default reads lena128.png
img = cvLoadImage(imagename, CV_LOAD_IMAGE_UNCHANGED);
if(!img)
printf("Could not load image file: %sn", imagename);
h = img-&gt;height;
w = img-&gt;width;
step = img-&gt;widthStep;
channels = img-&gt;nChannels;
data = (uchar *)img-&gt;imageData;

int factor = 2; //zoom by 2x

//create new image of required size
IplImage* zoomed = cvCreateImage(cvSize(factor*w, factor*h), 8, channels);
h = zoomed-&gt;height;
w = zoomed-&gt;width;
zstep = zoomed-&gt;widthStep;
channels = zoomed-&gt;nChannels;
newdata = (uchar *)zoomed-&gt;imageData;

//pixel replication algorithm
for(i=0; i&lt;h; i++)
if(i%factor==0)
for(j=0; j&lt;w; j++)
if(j%factor==0)
for(k=0; k&lt;channels; k++)
for(px=0; px&lt;factor; px++)
for(py=0; py&lt;factor; py++)
newdata[(i+px)*zstep+(j+py)*channels+k] = data[(i*step)/factor+(j*channels)/factor+k];

//display the zoomed image
cvNamedWindow("OpenCV", CV_WINDOW_AUTOSIZE);
cvShowImage("OpenCV", zoomed);
cvWaitKey(0);
cvReleaseImage(&zoomed);
cvReleaseImage(&img);
return 0;
}</pre>

  
Now lets see how the code works on a 64&#215;64 image. The image on left shows the input image and the image on the right shows the image zoomed by 2x.  
[<img class="alignleft size-full wp-image-62" title="lena64" src="http://opentechlife.files.wordpress.com/2010/10/lena64.png" alt="" width="64" height="64" />][1][<img class="size-full wp-image-64 alignright" title="lena128" src="http://opentechlife.files.wordpress.com/2010/10/lena128.png" alt="" width="131" height="131" />][2]

 [1]: http://opentechlife.files.wordpress.com/2010/10/lena64.png
 [2]: http://opentechlife.files.wordpress.com/2010/10/lena128.png