#!/usr/bin/python
# Mac Clayton 2016

import os
import subprocess
import sys

def symlink(source, link_name):
	if os.path.exists(link_name):
		os.unlink(link_name)
	os.symlink(source, link_name)

def install_for_linux():
	dotfiles = ('vimrc',)
	home_dir = os.environ['HOME'] + os.path.sep
	git_command = 'git clone https://github.com/VundleVim/Vundle.vim.git $HOME/.vim/bundle/Vundle.vim'
	subprocess.call(git_command, shell=True)
	vim_dotfile_dir = os.path.dirname(os.path.realpath(__file__)) + os.path.sep
	map(lambda file: symlink(vim_dotfile_dir + file,home_dir+'.'+file), dotfiles)

if 'linux' in sys.platform:
	install_for_linux()
	print 'Installed for Linux.'
else:
	print 'Platform %s not supported.' % sys.platform

