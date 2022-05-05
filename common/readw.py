# import os,openpyxl
# import pymysql
# class ReadW:
#
#     def db_mysql(self, db_name, sql=None):
#         '''数据库操作'''
#         db_parameter = {
#             "charset": 'utf8',
#             "db": db_name,
#             "host": '121.43.56.25',
#             "port": 3322,
#             "user": 'wp_user',
#             "passwd":'wp@2018',
#                 }
#         db = pymysql.connect(**db_parameter)
#         cursor = db.cursor()
#         cursor.execute(sql)
#         response = cursor.fetchall()
#         cursor.close()
#         return response[0][0]
#
#
#     def read_E(self,sheet,rows,cols):
#         '''操作excel'''
#         wb = openpyxl.load_workbook(r'{}/data_o.xlsx'.format(os.getcwd()))
#         tb = wb['{}'.format(wb.sheetnames[sheet])]
#         values = tb.cell(rows,cols).value
#         wb.close()
#         return values
#
# # if __name__ == '__main__':
# #     read = ReadW()
# #     print(read.read_E(0,2,6))
