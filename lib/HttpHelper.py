import urllib2

class HttpHelper:
    
    def __init(self):
        pass
    
    def get(self,url,referer):
        request = urllib2.Request(url)
        request.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;)')
        if referer:
            request.add_header('Referer',referer)
        opener = urllib2.build_opener()    
        data = opener.open(request).read()
        return data

    
def main():
    hh = HttpHelper()
    data = hh.get('http://hq.sinajs.cn/list=s_sh000001','http://finance.sina.com.cn/')
    print data

if __name__ == '__main__':    
    main()