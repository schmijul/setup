setup as bin/bash command


# Navigate to your home directory
`cd ~

# Create a directory called "bin" if it doesn't already exist
`mkdir -p bin

# Open your .bashrc file for editing
`nano .bashrc

# Add the following line at the end of the file
`export PATH="$HOME/bin:$PATH"

# Save the .bashrc file and close the editor

# Navigate to the "bin" directory
`cd bin

# Create a symbolic link to your Bash script
`ln -s /full/path/to/script/remove_comments.sh remove_comments`
# Replace "/full/path/to/script" with the actual path to the directory where your Bash script remove_comments.sh is located

# Set the execute permission for the Bash script
`chmod +x remove_comments.sh

# Start a new shell session or reload the .bashrc file
`source ~/.bashrc`

