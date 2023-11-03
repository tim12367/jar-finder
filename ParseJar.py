# -*- coding: utf-8 -*-
import os
import zipfile
"""
解析Jar檔

Created on Tue Oct 31 21:27:37 2023
@author: Tim
"""


class ParseJar():
    # 在當前位置 抓取jar檔資料
    def parseJarCurrentFolder(self):
        currentDir = os.getcwd()
        self.parseJarByFolder(currentDir)

    # 依照路徑 抓取jar檔資料
    def parseJarByFolder(self, path):
        for root, dir, files in os.walk(path, topdown=True):
            for file in files:
                fileExtension = os.path.splitext(file)[1]
                print("root: ", root, "\nfile: ", file, "\nfile_extension: ", fileExtension, '\n')

                # 若檔案為jar 則解壓縮
                if ".jar" == fileExtension:
                    fullPath = os.path.join(root, file)
                    self.extractJar(fullPath)

    def extractJar(self, fullPath):
        with zipfile.ZipFile(fullPath, 'r') as zipObj:
            for file_info in zipObj.infolist():
                print("JAR內容", file_info.filename)
                # 若為檔案
                if "/" != file_info.filename[-1]:
                    print("是檔案", "檔案大小為 : ", file_info.file_size)

# main 方法
def main():
    parser = ParseJar()
    parser.parseJarCurrentFolder()


if __name__ == "__main__":
    main()
