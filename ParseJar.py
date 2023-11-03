# -*- coding: utf-8 -*-
import os
"""
Parse jar and get info

Created on Tue Oct 31 21:27:37 2023
@author: Tim
"""


class ParseJar():
    '''在檔案位置抓取jar檔資料'''

    def doParseJarCurrentFolder(self):
        # 當前目錄位置
        currentDir = os.getcwd()
        self.doParseAllPath(currentDir)

    def doParseAllPath(self, path):
        # 遍歷當前目錄
        for root, dir, files in os.walk(path, topdown=True):  # topdown 是否優先遍歷TOP
            for file in files:
                print("root:", root, "files:", file, '\n')

    def doParseJar(self, path):
        print(path)

#main 方法
def main():
    parser = ParseJar()
    parser.doParseJarCurrentFolder()


if __name__ == "__main__":
    main()