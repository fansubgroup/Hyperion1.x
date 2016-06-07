#!/usr/bin/env python
#coding=utf8

from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os
import re
import urllib
import httplib
import md5
import random
import json

print '...hyperion 1.2 version...'
    
def search_txt(path, word):
    
    #Usage: Search and find the target file
    
    for filename in os.listdir(path):
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                if re.match(word, f):
                    print '\n' + '<<<[' + f + ']>>>' + '\n'
                    try:
                        choice = raw_input('Translation this file?[y/n]')
                        if choice == 'y':
                            return f
                        elif choice == 'n':
                            print 'Next-->'
                    except KeyboardInterrupt:
                        print 'Exit programs'
    print 'There have not that file  >_<! '
    print 'Please check your name again  >0< '

def get_txt_name():
    
    #Usage: Return the target file
    
    try:
        name = raw_input('Input your file name: ')
        path = os.getcwd()
        filename = search_txt(path, name)
        if filename:
            print filename
            return filename
        else:
            print 'Over the translation'
    except KeyboardInterrupt:
        print 'Exit Programs'


def split_txt():
    
    # Usage: split the src file into cells
    
    print '<Start split>'
    
    while True:
        filename = get_txt_name()
        if filename:
            break
    first_line = 1
    fp = open(filename, 'r')
    null_line_count = 1
    time_list = []
    english_list = []
    num_list = []
    null_list = []
    for f_miss in fp.readlines():
        f = f_miss.strip('\r\n')
        
        find_1x = re.findall(r"\-", f)
        find_2x = re.findall(r"\>", f)
        
        if len(find_1x):
            if len(find_2x):
                time_list.append(f)
                    
        find_english = re.findall("[A-Za-z]", f)
        f_mid = re.sub("\D", "", f)
        find_number = re.findall("[0-9]+", f_mid)
        if len(find_english):
            english_list.append(f)
        if len(find_1x) == 0:
            if len(find_english) == 0:
                if first_line:
                    if len(find_number) != 0:
                        num_list.append(f_mid)
                        first_line = 0
                else:
                    time_list.append(f)
                
        if len(find_1x) == 0:
            if len(find_2x) == 0:
                if len(find_english) == 0:
                    if len(find_number) == 0:
                        save_name = "%d_temp.txt" % null_line_count
                        save_fp = open('1/%s' % save_name, 'a')
                        num_save = num_list[0]
                        save_fp.writelines(num_save)
                        save_fp.writelines('\n')
                        
                        time_line = time_list[0]
                        save_fp.writelines(time_line)
                        save_fp.writelines('\n')
                        
                        for e in english_list:
                            save_fp.writelines(e)
                            save_fp.writelines('\n')
                            
                        save_fp.writelines("\n")
                        save_fp.close()
                        null_line_count += 1
                        first_line = 1
                        
                        null_list.append(f)
                        for t in xrange(0, len(time_list)):
                            time_list.pop()
                        for e in xrange(0, len(english_list)):
                            english_list.pop()
                        for num in xrange(0, len(num_list)):
                            num_list.pop()
                        for nu in xrange(0, len(null_list)):
                            null_list.pop()
    print '<End split>'


def get_trans_txt(input_file):
    
    #Usage: Return the translation lines
    
    english_pool = []
    find_english = re.compile("[A-Za-z]+")
    try:
        fp = open(input_file, 'r')
        for j in fp.readlines():
            is_word = find_english.findall(j)
            if len(is_word) == 0:
                continue
            elif len(is_word) != 0:
                english_pool.append(j)
    except Exception, e:
        print e
    finally:
        if fp:
            fp.close()
            return english_pool


def app_key():
    
    #Usage: Save or read appid and secreKey
    
    read_appkey = open('appkey', 'r')
    appid_c = 1
    appid_list = []
    skey_list = []
    ret = []
    for ra in read_appkey.readlines():
        if appid_c == 1:
            appid_list.append(ra)
            appid_c = 0
        elif appid_c == 0:
            skey_list.append(ra)
    read_appkey.close()
    if len(appid_list) == 1:
        if len(skey_list) == 1:
            ret.append(appid_list[0])
            ret.append(skey_list[0])
            return ret
        elif len(skey_list) > 1:
            print 'skey error'
    elif len(appid_list) > 1:
        print 'appid error'
    else:
        print '##[Notice]##'
        print '##[Please input you appid and scereKey]##'
        save_appkey = open('appkey', 'a')
        appid = raw_input('Input you addid:\n')
        save_appkey.writelines(appid)
        save_appkey.writelines('\n')
        skey = raw_input('Input you skey:\n')
        save_appkey.writelines(skey)
        save_appkey.close()
        ret.append(appid)
        ret.append(skey)
        return ret


def translation_txt():
    
    #Usage: Translation the target file
    
    print '<Start translation>'
    appid_return, secretKey_return = app_key()
    appid = appid_return.strip('\n')
    secretKey = secretKey_return.strip('\n')
    print appid
    print secretKey
    loop = True
    count_num = 1
    english = []
    httpClient = None
    myurl = '/api/trans/vip/translate'
    while loop:
        txt_name = '%d_temp.txt' % count_num
        txt_name_after = '1/%s' % txt_name
        if os.path.exists(txt_name_after):
            if get_trans_txt(txt_name_after):
                english = get_trans_txt(txt_name_after)
                for q in english:
                    fromLang = 'en'
                    toLang = 'zh'
                    salt = random.randint(32768, 65536)
                    sign = appid+q+str(salt)+secretKey
                    m1 = md5.new()
                    m1.update(sign)
                    sign = m1.hexdigest()
                    myurl = myurl+'?appid='+appid+'&q='+urllib.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
                    try:
                        httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
                        httpClient.request('GET', myurl)
                        response = httpClient.getresponse()
                        u = response.read()
                        json_mid = json.loads(u)
                        dict_trans = json_mid.get('trans_result')
                        dict_trans_mid = dict_trans[0]
                        result_mid = dict_trans_mid.get('dst')
                        result = (result_mid).encode("UTF-8")
                        print q
                        print result
                        try:
                            op = open(txt_name_after, 'a')
                            op.writelines(result)
                            op.write('\n')
                            if op:
                                op.close()
                        except Exception, ty:
                            print ty
                    except Exception, el:
                        print el
                    finally:
                        if httpClient:
                            httpClient.close()
                count_num += 1
            else:
                continue
        else:
            loop = False
    print '<End translation>'


def join_txt():
    
    #Usage: Merge the final result
    
    print '<Start join>'
    join_judge = True
    nb = 1
    result_name = '2/result.docx'
    wp = open(result_name, 'a')
    while join_judge:
        file_path = '%d_temp.txt' % nb
        file_path_2 = '1/%s' % file_path
        if os.path.exists(file_path_2):
            dp = open(file_path_2, 'r')
            for k in dp.readlines():
                wp.writelines(k)
            wp.write('\n')
            nb += 1
            dp.close()
        else:
            join_judge = False
    wp.close()
    print '<End join>'


def delete_txt():
    
    #Usage: Delete the temp file
    
    print '<Start delete>'
    remove_name = '1/%d_temp.txt'
    count = 1
    some_true = True
    while some_true:
        file_name = remove_name % count
        if os.path.exists(file_name):
            os.remove(file_name)
            count += 1
        else:
            some_true = False
            print '<End delete>'


def main():
    split_txt()
    translation_txt()
    join_txt()
    delete_txt()

if __name__ == "__main__":
    main()
