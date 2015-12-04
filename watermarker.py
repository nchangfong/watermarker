"""
A program to place a watermark on photos with the additional option of 
resizing both the watermark and the images.
"""

from PIL import Image
from PIL import ImageDraw
import glob, os

watermark = "./watermarks/" + raw_input("Enter filename of watermark: ")
wm = Image.open(watermark)

# directory where images are to be watermarked
# imagedir = raw_input("Enter image directory: ")
imagedir = "./input"


# where watermarked images will end up
# user has to make sure directory already exists
# outputdir = raw_input("Enter output directory: ")
outputdir = "./output"


# wm_scaling_factor = float(raw_input("Enter watermark scaling factor: "))

#0.8 is hardcoded value used for hack western
wm_scaling_factor = 0.8

# new values for watermark after scaling
new_x = int(wm.size[0]*wm_scaling_factor)
new_y = int(wm.size[1]*wm_scaling_factor)

wm = wm.resize((new_x,new_y),Image.ANTIALIAS)

for infile in glob.glob(imagedir + "/*.JPG"):
        file, ext = os.path.splitext(os.path.basename(infile))
        im = Image.open(infile)
       
        # calculates the scaling factor by finding dividing the longer axis of input
        # photo over pixel length of desired output
	# scaling to 1920 is for hack western facebook photo uploads
        im_scaling_factor = max(im.size[0],im.size[1])/float(1920)

        # applying scaling factor to image
    	im_x = int(im.size[0]/im_scaling_factor)
    	im_y = int(im.size[1]/im_scaling_factor)

        # resize the image
        im = im.resize((im_x,im_y), Image.ANTIALIAS)

        # correcting aspect ratios for odd cases
        if (im.size[0]>im.size[1]):
                im = im.crop([0,0,1920,1280])
        elif (im.size[1]>im.size[0]):
                im = im.crop([0,0,1280,1920])

        # position for watermark
        wm_x = im.size[0]-wm.size[0]-7
        wm_y = im.size[1]-wm.size[1]-5
        wm_pos = (wm_x,wm_y)
        im.paste(wm, wm_pos, mask=wm)
        im.save(outputdir + "/" + file + "-wm.jpg")
