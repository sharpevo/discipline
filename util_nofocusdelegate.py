from PyQt4.QtGui import *
from PyQt4.QtCore import *
class NoFocusDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        opt = QStyleOptionViewItem(option)
        if opt.state & QStyle.State_HasFocus:
            opt.state = opt.state ^ QStyle.State_HasFocus
        super(NoFocusDelegate, self).paint(painter, opt, index)
