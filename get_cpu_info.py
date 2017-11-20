'''
获取CPU信息,并将结果以表格的形式展现出来
author:zhua
'''
from utils import utils
from pychartdir import *

PATH = lambda p: os.path.abspath(p)

# 获取CPU process
pkg_name = 'com.eebbk.vtraining'

# 刷新次数
fresh_times = 20

# 获取cpu数据
def get_cpu():
    cpu = []
    comand_info = 'top -n %s | findstr %s$' % (str(fresh_times), pkg_name)

    result_info = utils.shell(comand_info).stdout.readlines()
    print(result_info)

    for line in result_info:
        print(line)
        temp_list = str(line.decode('utf-8')).split()
        if len(temp_list) >= 3:
            cpu.append(temp_list[2])

    return cpu


#显示到chart
def line_chart():
    cpu_datas = []
    temp_datas = get_cpu()
    # 去掉%,转换为int
    for cpu_data in temp_datas:
        print(cpu_data)
        cpu_datas.append(int(cpu_data.split("%")[0]))

    labels = []
    # 设置横坐标
    for i in range(1, fresh_times + 1):
        labels.append(str(i))

    if fresh_times <= 50:
        xArea = fresh_times * 40
    elif 50 < fresh_times <= 90:
        xArea = fresh_times * 20
    else:
        xArea = 1800

    c = XYChart(xArea, 800, 0xCCEEFF, 0x000000, 1)
    c.setPlotArea(60, 100, xArea - 100, 650)
    # c.addlegend(50, 30, 0, "arialbd.ttf", 12).setBackground(Transparent)

    c.addTitle("cpu info %s" % pkg_name, "arialbd.ttf", 12)
    c.yAxis().setTitle("The numerical", "arialbd.ttf", 12)
    c.xAxis().setTitle("Times", "arialbd.ttf", 12)

    c.xAxis().setLabels(labels)

    # 自动设置x轴步长
    if fresh_times <= 50:
        step = 1
    else:
        step = fresh_times / 50 + 1
    c.xAxis().setLabelStep(step)

    layer = c.addLineLayer()
    layer.setLineWidth(2)
    layer.addDataSet(cpu_datas, 0xff0000, "cpu(%)")
    path = PATH("%s/chart" %os.getcwd())

    if not os.path.isdir(path):
        os.makedirs(path)

    # 图片保存至脚本当前目录的chart目录下
    c.makeChart(PATH("%s/%s.png" % (path, utils.timestamp())))

if __name__ == '__main__':
    line_chart()
