# Add a `r` function to zsh that opens ranger either at the given directory or
# at the one autojump suggests
r() {
  if [ "$1" != "" ]; then
    if [ -d "$1" ]; then
      ranger "$1"
    else
      ranger "$(autojump $1)"
    fi
  else
    ranger
  fi
	return $?
}
