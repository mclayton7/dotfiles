#!/usr/bin/python
# Mac Clayton 2016

import os
import subprocess
import sys

def symlink(source, link_name):
	if os.path.islink(link_name):
		os.unlink(link_name)
	os.symlink(source, link_name)

def install_for_linux():
	rc_files = ('zpreztorc', 'zshrc')
	home_dir = os.environ['HOME'] + os.path.sep
	if os.path.exists(home_dir + '.zprezto') is not True:
		git_command = 'git clone --recursive https://github.com/sorin-ionescu/prezto.git "$HOME/.zprezto"'
		subprocess.call(git_command, shell=True)
	zsh_config_dir = os.path.dirname(os.path.realpath(__file__)) + os.path.sep
	map(lambda file: symlink(zsh_config_dir + file,home_dir+'.'+file), rc_files)
	subprocess.call('chsh -s /bin/zsh', shell=True)

if 'linux' in sys.platform:
	print 'make sure zsh is already installed'
	install_for_linux()
	print 'Installed for Linux.'
else:
	print 'Platform %s not supported.' % sys.platform

