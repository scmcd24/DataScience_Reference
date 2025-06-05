
# color format
GREEN="\[$(tput setaf 2)\]"
BLUE="\[$(tput setaf 4)\]"
PURPLE="\[$(tput setaf 5)\]"
RESET="\[$(tput sgr0)\]"

PS1="${GREEN}(base) \h:\W \u ${PURPLE}$ "
trap 'echo -ne "\033[0m"' DEBUG

# pwd/user in green, command in purple, output text=default


