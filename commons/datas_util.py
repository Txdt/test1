import xlrd


class DataUtil:
    # def __init__(self, data_path):
    #     self.data_path = data_path

    def get_regist_data(is_head=True):
        xlsx = xlrd.open_workbook(r'D:\桌面\7月找工作\09-web自动化实战\test1\datas\msjy3.xlsx')
        # 选中第一张表
        sheet = xlsx.sheet_by_index(0)
        datas = []
        # 遍历每一行数据
        for i in range(sheet.nrows):
            datas.append(sheet.row_values(i))
        if is_head:
            # 去掉第一行
            datas = datas[1:]
        print(datas)
        return datas