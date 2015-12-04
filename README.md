# watermarker

### Description
A program I wrote for adding watermarks to photos using the [Python Imaging Library](http://www.pythonware.com/products/pil/) (PIL). It's relatively untested but I've successfully executed the program in a virtual machine running Ubuntu 14.04.3 with only `git` and the VirtualBox Guest Additions installed. 

### Instructions
In the watermarker directory create `input`, `output`, and `watermarks` directories with the following command:

`mkdir input output watermarks`

Your file structure should now look like this:
```
├── input/
├── output/
├── README.md
├── watermarker.py
├── watermarks/
```

Place all input files (those to be watermarked) in `input/` as `.JPG` (case-sensitive for now)

Place watermark image in `watermarks/`

Execute program by executing the following command:
`python watermarker.py`

Enter the filename of watermark you'd like to use when prompted, wait for program to finish executing, and then view your watermarked photos in `output`!
