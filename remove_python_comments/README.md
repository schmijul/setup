
1.- Create a bin directory in your home directory
`mkdir -p ~/bin `

2.- Move the remove_python_comments.py script to the bin directory
` mv /home/schmijul/source/repos/agv_demo/gui/new_appearance/remove_python_comments.py ~/bin/ `

3.- Open your .bashrc file for editing
`nano ~/.bashrc`

4.- Add the following line at the end of the .bashrc file to create an alias
`alias removecomments="python3 ~/bin/remove_python_comments.py"`

5.- Save the .bashrc file and exit the editor

6.- Source the updated .bashrc file to apply the changes
`source ~/.bashrc`

