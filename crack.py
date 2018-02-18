'''import zipfile
from threading import Thread
        
def extract(zFile,pw):
    try:
        zFile.extractall(pwd=pw)
        return True
    except Exception, e:
        print e
        return

def main():
    zFile = zipfile.ZipFile("evil.zip")
    f = open("dic.txt")
    for line in f.readlines():   
        pw = line.strip(" \n\t")
        t = Thread(targer=extract, args(zFile,pw))
        t.start()
        guess = extract(zFile, pw)
        print guess
        if guess:
            print "[+] successfully cracked - password = " + pw + "\n"
            exit(0)
        
if __name__ == '__main__':
    main()
    '''

import zipfile
import optparse
from threading import Thread


        
def extract(zFile,pw):
    try:
        zFile.extractall(pwd=pw)
        print "[+] successfully cracked - password = " + pw + "\n"
        exit(0)
    except Exception, e:
        pass

def main():
    parser = optparse.OptionParser("usage% -f <zipfile> -d <dictionary>" )
    parser.add_option("-f", dest="zname", type="string", help="specify zip file")
    
    parser.add_option("-d", dest="dname", type="string", help="specify dictionary file")
    
    (options,args) = parser.parse_args()
    
    if (options.zname == None) | (options.dname == None):
        print parser.usage
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    
    zFile = zipfile.ZipFile(zname)
    f = open(dname)
    for line in f.readlines():   
        pw = line.strip(" \n\t")
        t = Thread(target=extract, args=(zFile,pw))
        t.start()
        
if __name__ == '__main__':
    main()
    
