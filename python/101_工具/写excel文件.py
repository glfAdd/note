import xlsxwriter as xw
import pandas as pd
import openpyxl as op


def get_data():
    orderIds = [1, 2, 3]
    items = ['A', 'B', 'C']
    myData = ["风犬少年的天空", "重启", "半泽直树"]
    testData = [orderIds, items, myData]
    return testData


# xlsxwriter 一行一行写
def xw_toexcel(data, file_name):
    """ 通过 xlsxwriter 方式 """
    # 创建工作簿
    workbook = xw.Workbook(file_name)
    # 创建子表
    worksheet = workbook.add_worksheet("sheet")
    # 激活表
    worksheet.activate()
    # 设置表头
    title = ['序号', '等级', '名称']
    # 从A1单元格开始写入表头
    worksheet.write_row('A1', title)
    # 从第二行开始写入数据
    i = 2
    for j in range(len(data)):
        insertData = [data[0][j], data[1][j], data[2][j]]
        row = 'A' + str(i)
        worksheet.write_row(row, insertData)
        i += 1
    # 关闭表
    workbook.close()


def pd_toexcel(data, file_name):
    """ pandas方式 """
    # 用字典设置DataFrame所需数据
    dfData = {
        '序号': data[0],
        '等级': data[1],
        '名称': data[2]
    }
    # 创建DataFrame
    df = pd.DataFrame(dfData)
    # 存表，去除原始索引列（0,1,2...）
    df.to_excel(file_name, index=False)


def op_toexcel(data, file_name):
    """ openpyxl方式 """
    # 创建工作簿对象
    wb = op.Workbook()
    # 创建子表
    ws = wb['Sheet']
    # 添加表头
    ws.append(['序号', '等级', '名称'])
    for i in range(len(data[0])):
        d = data[0][i], data[1][i], data[2][i]
        # 每次写入一行
        ws.append(d)
    wb.save(file_name)


def main():
    # xw_toexcel(get_data(), '测试1.xlsx')
    # pd_toexcel(get_data(), '测试2.xlsx')
    op_toexcel(get_data(), '测试3.xlsx')


if __name__ == '__main__':
    main()
