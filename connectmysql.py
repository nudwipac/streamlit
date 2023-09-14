import pymysql


def connectdb():
    connection = pymysql.connect(
        host='b9yra2epa2xtxtb3jdov-mysql.services.clever-cloud.com',  # 'localhost',
        user='ucepxxourcxvoskx',  # 'root',
        password='O287ngXlhlPwPwSpdFEV',
        db='b9yra2epa2xtxtb3jdov',  # 'pythondb',
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection


# test call funtion
print(connectdb())
