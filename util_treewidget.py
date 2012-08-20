from PyQt4.QtGui import *
from PyQt4.QtCore import *
from util_nofocusdelegate import NoFocusDelegate
class Tree_Widget(QTreeWidget):

    def __init__(self, parent=None):
        super(Tree_Widget, self).__init__(parent)
        # QTreeWidget.__init__(self)

        self.setAlternatingRowColors(False)
        self.setItemDelegate(NoFocusDelegate())
        ## flat view of tree
        # self.setIndentation(0)

        # self.setFocusPolicy(Qt.NoFocus)
        # self.setAcceptDrops(False)
        # self.setDragEnabled(True)
        # self.setDragDropMode(QAbstractItemView.DragOnly)
        # self.itemPressed.connect(self.on_itemPressed)



    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Space or key == Qt.Key_Return:
            cur_item = self.currentItem()
            if cur_item:
                self.itemDoubleClicked.emit(cur_item, 0)
                return
        if key == Qt.Key_J:
            event = QKeyEvent(QEvent.KeyPress, Qt.Key_Down, Qt.NoModifier)
        if key == Qt.Key_K:
            event = QKeyEvent(QEvent.KeyPress, Qt.Key_Up, Qt.NoModifier)
        if key == Qt.Key_H:
            event = QKeyEvent(QEvent.KeyPress, Qt.Key_Left, Qt.NoModifier)
        if key == Qt.Key_L:
            event = QKeyEvent(QEvent.KeyPress, Qt.Key_Right, Qt.NoModifier)

        ## pass the event up the chain or we will eat the event
        # QTreeWidget.keyPressEvent(self, event)
        super(Tree_Widget, self).keyPressEvent(event)

    def dropEvent(self, event):
        text = event.mimeData().text()
        print text
        item_list = self.findItems(title,Qt.MatchContains|Qt.MatchRecursive,0)
        if item_list:
            self.setCurrentItem(item_list[0])

    # def on_itemPressed(self, item, column):
    #     mimeData = QMimeData()
    #     mimeData.setText(item.statusTip(column))#, item.text())
    #     drag = QDrag(self)
    #     drag.setMimeData(mimeData)
    #     drag.exec_()
