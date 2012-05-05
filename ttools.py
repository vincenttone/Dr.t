#-*- Encoding: utf-8 -*-
import sys

class Tools:
    '''常用方法'''

    def recodeIt(self, data, f_code = None, t_code = None):
        '''重新编码一次'''
        if f_code is None:
            f_code = sys.getfilesystemencoding()
        
        if t_code is None:
            t_code = sys.getfilesystemencoding()

        if f_code == t_code:
            return data
        
        return data.decode(f_code).encode(t_code)

    def encodeIt(self, data, t_code=None):
        '''主要用于输出，不出乱码'''
        if t_code is None:
            t_code = sys.getfilesystemencoding()
        
        return data.encode(t_code)

        
