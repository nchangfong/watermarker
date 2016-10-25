"""
places a watermark on photos with the option to resize both the watermark and the images.
"""

from PIL import Image
from PIL import ImageDraw
import glob, os

watermark = raw_input("Enter path to watermark including file extension: ")
wm = Image.open(watermark)

# directory where images are to be watermarked
imagedir = raw_input("Enter path to input directory: ")


# where watermarked images will end up
outputdir = "./output"
if not os.path.exists(outputdir):
    os.makedirs(outputdir)

# factor by which to scale watermark
wm_scaling_factor = float(raw_input("Enter watermark scaling factor (HW default 0.8): "))

# new values for watermark after scaling
new_x = int(wm.size[0]*wm_scaling_factor)
new_y = int(wm.size[1]*wm_scaling_factor)

wm = wm.resize((new_x,new_y),Image.ANTIALIAS)

# distance between right and bottom edge of watermark and original photo
wm_x_offset = float(raw_input("Enter watermark x offset (HW default: 7): "))
wm_y_offset = float(raw_input("Enter watermark y offset (HW default: 5): "))

for infile in glob.glob(imagedir + "/*.[jJ][pP][gG]"):
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

        # cropping for a few photos with unexpected aspect ratios
        # if (im.size[0]>im.size[1]):
        #         im = im.crop([0,0,1920,1280])
        # elif (im.size[1]>im.size[0]):
        #         im = im.crop([0,0,1280,1920])

        # top-left position of watermark
        wm_x = im.size[0]-wm.size[0]-wm_x_offset
        wm_y = im.size[1]-wm.size[1]-wm_y_offset
        wm_pos = (wm_x,wm_y)
        im.paste(wm, wm_pos, mask=wm)
        im.save(outputdir + "/" + file + "-wm.jpg")
