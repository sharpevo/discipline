# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ryan/local/scripts/python/discipline/widget_query.ui'
#
# Created: Sat Jul 21 17:07:46 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Query(object):
    def setupUi(self, Query):
        Query.setObjectName(_fromUtf8("Query"))
        Query.resize(351, 75)
        self.horizontalLayout = QtGui.QHBoxLayout(Query)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.lb_view_query = QtGui.QLabel(Query)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.lb_view_query.setFont(font)
        self.lb_view_query.setObjectName(_fromUtf8("lb_view_query"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lb_view_query)
        self.edit_line_view_query = QtGui.QLineEdit(Query)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.edit_line_view_query.setFont(font)
        self.edit_line_view_query.setObjectName(_fromUtf8("edit_line_view_query"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.edit_line_view_query)
        self.lb_sql_query = QtGui.QLabel(Query)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.lb_sql_query.setFont(font)
        self.lb_sql_query.setObjectName(_fromUtf8("lb_sql_query"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lb_sql_query)
        self.edit_line_sql_query = QtGui.QLineEdit(Query)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.edit_line_sql_query.setFont(font)
        self.edit_line_sql_query.setObjectName(_fromUtf8("edit_line_sql_query"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.edit_line_sql_query)
        self.horizontalLayout.addLayout(self.formLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btn_submit_query = QtGui.QPushButton(Query)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_submit_query.sizePolicy().hasHeightForWidth())
        self.btn_submit_query.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.btn_submit_query.setFont(font)
        self.btn_submit_query.setObjectName(_fromUtf8("btn_submit_query"))
        self.verticalLayout.addWidget(self.btn_submit_query)
        self.cb_query = QtGui.QComboBox(Query)
        self.cb_query.setObjectName(_fromUtf8("cb_query"))
        self.verticalLayout.addWidget(self.cb_query)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.lb_view_query.setBuddy(self.edit_line_view_query)
        self.lb_sql_query.setBuddy(self.edit_line_sql_query)

        self.retranslateUi(Query)
        QtCore.QMetaObject.connectSlotsByName(Query)

    def retranslateUi(self, Query):
        Query.setWindowTitle(QtGui.QApplication.translate("Query", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_view_query.setText(QtGui.QApplication.translate("Query", "&View:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_sql_query.setText(QtGui.QApplication.translate("Query", "&SQL:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_submit_query.setText(QtGui.QApplication.translate("Query", "Submit", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Query = QtGui.QWidget()
    ui = Ui_Query()
    ui.setupUi(Query)
    Query.show()
    sys.exit(app.exec_())

