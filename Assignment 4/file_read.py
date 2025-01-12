def modify_file_content(input_filename, output_filename):
   
    try:
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()

        modified_lines = [line.strip() + " - Modified content!\n" for line in lines]

        
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_lines)

        print(f"Modified content has been written to '{output_filename}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError as e:
        print(f"Error: Unable to read/write file. Details: {e}")

if __name__ == "__main__":
    
    input_file = input("Enter the name of the file to read from: ")
    output_file = input("Enter the name of the file to write to: ")

    modify_file_content(input_file, output_file)
