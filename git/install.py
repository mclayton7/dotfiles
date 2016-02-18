#!/usr/bin/env python
# Mac Clayton 2016

import os
import shutil
import sys

base_dir = os.path.dirname(os.path.abspath(__file__))


def installForWindows():
   home_directory = os.environ['USERPROFILE']
   new_location = os.path.join(home_directory, '.gitconfig')
   shutil.copy('gitconfig', new_location)

def installForLinux():
   gitconfig_dotfile_path = os.path.join(base_dir, 'gitconfig')
   gitconfig_path = os.path.join(os.environ['HOME'], '.gitconfig')
   if os.path.exists(gitconfig_path):
      print 'Removing existing gitconfig symlink: %s' % gitconfig_path
      os.unlink(gitconfig_path)
   os.symlink(gitconfig_dotfile_path, gitconfig_path)


if __name__ == '__main__':
   if sys.platform.startswith('win'):
      installForWindows()
      print "Finished!"
   elif sys.platform.startswith('linux'):
      installForLinux()
      print "Finished!"
   else:
      print 'OS %s not supported' % sys.platform