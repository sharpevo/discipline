# syntax.py

import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MarkdownHighlighter(QSyntaxHighlighter):
    # link_detected = pyqtSignal(int, int)
    # def handel_link_detected(self):
    #     print "Yes!"

    def __init__(self, *args):
        QSyntaxHighlighter.__init__(self, *args)

        dft_font_fam="Trebuchet MS"
        dft_font_size=8
        # mono_font_fam="Comic Sans Ms"
        # mono_font_fam="WenQuanYi Zen Hei Mono"
        mono_font_fam="Tamsyn"
        mono_font_size=7
        self.dft_font = QFont()
        self.dft_font.setFamily(mono_font_fam)
        self.dft_font.setFixedPitch(True)
        self.dft_font.setPointSize(dft_font_size)

        self.mono_font = QFont()
        self.mono_font.setFamily(mono_font_fam)
        self.mono_font.setFixedPitch(True)
        self.mono_font.setPointSize(mono_font_size)

        format_dict = {
            # header
            "level_1": self.formater(size_diff=6, style="bold"),
            "level_2": self.formater(size_diff=5, style="bold"),
            "level_3": self.formater(size_diff=4),
            # "level_4": self.formater(size_diff=2, style="bold"),
            # `code-segments`
            # "code": self.formater(font=self.mono_font, size_diff=-1, style="bold", color="#606060"),
            "code": self.formater(font=self.mono_font, color="#606060"),
            "codeblock": self.formater(font=self.mono_font, color="#606060"),
            # *emphasized text*
            "emphasis": self.formater(color="#babdb6",style="bold"),
            # _italic_
            "italic": self.formater(style="italic", color="#babdb6"),
            # [link]
            "link": self.formater(color="#0000ff", size_diff=-1, style="link"),
            # > quote
            "quote": self.formater(color="#555753", size_diff=-1),
            "anchor":self.formater(font=self.mono_font, style="anchor", color="#555753"),
            "timeline": self.formater(color="#babdb6"),
            # "anchor":""
            }
        pattern_list = [
            # headers
            (r"^#{3}[^#]+$", 0, format_dict["level_1"]),
            (r"^#{2}[^#]+$", 0, format_dict["level_2"]),
            (r"^#{1}[^#]+$", 0, format_dict["level_3"]),
            # (r"^#{4}[^#]+$", 0, format_dict["level_4"]),
            # `code`, match.group() = code
            # (r"`.+`", 0, format_dict["code"]),
            (r"`[^`]+`", 0, format_dict["code"]),
            (r"^`.*$", 0, format_dict["codeblock"]),
            # (r"`([^`]+)`", 0, format_dict["code"]),
            (r"\*([^\*]+)\*", 0, format_dict["emphasis"]),
            # (r"\_([^\_]+)\_", 1, format_dict["italic"]),
            # (r"\W_([^ ^_]+)_(\W|$)", 1, format_dict["italic"]),
            (r"\W_([^_]+)_(\W|$)", 1, format_dict["italic"]),
            # (r"[^\\]\[[^\[^\]]+\]", 0, format_dict["link"]),
            # (r"[ ]\[([^\[^\]]+)\]", 1, format_dict["anchor"]),
            (r"[^\-^\\]\[([^\[^\]]+)\]", 1, format_dict["anchor"]),
            (r"^>.*$", 0, format_dict["quote"]),
            (r"[\-]\[(.*)\]", 1, format_dict["timeline"]),

            ]

        self.pattern_list = [(QRegExp(pat), group, fmt) for pat, group, fmt in pattern_list]

    def formater(self, font="", color="#888a85", size_diff=0, style=""):
        if font == "":
            font = self.dft_font
        char_color = QColor()
        char_color.setNamedColor(color)
        char_format = QTextCharFormat()
        char_format.setFont(font)
        char_format.setForeground(char_color)
        char_format.setFontPointSize(self.dft_font.pointSize() + size_diff)
        if "bold" in style:
            char_format.setFontWeight(QFont.Bold)
        if "italic" in style:
            char_format.setFontItalic(True)
        if "link" in style:
            char_format.setFontUnderline(True)
        if "anchor" in style:
            char_format.setFontUnderline(True)
            # char_format.setFontWeight(QFont.Bold)
            char_format.setAnchor(True)
        return char_format

    def highlightBlock(self, text):
        text = unicode(text)
        for expr, group, fmt in self.pattern_list:
            index = expr.indexIn(text, 0)
            while index >= 0:
                index = expr.pos(group)
                length = expr.cap(group).length()
                # if not fmt:
                #     pass
                #     # self.link_detected.emit(index, length)
                #     # print index, length
                #     char_format = QTextCharFormat()
                #     char_color = QColor()
                #     char_color.setNamedColor("#729fcf")
                #     char_format.setForeground(char_color)
                #     anchor_name = str(expr.cap(group))
                #     char_format.setAnchor(True)
                #     char_format.setAnchorName(anchor_name)
                #     char_format.setAnchorHref("www.google.com")
                #     fmt = char_format
                    # index = index + 2
                    # length = length - 3
                # else:
                #     self.setFormat(index, length, fmt)
                self.setFormat(index, length, fmt)
                index = expr.indexIn(text, index + length)
        self.setCurrentBlockState(0)

# editor.py
if __name__ == "__main__":
    from PyQt4 import QtGui
    import sys

    app = QtGui.QApplication([])
    editor = QtGui.QPlainTextEdit()

    # e_format = QTextCharFormat()
    # e_format.setFont(dft_font)
    # editor.setCurrentCharFormat(e_format)
    txt = """# About
    This example shows you a hard-coded markdown
    syntax-definition. Supporting `code-segments`,
    **emphasized text** or *emphasized text*.

    >quote
    >quote

    [link]

    ## list-support
    - a simple list item
    - an other

    1. A ordered list
    2. other item

    #### n-th order heading
    """
    editor.setPlainText(txt)
    # with open(sys.argv[0], "r") as f:
        # editor.setPlainText(f.read())
    MarkdownHighlighter(editor.document())
    editor.moveCursor(QTextCursor.Right)
    editor.moveCursor(QTextCursor.Right)
    print editor.textCursor().deleteChar()
    editor.show()


    app.exec_()
