# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ryan/local/scripts/python/discipline/main.ui'
#
# Created: Wed Jul 25 15:51:04 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from util_treewidget import Tree_Widget
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(480, 600)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget_query = Widget_Query(self.centralWidget)
        self.widget_query.setObjectName(_fromUtf8("widget_query"))
        self.verticalLayout.addWidget(self.widget_query)
        self.widget_tree = Tree_Widget(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_tree.sizePolicy().hasHeightForWidth())
        self.widget_tree.setSizePolicy(sizePolicy)
        self.widget_tree.setMouseTracking(True)
        self.widget_tree.setLineWidth(1)
        self.widget_tree.setDragEnabled(True)
        self.widget_tree.setDragDropMode(QtGui.QAbstractItemView.DragOnly)
        self.widget_tree.setObjectName(_fromUtf8("widget_tree"))
        self.verticalLayout.addWidget(self.widget_tree)
        self.widget_editor = Widget_Editor(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_editor.sizePolicy().hasHeightForWidth())
        self.widget_editor.setSizePolicy(sizePolicy)
        self.widget_editor.setMinimumSize(QtCore.QSize(0, 395))
        self.widget_editor.setObjectName(_fromUtf8("widget_editor"))
        self.verticalLayout.addWidget(self.widget_editor)
        MainWindow.setCentralWidget(self.centralWidget)
        self.bar_status = QtGui.QStatusBar(MainWindow)
        self.bar_status.setSizeGripEnabled(False)
        self.bar_status.setObjectName(_fromUtf8("bar_status"))
        MainWindow.setStatusBar(self.bar_status)
        self.bar_menu = QtGui.QMenuBar(MainWindow)
        self.bar_menu.setGeometry(QtCore.QRect(0, 0, 480, 22))
        self.bar_menu.setObjectName(_fromUtf8("bar_menu"))
        self.menuFile = QtGui.QMenu(self.bar_menu)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuTools = QtGui.QMenu(self.bar_menu)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        MainWindow.setMenuBar(self.bar_menu)
        self.actionShow_Query_Widget = QtGui.QAction(MainWindow)
        self.actionShow_Query_Widget.setCheckable(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/img/filter.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShow_Query_Widget.setIcon(icon)
        self.actionShow_Query_Widget.setObjectName(_fromUtf8("actionShow_Query_Widget"))
        self.actionJOE_Editor = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/img/reinhardticons-0.10-svg/scalable/actions/filenew.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionJOE_Editor.setIcon(icon1)
        self.actionJOE_Editor.setObjectName(_fromUtf8("actionJOE_Editor"))
        self.actionTree_Collapse_All = QtGui.QAction(MainWindow)
        self.actionTree_Collapse_All.setObjectName(_fromUtf8("actionTree_Collapse_All"))
        self.actionTree_Expand_All = QtGui.QAction(MainWindow)
        self.actionTree_Expand_All.setObjectName(_fromUtf8("actionTree_Expand_All"))
        self.actionFocus_Tree = QtGui.QAction(MainWindow)
        self.actionFocus_Tree.setObjectName(_fromUtf8("actionFocus_Tree"))
        self.actionSave_Note = QtGui.QAction(MainWindow)
        self.actionSave_Note.setObjectName(_fromUtf8("actionSave_Note"))
        self.actionInsert_or_Goto_Tree_Item = QtGui.QAction(MainWindow)
        self.actionInsert_or_Goto_Tree_Item.setObjectName(_fromUtf8("actionInsert_or_Goto_Tree_Item"))
        self.actionImport_Phatnotes_File = QtGui.QAction(MainWindow)
        self.actionImport_Phatnotes_File.setObjectName(_fromUtf8("actionImport_Phatnotes_File"))
        self.actionBackward = QtGui.QAction(MainWindow)
        self.actionBackward.setObjectName(_fromUtf8("actionBackward"))
        self.actionForward = QtGui.QAction(MainWindow)
        self.actionForward.setObjectName(_fromUtf8("actionForward"))
        self.menuFile.addAction(self.actionJOE_Editor)
        self.menuFile.addAction(self.actionShow_Query_Widget)
        self.menuFile.addAction(self.actionTree_Collapse_All)
        self.menuFile.addAction(self.actionTree_Expand_All)
        self.menuFile.addAction(self.actionFocus_Tree)
        self.menuFile.addAction(self.actionSave_Note)
        self.menuFile.addAction(self.actionInsert_or_Goto_Tree_Item)
        self.menuFile.addAction(self.actionBackward)
        self.menuFile.addAction(self.actionForward)
        self.menuTools.addAction(self.actionImport_Phatnotes_File)
        self.bar_menu.addAction(self.menuFile.menuAction())
        self.bar_menu.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.widget_tree.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTools.setTitle(QtGui.QApplication.translate("MainWindow", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_Query_Widget.setText(QtGui.QApplication.translate("MainWindow", "Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_Query_Widget.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionJOE_Editor.setText(QtGui.QApplication.translate("MainWindow", "Jump or Execute a Note or new", None, QtGui.QApplication.UnicodeUTF8))
        self.actionJOE_Editor.setToolTip(QtGui.QApplication.translate("MainWindow", "Jump or Execute a note blank or not.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionJOE_Editor.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTree_Collapse_All.setText(QtGui.QApplication.translate("MainWindow", "Tree Collapse All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTree_Collapse_All.setShortcut(QtGui.QApplication.translate("MainWindow", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTree_Expand_All.setText(QtGui.QApplication.translate("MainWindow", "Tree Expand All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTree_Expand_All.setShortcut(QtGui.QApplication.translate("MainWindow", "E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFocus_Tree.setText(QtGui.QApplication.translate("MainWindow", "Focus Tree", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFocus_Tree.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+T", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Note.setText(QtGui.QApplication.translate("MainWindow", "Save Note", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Note.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInsert_or_Goto_Tree_Item.setText(QtGui.QApplication.translate("MainWindow", "Insert or Goto Tree Item", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInsert_or_Goto_Tree_Item.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+L", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport_Phatnotes_File.setText(QtGui.QApplication.translate("MainWindow", "Import Phatnotes File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBackward.setText(QtGui.QApplication.translate("MainWindow", "Backward", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBackward.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionForward.setText(QtGui.QApplication.translate("MainWindow", "Forward", None, QtGui.QApplication.UnicodeUTF8))
        self.actionForward.setToolTip(QtGui.QApplication.translate("MainWindow", "Forward", None, QtGui.QApplication.UnicodeUTF8))
        self.actionForward.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+I", None, QtGui.QApplication.UnicodeUTF8))

from widget_query import Widget_Query
from widget_editor import Widget_Editor
import icon_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
