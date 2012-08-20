# -*- coding: utf-8 -*-

"""
Module implementing Widget_Editor.
"""

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Ui_widget_editor import Ui_widget_editor
from util_plaintext import PlaintextEditor
from util_highlighter import MarkdownHighlighter
from util_nofocusdelegate import NoFocusDelegate
from database import Database

class Widget_Editor(QWidget, Ui_widget_editor):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.lb_editor_id.hide()
        self.hl = MarkdownHighlighter(self.edit_plaintext.document())
        self.codec = QTextCodec.codecForName("UTF-16")
        ## remove border if widget is focused
        # self.cb_editor_state.setItemDelegate(NoFocusDelegate())
        # self.cb_editor_category.setItemDelegate(NoFocusDelegate())

        # self.edit_plaintext.setAcceptDrops(True)

    ## Handle setAnchor outside of QSyntaxHighlighter
    ## Since
    # self.hl.link_detected.connect(self.handle_link_detected)
    # def handle_link_detected(self, *args):
    #     index = args[0]
    #     length = args[1]
    #     cursor = self.edit_plaintext.textCursor()
    #     cursor.movePosition(QTextCursor.StartOfLine)
    #     beginning_of_line_pos = cursor.anchor()
    #     start_pos = beginning_of_line_pos + index + 2
    #     end_pos = start_pos + length - 3
    #     cursor.setPosition(start_pos)
    #     cursor.setPosition(end_pos,mode=QTextCursor.KeepAnchor)
    #     text = cursor.selectedText()
    #     char_format = QTextCharFormat()
    #     char_color = QColor()
    #     char_color.setNamedColor("#0000ff")
    #     char_format.setForeground(char_color)
    #     anchor_name = str(text)
    #     char_format.setAnchor(True)
    #     char_format.setAnchorName(anchor_name)
    #     char_format.setAnchorHref("google")
    #     cursor.setCharFormat(char_format)
    #     cursor.clearSelection()

    def encoding(self, text):
        return unicode(self.codec.fromUnicode(text), 'UTF-16')

    def get_title(self):
        text = self.edit_line_editor_sub.text()
        return self.encoding(text)

    def get_category(self):
        text = self.cb_editor_category.currentText()
        return self.encoding(text)

    def get_state(self):
        text = self.cb_editor_state.currentIndex()
        return text

    def get_content(self):
        text = self.edit_plaintext.toPlainText()
        return self.encoding(text)
