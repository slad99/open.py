#!/usr/bin/env python3

"""A simple Python replacement for xdg-open"""

import os, sys

fileman = "nautilus"
browser = "chromium"
imgview = "gwenview"
pdfview = "evince"
soundview = "vlc"
videoview = "vlc"
editor = "gedit"
zipview = "file-roller"

files = (
 (browser, ('htm', 'html')),
 (imgview, ('png', 'gif', 'jpg', 'jpeg', 'tif', 'bmp')),
 (pdfview, ('pdf')),
 (soundview, ('wav', 'au', 'flac', 'mp3', 'm4a')),
 (videoview, ('mp4', 'flv', 'mov', 'mkv', 'm4v')),
 (editor, ('txt', 'py', 'sh', 'cfg')),
 (zipview, ('zip', 'tar', 'tgz', 'gz', 'bz2', 'lha', 'rar')),
)

cmd = ''

if len(sys.argv) < 2:
	cmd = fileman + ' .'
	os.system(cmd)
	sys.exit(0)

ext = sys.argv[1].split('.')[-1].lower()

for x, y in files:
	if ext in y:
		cmd = '%s "%s"' % (x, sys.argv[1])

if ('http:' in sys.argv[1] or 'https:' in sys.argv[1] or
		'ftp:' in sys.argv[1] or 'www.' in sys.argv[1]):
	cmd = '%s "%s"' % (browser, sys.argv[1])

if cmd:
	print(cmd)
	os.system(cmd)


