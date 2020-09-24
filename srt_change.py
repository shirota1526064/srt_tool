#!/usr/bin/env python
import sys
import re

class Srt_change(object):
    def __init__(self, srt_path, current_str_path, result_pash):
        self.current_str_list = []
        self.srt_path = srt_path
        self.current_str_path = current_str_path
        self.result_path = result_path
        self.result_str = []

    def get_current_str_list(self):
        with open(self.current_str_path) as f:
            l = f.readlines()
        f.close()

        for i in xrange(1,len(l)):
            tmp_str = l[i]
            tmp_str_list = tmp_str.replace('\"','').split('\t')
            if len(tmp_str_list) == 4:
                self.current_str_list.append([tmp_str_list[0],tmp_str_list[3]])
            else:
                pass
        #print self.current_str_list

    def change_str(self):
        with open(self.srt_path) as f:
            l = f.readlines()
        f.close()

        count = 0

        for i in xrange(0,len(l)-2,4):
        #for i in xrange(0,200,4):
            if int(re.sub(r"\D", "", self.current_str_list[count][0])) == int(re.sub(r"\D", "", l[i])):
                print int(re.sub(r"\D", "", l[i]))
                #print int(re.sub(r"\D", "", self.current_str_list[count][0]))
                print l[i+2]
                print self.current_str_list[count][1]

                l[i+2] = self.current_str_list[count][1]
                count = count + 1
                if count == len(self.current_str_list):
                    break
        self.result_str = l

    def output(self):
        with open(self.result_path, mode='w') as f:
            f.writelines(self.result_str)


if __name__ == "__main__":
    args = sys.argv
    srt_path = args[1]
    current_str_path = args[2]
    result_path = args[3]

    srt_change = Srt_change(srt_path,current_str_path,result_path)

    srt_change.get_current_str_list()
    srt_change.change_str()
    srt_change.output()

    #path_w = args[2] 
    #srt_sort = Srt_sort(path,path_w,80)
    #srt_sort.insert_linefeed()
    #srt_sort.output()
