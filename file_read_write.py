

def read_and_modify_file(input_filename, output_filename):
    try:

        with open(input_filename, "r", encoding="utf-8") as infile:
            content = infile.read()

        
        modified_content = content.upper()  # Example modification: convert to uppercase
        with open(output_filename, "w", encoding="utf-8") as outfile:
            outfile.write(modified_content)

        print(f"✅ File '{input_filename}' was successfully read.")
        print(f"✍️ Modified content has been written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"❌ Error: Permission denied when accessing '{input_filename}'.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


if __name__ == "__main__":
    input_file = input("Enter the name of the file to read: ").strip()
    output_file = "modified_" + input_file
    read_and_modify_file(input_file, output_file)  # ✅ correct function call

