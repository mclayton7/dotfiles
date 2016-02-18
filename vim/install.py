#!/usr/bin/env python
# Mac Clayton 2016

import os
import shutil
import subprocess
import sys

base_dir = os.path.dirname(os.path.abspath(__file__))


def installVundleOnWindows():
   vundle_path = os.path.join(os.environ['USERPROFILE'], 'vimfiles', 'bundle', 'Vundle.vim')
   if not os.path.exists(vundle_path):
      print 'Cloning Vundle...'
      pr = subprocess.Popen('git clone https://github.com/gmarik/Vundle.vim.git ' + vundle_path,
         shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      (git_status, error) = pr.communicate()
      print 'Done cloning'
   else:
      print 'Vundle already installed'


def copyVimrcOnWindows():
   print 'Copying vimrc'
   home_directory = os.environ['USERPROFILE']
   new_location = os.path.join(home_directory, '_vimrc')
   shutil.copy(os.path.join(base_dir, 'vimrc'), new_location)
   print 'Done copying'


def installForWindows():
   installVundleOnWindows()
   copyVimrcOnWindows()


def installForLinux():
   installVundleOnLinux()
   symlinkVimrcOnLinux()


def installVundleOnLinux():
   vundle_path = '~/.vim/bundle/Vundle.vim'
   if not os.path.exists(vundle_path):
      print 'Cloning Vundle...'
      pr = subprocess.Popen('git clone https://github.com/gmarik/Vundle.vim.git ' + vundle_path,
         shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      (git_status, error) = pr.communicate()
      print 'Done cloning'
   else:
      print 'Vundle already installed'

def symlinkVimrcOnLinux():
   vimrc_dotfile_path = os.path.join(base_dir, 'vimrc')
   vimrc_path = os.path.join(os.environ['HOME'], '.vimrc')
   if os.path.exists(vimrc_path):
      print 'Removing existing vimrc symlink: %s' % vimrc_path
      os.unlink(vimrc_path)
   os.symlink(vimrc_dotfile_path, vimrc_path)


if __name__ == '__main__':
   if sys.platform.startswith('win'):
      installForWindows()
      print "Finished!"
   elif sys.platform.startswith('linux'):
      installForLinux()
      print "Finished!"
   else:
      print 'OS %s not supported' % sys.platform