import pymysql

"""
1）历史上有销量的目标医院，在新销量数据上没有了。
2）历史同一时期，某一家医院的销量减少超过10%
3）历史同一时期，整体目标医院（对照医院）的销量减少超过5%
4）历史同一时期，整体目标医院（对照医院）的销量增加超过10%
5）历史同一时期，某一家医院的销量增加超过30%
"""

mysqlInfo = {
    'host': 'rm-2ze72hfw6y2v2s1xiio.mysql.rds.aliyuncs.com',
    "user": 'ndc_test_all_user',
    "passwd": 'ndc123456--',
    "db": 'ndc_test',
    "port": 3306,
    "charset": 'utf8'
}


def connectDatabase(sql):  # 连接mysql数据库
    db1 = pymysql.connect(mysqlInfo['host'], mysqlInfo['user'], mysqlInfo['passwd'], mysqlInfo['db'], mysqlInfo['port'], charset='utf8')
    cursor1 = db1.cursor()
    cursor1.execute(sql)  # 执行数据库的查询命令
    results = cursor1.fetchall()  # 获取结果
    cursor1.close()
    db1.close()
    return results


def get_data(sql):  # 获取数据
    results = connectDatabase(sql)
    return results


def target_hci_check():
    """
    通过临时表医院数据,去匹配到库中医院维表数据,并且拿到hci_id协同prod_sales_ori_info表中的id对比,是否相同
    若相同,则对比销量数据,观察prod_sales_ori_info表中相同客户名称和项目名称的数据匹配关联,表中有销量的同期临时表也必须有销量即可
    若医院维表没有全部匹配成功,则直接报错;若销量没有,也直接报错
    :return:True or False
    """
    sql_01 = '''select count(1) from prod_sales_check_info a 
        left join prod_sales_data_info b on a.cust_hci_name = b.cust_hci_name
        left join (select * from prod_sales_data_info where sales_volume > 0) c on a.sales_date = c.sales_date and a.cust_id = c.cust_id and a.prod_id = c.prod_id and a.drug_prod_id = c.drug_prod_id and a.drug_prod_speci_id = c.drug_prod_speci_id and a.sales_volume = 0
        left join (select * from prod_sales_data_info where sales_volume = 0) d on a.sales_date = d.sales_date and a.cust_id = c.cust_id and a.prod_id = c.prod_id and a.drug_prod_id = c.drug_prod_id and a.drug_prod_speci_id = c.drug_prod_speci_id and a.num_boxes = 0
        where b.id is not null
        '''
    # # 拿到销量数据不符合的总数
    get_error_sum1 = get_data(sql_01)
    get_error_sum = get_data(sql_01)[0][0]

    # 若总数为0则直接通过,若不为0则返回错误
    if get_error_sum == 0:
        print('检测1:历史上有销量的目标医院，在新销量数据上没有问题')
    else:
        print('检测1:历史上有销量的目标医院，在新销量数据上存在' + get_error_sum + '家医院销量数据没有了')


def target_hci_of_every_month():
    '''
    2）历史同一时期，某一家医院的销量减少超过10%
    :return:
    '''
    sql_02 = '''
        select a.sales_date,a.cust_name,a.proj_name_ch,a.cust_hci_name,a.product_name,a.prod_speci,a.sales_volume,a.num_boxes, c.sales_volume
        from prod_sales_check_info a 
        left join prod_sales_data_info b on a.cust_hci_name = b.cust_hci_name
        left join (select * from prod_sales_data_info where sales_volume is not null) c on a.sales_date = c.sales_date and a.product_name = c.product_name and a.cust_name = c.cust_name and a.proj_name_ch = c.proj_name_ch and a.prod_speci = c.prod_speci and a.sales_volume = 0
        where b.id is not null;
        '''


if __name__ == '__main__':
    target_hci_check()
