# -*- coding:utf8 -*-
import sys
try :
    reload(sys)
    sys.setdefaultencoding('utf8')
except :
    pass

import re

def gnoon(_dic_rules, _data_raw) :
    term = ''
    term_display = ''
    term_class = ''
    delimiters = []
    vals = {}
    val =  ''

    for dic_rule in _dic_rules :
        for ext in dic_rule :
            for k, v in ext.items() :
                if k == 'term' :
                    term = v
                elif k == 'delimiters' :
                    delimiters = v
                elif k == 'term_display' :
                    term_display = v
                elif k == 'class' :
                    term_class = v
        # find the line 
        val = re.findall(re.compile(r".*%s.*"%(re.escape(term)), re.MULTILINE), _data_raw)[0]
        for delimiter in delimiters :
            for k, v in delimiter.items() :
                if v == 0 :
                    val = "".join(re.split(re.escape(k), val)[v]).strip()
                else :
                    val = k.join(re.split(re.escape(k), val)[v:]).strip()

        print(term_class + " : " + term_display + " : " + val)
        vals.setdefault(term_class, []).append({term_display : val})
        
    return vals

