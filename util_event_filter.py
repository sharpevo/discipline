from PyQt4.QtGui import *
from PyQt4.QtCore import *

class EmacsKeybinding(QObject):
    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            if obj.inherits("QLineEdit"):
                if event.matches(QKeySequence.SelectAll):
                    obj.home(False)
                    return True
                elif event.matches(QKeySequence.Bold):
                    obj.cursorBackward(False)
                    return True
                elif event.matches(QKeySequence.Find):
                    obj.cursorForward(False)
                    return True
                # elif event.matches(QKeySequence(Qt.CTRL + Qt.Key_H)):
                #     obj.backspace()
                #     print "yes"
                #     return True
            if obj.inherits("QPlainTextEdit"):
                pass
        return QObject.eventFilter( self, obj, event )
