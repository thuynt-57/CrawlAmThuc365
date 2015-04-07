# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

class Amthuc365Pipeline(object):
    def __init__(self):
    # sua ten database
        self.conn=MySQLdb.connect(user='root',passwd='cobala15111994',db='amthuc365',host='127.0.0.1',charset="utf8",use_unicode='True')
        self.cursor=self.conn.cursor()

    def process_item(self, item,   spider):
        if (spider.name == 'getlink'):
            try:
                # sua lai lenh insert cho phu hop voi database
                sql = """INSERT IGNORE INTO dishes(link) VALUES (\'%s\')""" %(''.join(item['link']).decode('utf-8'))
                self.cursor.execute(sql)
                self.conn.commit()
            except MySQLdb.Error, e:
                print ("Error %s" % e.args[1])
            return item

        elif (spider.name =='amthucparse'):
            #line = json.dumps(dict(item)).decode('unicode-escape').encode('utf-8') + "\n"
            #self.file.write(line)
            try:
            	# sua lenh update
                self.cursor.execute("UPDATE dishes SET name = %s, image = %s, num_of_people = %s, guide = %s, time_to_cook = %s, time_to_prepare = %s, addition = %s  WHERE link = %s",(''.join(item['name']), ''.join(item['image']), ''.join(item['num_of_people']), ''.join(item['guide']), ''.join(item['time_to_cook']), ''.join(item['time_to_prepare']), ''.join(item['addition']), ''.join(item['link'])))
                self.conn.commit()

            except MySQLdb.Error, e:
                print("Error %s" % e.args[1])
            return item
