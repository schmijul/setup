import sys
import os

def remove_commented_lines(input_file):
    output_file = os.path.splitext(input_file)[0] + "_nocomments.py"
    with open(input_file, 'r') as input_file:
        with open(output_file, 'w') as output_file:
            for line in input_file:
                if not line.strip().startswith('#'):
                    output_file.write(line)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the input file name as a parameter.")
    else:
        input_file_name = sys.argv[1]
        remove_commented_lines(input_file_name)
        print("The commented lines have been removed. The output file is named:", os.path.splitext(input_file_name)[0] + "_nocomments.py")

