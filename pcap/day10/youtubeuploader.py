from pcap.day10.uploader import Uploader


class YoutubeUploader(Uploader):
    def __init__(self, filename=None):
        Uploader.__init__(self, filename)

    # Prevent accidental overrides
    # and misuse, we add the double underscore
    # before the name.
    # This is a private method, that
    # subclasses shouldn't be able to override.
    def __get_file_from_tkinter(self):
        return "some_file.png"
