
# Bash Basics

#### Data Types
 - Bash natively only has 3 data types: string, int, and lists
 - String and ints can be assigned as such:
    - ```my_name='cardinal'```             ```my_age=31 ```
    - Note that spaces around the '=' will error, ```my_age = 31```, etc.
    - You can reference your variable with the $ sign: ```$my_name```
 - Parameter expansion:
    - An assigned variable is known as a parameter in bash. Parameters are
      indicated with curly brackets: ```echo ${my_var}```
        - You don't always NEED curly brackets, but they help bash know exactly
          what your parameter name is. Helpful for contructing paths, for ex!
          ```my_path="/Users/${my_name}/Downloads"```
    - When bash reads and prints the value of $my_var, it is performing
      'parameter expansion' (PM). Parameters are expanded by default within the
      terminal. You use single vs double quotes to control expansion:
        - Single quotes: value is treated as literal, suppress expansion: 
        ```echo '$my_name'``` >>> ```$ my_name```
        - Double quotes: value is expanded 
        ```echo "$my_name"```, ```echo "${my_name}"``` >>> ```$ cardinal```
    - Best practice: use both double quotes and curly braces!
 - Indexing parameters: ```echo ${my_name:2:5}``` >>> ```$ rdina```
    - Remember bash uses 0-based indexing
 - String manipulation:
    - To uppercase: ```${my_name^^}```    Just the first var: ```${my_name^}```
    - To lowercase: ```${my_name,,}```    Just the first var: ```${my_name,}```
    - Find and replace: ```${my_name//old_string/new_string}```
                        ```echo ${my_name//ca/o}``` >>> ```$ ordinal```
    - Pattern matching: ```if [[ "$my_name" == *cardinal ]]; then...```
        - Do NOT quote the wildcard, interprets literally ('*cardinal')
 - Lists (technically 'arrays'):
    - Define list: ```my_list=("one" "two" "three")```
    - Access first item in list: ```echo ${my_list}```
    - Access list item by index: ```echo ${my_list[1]}``` (0-based indexing)
    - Expand entire list: ```echo ${my_list[@]}```
    - ```${@}```: A list of whatever was passed, use like kwargs/args in python
 - Command expansion:
    - Like parameters, commands can be executed and assigned to variables using
      parentheses:
        ```num_name_chars="$(echo $my_name | wc -c)"``` >> ```$ 9```
        - Like in parameter expansion, commands need to be surrounded in double
          quotes. Because the double quotes also surround $my_name, it is also
          expanded.
    - Use double quotes to perform math in bash:
        ```echo "In 1 year, I will be $((my_age+1)) years old"``
    - or use the bc utility (usually for more advanced math): 
        ```echo "my_age + 1 | bc -l"```

#### More String Manipulation
 - Heredoc: multi-line string
    - ```cat << EOF```
      ```echo "This is a here doc"```
      ```echo "It will just print to terminal"```
      ```EOF```
    - EOF is the delimiter; string will be anything between those words; can be
      any words as long as they are the same!
        - Unquoted EOF: expansion on by default
        - Quoted EOF ("EOF", 'EOF'): expansion does not occur
        - When using unquoted EOFs, may sometimes have to escape parameters and
          commands: ```echo "My name is \${my_name}"```, etc.
    - Heredocs are sensitive to whitespace - by default, everything inside the
      delimiters should be aligned right. You can use ```<<-``` instead of 
      ```<<``` to ignore leading whitespace. (AKA tab suppression)
    - Can pass heredoc to any command, but usually uses ```cat```.
    - Writing heredoc to file:
      ```cat << EOF > file.txt``` or ```cat > file.txt << EOF```
 - Here string: direct strings to a command: ```cat <<< $my_name```
    - No delimiter (and cannot suppress expansion?)

#### Special commands/characters, base:
 - ```$(pwd)``` or `pwd`: present working directory
    - Also '.': ```find . -type f```, etc.
 - ```cd -```: go to previous directory
 - ```cd ..```: go up one directory
 - ```~```: root directory
 - ```*```: wildcard, pattern matching: ```mv *.txt ..```
 - ```!```: NOT operator, such as ```! -f file.txt```, etc.
 - ```-eq, -gt , -lt```: equals, greater than, less than
 - ```\```: for multi-line commands, wraps to next line
    - Ex., ```sh some_script.sh parameter1 \```
           ```  parameter 2 \```
           ```  parameter 3 \```
           (executes as one line)
 - ```|``` (pipe): passes content of one command to other
 - ```&&``` AND, ```||``` OR: and/or commands
 - ```#```: Comments

#### Special commmands, advanced:
 - echo: prints to terminal ```echo $my_name```
   - ```echo "" > file.txt``` '>>' write to file, overwrite
   - ```echo "" >> file.txt``` '>>' write to file, append
 - ls: lists items in directory ```ls -l $directory```
 - cat: reads files/text: ```cat file.txt```
 - wc: Calculate length of words.text
    ```echo $my_name | wc -c```: Number of characters in $my_name
    ```cat file.txt | wc -l```: Number of lines in file.txt
 - Make directory: ```mkdir -p $directory``` (-p: make parents if not there)
 - Remove files: ```rm file.txt``` or directories: ```rm -r $directory```
 - Move files: ```mv file.txt ..```
 - grep: 
    - search for text: ```cat file.txt | grep "cardinal"```
    - Recursively search directory: ```grep -R 'cardinal' /path/```
    - Ignore binary files: 
      ```grep -r --binary-file=without-match "criteria" /path/  2>/dev/null```
 - cut: ```cut -d'delimiter' -f'position'```
    - Ex., ```echo $my_name | cut -d'a' -f1``` >>> ```$ c```
 - awk: ```awk -F'delimiter' '{print $position}'```
    - Ex., ```echo $my_name | awk -F'a' '{print $1}'``` >>> ```$ c```
 - find: ```find directory [options]```
    - Ex., ```find $(pwd) -type f``` to list files in current directory
    - Fav options:
        - ```-path```: specify path components
        - ```-inum N```: find by inode
        - ```-type```: f: files, d: directories
        - ```-name```: find by file name ```! *.csv```, etc. 
        - ```empty``` or ```-size 1M```: find empty
        - ```find . 2>/dev/null```: suppress permission errors
    - Find/exec: ```find . -type f -exec rm {} +``` ({} + indicates each item)
 - tree: list contents of a dir, recursive
    - ```tree $directory```: list ALL files in ALL directories
    - ```tree -L 2 $directory```: list everything 2 levels down in directory
 - Show space useage: ```du -sh .``` (-h: human readable)
    - Show items using the most space: ```du -ah | sort -rh | head -n 20```
 - Remove whitespace from file: ```sed -i 's/[[:space:]]*$//' $csv_file```
 - ```dirname $directory```, ```basename $directory```: parent/child of path

#### Loops
 - While loop:
    - csv file:
        ```while IFS=',' read -r col1 col2 col3; do```
        ```     do something```
        ```done < $csv_file```
 - for loop:
    ```for item in $directory/*; do```
    ```    do something```
    ```done```
 - if loop:
    ```if [ ! -d "$directory" ]; then```
    ```     do something```
    ```elif [ ! -d $other_directory ]; then```
    ```     do something```
    ```else```
    ```     do something```
    ```fi```
    - Absolutely need spaces between criteria ('! -f...') and []
    - In this form, absolutely need double quotes to expand 
    - Common if flags: ```-f, ! -d, -z, -n```

#### To add:
 - in-terminal text editors: vim, nano && keybinds (Ctrl+C, etc.)
 - realpath
 - head/tail
 - tree: needs to be installed?
 - chmod / chown
 - keybinds (Ctrl+C, Ctrl+A, Ctrl+E, Ctrl+U, Cmd+Opt+C, Esc+B, Esc+Del, 
   Opt+Click)
 - ~/.bashrc

#### References
 - https://linuxize.com/post/bash-heredoc/
 - https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html