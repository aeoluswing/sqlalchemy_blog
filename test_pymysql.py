import pymysql.cursors
from prettytable import PrettyTable

# Connect to the database
conneciton = pymysql.connect(
                host='localhost',
                port=3306,
                user='root',
                password='jiangyu2718',
                db='test',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )

try:
    cursor = conneciton.cursor()
    #sql comment
    sql = 'SELECT * FROM user;'
    cursor.execute(sql)
    rows = cursor.fetchall()
    description = cursor.description
    conneciton.commit()
    
    header_list = []
    col = len(description)
    for index in range(0,col):
        header_list.append(description[index][0])
    pt = PrettyTable()
    pt._set_field_names(header_list)
    for row_dict in rows:
        pt.add_row(row_dict.values())
    print(pt)
finally:
    conneciton.close()
    
    