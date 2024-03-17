import pandas as pd
import pytest

from app.io.input import file_input, file_input_pandas


class TestInput:

    def test_file_input(self):
        with open("../../data/test_1.txt", "w") as f:
            f.write("Hello, world!")
            f.close()
        assert file_input("../../data/test_1.txt") == "Hello, world!"

    def test_file_input_invalid_path(self):
        with pytest.raises(FileNotFoundError):
            file_input("non_existing_file.txt")

    def test_file_input_empty(self):
        with open("../../data/test_1.txt", "w") as f:
            f.write("")
            f.close()
        assert file_input("../../data/test_1.txt") == ""

    def test_file_input_pandas_invalid_path(self):
        with pytest.raises(FileNotFoundError):
            file_input_pandas("non_existing_file.txt")

    def test_file_input_pandas(self):
        df_expected = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
        df_expected.to_csv("../../data/test.csv", index=False)
        pandas_input = file_input_pandas("../../data/test.csv")
        print(pandas_input)
        print(df_expected)
        pd.testing.assert_frame_equal(pandas_input, df_expected)

    def test_file_input_pandas_empty_file(self):
        with open("../../data/test_1.csv", "w") as f:
            f.write("")
            f.close()

        with pytest.raises(pd.errors.EmptyDataError):
            file_input_pandas("../../data/test_1.csv")
