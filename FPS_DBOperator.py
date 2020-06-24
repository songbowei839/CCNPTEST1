import pymysql

class MysqlDBOperator:
    def __init__(self, user, pwd, host, dbname):
        self._user = user
        self._pwd = pwd
        self._host = host
        self._dbname = dbname
        self._conn = None
    def connect(self):
        if not self._conn:
            self._conn = pymysql.connect(self._host, self._user, self._pwd, self._dbname)

    def execute(self, sql):
        cursor = self._conn.cursor()
        try:
            cursor.execute(sql)
            self._conn.commit()

        except:
 #           rollback on error
            self._conn.rollback()

    def query(self, sql):
        cursor = self._conn.cursor()
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            return  results

        except:
            print ("Error: unable to fetch data")

    def close(self):
        self._conn.close()

if __name__ == '__main__':
    _db = MysqlDBOperator("root", "123456", "10.130.28.3", "ccnp")
    _db.connect()
    # # test mysql select
    # szSQL = """
    # select a.id, b.id
    #     from number_pool a, number_group b
    # where a.enterprise_id = b.enterprise_id
    #     and a.enterprise_id = '10010'
    # """
    # results = _db.query(szSQL)
    # for row in results:
    #     pool_id = row[0]
    #     group_id = row[1]
    #
    # print ("pool_id: ", pool_id)
    # print ("group_id: ",  group_id)

    # # test generate different isp
    # enterprise_id = '1001'
    # isp_identity = 'isp'
    # isp_count = 8
    #
    #
    # start_num = 10
    # num_count = 20
    # for number in range(start_num, start_num + num_count):
    #     id = number % isp_count
    #     isp_code = f"{enterprise_id}_{isp_identity}_{id}"
    #     print (number, isp_code)
    #
    # for isp_id in range(isp_count):
    #     isp_code = f"{enterprise_id}_{isp_identity}_{isp_id}"
    #     print (isp_code)
    szSQL = f"select area_code from mobile_info group by area_code limit 100"
    results = _db.query(szSQL)
    listAreaCode =  []
    for row in results:
        listAreaCode.append(row[0])

    print (listAreaCode)

    enterprise_id = '10070'
    start_num = 100
    number_count = 200
    isp_identity = 'ispRatio'
    isp_count = 5

    for number in range(start_num, start_num + number_count):
        id = number % isp_count
        areaID = number % 100

        isp_code = f"{enterprise_id}_{isp_identity}_{id}"
        szSQL = f"""
            insert into dialout_number_info
                (enterprise_id, number, area_alias, isp_code, open_date, enable_number, area_type)
            values
                ('{enterprise_id}', '{number}', '{listAreaCode[areaID]}', '{isp_code}', '20200616', 2, {areaID % 2 + 1})
            """
        print (szSQL)
        # _db.execute(szSQL)





