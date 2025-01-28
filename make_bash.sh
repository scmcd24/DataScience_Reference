#!/usr/bin/bash

# VERS: 28JAN2025
# If script doesn't exist, write it with a date/description
# If it does, make a copy w/ SOC

script_name=${1}
description=${2}
copy_change="${3:-copy}"

if [[ $script_name == *help* ]]; then
    echo "Usage: make_bash.sh <script_name> <description> <copy_change>"
    exit 0
fi

current_date=$(date +'%d%b%Y')
current_date="${current_date^^}"

if [ -f "${script_name}.sh" ]; then
    echo "collating files"
    contents="Continued from ${script_name}.sh:
    $(tail -n +2 "${script_name}.sh")"
    script_basename="${script_name: :-10}"
    script_file="${script_basename}_${copy_change}_${current_date}.sh"
else
    script_file="${script_name}_${current_date}.sh"
fi

cat > "${script_file}" << EOF
#!/usr/bin/bash

# VERS: ${current_date}
# ${description}

${contents}
EOF


# Add to your bashrc:
mkscript () {
    sh /path/to/make_bash.sh "${@}"
}
