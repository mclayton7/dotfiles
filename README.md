# dotfiles
This is a collection of configuration files for my development VMs.

## To Install
* clone this repo in your home directory
* Then run the install.sh script

## Configured Apps

### Vim (http://www.vim.org/)
* Includes YouCompleteMe support for C++ syntax highlighting in Waf projects (https://github.com/Valloric/YouCompleteMe)
* Vundle to manage plugins (https://github.com/VundleVim/Vundle.vim)

### Sublime Text (http://www.sublimetext.com/3)
* Helpful snippets and such

### GDB (https://www.gnu.org/software/gdb/)
* Qt4 Pretty Printing (for QStrings, Qt Containers, etc.)
* Enabling command history (saves previous commands so you don't have to retype or copy/paste file names)

### Aliases
* Sourcing and cd'ing to development environments automatically
* Using '..' to automatically cd to the parent directory
* Always 'sudo yum' when using Yum

### Git (https://git-scm.com/)
* Add colors
* Use Meld as a diff tool
* Trim trailing whitespace

### Scripts
* runUntilFailure - Will run a unit or acceptance test until it fails

### Zsh (http://www.zsh.org/)
* Use Presto  (https://github.com/sorin-ionescu/prezto)
* Add shell aliases
* Add dotfile scripts automatically
* adds /opt/clang and /opt/qtcreator paths


# Todo
* Add Windows Support
* Make shell scripts cross platform (Python?)
