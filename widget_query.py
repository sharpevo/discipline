# -*- coding: utf-8 -*-

"""
Module implementing Widget_Query.
"""

from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature

from Ui_widget_query import Ui_Query
from main import MainWindow
from util_event_filter import EmacsKeybinding

class Widget_Query(QWidget, Ui_Query):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QWidget.__init__(self, parent)
        self.setupUi(self)

        # self.filter = EmacsKeybinding()
        # self.edit_line_sql_query.installEventFilter(self.filter)

        self.edit_line_sql_query.installEventFilter(EmacsKeybinding(self))
        self.edit_line_view_query.installEventFilter(EmacsKeybinding(self))
