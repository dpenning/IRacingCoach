import csv, colorsys, os, argparse, glob
import matplotlib.pyplot as plt

separate_lines = False

def getInverseCornerRadius(row, columnNameToRow):
    latAccelIndex = columnNameToRow['latAccel']
    speedIndex = columnNameToRow['speed']
    return float(row[latAccelIndex]) / (float(row[speedIndex]) ** 2)

def addPlotLine(series_x, series_y, offset, hue):
    plt.plot(
        series_x[1:-1],
        [x + offset for x in series_y[1:-1]],
        color=colorsys.hsv_to_rgb(hue, .7, .7)
    )

def readColumnSeriesFromFile(filepath, columnName=None, colFunction=None):
    f = open(filepath, 'r')
    csv_f = csv.reader(f)
    columnNameToRow = None
    series_x = []
    series_y = []
    for row in csv_f:
        if columnNameToRow == None:
            columnNameToRow = dict()
            for i, val in enumerate(row):
                columnNameToRow[val.strip()] = i

            if columnNameToRow == None:
                raise Exception('FUCK')
        else:
            if colFunction != None:
                series_y.append(colFunction(row, columnNameToRow))
            else:
                series_y.append(float(row[columnNameToRow[columnName]]))
            series_x.append(float(row[0]))
    f.close()
    return (series_x, series_y)

if __name__ == '__main__':
    series_x_list = []
    series_y_list = []
    for filepath in glob.glob('LoggedLaps/*.csv'):
        (series_x, series_y) = readColumnSeriesFromFile(filepath, colFunction=getInverseCornerRadius)
        series_x_list.append(series_x)
        series_y_list.append(series_y)

    offset = 0
    for i in range(0, len(series_y_list)):
        if separate_lines:
            # get the min/max of the values for offsetting
            min_val = min(series_y_list[i])
            max_val = max(series_y_list[i])
            offset += min_val
            addPlotLine(series_x_list[i], series_y_list[i], offset, float(i) / len(series_y_list))
            offset += max_val
        else:
            addPlotLine(series_x_list[i], series_y_list[i], offset, float(i) / len(series_y_list))
    plt.show()
