# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ryan/local/scripts/python/discipline/widget_editor.ui'
#
# Created: Tue Jul 24 10:47:43 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from util_plaintext import PlaintextEditor
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_widget_editor(object):
    def setupUi(self, widget_editor):
        widget_editor.setObjectName(_fromUtf8("widget_editor"))
        widget_editor.resize(489, 500)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widget_editor.sizePolicy().hasHeightForWidth())
        widget_editor.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(widget_editor)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn_editor_submit = QtGui.QPushButton(widget_editor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_editor_submit.sizePolicy().hasHeightForWidth())
        self.btn_editor_submit.setSizePolicy(sizePolicy)
        self.btn_editor_submit.setMinimumSize(QtCore.QSize(25, 25))
        self.btn_editor_submit.setMaximumSize(QtCore.QSize(30, 27))
        self.btn_editor_submit.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/img/apply.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_editor_submit.setIcon(icon)
        self.btn_editor_submit.setIconSize(QtCore.QSize(16, 16))
        self.btn_editor_submit.setObjectName(_fromUtf8("btn_editor_submit"))
        self.horizontalLayout.addWidget(self.btn_editor_submit)
        self.edit_line_editor_sub = QtGui.QLineEdit(widget_editor)
        self.edit_line_editor_sub.setObjectName(_fromUtf8("edit_line_editor_sub"))
        self.horizontalLayout.addWidget(self.edit_line_editor_sub)
        self.btn_editor_delete = QtGui.QPushButton(widget_editor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_editor_delete.sizePolicy().hasHeightForWidth())
        self.btn_editor_delete.setSizePolicy(sizePolicy)
        self.btn_editor_delete.setMinimumSize(QtCore.QSize(25, 25))
        self.btn_editor_delete.setMaximumSize(QtCore.QSize(30, 27))
        self.btn_editor_delete.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/img/reinhardticons-0.10-svg/scalable/actions/delete.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_editor_delete.setIcon(icon1)
        self.btn_editor_delete.setIconSize(QtCore.QSize(16, 16))
        self.btn_editor_delete.setObjectName(_fromUtf8("btn_editor_delete"))
        self.horizontalLayout.addWidget(self.btn_editor_delete)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.edit_plaintext = PlaintextEditor(widget_editor)
        self.edit_plaintext.setObjectName(_fromUtf8("edit_plaintext"))
        self.verticalLayout.addWidget(self.edit_plaintext)
        self.lb_editor_id = QtGui.QLabel(widget_editor)
        self.lb_editor_id.setObjectName(_fromUtf8("lb_editor_id"))
        self.verticalLayout.addWidget(self.lb_editor_id)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lb_editor_category = QtGui.QLabel(widget_editor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_editor_category.sizePolicy().hasHeightForWidth())
        self.lb_editor_category.setSizePolicy(sizePolicy)
        self.lb_editor_category.setObjectName(_fromUtf8("lb_editor_category"))
        self.horizontalLayout_3.addWidget(self.lb_editor_category)
        self.cb_editor_category = QtGui.QComboBox(widget_editor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_editor_category.sizePolicy().hasHeightForWidth())
        self.cb_editor_category.setSizePolicy(sizePolicy)
        self.cb_editor_category.setEditable(True)
        self.cb_editor_category.setObjectName(_fromUtf8("cb_editor_category"))
        self.horizontalLayout_3.addWidget(self.cb_editor_category)
        self.lb_editor_state = QtGui.QLabel(widget_editor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_editor_state.sizePolicy().hasHeightForWidth())
        self.lb_editor_state.setSizePolicy(sizePolicy)
        self.lb_editor_state.setObjectName(_fromUtf8("lb_editor_state"))
        self.horizontalLayout_3.addWidget(self.lb_editor_state)
        self.cb_editor_state = QtGui.QComboBox(widget_editor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_editor_state.sizePolicy().hasHeightForWidth())
        self.cb_editor_state.setSizePolicy(sizePolicy)
        self.cb_editor_state.setAutoFillBackground(False)
        self.cb_editor_state.setEditable(False)
        self.cb_editor_state.setObjectName(_fromUtf8("cb_editor_state"))
        self.horizontalLayout_3.addWidget(self.cb_editor_state)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.lb_editor_id.setBuddy(self.edit_plaintext)
        self.lb_editor_category.setBuddy(self.cb_editor_category)
        self.lb_editor_state.setBuddy(self.cb_editor_state)

        self.retranslateUi(widget_editor)
        QtCore.QMetaObject.connectSlotsByName(widget_editor)

    def retranslateUi(self, widget_editor):
        widget_editor.setWindowTitle(QtGui.QApplication.translate("widget_editor", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_editor_id.setText(QtGui.QApplication.translate("widget_editor", "Edito&r", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_editor_category.setText(QtGui.QApplication.translate("widget_editor", "&Category:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_editor_state.setText(QtGui.QApplication.translate("widget_editor", "St&ate:", None, QtGui.QApplication.UnicodeUTF8))

import icon_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    widget_editor = QtGui.QWidget()
    ui = Ui_widget_editor()
    ui.setupUi(widget_editor)
    widget_editor.show()
    sys.exit(app.exec_())
