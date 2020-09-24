#!/usr/bin/env python
import sys
import textwrap

class Srt_sort(object):
    def __init__(self, path, path_w, max_len):
        self._path = path
        self._path_w = path_w
        self._max_len = max_len

        with open(self._path) as f:
            self._l = f.readlines()
        f.close()
        # print self._l

    def insert_linefeed(self):
        add_number = 0
        for i in xrange(len(self._l) + add_number):
            counter = 0
            s_wrap_list = textwrap.wrap(self._l[i + add_number], self._max_len)

            # print i, s_wrap_list

            #if s_wrap_list != None:
            if len(s_wrap_list) > 1:
                self._l.pop(i + add_number)
                for j in xrange(len(s_wrap_list)):
                    s_wrap_list[j] = s_wrap_list[j] + '\r\n'
                    counter = counter + 1
                #s_wrap_list.append("\r\n")
                self._l[i + add_number: i + add_number] = s_wrap_list
                #add_number = add_number + counter
                add_number = add_number + counter - 1
                print s_wrap_list

    def output(self):
        # print self._l
        with open(self._path_w, mode='w') as f:
            f.writelines(self._l)


if __name__ == "__main__":
    args = sys.argv
    path = args[1]
    path_w = args[2] 
    srt_sort = Srt_sort(path,path_w,80)
    srt_sort.insert_linefeed()
    srt_sort.output()
