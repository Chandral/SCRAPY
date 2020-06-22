# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3


class QuotestutorialPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('myquotes.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("DROP TABLE IF EXISTS quotes_tb")
        self.curr.execute("CREATE TABLE quotes_tb (title text, author text, tags text)")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        title = item['title'][0]
        author = item['author'][0]
        tags = item['tags'][0]
        self.curr.execute("""INSERT INTO quotes_tb (title, author, tags) VALUES (?,?,?)""", (title, author, tags))
        self.conn.commit()
