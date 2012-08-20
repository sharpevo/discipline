from PyQt4.QtGui import *
from PyQt4.QtCore import *
from datetime import datetime
class PlaintextEditor(QPlainTextEdit):

    def __init__(self, parent=None):
        super(PlaintextEditor, self).__init__(parent)


        # plaintext_font = QFont()
        # plaintext_font.setFamily("Trebuchet MS")
        # plaintext_font.setFixedPitch(True)
        # plaintext_font.setPointSize(10)
        # char_format = QTextCharFormat()
        # char_format.setFont(plaintext_font)
        # self.setCurrentCharFormat(char_format)
        # # self.setLineWrapMode(QPlainTextEdit.WidgetWidth)

        self.cursorPositionChanged.connect(self.caret_highlight)
        self.setup_keybinding()
        # self.textChanged.connect(self.on_textChanged)

        self.setMouseTracking(True)

    def caret_highlight(self):

        hi_selection = QTextEdit.ExtraSelection()
        # d4d0c8
        hi_selection.format.setBackground(QColor("#000000"))#self.palette().alternateBase())
        hi_selection.format.setProperty(QTextFormat.FullWidthSelection, QVariant(True))
        hi_selection.cursor = self.textCursor()
        hi_selection.cursor.clearSelection()
        self.setExtraSelections([hi_selection])

    def mouseMoveEvent(self,mouse_event):
        point = mouse_event.pos()
        if self.anchorAt(point):
            self.viewport().setCursor(Qt.PointingHandCursor)
        else:
            self.viewport().setCursor(Qt.ArrowCursor)
            super(PlaintextEditor, self).mouseMoveEvent(mouse_event)

    # def mouseReleaseEvent(self, mouse_event):
    #     point = mouse_event.pos()
    #     if self.anchorAt(point):
    #         print self.currentCharFormat().anchorName()
    #     else:
    #         super(PlaintextEditor, self).mouseReleaseEvent(mouse_event)

    # def mouseReleaseEvent(self, mouse_event):
    #     # pos = mouse_event.pos()
    #     # print pos
    #     if not self.goto_link():
    #         super(PlaintextEditor, self).mouseReleaseEvent(mouse_event)

    # def on_textChanged(self):
    #     c = self.textCursor()
    #     pos = c.positionInBlock()
    #     format_range_list = c.block().layout().additionalFormats()
    #     for r in format_range_list:
    #         if pos >= r.start and pos <= r.start + r.length + 3 and r.format.isAnchor():
    #             c.setPosition(c.block().position() + r.start)
    #             c.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, r.length)
    #             c.setCharFormat(r.format)
    #             break

    def goto_link(self):
        c = self.textCursor()
        pos = c.positionInBlock()
        format_range_list = c.block().layout().additionalFormats()
        for r in format_range_list:
            if pos >= r.start and pos <= r.start + r.length + 3 and r.format.isAnchor():
                c.setPosition(c.block().position() + r.start)
                c.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, r.length)
                item_id = c.selectedText()
                main_widget = self.parentWidget().parentWidget().parentWidget()
                main_widget.open_widget_editor_with_item(item_id)
                return True
        return False


    # def mousePressEvent(self,event):
    #     mimeData = QMimeData()
    #     mimeData.setText(self.textCursor().selectedText())
    #     drag = QDrag(self)
    #     drag.setMimeData(mimeData)
    #     drag.exec_()

    # def mouseMoveEvent(self,mouse_event):
    #     point = mouse_event.pos()
    #     if self.anchorAt(point):
    #         self.viewport().setCursor(Qt.PointingHandCursor)
    #     else:
    #         self.viewport().setCursor(Qt.ArrowCursor)

    # def mouseReleaseEvent(self, mouse_event):
    #     point = mouse_event.pos()
    #     if self.anchorAt(point):
    #         item_href = self.currentCharFormat().anchorHref()

    # def dropEnterEvent(self, event):
    #     print "enter event"
    #     event.accept()
    #     event.acceptProposedAction()

    # def dropEvent(self, event):
    #     self.insertFromMimeData(event.mimeData())

    # def canInsertFromMimeData(self, mimeData):
    #     return True

    # def insertFromMimeData(self, mimeData):
    #     text = "[%s]" % mimeData.text()
    #     self.textCursor().insertText(text)


    def setup_keybinding(self):
        self.setContextMenuPolicy(Qt.NoContextMenu)

        self.create_action("next_line", "Ctrl+N", self.next_line)
        self.create_action("prev_line", "Ctrl+P", self.prev_line)
        self.create_action("line_tail", "Ctrl+E", self.line_tail)
        self.create_action("line_head", "Ctrl+A", self.line_head)
        self.create_action("next_char", "Ctrl+F", self.next_char)
        self.create_action("prev_char", "Ctrl+B", self.prev_char)
        self.create_action("next_word", "Alt+F", self.next_word)
        self.create_action("prev_word", "Alt+B", self.prev_word)
        # self.create_action("scroll_up", "Alt+V", self.scroll_up)
        # self.create_action("scroll_down", "Ctrl+V", self.scroll_down)
        self.create_action("page_tail", "Alt+>", self.page_tail)
        self.create_action("page_head", "Alt+<", self.page_head)
        self.create_action("del_char_right", "Ctrl+D", self.del_char_right)
        self.create_action("del_char_left", "Ctrl+H", self.del_char_left)
        # self.create_action("del_word_right", "Alt+D", self.del_word_right)
        # self.create_action("del_word_left", "Alt+SPACE", self.del_word_left)
        # self.create_action("cut", "Ctrl+W", self.cut)
        # self.create_action("copy", "Alt+W", self.copy)
        # self.create_action("paste2", "Ctrl+SPACE", self.paste)
        # self.create_action("del_line_left", "Ctrl+K", self.del_line_left)
        self.create_action("insert timestamp", "Ctrl+T", self.insert_timestamp)

    def create_action(self, name, shortcut, slot):
        action = QAction(name, self)
        action.setShortcut(shortcut)
        self.connect(action, SIGNAL("triggered()"), slot)
        self.addAction(action)

    def keyPressEvent(self, event):

        # if e.matches(QKeySequence.Paste):
            # self.scroll_down()
        if event.matches(QKeySequence.SelectAll):
            self.line_head()
        # elif e.matches(QKeySequence.Delete):
            # self.del_char_right()
        # elif e.matches(QKeySequence.Redo):
            # print "---"
        else:
            super(PlaintextEditor, self).keyPressEvent(event)

    def insert_timestamp(self):
        timestamp = "--------------------------%s--------------------------" % \
                    datetime.now().strftime("[%Y.%m.%d %H:%M]")
        self.textCursor().insertText(timestamp)

    def next_line(self):
        self.moveCursor(QTextCursor.Down)

    def prev_line(self):
        self.moveCursor(QTextCursor.Up)

    def line_tail(self):
        self.moveCursor(QTextCursor.EndOfLine)

    def line_head(self):
        self.moveCursor(QTextCursor.StartOfLine)

    def next_char(self):
        self.moveCursor(QTextCursor.Right)

    def prev_char(self):
        self.moveCursor(QTextCursor.Left)

    def next_word(self):
        self.moveCursor(QTextCursor.NextWord)

    def prev_word(self):
        self.moveCursor(QTextCursor.PreviousWord)

    # def scroll_down(self):
    #     self.moveCursor(QTextCursor.)

    # def scroll_up(self):
    #     self.moveCursor(QTextCursor.)

    def page_tail(self):
        self.moveCursor(QTextCursor.End)

    def page_head(self):
        self.moveCursor(QTextCursor.Start)

    def del_char_right(self):
        self.textCursor().deleteChar()

    def del_char_left(self):
        self.textCursor().deletePreviousChar()

    # def del_word_right(self):
    #     self.moveCursor(QTextCursor.EndOfLine)

    # def del_word_left(self):
    #     self.moveCursor(QTextCursor.EndOfLine)

    # def cut(self):
    #     self.moveCursor(QTextCursor.EndOfLine)

    # def copy(self):
    #     self.moveCursor(QTextCursor.EndOfLine)

    # def del_line_left(self):
    #     self.moveCursor(QTextCursor.EndOfLine)
    #     cur_pos = self.SendScintilla(QsciScintilla.SCI_GETCURRENTPOS)
    #     line_num = self.SendScintilla(QsciScintilla.SCI_LINEFROMPOSITION, cur_pos)
    #     line_tail_pos = self.SendScintilla(QsciScintilla.SCI_GETLINEENDPOSITION, line_num)
    #     line_head_pos = self.SendScintilla(QsciScintilla.SCI_POSITIONFROMLINE, line_num)
    #     if line_head_pos == line_tail_pos:
    #         self.SendScintilla(QsciScintilla.SCI_LINEDELETE)
    #     elif cur_pos == line_tail_pos:
    #         self.SendScintilla(QsciScintilla.SCI_DELWORDRIGHT)
    #     else:
    #         self.SendScintilla(QsciScintilla.SCI_SETSELECTIONSTART, cur_pos)
    #         self.SendScintilla(QsciScintilla.SCI_SETSELECTIONEND, line_tail_pos)
    #         self.cut()

    # def paste(self):
    #     self.moveCursor(QTextCursor.EndOfLine)



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    editor = Qsci_Editor()
    editor.show()
    with open(sys.argv[0]) as f:
        editor.setText(f.read())
    sys.exit(app.exec_())
