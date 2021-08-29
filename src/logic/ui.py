import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QFileDialog, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget

from photo_service import PhotoService


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.path = ''
        self.destination_path = ''
        self.path_label = QLabel('')
        self.destination_path_label = QLabel('')
        self.ids = QLineEdit()

        self.setWindowTitle("My App")
        wid = QWidget(self)
        self.setCentralWidget(wid)
        layout = QVBoxLayout()
        start_button = QPushButton('Przenieś')
        start_button.clicked.connect(self.run_moving_photos)

        layout.addWidget(self.createPath())
        layout.addWidget(self.createDestPath())
        layout.addWidget(self.createIdWidget())
        layout.addWidget(start_button)
        # Set the layout on the application's window
        wid.setLayout(layout)


    def createPath(self):
        widget = QWidget()
        widgetLayout = QHBoxLayout()
        pathButton = QPushButton("Wybierz folder ze zdjęciami")
        pathButton.clicked.connect(self.dialog_path);
        widgetLayout.addWidget(pathButton)
        widgetLayout.addWidget(self.path_label)
        widget.setLayout(widgetLayout);
        return widget

    def createDestPath(self):
        widget = QWidget()
        widgetLayout = QHBoxLayout()
        pathButton = QPushButton("Wybierz folder do przeniesienia")
        pathButton.clicked.connect(self.dialog_dest_path);
        widgetLayout.addWidget(pathButton)
        widgetLayout.addWidget(self.destination_path_label)
        widget.setLayout(widgetLayout);
        return widget

    def createIdWidget(self):
        id_widget = QWidget()
        id_widget_layout = QHBoxLayout()
        id_widget_layout.addWidget(QLabel('Podaj id zdjęć do przeniesienia'))
        id_widget_layout.addWidget(self.ids)
        id_widget.setLayout(id_widget_layout);
        return id_widget


    def dialog_path(self):
        self.path = self.createFileDialog()
        self.path_label.setText(self.path)

    def dialog_dest_path(self):
        self.destination_path = self.createFileDialog()
        self.destination_path_label.setText(self.destination_path)

    def createFileDialog(self):
        return QFileDialog().getExistingDirectory(self, 'Wybierz katalog')

    def run_moving_photos(self):
        print(self.path)
        print(self.destination_path)
        print(self.ids.text())
        ids = list(map(lambda id: id.strip(), self.ids.text().split(',')))
        print(ids)
        photo_service = PhotoService(self.path, self.destination_path, ids)
        photo_service.move_photos()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()