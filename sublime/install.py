#!/usr/bin/env python
# Mac Clayton 2016

import distutils
from distutils import dir_util
import os
import shutil
import subprocess
import sys

base_dir = os.path.dirname(os.path.abspath(__file__))


def copyPreferencesOnWindows():
   user_directory = os.path.join(os.environ['APPDATA'], 'Sublime Text 3', 'Packages', 'User')
   shutil.copy(os.path.join(base_dir, 'Preferences.sublime-settings'), user_directory)


def installForWindows():
   copyPreferencesOnWindows()


def symlinkPreferencesOnLinux():
   prefs_dotfile_path = os.path.join(base_dir, 'Preferences.sublime-settings')
   prefs_path = os.path.join(os.environ['HOME'], '.config', 'sublime-text-3',
      'Packages', 'User', 'Preferences.sublime-settings')
   if os.path.exists(prefs_path):
      print 'Removing existing Sublime Preferences symlink: %s' % prefs_path
      os.unlink(prefs_path)
   os.symlink(prefs_dotfile_path, prefs_path)


def installForLinux():
   symlinkPreferencesOnLinux()


if __name__ == '__main__':
   if sys.platform.startswith('win'):
      installForWindows()
      print "Finished!"
   elif sys.platform.startswith('linux'):
      installForLinux()
      print "Finished!"
   else:
      print 'OS %s not supported' % sys.platform