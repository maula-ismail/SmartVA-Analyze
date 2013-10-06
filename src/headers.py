#!/opt/virtualenvs/ihme-va/bin/pythonw

import csv
import string
import wx
import workerthread
import os

# Thread class that executes processing
class Headers():
    """Worker Thread Class."""
    def __init__(self, notify_window, input_file, output_dir):
        self._notify_window = notify_window
        self.inputFilePath = input_file
        self.output_dir = output_dir
        self.want_abort = 0

    def run(self):
        reader = csv.reader(open( self.inputFilePath, 'Ub'))
        writer = csv.writer(open(self.output_dir + os.sep + 'cleanheaders.csv', 'wb', buffering=0))
        
        updatestr = "Cleaning column headers\n"
        wx.PostEvent(self._notify_window, workerthread.ResultEvent(updatestr))

        first = 1
        for row in reader:
            newrow = list()
            if (first == 1):
                first = 2
                for col in row:
                    newcolname = ""
                    try:
                        lastindex = string.rindex(col, "-")
                        newcolname = col[lastindex+1:]
                    except ValueError:
                        newcolname = col
                    newrow.append(newcolname)

                writer.writerow(newrow)
            else:
                writer.writerow(row)


        return 1

    	
    def abort(self):
        self.want_abort = 1