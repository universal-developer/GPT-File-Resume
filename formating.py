def remove_timestamps(input_file, output_file):
    try:
        # Read input text from the file
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Remove lines containing timestamps
        filtered_lines = [line for line in lines if not any(
            c.isdigit() for c in line)]

        # Write filtered lines to the output file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.writelines(filtered_lines)

        print(f"Timestamps removed. Cleaned text written to '{output_file}'")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
input_file = 'input.txt'
output_file = 'cleaned_transcript.txt'
remove_timestamps(input_file, output_file)
