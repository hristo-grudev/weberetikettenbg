import sqlite3


class WeberetikettenbgPipeline:
    conn = sqlite3.connect('weberetikettenbg.db')
    cursor = conn.cursor()

    def open_spider(self, spider):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS `weberetikettenbg` (
                                                                                    title varchar(100),
                                                                                    description text,
                                                                                    date varchar(25),
                                                                                    lang varchar(5)                                                                                    
                                                                                    )''')
        self.conn.commit()

    def process_item(self, item, spider):
        title = item['title'][0]
        description = item['description'][0]
        date = item['date'][0]
        lang = item['lang'][0]


        self.cursor.execute(f"""select * from weberetikettenbg where title = '{title}' and lang = '{lang}' and date = '{date}'""")
        is_exist = self.cursor.fetchall()

        if len(is_exist) == 0:
            self.cursor.execute(f"""insert into `weberetikettenbg`
                                            (`title`, `description`, `date`, `lang`)
                                            values (?, ?, ?, ?)""", (title, description, date, lang))
            self.conn.commit()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
