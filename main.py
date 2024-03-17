import app.io.input as input
import app.io.output as output


def main():
    console_input = input.console_input()
    print(console_input)

    file_input = input.file_input('data/test.txt')
    print(file_input)

    file_input_pandas = input.file_input_pandas('data/test_csv.csv')
    print(file_input_pandas)

    output_text = console_input + file_input + file_input_pandas.to_string(index=False)
    output.file_write('data/output.txt', output_text)

if __name__ == '__main__':
    main()
