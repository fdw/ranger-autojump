# Ranger & Autojump

This plugin for ranger adds complete support for [autojump](https://github.com/wting/autojump) to [ranger](https://github.com/ranger/ranger):
Whenever a new directory is opened in ranger, autojump is notified and can change the weights accordingly.
Using `:j` you can use autojump to jump to a directory. This is made even better by adding `map cj console j ` to your `rc.conf`. 

## Installation
Copy `autojump.py` to `{$XDG_CONFIG_HOME}/ranger/plugins`.
