from  FPS_DBOperator  import MysqlDBOperator



if __name__ == '__main__':
    _db = MysqlDBOperator("root", "123456", "10.130.28.3", "ccnp")
    _db.connect()

    enterprise_id = '10106'
    start_num = 10121
    number_count = 5
    isp_identity = 'isp'
    isp_count = 1
    areaCode_count = 4

    szSQL = f"select area_code from mobile_info group by area_code limit {areaCode_count}"
    results = _db.query(szSQL)
    listAreaCode =  []
    for row in results:
        listAreaCode.append(row[0])

    print (listAreaCode)




#     # switch
#
    szSQL = f"""
    insert into enterprise_enable_info
      (enterprise_id, isolated)
    values
      ('{enterprise_id}', 1)
    """
    _db.execute(szSQL)

    szSQL = f"""
        insert into number_rule_info
          (enterprise_id, enable_rule)
        values
          ('{enterprise_id}', '1')
        """
    _db.execute(szSQL)

    # new pool
    # every time you excute it, you can build a new pool, because id increment auto, and you  can get the pool id
    # enterprise_id is must
    szSQL = f"""
    insert into number_pool
        (enterprise_id,
        time_frame,
        nvalid_times,
        pool_desc,
        name,
        use_last_connected_nummber,
        use_group_by_order)
    values
        ('{enterprise_id}', 0, 0, 'test', 'test', 0, 0)
    """
    _db.execute(szSQL)

    # need a sql to get a pool id

  # new group, similar pool
    szSQL = f"""
        insert into number_group
            (enterprise_id,
            group_name,
            number_choice_type,
            enable_overflow,
            enable_overflow_to_custom,
            match_type)
        values
            ('{enterprise_id}', 'test', 1, 0, 0, 1)
        """
    _db.execute(szSQL)

    # need a interface to get group id
    szSQL = f"""
    select a.id, b.id
        from number_pool a, number_group b
    where a.enterprise_id = b.enterprise_id
        and a.enterprise_id = '{enterprise_id}'
    """
    results = _db.query(szSQL)
    for row in results:
        pool_id = row[0]
        group_id = row[1]


    print ("pool_id: ", pool_id)
    print ("group_id: ",  group_id)

    # pool_id = 882
    # group_id = 68


# Bind with pool ID and group ID
    szSQL = f"""
        insert into pool_group_relation
            (enterprise_id, pool_id, group_id)
        values
            ('{enterprise_id}', {pool_id}, {group_id})
        """
    _db.execute(szSQL)




#########################################################

    # new number
    # szSQL = """
    #     insert into dialout_number_info
    #         (enterprise_id, number, area_alias, isp_code, open_date, enable_number)
    #     values
    #         ('10010', '2001', '010', 'isp1', '20200611', 2)
    #     """
    # data = _db.execute(szSQL)

    # bind number and group_id

    # szSQL = """
    #         insert into group_number_relation
    #             (group_id, number, enterprise_id) values
    #             (69, '2001', '10010')
    #         """
    # data = _db.execute(szSQL)

    #############################################################


    # pool_id = 892
    # group_id = 70


    # for number in range(start_num, start_num + number_count):
    #     id = number % isp_count
    #     isp_code = f"{enterprise_id}_{isp_identity}_{id}"
    #     szSQL = f"""
    #         insert into dialout_number_info
    #             (enterprise_id, number, area_alias, isp_code, open_date, enable_number)
    #         values
    #             ('{enterprise_id}', '{number}', '010', '{isp_code}', '20200616', 2)
    #         """
    for number in range(start_num, start_num + number_count):
        id = number % isp_count
        areaID = number % areaCode_count

        isp_code = f"{enterprise_id}_{isp_identity}_{id}"
        szSQL = f"""
            insert into dialout_number_info
                (enterprise_id, number, area_alias, isp_code, open_date, enable_number, area_type)
            values
                ('{enterprise_id}', '{number}', '{listAreaCode[areaID]}', '{isp_code}', '20200616', 2, {areaID % 2 + 1})
            """
        # print (szSQL)
        _db.execute(szSQL)

        szSQL = f"""
                insert into group_number_relation
                    (group_id, number, enterprise_id) values
                    ({group_id}, '{number}', '{enterprise_id}')
                """
        data = _db.execute(szSQL)



    # add para limit

    for isp_id in range(isp_count):
        isp_code = f"{enterprise_id}_{isp_identity}_{isp_id}"
        szSQL = f"""
                insert into isp
                    (enterprise_id, isp_code, enable_ani_frequency_limit)
                values
                    ('{enterprise_id}', '{isp_code}', 1)
                """
        _db.execute(szSQL)

        szSQL = f"""
                    insert into ani_limit
                      (enterprise_id,
                       type,
                       isp_code,
                       time_unit_minute,
                       time_unit_hour,
                       time_unit_day,
                       time_unit_week,
                       time_unit_month)
                    values
                        ('{enterprise_id}', 0, '{isp_code}', 1000, 4500, 50000, 300000, 1000000)
                    """
        _db.execute(szSQL)