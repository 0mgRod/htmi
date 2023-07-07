import sys
import os
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from tkinter import Tk, filedialog


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

    # Ask for the HTML file to view
    html_file_path = filedialog.askopenfilename(title="Select HTML File", filetypes=[("HTML Files", "*.html")])
    if not html_file_path:
        sys.exit()

    # Open HTML in PyQt5 window
    app = QApplication(sys.argv)
    window = HtmlWindow(html_file_path)
    window.show()
    sys.exit(app.exec_())
