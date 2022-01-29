# Add a `r` function to zsh that opens ranger either at the given directory or
# at the one autojump suggests
r() {
  if [ "$1" != "" ]; then
    if [ -d "$1" ]; then
      ranger "$1"
    elif [ -f "$1" ]; then
      ranger --selectfile="$1"
    else
      out="$(autojump $1)"
      if [ -d "$out" ]; then
        ranger "$out"
      else
        ranger --selectfile="$out"
      fi
    fi
  else
    ranger
  fi
	return $?
}


