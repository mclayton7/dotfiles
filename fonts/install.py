#!/usr/bin/python
# Mac Clayton 2016

import os
import subprocess
import sys


def install_for_linux():
	script_dir = os.path.dirname(os.path.realpath(__file__)) + os.path.sep
	font_dir = os.path.join(script_dir, 'fonts')
	if os.path.exists(script_dir + 'fonts') is not True:
		git_command = 'git clone --recursive git@github.com:powerline/fonts.git '
		subprocess.call(git_command, shell=True)
	subprocess.call(font_dir + os.path.sep + 'install.sh', shell=True)

if 'linux' in sys.platform:
	install_for_linux()
	print 'Installed for Linux.'
else:
	print 'Platform %s not supported.' % sys.platform

