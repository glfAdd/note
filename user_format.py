"""
医疗质量督查项目数据处理脚本
1. 检查提交的用户的账号是否有效, 如果填写的是手机号, 则用手机号去 mysql 查用户名, 打印出没有找到账号的用户, 补全后程序才能继续执行
2. 检查科室名时候已经存在, 输出缺少的科室, 补全后程序才能继续执行
3. 检查医院是否存在, 输出缺少的医院, 补全后程序才能继续执行
4. 

"""
import uuid
from datetime import datetime
from typing import Any

import pandas as pd


class UserFormat:
    user_info_file_path = '/Users/glfadd/Desktop/权限/用户数据处理_副本.xlsx'
    user_info_from_mysql_path = '/Users/glfadd/Desktop/权限/数据库查到的用户登录信息.xlsx'
    dept_path = '/Users/glfadd/Desktop/权限/(基础数据)科室.xlsx'
    org_path = '/Users/glfadd/Desktop/权限/(基础数据)医院.xlsx'
    # 文件输出路径
    save_user_path = '/Users/glfadd/Desktop/权限/姓名和账号映射.xlsx'
    save_dept_sql_path = '/Users/glfadd/Desktop/权限/sql创建科室.txt'
    save_user_sql_path = '/Users/glfadd/Desktop/权限/sql创建用户.txt'
    save_role_sql_path = '/Users/glfadd/Desktop/权限/sql创建角色.txt'
    # 科室编码开始编码(是当前的下一个)
    dept_index = 12000
    # 角色
    d_role = {
        "督查员": 1,
        "科室管理员": 2,
        "院管理员": 3,
        "平台管理员": 4,
        "集团管理员": 5
    }
    d_role_fix = {
        "督察员": "督查员",
        "院级管理员": "院管理员",
        "医疗平台管理员": "平台管理员",
    }

    # 忽略的医院
    pass_org = ['华北石油油建医院', '华北石油井下医院']

    def __init__(self):
        self.l_base_user_data = self.read_base_user_data()
        self.d_mysql_user = self.read_user_from_excel()
        self.d_dept = self.read_dept_from_excel()
        self.d_org = self.read_org_from_excel()
        # 用于生成 excel 的最终数据
        self.data = []

    @staticmethod
    def current_datetime_to_str() -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def get_uuid():
        return str(uuid.uuid4()).replace('-', '')

    @staticmethod
    def format_string(s: Any) -> str:
        """
        格式化字符串, 去掉非法字符

        Args:
            s: 字符串或者数字

        Returns:
            string
        """
        new_s = '%s' % s
        return new_s.replace(' ', '').replace('\n', '').replace('\t', '').replace('\r', '')

    @staticmethod
    def print_error(error_list: list) -> None:
        for i in error_list:
            org_name = format(i['org_name'], ' <20')
            dept_name = format(i['dept_name'], ' <20')
            nickname = format(i['nickname'], ' <20')
            mobile_phone = format(i['mobile_phone'], ' <20')
            account = format(i['account'], ' <20')
            role = format(i['role'], ' <10')
            print('%s   %s   %s   %s   %s   %s' % (org_name, dept_name, nickname, mobile_phone, account, role))

    def read_base_user_data(self) -> list:
        """
        读取用户提供的信息

        Returns:
            用户信息列表
        """
        base_data = []
        f = pd.read_excel(self.user_info_file_path, sheet_name='第一批')
        for index, row in f.iterrows():
            org_name = self.format_string(row['单位'])
            dept_name = self.format_string(row['科室名称'])
            nickname = self.format_string(row['姓名'])
            mobile_phone = self.format_string(row['手机号'])
            role = self.format_string(row['开通权限'])
            if org_name in self.pass_org:
                continue
            # 邮箱切分
            account = self.format_string(row['智慧通用账号'])
            account = account.split('@')[0]
            base_data.append({
                'org_name': org_name,
                'dept_name': dept_name,
                'nickname': nickname,
                'mobile_phone': mobile_phone,
                'role': role,
                'account': account,
            })
        return base_data

    def read_dept_from_excel(self) -> dict:
        """
        从 (基础数据)科室.xlsx 读取已有科室信息

        Returns:
            科室名称和科室编码映射
        """
        data = dict()
        f = pd.read_excel(self.dept_path, sheet_name='Sheet1')
        for index, row in f.iterrows():
            m = self.format_string(row['科室名称'])
            a = self.format_string(row['科室编码'])
            data[m] = a
        return data

    def read_org_from_excel(self) -> dict:
        """
        读取医院编码和名称映射信息

        Returns:
            医院名称和编码映射
        """
        data = dict()
        f = pd.read_excel(self.org_path, sheet_name='Sheet1')
        for index, row in f.iterrows():
            code = self.format_string(row['系统医院编码'])
            data[self.format_string(row['系统医院名称'])] = code
            data[self.format_string(row['简称1'])] = code
            data[self.format_string(row['简称2'])] = code
            data[self.format_string(row['简称3'])] = code
            data[self.format_string(row['简称4'])] = code
            data[self.format_string(row['简称5'])] = code
            data[self.format_string(row['简称6'])] = code
        return data

    def read_user_from_excel(self) -> dict:
        """
        根据手机号从数据库查询到的用户账号

        Returns:
            手机号和用户登录名映射
        """
        data = dict()
        f = pd.read_excel(self.user_info_from_mysql_path, sheet_name='Sheet1')
        for index, row in f.iterrows():
            m = self.format_string(row['mobile'])
            a = self.format_string(row['username'])
            data[m] = a
        return data

    def begin(self):
        """
        开始执行脚本

        Returns:
            None
        """
        account_error = self.verify_user()
        if account_error:
            print('******************** 没匹配正确 >>>智慧通用账号<<< 的用户 ********************')
            self.print_error(account_error)
        else:
            print('******************** 智慧通用账号 匹配完成 ********************')
            self.save_user_info()

        role_error = self.verify_role()
        if role_error:
            print('******************** 没匹配正确 >>>角色<<< 的用户 ********************')
            self.print_error(role_error)
        else:
            print('******************** 角色 匹配完成 ********************')

        dept_error = self.verify_dept()
        if dept_error:
            print('******************** 没匹配正确 >>>科室<<< 的用户 ********************')
            self.print_error(dept_error)
            self.save_dept_insert_sql(dept_error)
        else:
            print('******************** 科室 匹配完成 ********************')

        org_error = self.verify_org()
        if org_error:
            print('******************** 医院未匹配到编码 ********************')
            t = set()
            for i in org_error:
                t.add(i['org_name'])
            print(t)
        else:
            print('******************** 医院 匹配完成 ********************')

        if not len(account_error) == 0 or not len(role_error) == 0 or not len(dept_error) == 0:
            print('******************** 脚本退出!!!!! 补全信息后重新执行 ********************')
            exit(0)

        self.save_user_insert_sql()
        self.save_role_insert_sql()

    def verify_user(self) -> list:
        """
        检查用户, 如果存在匹配不到的, 退出脚本

        Returns:
            错误的用户信息
        """
        l_error = []
        for i in self.l_base_user_data:
            mobile_phone = i['mobile_phone']
            account = i['account']
            if account.isnumeric():
                n_account = self.d_mysql_user.get(mobile_phone)
                if n_account:
                    i['account'] = n_account
                else:
                    l_error.append(i)
        return l_error

    def verify_role(self) -> list:
        """
        检查权限角色, 退出脚本

        Returns:
            None
        """
        error_list = []
        for i in self.l_base_user_data:
            role = self.d_role.get(i['role'])
            if not role:
                n_role = self.d_role_fix.get(i['role'])
                if n_role:
                    i['role'] = n_role
                else:
                    error_list.append(i)
                    continue

            i['role_code'] = self.d_role.get(i['role'])
        return error_list

    def verify_dept(self) -> list:
        """
        检查部门, 如果存在匹配不到的, 退出脚本

        Returns:
            错误的科室
        """
        error_list = []
        for i in self.l_base_user_data:
            temp_str = self.d_dept.get(i['dept_name'])
            if temp_str:
                i['dept_code'] = temp_str
            else:
                error_list.append(i)
        return error_list

    def verify_org(self) -> list:
        """
        设置医院名称映射

        Returns:
            None
        """
        error_list = []
        for i in self.l_base_user_data:
            org_code = self.d_org.get(i.get('org_name'))
            if org_code:
                i['org_code'] = org_code
            else:
                error_list.append(i)
        return error_list

    def save_user_info(self) -> None:
        """
        保存用户名和账号到 excel 用户开通应用权限, 用户开通用户权限

        Returns:
            None
        """
        l_nickname = []
        l_account = []
        for i in self.l_base_user_data:
            l_nickname.append(i['nickname'])
            l_account.append(i['account'])
        data = {
            '姓名': l_nickname,
            '登录名': l_account,
        }
        df = pd.DataFrame(data)
        df.to_excel(self.save_user_path, index=False)
        print('******************** 需要开通权限的用户已保存到 %s ********************' % self.save_user_path)

    def save_dept_insert_sql(self, data: list) -> None:
        """
        生成 insert 科室的 sql 语句

        Args:
            data: 新建科室信息

        Returns:
            None
        """
        base = 'INSERT INTO `dept` ( `uuid`, `office_name`, `office_code`, `enabled`, `modified_date`, `modified_by` ) VALUES '
        data_list = []
        for i in data:
            create_by = 'liyunzhi'
            t = " ( '%s', '%s', %s, %s, '%s', '%s' ) " % (self.get_uuid(), i['dept_name'], self.dept_index, 1, self.current_datetime_to_str(), create_by)
            data_list.append(t)
            self.dept_index += 1

        sql_str = base + ','.join(data_list) + ';'
        with open(self.save_dept_sql_path, 'w', encoding='utf-8') as f:
            f.write(sql_str)
        # print(sql_str)
        print('******************** 创建科室 sql 语句已保存到 %s ********************' % self.save_dept_sql_path)

    def save_user_insert_sql(self) -> None:
        """
        生成 insert 用户 sql 语句

        Returns:
            None
        """
        base = "INSERT INTO `health_division_user_info` (`uuid`, `platform_name`, `platform_code`, `dept_name`, `dept_code`, `office_name`, `office_code`,`userid`,`username`, `mobile`, `email`, `modified_date`,`modified_by`) VALUES "
        data_list = []
        for i in self.l_base_user_data:
            create_by = 'liyunzhi'
            t = " ('%s','','','%s','%s','%s','%s','%s','%s','%s','','%s','%s') " % (
                self.get_uuid(), i['org_name'], i['org_code'], i['dept_name'], i['dept_code'], i['account'], i['nickname'], i['mobile_phone'],
                self.current_datetime_to_str(), create_by)
            data_list.append(t)
        sql_str = base + ','.join(data_list) + ';'
        with open(self.save_user_sql_path, 'w', encoding='utf-8') as f:
            f.write(sql_str)
        # print(sql_str)
        print('******************** 用户 sql 语句已保存到 %s ********************' % self.save_user_sql_path)

    def save_role_insert_sql(self) -> None:
        """
        生成 insert 用户权限 sql 语句

        Returns:
            None
        """
        base = "INSERT INTO `health_division_user_roles` (`userid`, `permission`, `enabled`, `modified_date`, `modified_by`) VALUES "
        data_list = []
        for i in self.l_base_user_data:
            create_by = 'liyunzhi'
            t = " ('%s', %s, %s, '%s', '%s') " % (i['account'], i['role_code'], 1, self.current_datetime_to_str(), create_by)
            data_list.append(t)
        sql_str = base + ','.join(data_list) + ';'
        with open(self.save_role_sql_path, 'w', encoding='utf-8') as f:
            f.write(sql_str)
        # print(sql_str)
        print('******************** 用户权限 sql 语句已保存到 %s ********************' % self.save_role_sql_path)


if __name__ == '__main__':
    u = UserFormat()
    u.begin()
    print('成功 !!!!!!!')
