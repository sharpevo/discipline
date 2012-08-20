import sqlite3 as sqlite
import os,re,codecs
from datetime import datetime
from datetime import timedelta

class Database:

    def __init__(self, database_file_path):

        ## Check existence of database.
        # sqlite.connect() will create database regardless of file existence.
        has_database = False
        if os.path.exists(database_file_path):
            has_database = True

        self.conn = sqlite.connect(database_file_path)
        self.cursor = self.conn.cursor()

        if not has_database:
            self.init_database()

        self.update_cache()
        self.time_format = "%Y%m%d%H%M%S"
        # self.sql_get = """
        # SELECT items.created, items.title, items.modified,
        # category.name, items.state, items.content FROM items, category
        # WHERE items.category=category.id ?
        # """

        self.sql_get = ("SELECT items.created, items.title, items.modified, "
                        "category.name, items.state, items.content FROM items, category "
                        "WHERE items.category=category.id %s")
        self.sql_category_list = ("SELECT name FROM category")

    def init_database(self):
        self.cursor.execute("CREATE TABLE items ("
                            "created DATETIME Primary key NOT NULL,"
                            "title NVARCHAR(100) NOT NULL, "
                            "modified DATETIME NOT NULL,"
                            "category NVARCHAR(50) NOT NULL, "
                            "state INTEGER NOT NULL DEFAULT(0), "
                            "content NTEXT NOT NULL)")
        self.cursor.execute("CREATE INDEX items_index on items ("
                            "created DESC, title ASC, modified DESC, category ASC,"
                            "state ASC, content ASC)")
        self.cursor.execute("CREATE TABLE category ("
                            "id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                            "name NVARCHAR(50) NOT NULL)")
        self.conn.commit()

    def close_conn(self):
        self.conn.close()

    def _get_categories(self):
        # return a list containing item tuple.
        # [(1, u'Aspen'), (2, u'Phatnotes')]
        return self.cursor.execute("SELECT * FROM category ORDER BY id").fetchall()

    def _get_titles(self):
        title_list = self.cursor.execute("SELECT title FROM items").fetchall()
        return [title[0] for title in title_list]

    def update_cache(self):
        self.categories = self._get_categories()
        # self.titles = self._get_titles()

    def get_category_id(self, category_name):

        for category in self.categories:
            if category_name == category[1]:
                return category[0]

        self.insert_category(category_name)
        self.categories = self._get_categories()
        # return self.cursor.lastrowid
        return self.categories[-1][0]

    def get_timestamp(self):
        return datetime.now().strftime(self.time_format)

    def get_daybreak_time(self, date):
        """
        Get the beginning time of day,
        i.e. midnight time, e.g. 2012-07-17 00:00:00
        return string as '20120717000000'.
        date must like 'datetime.now().date().
        """
        return date.strftime(self.time_format)

    def insert_category(self, name=""):
        # tpye(name) is QString
        # name_string = str(name)
        self.cursor.execute("INSERT INTO category VALUES(NULL, ?)", [name])
        self.conn.commit()

    def insert_item(self, title="", category_name="", state=0, content="" ):

        # modified equals to created if it is the new one.
        timestamp = self.get_timestamp()
        # print timestamp, title, timestamp, category_name, state, content
        self.cursor.execute("INSERT INTO items VALUES(?, ?, ?, ?, ?, ?)",
                            [timestamp, str(title), timestamp, self.get_category_id(category_name), state, content])
        # self.titles = self._get_titles()
        self.conn.commit()

    def delete_item(self, id):
        self.cursor.execute("DELETE FROM items WHERE created=?", [str(id)])
        self.conn.commit()

    def delete_category(self, id):
        self.cursor.execute("DELETE FROM category WHERE id=?", [id])
        self.conn.commit()

    def delete_useless_category(self):
        for id, name in self.categories:
            if not self.fetch_items_by_categoryid(id):
                self.delete_category(id)
                self.categories = self._get_categories()
        self.conn.commit()

    def update_item(self, created="", title="", category="", state="", content=""):
        ## type(title) type(created) are QString
        sql_update = "UPDATE items SET title=?, category=?, state=?, content=?, modified=? WHERE created=?"
        # self.cursor.execute(sql_update, [str(title), self.get_category_id(category), state, content, str(created)])
        self.cursor.execute(sql_update, [title, self.get_category_id(category), state, content, self.get_timestamp(), str(created)])
        self.conn.commit()
        # self.titles = self._get_titles()
        self.delete_useless_category()

    def update_category(self, id, new_name):
        self.cursor.execute("UPDATE category SET name=? WHERE id=?",[new_name, id])
        self.conn.commit()

    def fetch_items_by_year(self):
        self.cursor.execute(self.sql_get % "ORDER BY items.created")
        # self.cursor.execute(self.sql_get, ["ORDER BY items.created"])
        return self.cursor.fetchall()

    def fetch_items_by_day(self, date):
        # date must be datetime.date()
        sql_criterion = "and created > '%s' ORDER BY created ASC" % self.get_daybreak_time(date)
        self.cursor.execute(self.sql_get % sql_criterion)
        # self.cursor.execute(self.sql_get,
                            # ["and created > ? ORDER BY created ASC",
                             # self.get_daybreak_time(date)])
        return self.cursor.fetchall()

    def fetch_items_by_days(self):
        # date must be datetime.date()
        sql_criterion = "ORDER BY created DESC"
        self.cursor.execute(self.sql_get % sql_criterion)
        return self.cursor.fetchall()

    def fetch_items_by_week(self):
        today_date = datetime.now().date()
        monday_date = today_date - timedelta(days=today_date.weekday())
        sql_criterion = "and created > '%s' ORDER BY created ASC" % self.get_daybreak_time(monday_date)
        self.cursor.execute(self.sql_get % sql_criterion)
        return self.cursor.fetchall()

    def fetch_items_by_categoryid(self, categoryid):
        sql_criterion = "and category.id='%s'" % categoryid
        self.cursor.execute(self.sql_get % sql_criterion)
        return self.cursor.fetchall()

    def fetch_items_by_category(self):
        self.cursor.execute(self.sql_get % "ORDER BY category.name ASC, items.created ASC")
        return self.cursor.fetchall()

    def fetch_items_by_state(self, state):
        sql_criterion = "and items.state='%s'" % state
        self.cursor.execute(self.sql_get % sql_criterion)
        return self.cursor.fetchall()

    def fetch_items_by_tmp(self, tmp):
        sql_criterion = "and category.name='%s'" % tmp
        self.cursor.execute(self.sql_get % sql_criterion)
        return self.cursor.fetchall()

    def fetch_items_by_states(self):
        self.cursor.execute(self.sql_get % "ORDER BY items.state, items.created DESC")
        return self.cursor.fetchall()

    def util_parse_phatnote(self, phatnote_file):
        """
        Parse phatnotes file:
        - Comma separated values
        - Save as UNICODE
        and uncheck all other options.
        """
        head = ('^"([0-9]{2}-[0-9]{1,2}-[0-9]{1,2} [0-9]{1,2}:[0-9][0-9])",'
                '"([0-9]{2}-[0-9]{1,2}-[0-9]{1,2} [0-9]{1,2}:[0-9][0-9])","(.*)","(.*)",')
        tail = '(\w*),(\w*),"([0-9]{2}-[0-9]{1,2}-[0-9]{1,2} [0-9]{1,2}:[0-9][0-9])"\r\n'
        content = '"(.*)",'
        head_regex = re.compile("%s%s" % (head, content[:-2]))
        tail_regex = re.compile("%s%s" % (content[1:], tail))
        item_regex = re.compile("%s%s%s" % (head, content, tail))

        with codecs.open(phatnote_file, encoding="utf16", errors="ignore") as f:

            for line in f:
                match_head = re.search(head_regex, line)
                match_tail = re.search(tail_regex, line)
                match_item = re.search(item_regex, line)
                if match_item:
                    groups = match_item.groups()
                    created = groups[0]
                    modified = groups[1]
                    subject = groups[2]
                    category = groups[3]
                    body = groups[4]
                    color = groups[5]
                    priority = groups[6]
                    authored = groups[7]
                    self.util_import_phatnote(created, subject, modified,
                                              category, priority, body)
                    continue
                if match_head:
                    groups = match_head.groups()
                    created = groups[0]
                    modified = groups[1]
                    subject = groups[2]
                    category = groups[3]
                    body_list = []
                    body_list.append(groups[4])
                elif match_tail:
                    groups = match_tail.groups()
                    body_list.append(groups[0])
                    body = "".join(body_list)
                    color = groups[1]
                    priority = groups[2]
                    authored = groups[3]
                    self.util_import_phatnote(created, subject, modified,
                                              category, priority, body)
                else:
                    body_list.append(line)

    def util_parse_phatnote_time(self, pn_datetime):
        """
        translate time string from 12-7-9 7:06 to 201207090706.
        pn only provide one digits to present month, and there is not responsed mask
        supported by python, so strptime does not work directly.
        """
        pn_date, pn_time = pn_datetime.split(" ")
        year, month, day = pn_date.split("-")
        hour, minute = pn_time.split(":")
        return datetime(int("20%s" % year), int(month), int(day),
                        int(hour), int(minute)).strftime(self.time_format)
    def util_parse_phatnote_state(self, pn_state):
        if pn_state.lower() == "low":
            return 0
        if pn_state.lower() == "normal":
            return 1
        if pn_state.lower() == "high":
            return 2

    def util_import_phatnote(self, created, title, modified,
                             category_name, state, content):

        self.cursor.execute("INSERT INTO items VALUES(?, ?, ?, ?, ?, ?)",
                            [self.util_parse_phatnote_time(created),
                             title,
                             self.util_parse_phatnote_time(modified),
                             self.get_category_id(category_name),
                             self.util_parse_phatnote_state(state),
                             content])
        self.conn.commit()
