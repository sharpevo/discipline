## -*- coding: utf-8 -*-
from datetime import datetime
"""
Module implementing MainWindow.
"""
from database import Database
from datetime import datetime

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Ui_main import Ui_MainWindow
from util_command_stack import CommandStack
import shutil

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        # self.bar_menu.hide()
        # self.widget_tree.headerItem().setText(0, "Day View of 2012")

        self.widget_query.hide()
        self.widget_editor.cb_editor_state.addItems([self.translate_state(0),
                                                     self.translate_state(1),
                                                     self.translate_state(2)])
        self.widget_editor.hide()

        self.database = Database("data.db")
        self.cmd_dict = {}
        # self.widget_tree.setSelectionMode(QAbstractItemView.SingleSelection)

        self.widget_editor.cb_editor_category.addItems([cat[1] for cat in self.database.categories])

        self.current_view = ""

        self.show_year = [lambda item: str(item[0])[:4], lambda item: str(item[0])[:4]]
        self.show_month = [lambda item: str(item[0])[4:6], lambda item: self.get_month_text(item)]
        self.show_day = [lambda item: str(item[0])[:8], lambda item: self.get_day_text(item)]
        # self.show_time = [lambda item: str(item[0])[8:], lambda item: self.get_day_text(item)]

        self.show_year_m = [lambda item: str(item[2])[:4], lambda item: str(item[2])[:4]]
        self.show_month_m = [lambda item: str(item[2])[4:6], lambda item: self.get_month_text_m(item)]
        self.show_day_m = [lambda item: str(item[2])[:8], lambda item: self.get_day_text_m(item)]
        # self.show_time_m = [lambda item: str(item[2])[8:], lambda item: self.get_day_text_m(item)]

        self.show_category = [lambda item: item[3], lambda item: item[3]]
        self.show_state = [lambda item: item[4], lambda item: self.translate_state(item[4])]

        self.cmd_stack = CommandStack()
        self.setWindowOpacity(0.85)
    # def on_widget_tree_itemSelectionChanged(self):
    #     if not self.widget_editor.isHidden():
    #         self.widget_editor.hide()

    def on_actionForward_triggered(self, checked=None):
        if checked is None: return
        self.cmd_stack.move_cursor_forward()
        self.open_history_item()
    def on_actionBackward_triggered(self, checked=None):
        if checked is None: return
        self.cmd_stack.move_cursor_backward()
        self.open_history_item()
    def open_history_item(self):
        item_id = self.cmd_stack.get_item()
        self.open_widget_editor_with_item(item_id)

    def on_widget_tree_itemDoubleClicked(self, item, column):
        item_id = item.statusTip(column)
        if item_id:
            self.open_widget_editor_with_item(item_id)
            # self.add_to_history_items(str(item_id))
            self.cmd_stack.add_item(str(item_id))
    def open_widget_editor_with_item(self, item_id):
        sql_criterion = "and items.created='%s'" % item_id
        item_data = self.database.cursor.execute(self.database.sql_get % sql_criterion).fetchall()
        if item_data:
            self.widget_editor.cb_editor_category.clear()
            self.widget_editor.cb_editor_category.addItems([cat[1] for cat in self.database.categories])
            self.widget_editor.lb_editor_id.setText(item_id)
            self.widget_editor.edit_line_editor_sub.setText(item_data[0][1])
            self.widget_editor.edit_plaintext.setPlainText(item_data[0][5])
            self.widget_editor.cb_editor_category.setEditText(item_data[0][3])
            self.widget_editor.cb_editor_state.setCurrentIndex(int(item_data[0][4]))
            self.widget_editor.show()
            self.widget_editor.edit_plaintext.setFocus()


    def on_btn_editor_submit_released(self):
        ## QPlainTextEdit.toPlainText() returns QString which should be UTF-16,
        ## whereas unicode() constructor expects a byte string.
        text_utf16 = self.widget_editor.edit_plaintext.toPlainText()
        codec_utf16 = QTextCodec.codecForName("UTF-16")
        note_id = self.widget_editor.lb_editor_id.text()
        if note_id:
            self.database.update_item(created=note_id,
                                      # title=self.widget_editor.edit_line_editor_sub.text(),
                                      title=self.widget_editor.get_title(),
                                      category=self.widget_editor.get_category(),
                                      state=self.widget_editor.get_state(),
                                      content=self.widget_editor.get_content())
        else:
            title = self.widget_editor.get_title()
            content = self.widget_editor.get_content()
            if not title:
                title, newline, content = content.partition("\n")
            self.database.insert_item(title=title,
                                      category_name=self.widget_editor.get_category(),
                                      state=self.widget_editor.get_state(),
                                      content=content)
        self.update_view(self.widget_editor.edit_line_editor_sub.text())
        self.widget_editor.hide()

    def on_btn_editor_delete_released(self):
        text_utf16 = self.widget_editor.edit_plaintext.toPlainText()
        codec_utf16 = QTextCodec.codecForName("UTF-16")
        note_id = self.widget_editor.lb_editor_id.text()
        category = self.widget_editor.cb_editor_category.currentText()
        if note_id:
            if category == "__trash__":
                self.database.delete_item(note_id)
            else:
                self.database.update_item(created=note_id,
                                          title=self.widget_editor.get_title(),
                                          category="__trash__",
                                          state=self.widget_editor.get_state(),
                                          content=self.widget_editor.get_content())
            self.widget_editor.hide()
            self.update_view(self.widget_editor.edit_line_editor_sub.text())

    def on_actionShow_Query_Widget_triggered(self,checked=None):
        if checked is None: return
        if self.widget_query.isHidden():
            self.widget_query.show()
            self.widget_query.edit_line_view_query.setFocus()
        else:
            self.widget_query.hide()

    def on_actionJOE_Editor_triggered(self,checked=None):
        if checked is None: return
        if self.widget_editor.isHidden():
            self.widget_editor.lb_editor_id.setText("")
            self.widget_editor.edit_line_editor_sub.setText("")
            self.widget_editor.edit_plaintext.setPlainText("")
            self.widget_editor.cb_editor_category.setEditText("note")
            self.widget_editor.cb_editor_state.setCurrentIndex(0)
            self.widget_editor.show()
            self.widget_editor.edit_plaintext.setFocus()
        else:
            if self.widget_editor.edit_plaintext.hasFocus():
                self.widget_editor.hide()
            else:
                self.widget_editor.edit_plaintext.setFocus()

    def on_edit_line_view_query_textChanged(self, text):
        cmd_dict = self.get_cmd_dict()
        order_list = []
        for cmd in text:
            if cmd in cmd_dict.keys():
                if cmd == "v":
                    order_list[-1] = "%s %s" % (order_list[-1], cmd_dict[str(cmd)])
                    continue
                order = cmd_dict[str(cmd)][1]
                if  order not in order_list:
                    order_list.append(order)

        self.widget_query.edit_line_sql_query.setText("ORDER BY %s" % ",".join(order_list))

    def on_edit_line_view_query_returnPressed(self):
        self.on_btn_submit_query_released()

    def on_edit_line_sql_query_returnPressed(self):
        self.on_btn_submit_query_released()

    def on_btn_submit_query_released(self):
        cmd_dict = self.get_cmd_dict()
        parent_list = []
        view_cmd = self.widget_query.edit_line_view_query.text()
        query_cmd = self.widget_query.edit_line_sql_query.text()

        if view_cmd:
            for cmd in view_cmd:
                if cmd in cmd_dict.keys():
                    if not cmd == "v":
                        parent_list.append(cmd_dict[str(cmd)][0])
                else:
                    self.bar_status.showMessage("Invalid View Commands: '%s'" % cmd)
                    return
        else:
            self.bar_status.showMessage("Error: You need to provide view commands.")
            return

        try:
            # items = self.database.cursor.execute(self.database.sql_get, [query_cmd])
            self.widget_tree.clear()
            self.generate_view(header="Custom view for '%s'" % view_cmd,
                               sql=self.database.sql_get % query_cmd,
                               parent_list=parent_list)
        except Exception, e:
            self.bar_status.showMessage("Error: %s" % e.message )

    def get_cmd_dict(self):
        if not self.cmd_dict:
            self.cmd_dict = {"y":(self.show_year, "substr(items.created, 1, 4)"),
                             "m":(self.show_month, "substr(items.created, 1, 6)"),
                             "d":(self.show_day, "substr(items.created, 1, 8)"),
                             # "t":(self.show_time, "substr(items.created, 9, 14)"),
                             "Y":(self.show_year_m, "substr(items.modified, 1, 4)"),
                             "M":(self.show_month_m, "substr(items.modified, 1, 6)"),
                             "D":(self.show_day_m, "substr(items.modified, 1, 8)"),
                             # "T":(self.show_time_m, "substr(items.modified, 9, 14)"),
                             # "c":(self.show_category, "items.category"),
                             "c":(self.show_category, "category.name"),
                             "s":(self.show_state, "items.state"),
                             "v":"desc"}
        return self.cmd_dict

    def on_actionTree_Expand_All_triggered(self, checked=None):
        if checked is None: return
        self.widget_tree.expandAll()

    def on_actionTree_Collapse_All_triggered(self, checked=None):
        if checked is None: return
        self.widget_tree.collapseAll()

    def on_actionFocus_Tree_triggered(self, checked=None):
        if checked is None: return
        self.widget_tree.setFocus()

    def on_actionSave_Note_triggered(self, checked=None):
        if checked is None: return
        self.on_btn_editor_submit_released()

    def on_actionInsert_or_Goto_Tree_Item_triggered(self, checked=None):
        if checked is None: return
        if self.widget_tree.hasFocus():
            item = self.widget_tree.currentItem()
            item_link = " [%s]:`%s`" % (item.statusTip(0), item.text(0)[8:])
            self.widget_editor.edit_plaintext.textCursor().insertText(item_link)
            self.widget_editor.edit_plaintext.setFocus()
        elif self.widget_editor.edit_plaintext.hasFocus():
            self.widget_editor.edit_plaintext.goto_link()

    def on_actionImport_Phatnotes_File_triggered(self, checked=None):
        """
        Parse phatnotes file:
        - Comma separated values
        - Save as UNICODE
        and uncheck all other options.
        """

        if checked is None: return
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        shutil.copyfile("data.db", "data%s.db" % timestamp)
        self.database.util_parse_phatnote("pn.txt")

    # def on_widget_editor_textChanged(self):
    #     cursor = self.widget_editor.edit_plaintext.textCursor()
    #     cur_pos = cursor.anchor()
    #     line_start = cursor.movePosition(QTextCursor.StartOfLine)
    #     cursor.setPosition(cur_pos, mode=QTextCursor.KeepAnchor)
    #     text = cursor.selectedText()
    #     if text and "]" == text[-1] and "[" in text:
    #         start_pos = str(text).index("[") + line_start
    #         cursor.setPosition(start_pos, mode=QTextCursor.KeepAnchor)
    #         link_text = cursor.selectedText()
    #         if link_text in self.database.titles:
    #             self.char_format.setForeground(QColor("#0000ff"))
    #         else:
    #             self.char_format.setForeground(QColor("#606060"))
    #         cursor.setCharFormat(self.char_format)
    #     cursor.clearSelection()
    #     self.char_format.setForeground(QColor("#000000"))
    #     cursor.setCharFormat(self.char_format)
    #     print "-------"
        ## TODO: callout tip
        # elif "[" == text[-1]:

    def update_view(self, title):
        self.widget_tree.clear()
        self.generate_view(header=self.current_view[0],
                           sql=self.current_view[2],
                           parent_list=self.current_view[1])
        item_list = self.widget_tree.findItems(title,Qt.MatchContains|Qt.MatchRecursive,0)
        if item_list:
            self.widget_tree.setCurrentItem(item_list[0])
        # self.widget_tree.scrollToItem(item_list[0])

    def generate_view(self, parent_list="", header="", sql=""):
        """
        hierarchy:
        0.Method to get current data state.
        1.Method to generate text display in the tree."""

        dft_font = QFont()
        dft_font.setFamily("Trebuchet MS")
        dft_font.setFixedPitch(True)
        dft_font.setPointSize(10)

        self.current_view = (header, parent_list, sql)

        ## I dont know why this work, without fetch...
        items = self.database.cursor.execute(sql)
        # items = self.database.cursor.execute(sql).fetchall()
        # header = "%s, %s items." % (header, len(items))
        self.widget_tree.headerItem().setText(0, header)

        # just the copy of reference, if set one, e.g. a[0][0] = "ttt",
        # all the sub list value should be 'ttt'
        # previous = [["",""]] * len(items)
        previous = []
        for item in items:
            ## check whether item is child of all the current parents.
            for level, parent in enumerate(parent_list):
                if len(previous) <= level:
                    previous.append(["", ""])
                cur_state = parent[0](item)
                cur_text = parent[1](item)
                prev_state = previous[level][0]
                prev_parent_item = previous[level-1][1]
                # gradient_font_size = 10 - level * 3
                if not cur_state == prev_state:
                    if level == 0:
                        cur_item = QTreeWidgetItem(self.widget_tree)
                        # cur_item.setFont(0, QFont("Tamsyn", weight=QFont.Bold))
                    else:
                        cur_item = QTreeWidgetItem(prev_parent_item)
                    # cur_item.setFont(0, QFont("Tamsyn", pointSize=gradient_font_size))
                    cur_item.setText(0, cur_text)
                    previous[level][0] = cur_state
                    previous[level][1] = cur_item
                    ## clear all the children previous, to generate all the new
                    ## rather than if idea->2011->6, then 2012->6, will add into 2011.
                    ## start with full previous, jump the first item.
                    if len(previous) == len(parent_list):
                        for i in range(level+1, len(parent_list), 1):
                            previous[i][0] = ""
                            previous[i][1] = ""
                    self.widget_tree.expandItem(cur_item)
            ## insert item to the current parent.

            child = QTreeWidgetItem(previous[-1][1])
            # child.setFont(0, QFont("Comic Sans MS", pointSize=10))
            child_date_obj = datetime.strptime(str(item[0]),"%Y%m%d%H%M%S")
            child_text = "%s  %s" % (child_date_obj.strftime("%H:%M"), item[1])
            # child_text = "%s  %s:  %s" % (child_date_obj.strftime("%H:%M"), item[3], item[1])
            # if item[0] == item[2]:
            #     child_date_obj = datetime.strptime(str(item[0]),"%Y%m%d%H%M%S")
            #     child_text = "[%s] %s" % (child_date_obj.strftime("%H:%M"), item[1])
            # else:
            #     child_date_obj = datetime.strptime(str(item[2]),"%Y%m%d%H%M%S")
            #     child_text = "<%s> %s" % (child_date_obj.strftime("%H:%M"), item[1])
            child.setText(0, child_text)
            child_tooltip = "%s > %s" % (item[3], self.translate_state(item[4]))
            child.setToolTip(0, child_tooltip)
            child.setStatusTip(0,str(item[0]))

            ## expand until last level
            # for i in range(len(previous)-1):
                # self.widget_tree.expandItem(previous[i][1])

    # def get_db_date_obj(self, item):
    #     return datetime.strptime(str(item[0]), self.database.time_format)
    # def get_month_text(self, item):
    #     return self.get_db_date_obj(item).strftime("%Y %b")
    # def get_day_text(self, item):
    #     return self.get_db_date_obj(item).strftime("%Y.%m.%d %a")

    def get_db_date_obj(self, date):
        return datetime.strptime(str(date), self.database.time_format)

    def get_month_text(self, item):
        return self.get_db_date_obj(item[0]).strftime("%Y %b")

    def get_day_text(self, item):
        return self.get_db_date_obj(item[0]).strftime("%Y.%m.%d %a")

    def get_month_text_m(self, item):
        return self.get_db_date_obj(item[2]).strftime("%Y %b")

    def get_day_text_m(self, item):
        return self.get_db_date_obj(item[2]).strftime("%Y.%m.%d %a")

    def init_view(self):
        sql_criterion = "and created > '20120700000000' ORDER BY created DESC"
        sql = self.database.sql_get % sql_criterion

        self.generate_view(header="by date",
                           sql=sql,
                           parent_list=[self.show_day])

    def translate_state(self, state):
        if state == 0:
            return "new"
        if state == 1:
            return "follow-up"
        if state == 2:
            return "archive"

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    with open("tangle.qss") as f:
        app.setStyle("plastique")
        app.setStyleSheet(f.read())
    main_window = MainWindow()
    main_window.init_view()
    main_window.show()
    sys.exit(app.exec_())
