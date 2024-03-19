from app.io.input import get_user_input, read_file, read_file_with_pandas
from app.io.output import print_to_console, write_to_file

def main():
    console_input = get_user_input()
    file_input = read_file("data/test.txt")
    pandas_input = read_file_with_pandas("data/test.csv")
    print_to_console(console_input)
    print_to_console(file_input)
    print_to_console(pandas_input)
    write_to_file(console_input, "data/output.txt")
    write_to_file(file_input, "data/output.txt")
    write_to_file(pandas_input, "data/output.txt")

if __name__ == "__main__":
    main()
