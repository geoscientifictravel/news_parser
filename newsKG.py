import sys, re, urllib, html2text
from urllib import request

# Импортируем наш интерфейс
from newsform import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.newsurl=[]
        self.Parse()
        

        # Здесь прописываетс событие нажатие на конпку
        self.ui.pushButton.clicked.connect(self.AllNews)

    # Пока пуста функция, которая выполнетс при нажатии на кнопку
    def Parse(self):
        s = 'https://kloop.kg/news/'
        doc = urllib.request.urlopen(s).read().decode('utf-8', errors='ignore')
        doc = doc.replace('\n','')
        zagolovki = re.findall('<a href="(.+?)</a>', doc)
        for x in zagolovki:
            self.newsurl.append(x.split('" >')[0])
            self.ui.listWidget.addItem(x.split('" >')[1].strip())

    def AllNews(self):
        n = self.ui.listWidget.currentRow()
        u = 'https://kloop.kg/news/'+self.newsurl[n]
        doc = urllib.request.urlopen(u).read().decode('utf-8', errors='ignore')
        h = html2text.HTML2Text()
        h.ignore_links = True
        h.body_width = False
        h.ignore_images = True
        doc = h.handle(doc)
        mas = doc.split('\n')
        stroka = ''
        for x in mas:
            if(len(x)>90):
                stroka = stroka+x+'\n\n'
        self.ui.textEdit.setText(stroka)
        

        
        
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())


    
