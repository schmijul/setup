# setup as bin/bash command


1.- Navigate to your home directory
`cd ~`

2.- Create a directory called "bin" if it doesn't already exist
`mkdir -p bin`

3.- Open your .bashrc file for editing
`nano .bashrc`

4.- Add the following line at the end of the file
`export PATH="$HOME/bin:$PATH"`

5.- Save the .bashrc file and close the editor

6.- Navigate to the "bin" directory
`cd bin`

7.- Create a symbolic link to your Bash script
`ln -s /full/path/to/script/remove_comments.sh remove_comments`
8.- Replace "/full/path/to/script" with the actual path to the directory where your Bash script remove_comments.sh is located

9.- Set the execute permission for the Bash script
`chmod +x remove_comments.sh`

# Start a new shell session or reload the .bashrc file
`source ~/.bashrc`

