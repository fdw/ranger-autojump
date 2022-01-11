# Ranger & Autojump

This plugin for ranger adds complete support for [autojump](https://github.com/wting/autojump) to [ranger](https://github.com/ranger/ranger):
Whenever a new directory is opened in ranger, autojump is notified and can change the weights accordingly.
Using `:j` you can use autojump to jump to a directory. This is made even better by adding `map cj console j%space` to your `rc.conf`. Thus typing `cj dirname` will let you jump to dirname.

As an added bonus, there is a zsh plugin introducing a new function called `r`. Without arguments, it just opens ranger. If you supply an argument that is a directory, ranger is opened in that directory. But if you supply anything else as an argument, `autojump` is called with the argument and `ranger` is opened there 🧙

If you want similar functionality for [zoxide](https://github.com/ajeetdsouza/zoxide), you can try [ranger-zoxide](https://github.com/fdw/ranger-zoxide).

# Installation
### Ranger plugin
- Copy `autojump.py` to `${XDG_CONFIG_HOME}/ranger/plugins`.
- Add the following mapping to your `rc.conf` for convenience:
	```
	map cj console j%space
	```
	


### vim plugin (optional extra)
- To use autojump with vim, the [autojump.vim](https://github.com/trotter/autojump.vim) plugin can be installed. This can also be integrated with ZSH as shown below.

### zsh plugin
- Install the zsh plugin using your favorite plugin manager, e.g.:
	-	[zgen](https://github.com/tarjoilija/zgen): 
		-	`zgen load fdw/ranger_autojump`
	- [oh-my-zsh](https://github.com/ohmyzsh/ohmyzsh): 
		1. Clone this repository into oh-my-zsh's plugin directory:
			```
			git clone https://github.com/fdw/ranger-autojump ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/ranger-autojump
			```
		2. Activate the plugin in `~/.zshrc`:
			 ```
			 plugins=( [plugins...] ranger-autojump)
			 ```
- (Optional) For vim integration add the following convenience function to your .zshrc:
```
function jvim { file="$(AUTOJUMP_DATA_DIR=~/.autojump.vim/global autojump $@)"; if [ -n "$file" ]; then vim "$file"; fi }
```

