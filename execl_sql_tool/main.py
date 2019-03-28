from execl_sql_tool.pyqt_UI.execl_tool import *
from execl_sql_tool.pyqt_UI.config import *
from execl_sql_tool.pyqt_UI.info import *
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog
import sys

class mainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)

class configWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=Ui_conf_Dialog()
        self.child.setupUi(self)

class infoWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=Ui_info_Dialog()
        self.child.setupUi(self)

if __name__=='__main__':
    app = QApplication(sys.argv)
    main = mainWindow()
    config = configWindow()
    info = infoWindow()
    config_ui = main.main_ui.actionconfig
    info_ui = main.main_ui.actionversion
    config_ui.triggered.connect(config.show)
    info_ui.triggered.connect(info.show)
    main.show()
    sys.exit(app.exec_())