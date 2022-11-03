import sys
import youtube_dl
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon

class window_donloader(QMainWindow):
    def __init__(self):
        super(window_donloader, self).__init__()
        self.setGeometry(800, 300, 500, 500)
        self.setWindowTitle("YouTube Downloader By Norbert Wrzos")
        self.setWindowIcon(QIcon("icon.jpg"))
        self.Link()

    def Link(self):
        self.lbl_link = QtWidgets.QLabel(self)
        self.lbl_link.setText('Enter your link :')
        self.lbl_link.move(200, 200)
        self.text_link = QtWidgets.QLineEdit(self)
        self.text_link.move(200, 240)

        self.btn_download = QtWidgets.QPushButton(self)
        self.btn_download.setText('Download')
        self.btn_download.clicked.connect(self.downloader)
        self.btn_download.move(200, 280)

    def downloader(self):
        video_info = youtube_dl.YoutubeDL().extract_info(
            url=self.text_link.text(), download=False
        )
        filename = f"{video_info['title']}.mp3"
        options = {
            'format': 'bestaudio/best',
            'keepvideo': False,
            'outtmpl': filename,
        }
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])
def window():
    app = QApplication(sys.argv)
    win = window_donloader()
    win.show()
    sys.exit(app.exec())


window()
