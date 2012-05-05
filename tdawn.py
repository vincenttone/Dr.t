#-* Encoding: utf-8 *-
import urllib, urllib2, cookielib

class Dawn:
    '''这是一个访问浏览器的方法，目前只是写着玩，已经一年没有写Python，该忘的都忘了吧'''
    timeout = 30

    def __init__(self):
        '''初始化模块,增加cookie支持'''
        httpHandler = urllib2.HTTPHandler()
        httpsHandler = urllib2.HTTPSHandler()
        cookie = cookielib.CookieJar()
        cookie_support = urllib2.HTTPCookieProcessor(cookie)
        opener = urllib2.build_opener(cookie_support, httpHandler, httpsHandler)
        urllib2.install_opener(opener)

    def getHeader(self):
        '''返回浏览器header'''
        header = {
            "User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.2.13) Gecko/20101203 Firefox/3.6.13",
            #"User-Agent" = "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language":"zh-cn,zh;q=0.5",
            #"Accept-Encoding":"gzip,deflate",
            "Accept-Charset":"GB2312,utf-8;q=0.7,*;q=0.7",
            "Keep-Alive":"115",
            "Connection":"keep-alive"
            }
        return header

    def request(self, url, headers=None, data = None):
        '''请求处理'''
        if headers is None:
            header = self.getHeader()

        #开始设置请求数据
        req = urllib2.Request(
            url = url,
            headers = header
            )
        if data is not None:
            data = urllib.urlencode(data)

        #请求开始
        try:
            request = urllib2.urlopen(req, data, self.timeout)
            source = request.read()
            request.close()
        except:
            source = None
            #print "connect faild..."
            
        return source

if __name__ == "__main__":
    dawn = Dawn()
    hi = dawn.request("http://www.baidu.com")
    print hi
