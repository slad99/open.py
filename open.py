#!/usr/bin/env python3

"""
	A simple Python replacement for xdg-open

	It is suggested to create a symlink to this script with
	a shorter name, e.g. with "ln -s open.py o", for faster typing.
"""

import os, sys

# Some default applications
fileman = "nautilus"
browser = "chromium"
imgview = "eog"
pdfview = "evince"
soundview = "vlc"
videoview = "vlc"
editor = "gedit"
hexeditor = "ghex"
zipview = "file-roller"

# Supported file types list

#    get file type stats for directory:
#      find dir/  -type f -and -printf "%f\n" | egrep -io '\.[^.]*$' | sort | uniq -c | sort -rn

files = (
 (browser, {'htm', 'html'}),
 (imgview, {'png', 'gif', 'jpg', 'jpeg', 'tif', 'tiff', 'tga', 'bmp', 'svg', 'ppm', 'xpm', 'xbm', 'ico'}),
 (pdfview, {'pdf', 'dvi', 'eps', 'epsi', 'ps'}),
 (soundview, {'wav', 'au', 'flac', 'mp2', 'mp3', 'm4a', 'ra', 'ogg', 'aiff'}),
 (videoview, {'avi', 'mp4', 'flv', 'mov', 'mkv', 'm4v', 'webm', 'rm', 'ram', 'ogv', 'vob', 'wmv'}),
 ('mplayer', {'mpg', 'mpeg', 'mpe', 'fli'}),
 (editor, {'txt', 'py', 'pl', 'php', 'rb', 'sh', 'cfg', 'conf', 'c', 'cpp', 'h'}),
 (zipview, {'zip', 'tar', 'tgz', 'gz', 'xz', 'bz2', 'lha', 'lzh', 'rar', 'exe', 'arj', '7z', 'cab', 'iso', 'rpm', 'deb', 'lz4', 'sit', 'zoo'}),
 ('kompare', {'diff', 'patch'}),
 ('timidity', {'mid'}),
 ('xmp', {'mod', 'xm', 's3m', 'med'}),
 ('sidplayfp', {'sid'}),
 ('blender', {'blend'}),
 ('display', {'iff', 'ilbm', 'lbm', 'rgb'}),
 ('openscad', {'scad'}),
 ('freecad', {'stl'}),
 ('retext', {'md', 'markdown'}),
 ('gnome-font-viewer', {'otf', 'ttf'}),
 (hexeditor, {'bin', 'raw', 'dat', 'com', 'dsk', 'adf', 'dll', 'a', 'lib', 'dylib'}),
 ('lyx', {'lyx'}),
 ('xboard -lgf', {'pgn'}),
 ('gimp', {'xcf', 'psd', 'jp2'}),
 ('libreoffice --writer', {'doc', 'docx', 'odt', 'wri'}),
 ('libreoffice --impress', {'ppt', 'pptx', 'odp'}),
 ('libreoffice --calc', {'xls', 'xlsx', 'ods'}),
 ('poedit', {'po'}),
 ('ncview', {'nc'}),
 ('srview', {'srv'}),
 ('dia', {'dia'}),
 ('inkscape', {'ai', 'wmf', 'dxf'}),
 ('man', {'0', '1', '2', '3', '4', '5', '6', '7', '8'}),
)

cmd = ''

# open current folder in file manager if no argument is supplied
if len(sys.argv) < 2:
	cmd = fileman + ' .'
	os.system(cmd)
	sys.exit(0)

arg = ' '.join(sys.argv[1:])

# open directory in file manager
if os.path.isdir(arg):
	cmd = '%s "%s"' % (fileman, arg)
	os.system(cmd)
	sys.exit(0)

ext = arg.split('.')[-1].lower()

for x, y in files:
	if ext in y:
		cmd = '%s "%s"' % (x, arg)

def isurl(x):
	for n in 'http:', 'https:', 'ftp:', 'www.':
		if x[:len(n)] == n:
			return True
	return False

# open in web browser
if isurl(arg):
	cmd = '%s "%s"' % (browser, arg)

# open in text or hex editor if nothing else is found
if not cmd:
	# https://stackoverflow.com/questions/898669/how-can-i-detect-if-a-file-is-binary-non-text-in-python
	textchars = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
	is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))
	if is_binary_string(open(arg, 'rb').read(1024)):
		cmd = '%s "%s"' % (hexeditor, arg)
	else:
		cmd = '%s "%s"' % (editor, arg)

os.system(cmd)


