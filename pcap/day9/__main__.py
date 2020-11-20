"""Docstring for __main__.py"""

from pcap.day9.uploader import Uploader

# If this file is being run directly
# instead of being imported
if __name__ == "__main__":
    uploader = Uploader()
    uploader.upload()
    print(uploader.url)
