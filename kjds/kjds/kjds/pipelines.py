# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import  pymysql

class KjdsPipeline(object):
    def __init__(self):
        # 连接MySQL数据库
        self.connect = pymysql.connect(host='192.168.19.126', user='kjds', password='kjds', db='kjds', port=3306)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        seqs=item["seq"]
        i=0
        for seq in  seqs:
            # 查重处理
            self.cursor.execute(
                """select * from trans_amt_info where seq = %s""",
                seq)
            # 是否有重复数据
            repetition = self.cursor.fetchone()

            # 重复
            if repetition:
                print("数据库已有数据，不插入")
                pass

            else:
                # 插入数据
                self.cursor.execute(
                    'insert into trans_amt_info (seq,TRANS_AMT,CREATE_DATE) VALUES ("{}","{}","{}")'.format(
                        item['seq'][i],
                        item['trans_amt'][i],
                        item['create_date'][i]
                        ))
                # 提交sql语句
                self.connect.commit()
                i=i+1


