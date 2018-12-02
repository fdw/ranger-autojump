# Ranger & Autojump

This plugin for ranger adds complete support for [autojump](https://github.com/wting/autojump) to [ranger](https://github.com/ranger/ranger):
Whenever a new directory is opened in ranger, autojump is notified and can change the weights accordingly.
Using `:j` you can use autojump to jump to a directory. This is made even better by adding `map cj console j ` to your `rc.conf`. 

As an added bonus, there is a zsh plugin introducing a new `r` function. Without arguments, it just opens ranger. If you supply an argument which is also a directory, ranger is open in that directory. But if you supply anything else as an argument, `autojump` is called with the argument and `ranger` is opened there.

## Installation
### Ranger plugin
Copy `autojump.py` to `{$XDG_CONFIG_HOME}/ranger/plugins`.

### zsh plugin
Install the zsh plugin using your favorite plugin manager, for example [zgen](https://github.com/tarjoilija/zgen): `zgen load fdw/ranger_autojump`
