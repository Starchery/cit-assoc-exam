import requests
import sys
import tkinter
import tkinter.filedialog


class Uploader:
    def __init__(self, filename=None):
        print("Getting file from argument")
        self.filename = (
            filename
            or self.__get_file_from_argv()
            or self.__get_file_from_tkinter()
        )

        self.url = None

    def upload(self):
        print("Sending POST request to http://0x0.st")
        try:
            with open(self.filename, "rb") as f:
                response = requests.post(
                    url="http://0x0.st", files={"file": f}
                )
                self.url = response.text.strip()
        except FileNotFoundError:
            print(f"The file {self.filename} doesn't exist.", file=sys.stderr)
            print("Upload failed.", file=sys.stderr)

    def __get_file_from_tkinter(self) -> str:
        print("Getting file from Tkinter")
        console_window = tkinter.Tk()
        console_window.withdraw()
        filename = tkinter.filedialog.askopenfilename()
        return filename

    def __get_file_from_argv(self):
        print("Getting file from argv")
        try:
            return sys.argv[1]
        except IndexError:
            return None
