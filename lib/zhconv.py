#!/usr/bin/env python
#coding: utf-8
"""
zh-conv.py

Created by haoyu on 2012-02-15.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os

class ZhConv:
    """docstring for ZhConv"""
    def __init__(self):
        self.dic = {}
        self.dic['TW'] = None
        self.dic['HK'] = None
        self.dic['CN'] = None
        self.load_dic()
    # 生成转换字典
    def load_dic(self):
        table = open(os.path.join(os.path.dirname( os.path.realpath( __file__ ) ),'./ZhConversion.php'),'r').readlines()
        dic = dict()
        name = []
        for line in table:
            if line[0] == '$':
                #print line.split()[0][1:]
                name.append(dic)
                dic = dict()
            if line[0] == "'":
                word = line.split("'")
                dic[word[1]] = word[3]
        name[3].update(name[1]) # 简繁通用转换规则(zh2Hant)加上台湾区域用法(zh2TW)
        name[4].update(name[1]) # 简繁通用转换规则(zh2Hant)加上香港区域用法(zh2HK)
        name[5].update(name[2]) # 繁简通用转换规则(zh2Hans)加上大陆区域用法(zh2CN)
        [self.dic['TW'],self.dic['HK'],self.dic['CN']] = name[3],name[4],name[5]
    
    # 最大正向匹配
    def conv(self,string,lang):
        i = 0
        if self.dic.has_key(lang):
            dic = self.dic[lang]
        else:
            return string
        
        if lang == 'TW':
            dic = dic
        
        while i < len(string):
            #匹配的最大长度
            max_len = len(string) - i
            if max_len>30:
              max_len = 30
            for j in range(max_len, 0, -1):
                if string[i:][:j] in dic:
                    t = dic[string[i:][:j]]
                    string = string[:i] + t + string[i:][j:]
                    i += len(t) - 1
                    break
            i += 1
        return string

def main():
    zhconv = ZhConv()
    a="头发发展萝卜卜卦秒表表达"
    b="大衛碧咸在寮國見到了布希"
    c="大卫·贝克汉姆在老挝见到了布什"
    
    print a, ' <->  ', zhconv.conv(a,'TW')
    print b, ' <->  ', zhconv.conv(b,'CN')
    print c, ' <->  ', zhconv.conv(c,'HK')


if __name__ == '__main__':
    main()

