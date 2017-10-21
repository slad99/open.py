#!/usr/bin/env python3

"""A simple Python replacement for xdg-open"""

import os, sys

fileman = "nautilus"
browser = "chromium"
imgview = "eog"
pdfview = "evince"
soundview = "vlc"
videoview = "vlc"
editor = "gedit"
zipview = "file-roller"

# supported file types
files = (
 (browser, ('htm', 'html')),
 (imgview, ('png', 'gif', 'jpg', 'jpeg', 'tif', 'tiff', 'tga', 'bmp', 'svg', 'xpm', 'xbm', 'ico')),
 (pdfview, ('pdf', 'dvi', 'eps', 'ps')),
 (soundview, ('wav', 'au', 'flac', 'mp3', 'm4a', 'ra')),
 (videoview, ('avi', 'mp4', 'flv', 'mov', 'mkv', 'm4v', 'webm', 'rm', 'ram')),
 (editor, ('txt', 'py', 'pl', 'php', 'rb', 'sh', 'cfg', 'conf', 'c', 'cpp', 'h')),
 (zipview, ('zip', 'tar', 'tgz', 'gz', 'xz', 'bz2', 'lha', 'rar')),
 ('kompare', ('diff', 'patch')),
 ('timidity', ('mid')),
 ('xmp', ('mod', 'xm')),
 ('sidplayfp', ('sid')),
 ('blender', ('blend')),
 ('gm display', ('iff', 'ilbm')),
 ('openscad', ('scad')),
 ('freecad', ('stl')),
 ('retext', ('md', 'markdown')),
)

cmd = ''

# open current folder in file manager if no argument is supplied
if len(sys.argv) < 2:
	cmd = fileman + ' .'
	os.system(cmd)
	sys.exit(0)

ext = sys.argv[1].split('.')[-1].lower()

for x, y in files:
	if ext in y:
		cmd = '%s "%s"' % (x, sys.argv[1])

# open in web browser
if ('http:' in sys.argv[1] or 'https:' in sys.argv[1] or
		'ftp:' in sys.argv[1] or 'www.' in sys.argv[1]):
	cmd = '%s "%s"' % (browser, sys.argv[1])

# open in editor if nothing else is found
if not cmd:
	cmd = '%s "%s"' % (editor, sys.argv[1])

os.system(cmd)


