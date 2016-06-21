#!/usr/bin/env python
#coding=utf8

from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os
import re
import shutil
import random
import xhttp

print '...hyperion 1.3 version...'
    
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
    if os.path.isdir('1'):
        shutil.rmtree('1')
        os.mkdir('1')
    else:
        os.mkdir('1')
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
    appid_key = read_appkey.readline()
    s_key = read_appkey.readline()
    if len(appid_key) == 0 and len(s_key) == 0:
        print '##[Notice]##'
        print '##[Please input you appid and scereKey]##'
        save_appkey = open('appkey', 'a')
        appid = raw_input('Input you addid:\n')
        save_appkey.writelines(appid)
        skey = raw_input('Input you skey:\n')
        save_appkey.writelines(skey)
        save_appkey.close()
        return(appid, skey)
    else:
        return(appid_key, s_key)    


def translation_txt():
    
    #Usage: Translation the target file
    
    print '<Start translation>'
    appid_return, secretKey_return = app_key()
    appid = appid_return.strip('\n')
    secretKey = secretKey_return.strip('\n')
    loop = True
    count_num = 1
    english = []
    while loop:
        pig_for_everytime = 1
        txt_name = '%d_temp.txt' % count_num
        txt_name_after = '1/%s' % txt_name
        print txt_name_after
        if os.path.exists(txt_name_after):
            
            if get_trans_txt(txt_name_after):
                english = get_trans_txt(txt_name_after)
                for q in english:
                    q = q.strip('\n')
                    http_return = xhttp.xhttp(appid, secretKey, q, "en", "zh")
                    pig = re.findall(r'<html>', http_return)
                    if len(pig) != 0:
                        loop_pig = True
                        while loop_pig:
                            if pig_for_everytime > 1:
                                print '<*****Ok, I give up.*****>'
                                rescue_q = 'Sorry, I try 2 times and it still can not work'
                                http_return = xhttp.xhttp(appid, secretKey, rescue_q, "en", "jp")
                                loop_pig = False
                            else:
                                print '<-----The program find some bug in sentences----->'
                                print '<-----We will rescue the work and translate the as much as we can do----->'
                                print '<-----If you find more bug in translate you srt file----->'
                                print '<-----Please send a email with you srt file to super_big_hero@163.com----->'
                                print '<-----Thanks----->'
                                q = re.findall('[A-Za-z]+', q)
                                rescue_q = ' '.join(q)
                                http_return = xhttp.xhttp(appid, secretKey, rescue_q, "en", "zh")
                                pig = re.findall(r'<html>', http_return)
                                if len(pig) != 0:
                                    pig_for_everytime += 1
                                else:
                                    loop_pig = False
                        
                    print http_return
                    http_mid = eval(http_return)
                    http_return_1 = http_mid['trans_result']
                    http_return_2 = http_return_1[0]
                    http_return_3 = http_return_2['dst']
                    op = open(txt_name_after, 'a')
                    op.writelines(http_return_3)
                    op.write('\n')
                    if op:
                        op.close()
            count_num += 1
        else:
            loop = False
    print '<End translation>'


def join_txt():
    
    #Usage: Merge the final result
    
    print '<Start join>'
    result_name = '2/result.docx'
    join_judge = True
    nb = 1
    if not os.path.isdir('2'):
        os.mkdir('2')
    else:
        if os.path.exists('2/result.docx'):
            result_name = '2/result_%d.docx' % random.randint(2, 10)
            print 'Warning, you should take the result out of the 2 until do next translate'
            print 'I put the new result in %s' % result_name
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
