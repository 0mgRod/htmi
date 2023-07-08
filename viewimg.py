import sys
import os
import tempfile
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from tkinter import Tk, filedialog
import gzip


class HtmlWindow(QMainWindow):
    def __init__(self, html_path):
        super().__init__()
        self.setWindowTitle("HTML Viewer")
        self.resize(800, 600)

        web_view = QWebEngineView()
        layout = QVBoxLayout()
        layout.addWidget(web_view)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        web_view.load(QUrl.fromLocalFile(html_path))


if __name__ == '__main__':
    # Create a Tkinter root window
    root = Tk()
    root.withdraw()

    # Define the file type filter
    file_types = [("HTML Files", "*.html"), ("GZ Files", "*.gz")]

    # Ask for the HTML or GZ file to view
    html_file_path = filedialog.askopenfilename(title="Select HTML or GZ File", filetypes=file_types)
    if not html_file_path:
        sys.exit()

    # Decompress the file if it is a GZ file
    if html_file_path.endswith(".gz"):
        uncompressed_path = os.path.join(tempfile.gettempdir(), "output.html")
        with open(uncompressed_path, 'wb') as output_file, gzip.open(html_file_path, 'rb') as input_file:
            output_file.write(input_file.read())
        html_file_path = uncompressed_path

    # Open HTML in PyQt5 window
    app = QApplication(sys.argv)
    window = HtmlWindow(html_file_path)
    window.show()
    sys.exit(app.exec_())
