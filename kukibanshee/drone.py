import elist.elist as elel
from kukibanshee import rfc6265

def help():
    if(func_name == ''):
        doc = '''
            >>> from kukibanshee.drone import *
            >>> ckpair = "TS=0105b666"
            >>> ckpt = ckpair2tuple(ckpair)
            >>> ckpt
            ('TS', '0105b666')
            >>>
        '''
        print(doc)
    elif(func_name == ''):
        doc = '''
        '''
        print(doc)
    elif(func_name == ''):
        doc = '''
        '''
        print(doc)
    elif(func_name == ''):
        doc = '''
        '''
        print(doc)
    elif(func_name == ''):
        doc = '''
        '''
        print(doc)
    elif(func_name == ''):
        doc = '''
        '''
        print(doc)
    elif(func_name == ''):
        doc = '''
        '''
        print(doc)
    elif(func_name == ''):
        doc = '''
        '''
        print(doc)
    elif(func_name == ''):
        doc = '''
        '''
        print(doc)
    elif(func_name == ''):
        doc = '''
        '''
        print(doc)
    elif(func_name == ''):
        doc = '''
        '''
        print(doc)
    elif(func_name == ''):
        doc = '''
        '''
        print(doc)
    elif(func_name == ''):
        doc = '''
        '''
        print(doc)
    elif(func_name == ''):
        doc = '''
        '''
        print(doc)
    elif(func_name == ''):
        doc = '''
        '''
        print(doc)
    elif(func_name == ''):
        doc = '''
        '''
        print(doc)


SEPARATORS = {
    'ckheader':': ',
    'ckstr':'; ',
    'ckpair':'='
}

TYPES = {
    'cktype': "Cookie"
}

#ckheader              cookie-header              "Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax"
#cktype                coookie-type               "Cookie"
#ckstr                 cookie-string              "BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epaxjzubchbotfbwr5te1gwf"
#ckpair                cookie-pair                "TS=0105b666"
#ckname                cookie-name                "TS"
#ckvalue               cookie-value               "0105b666"
#cknv                  cookie-name-and-value      "TS","0105b666"
#ckpt                  cookie-pairTuple           ("TS","0105b666")
#ckpd                  cookie-pairDict            {"TS":"0105b666"}
#ckpl                  cookie-pair-list           ['BIGipServer=rd19', 'TS013d8ed5=0105b6b0', 'TSPD_101=08819c2a', '__RequestVerificationToken=9VdrIliI', 'ASP.NET_SessionId=epaxjzubchbotfbwr5te1gwf']
#ckpdl                 cookie-pair-dictList       [{'BIGipServer': 'rd19'}, {'TS013d8ed5': '0105b6b0'}, {'TSPD_101': '08819c2a'}, {'__RequestVerificationToken': '9VdrIliI'}, {'ASP.NET_SessionId': 'epax'}]
#ckptl                 cookie-pair-tupleList      [('BIGipServer', 'rd19'), ('TS013d8ed5', '0105b6b0'), ('TSPD_101', '08819c2a'), ('__RequestVerificationToken', '9VdrIliI'), ('ASP.NET_SessionId', 'epax')]
#ckdict                cookie-dict  
#ckbody                cookie-body                ckstr | ckpl | ckptl | ckpdl | ckdict
              

#Part.1  cookie-pair
#命名规则priority ckpair > cknv > ckpt > ckpd
#[ckpair2tuple,tuple2ckpair,ckpair2nv,nv2ckpair,ckpair2dict,dict2ckpair,cknv2tuple,tuple2cknv,cknv2dict,dict2cknv,ckpt2dict,dict2ckpt]
# ['ckpair2tuple', 'tuple2ckpair', 'ckpair2nv', 'nv2ckpair', 'ckpair2dict', 'dict2ckpair', 'cknv2tuple', 'tuple2cknv', 'cknv2dict', 'dict2cknv', 'ckpt2dict', 'dict2ckpt']
# [
#     ckpair2tuple,
#     tuple2ckpair,
#     ckpair2nv,
#     nv2ckpair,
#     ckpair2dict,
#     dict2ckpair,
#     cknv2tuple,
#     tuple2cknv,
#     cknv2dict,
#     dict2cknv,
#     ckpt2dict,
#     dict2ckpt
# ]

def ckpair2tuple(ckpair):
    '''
        from kukibanshee.drone import *
        ckpair = "TS=0105b666"
        ckpt = ckpair2tuple(ckpair)
        ckpt
    '''
    ckpt = tuple(ckpair.split(SEPARATORS['ckpair']))
    return(ckpt)

def tuple2ckpair(ckpt):
    '''
        ckpt = ("TS","0105b666")
        ckpair = tuple2ckpair(ckpt)
        ckpair
    '''
    ckname,ckvalue = ckpt
    ckpair = ckname+ SEPARATORS['ckpair'] +ckvalue
    return(ckpair)

def ckpair2nv(ckpair):
    '''
        ckpair = "TS=0105b666"
        ckname,ckvalue = ckpair2nv(ckpair)
        ckname
        ckvalue
    '''
    return(ckpair2tuple(ckpair))

def nv2ckpair(ckname,ckvalue):
    '''
        ckname = "TS"
        ckvalue = "0105b666"
        ckpair = nv2ckpair(ckname,ckvalue)
        ckpair
    '''
    return(tuple2ckpair((ckname,ckvalue)))

def ckpair2dict(ckpair):
    '''
        ckpair = "TS=0105b666"
        ckpd = ckpair2dict(ckpair)
        pobj(ckpd)
    '''
    ckname,ckvalue = ckpair2nv(ckpair)
    return({ckname:ckvalue})

def dict2ckpair(ckpd):
    '''
        ckpd = {"TS": "0105b666"}
        ckpair = dict2ckpair(ckpd)
        ckpair
    '''
    ckname = list(ckpd.keys())[0]
    ckvalue = list(ckpd.values())[0]
    return(nv2ckpair(ckname,ckvalue))

def cknv2tuple(ckname,ckvalue):
    '''
        ckname = "TS"
        ckvalue = "0105b666"
        ckpt = cknv2tuple(ckname,ckvalue)
        ckpt
    '''
    return((ckname,ckvalue))

def tuple2cknv(ckpt):
    '''
        ckpt = ("TS","0105b666")
        ckname,ckvalue = tuple2cknv(ckpt)
        ckname
        ckvalue
    '''
    return(ckpt)

def cknv2dict(ckname,ckvalue):
    '''
        ckname = "TS"
        ckvalue = "0105b666"
        ckpd = cknv2dict(ckname,ckvalue)
        ckpd
    '''
    return({ckname : ckvalue})

def dict2cknv(ckpd):
    '''
        ckpd = {"TS": "0105b666"}
        ckname,ckvalue = dict2cknv(ckpd)
        ckname
        ckvalue
    '''
    ckname = list(ckpd.keys())[0]
    ckvalue = list(ckpd.values())[0]
    return((ckname,ckvalue))

def ckpt2dict(ckpt):
    '''
        ckpt = ("TS","0105b666")
        ckpd = ckpt2dict(ckpt)
        pobj(ckpd)
    '''
    ckname,ckvalue = ckpt
    return({ckname:ckvalue})

def dict2ckpt(ckpd):
    '''
        ckpd = {"TS": "0105b666"}
        ckpt = dict2ckpt(ckpd)
        ckpt 
    '''
    return(dict2cknv(ckpd))

#validate_ckpt
def validate_ckpt(ckpt):
    '''
    '''
    if(type(ckpt) == type(())):
        ckname,ckvalue = tuple2cknv(ckpt)
        cond1 = rfc6265.is_cookie_name(ckname)
        cond2 = rfc6265.is_cookie_value(ckvalue)
        return(cond1 & cond2)        
    else:
        return(False)

#Part.2 cookie-string
#命名规则priority ckstr > ckpl > ckptl > ckpdl > ckdict

#ckstr2pl             ckstr2list
#pl2ckstr             list2ckstr
#ckstr2ptl            ckstr2tupleList
#ptl2ckstr            tupleList2ckstr
#ckstr2pdl            ckstr2dictList
#pdl2ckstr            dictList2ckstr
#ckpl2ptl             ckpl2tupleList
#ptl2ckpl             tupleList2ckpl
#ckpl2pdl             ckpl2dictList
#pdl2ckpl             dictList2ckpl
#ckptl2pdl            ckptl2dictList
#pdl2ckptl            dictList2ckptl

##cookie-dict 不能保持原有次序,并且不允许重复key值,但是使用和阅读方便
#ckstr2dict          
#dict2ckstr       
#ckpl2dict
#dict2ckpl
#ckptl2dict
#dict2ckptl
#ckpdl2dict
#dict2ckpdl



# ABBREV 
#[ckstr2pl,pl2ckstr,ckstr2ptl,ptl2ckstr,ckstr2pdl,pdl2ckstr,ckpl2ptl,ptl2ckpl,ckpl2pdl,pdl2ckpl,ckptl2pdl,pdl2ckptl]
# [
#     ckstr2pl,
#     pl2ckstr,
#     ckstr2ptl,
#     ptl2ckstr,
#     ckstr2pdl,
#     pdl2ckstr,
#     ckpl2ptl,
#     ptl2ckpl,
#     ckpl2pdl,
#     pdl2ckpl,
#     ckptl2pdl,
#     pdl2ckptl
# ]
#[ckstr2list,list2ckstr,ckstr2tupleList,tupleList2ckstr,ckstr2dictList,dictList2ckstr,ckpl2tupleList,tupleList2ckpl,ckpl2dictList,dictList2ckpl,ckptl2dictList,dictList2ckptl]
#[
# ckstr2list,
# list2ckstr,
# ckstr2tupleList,
# tupleList2ckstr,
# ckstr2dictList,
# dictList2ckstr,
# ckpl2tupleList,
# tupleList2ckpl,
# ckpl2dictList,
# dictList2ckpl,
# ckptl2dictList,
# dictList2ckptl
#]

##cookie-dict 不能保持原有次序,并且不允许重复key值,但是使用和阅读方便
#[ckstr2dict,dict2ckstr,ckpl2dict,dict2ckpl,ckptl2dict,dict2ckptl,ckpdl2dict,dict2ckpdl]
# [
    # ckstr2dict,          
    # dict2ckstr,       
    # ckpl2dict,
    # dict2ckpl,
    # ckptl2dict,
    # dict2ckptl,
    # ckpdl2dict,
    # dict2ckpdl,
#]
#['ckstr2pl', 'pl2ckstr', 'ckstr2ptl', 'ptl2ckstr', 'ckstr2pdl', 'pdl2ckstr', 'ckpl2ptl', 'ptl2ckpl', 'ckpl2pdl', 'pdl2ckpl', 'ckptl2pdl', 'pdl2ckptl', 'ckstr2list', 'list2ckstr', 'ckstr2tupleList', 'tupleList2ckstr', 'ckstr2dictList', 'dictList2ckstr', 'ckpl2tupleList', 'tupleList2ckpl', 'ckpl2dictList', 'dictList2ckpl', 'ckptl2dictList', 'dictList2ckptl', 'ckstr2dict', 'dict2ckstr', 'ckpl2dict', 'dict2ckpl', 'ckptl2dict', 'dict2ckptl', 'ckpdl2dict', 'dict2ckpdl']


#转换规则: 所有结构转换为ckptl , 然后再由ckptl 转换为其他格式

def ckstr2pl(ckstr):
    '''
        ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        ckpl = ckstr2ckpl(ckstr)
        pobj(ckpl)
        #ckstr2list = ckstr2pl
    '''
    ckpl = ckstr.split(SEPARATORS['ckstr'])
    return(ckpl)

ckstr2list = ckstr2pl

def pl2ckstr(ckpl):
    '''
        ckpl = ['BIGipServer=rd19', 'TS013d8ed5=0105b6b0', 'TSPD_101=08819c2a', '__RequestVerificationToken=9VdrIliI', 'ASP.NET_SessionId=epax']
        ckstr = pl2ckstr(ckpl)
        ckstr
        #list2ckstr
    '''
    ckstr = elel.join(ckpl,separator = SEPARATORS['ckstr'])
    return(ckstr)

list2ckstr = pl2ckstr

def ckstr2ptl(ckstr):
    '''
        ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        ckptl = ckstr2ptl(ckstr)
        pobj(ckptl)
        #ckstr2tupleList = ckstr2ptl
    '''
    ckpl = ckstr2pl(ckstr)
    ckptl = ckpl2ptl(ckpl)
    return(ckptl)

ckstr2tupleList = ckstr2ptl

def ptl2ckstr(ckptl):
    '''
        ckptl = [('BIGipServer', 'rd19'), ('TS013d8ed5', '0105b6b0'), ('TSPD_101', '08819c2a'), ('__RequestVerificationToken', '9VdrIliI'), ('ASP.NET_SessionId', 'epax')]
        ckstr = ptl2ckstr(ckptl)
        ckstr
        #tupleList2ckstr = ptl2ckstr
    '''
    ckpl = ptl2ckpl(ckptl)
    ckstr = pl2ckstr(ckpl)
    return(ckstr)

tupleList2ckstr = ptl2ckstr

def ckstr2pdl(ckstr):
    '''
        ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        ckpdl = ckstr2pdl(ckstr)
        pobj(ckpdl)
        #ckstr2dictList = ckstr2pdl
    '''
    ckpl = ckstr2pl(ckstr)
    ckpdl = ckpl2pdl(ckpl)
    return(ckpdl)

ckstr2dictList = ckstr2pdl

def pdl2ckstr(ckpdl):
    '''
        ckpdl = [{'BIGipServer': 'rd19'}, {'TS013d8ed5': '0105b6b0'}, {'TSPD_101': '08819c2a'}, {'__RequestVerificationToken': '9VdrIliI'}, {'ASP.NET_SessionId': 'epax'}]
        ckstr = pdl2ckstr(ckpdl)
        ckstr
        #dictList2ckstr = pdl2ckstr
    '''
    ckpl = pdl2ckpl(ckpdl)
    ckstr = pl2ckstr(ckpl)
    return(ckstr)

dictList2ckstr = pdl2ckstr

def ckpl2ptl(ckpl):
    '''
        ckpl = ['BIGipServer=rd19', 'TS013d8ed5=0105b6b0', 'TSPD_101=08819c2a', '__RequestVerificationToken=9VdrIliI', 'ASP.NET_SessionId=epax']
        ckptl = ckpl2ptl(ckpl)
        pobj(ckptl)
        #ckpl2tupleList = ckpl2ptl
    '''
    ckptl = elel.array_map(ckpl,ckpair2tuple)
    return(ckptl)

ckpl2tupleList = ckpl2ptl

def ptl2ckpl(ckptl):
    '''
        ckptl = [('BIGipServer', 'rd19'), ('TS013d8ed5', '0105b6b0'), ('TSPD_101', '08819c2a'), ('__RequestVerificationToken', '9VdrIliI'), ('ASP.NET_SessionId', 'epax')]
        ckpl = ptl2ckpl(ckptl)
        pobj(ckpl)
        #tupleList2ckpl = ptl2ckpl
    '''
    ckpl = elel.array_map(ckptl,tuple2ckpair)
    return(ckpl)

tupleList2ckpl = ptl2ckpl

def ckpl2pdl(ckpl):
    '''
        ckpl = ['BIGipServer=rd19', 'TS013d8ed5=0105b6b0', 'TSPD_101=08819c2a', '__RequestVerificationToken=9VdrIliI', 'ASP.NET_SessionId=epax']
        ckpdl = ckpl2pdl(ckpl)
        pobj(ckpdl)
        #ckpl2dictList = ckpl2pdl
    '''
    ckpdl = elel.array_map(ckpl,ckpair2dict)
    return(ckpdl)

ckpl2dictList = ckpl2pdl

def pdl2ckpl(ckpdl):
    '''
        ckpdl = [{'BIGipServer': 'rd19'}, {'TS013d8ed5': '0105b6b0'}, {'TSPD_101': '08819c2a'}, {'__RequestVerificationToken': '9VdrIliI'}, {'ASP.NET_SessionId': 'epax'}]
        ckpl = pdl2ckpl(ckpdl)
        pobj(ckpl)
        #dictList2ckpl = pdl2ckpl
    '''
    ckpl = elel.array_map(ckpdl,dict2ckpair)
    return(ckpl)

dictList2ckpl = pdl2ckpl

def ckptl2pdl(ckptl):
    '''
        ckptl = [('BIGipServer', 'rd19'), ('TS013d8ed5', '0105b6b0'), ('TSPD_101', '08819c2a'), ('__RequestVerificationToken', '9VdrIliI'), ('ASP.NET_SessionId', 'epax')]
        ckpdl = ckptl2pdl(ckptl)
        pobj(ckpdl)
        #ckptl2dictList = ckptl2pdl
    '''
    ckpdl = elel.array_map(ckptl,ckpt2dict)
    return(ckpdl)

ckptl2dictList = ckptl2pdl

def pdl2ckptl(ckpdl):
    '''
        ckpdl = [{'BIGipServer': 'rd19'}, {'TS013d8ed5': '0105b6b0'}, {'TSPD_101': '08819c2a'}, {'__RequestVerificationToken': '9VdrIliI'}, {'ASP.NET_SessionId': 'epax'}]
        ckptl = pdl2ckptl(ckpdl)
        pobj(ckptl)
        #dictList2ckptl = pdl2ckptl
    '''
    ckptl = elel.array_map(ckpdl,dict2ckpt)
    return(ckptl)

dictList2ckptl = pdl2ckptl

def ckstr2dict(ckstr):
    '''
        ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        ckdict = ckstr2dict(ckstr)
        pobj(ckdict)
    '''
    ckptl = ckstr2ptl(ckstr)
    ckdict = ckptl2dict(ckptl)
    return(ckdict)

def dict2ckstr(ckdict):
    '''
        ckdict = {'__RequestVerificationToken': '9VdrIliI', 'ASP.NET_SessionId': 'epax', 'BIGipServer': 'rd19', 'TS013d8ed5': '0105b6b0', 'TSPD_101': '08819c2a'}
        ckstr = dict2ckstr(ckdict)
        ckstr
    '''
    ckptl = dict2ckptl(ckdict)
    ckstr = ptl2ckstr(ckptl)
    return(ckstr)

def ckpl2dict(ckpl):
    '''
        ckpl = ['BIGipServer=rd19', 'TS013d8ed5=0105b6b0', 'TSPD_101=08819c2a', '__RequestVerificationToken=9VdrIliI', 'ASP.NET_SessionId=epax']
        ckdict = ckpl2dict(ckpl)
        pobj(ckdict)
    '''
    ckptl = ckpl2ptl(ckpl)
    ckdict = ckptl2dict(ckptl)
    return(ckdict)

def dict2ckpl(ckdict):
    '''
        ckdict = {'__RequestVerificationToken': '9VdrIliI', 'ASP.NET_SessionId': 'epax', 'BIGipServer': 'rd19', 'TS013d8ed5': '0105b6b0', 'TSPD_101': '08819c2a'}
        ckpl = dict2ckpl(ckdict)
        pobj(ckpl)
    '''
    ckptl = dict2ckptl(ckdict)
    ckpl = ptl2ckpl(ckptl)
    return(ckpl)

def ckptl2dict(ckptl):
    '''
        ckptl = [('BIGipServer', 'rd19'), ('TS013d8ed5', '0105b6b0'), ('TSPD_101', '08819c2a'), ('__RequestVerificationToken', '9VdrIliI'), ('ASP.NET_SessionId', 'epax')]
        d = ckptl2dict(ckptl)
        pobj(d)
    '''
    return(dict(ckptl))

def dict2ckptl(ckdict):
    '''
        ckdict = {'__RequestVerificationToken': '9VdrIliI', 'ASP.NET_SessionId': 'epax', 'BIGipServer': 'rd19', 'TS013d8ed5': '0105b6b0', 'TSPD_101': '08819c2a'}
        ckptl = dict2ckptl(ckdict)
        pobj(ckptl)
    '''
    return(list(ckdict.items()))

def ckpdl2dict(ckpdl):
    '''
        ckpdl = [{'BIGipServer': 'rd19'}, {'TS013d8ed5': '0105b6b0'}, {'TSPD_101': '08819c2a'}, {'__RequestVerificationToken': '9VdrIliI'}, {'ASP.NET_SessionId': 'epax'}]
        ckdict = ckpdl2dict(ckpdl)
        pobj(ckdict)
    '''
    ckptl = pdl2ckptl(ckpdl)
    return(ckptl2dict(ckptl))
    
def dict2ckpdl(ckdict):
    '''
        ckdict = {'__RequestVerificationToken': '9VdrIliI', 'ASP.NET_SessionId': 'epax', 'BIGipServer': 'rd19', 'TS013d8ed5': '0105b6b0', 'TSPD_101': '08819c2a'}
        ckpdl = dict2ckpdl(ckdict)
        pobj(ckpdl)
    '''
    ckptl = dict2ckptl(ckdict)
    ckpdl = ckptl2pdl(ckptl)
    return(ckpdl)

######wait to implement
# [validate_ckstr,validate_ckpl,validate_ckptl,validate_ckpdl,validate_ckdict,detect_ckbody,validate_ckbody]
# ['validate_ckstr', 'validate_ckpl', 'validate_ckptl', 'validate_ckpdl', 'validate_ckdict', 'detect_ckbody', 'validate_ckbody']

def validate_ckstr(ckstr):
    '''
    '''
    ckptl = ckstr2ptl(ckstr)
    return(validate_ckptl(ckptl))

def validate_ckpl(ckpl):
    '''
    '''
    ckptl = ckpl2ptl(ckpl)
    return(validate_ckptl(ckptl))

def validate_ckptl(ckptl):
    '''
    '''
    rslt = elel.every(ckptl,validate_ckpt)
    print(rslt)
    return(rslt[0])

def validate_ckpdl(ckpdl):
    '''
    '''
    ckptl = pdl2ckptl(ckpdl)
    return(validate_ckptl(ckptl))

def validate_ckdict(ckdict):
    '''
    '''
    ckptl = dict2ckptl(ckdict)
    return(validate_ckptl(ckptl))

def detect_ckbody(ckbody):
    '''
        ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        ckpl = ['BIGipServer=rd19', 'TS013d8ed5=0105b6b0', 'TSPD_101=08819c2a', '__RequestVerificationToken=9VdrIliI', 'ASP.NET_SessionId=epax']
        ckptl = [('BIGipServer', 'rd19'), ('TS013d8ed5', '0105b6b0'), ('TSPD_101', '08819c2a'), ('__RequestVerificationToken', '9VdrIliI'), ('ASP.NET_SessionId', 'epax')]
        ckpdl = [{'BIGipServer': 'rd19'}, {'TS013d8ed5': '0105b6b0'}, {'TSPD_101': '08819c2a'}, {'__RequestVerificationToken': '9VdrIliI'}, {'ASP.NET_SessionId': 'epax'}]
        ckdict = {'__RequestVerificationToken': '9VdrIliI', 'ASP.NET_SessionId': 'epax', 'BIGipServer': 'rd19', 'TS013d8ed5': '0105b6b0', 'TSPD_101': '08819c2a'}
        detect_ckbody(ckstr)
        detect_ckbody(ckpl)
        detect_ckbody(ckptl)
        detect_ckbody(ckpdl)
        detect_ckbody(ckdict)
    '''
    if(type(ckbody) == type('')):
        return('ckstr')
    elif(type(ckbody) == type([])):
        if(type(ckbody[0]) == type('')):
            return('ckpl')
        elif(type(ckbody[0]) == type(())):
            return('ckptl')
        elif(type(ckbody[0]) == type(dict({}))):
            return('ckpdl')
        else:
            return('unknown')
    elif(type(ckbody) == type(dict())):
        return('ckdict')
    else:
        return('unknown')

def validate_ckbody(ckbody):
    '''
    '''
    mode = detect_ckbody(ckbody)
    if(mode == 'ckstr'):
        return(validate_ckstr(ckbody))
    elif(mode == 'ckpl'):
        return(validate_ckpl(ckbody))
    elif(mode == 'ckptl'):
        return(validate_ckptl(ckbody))
    elif(mode == 'ckpdl'):
        return(validate_ckpdl(ckbody))
    elif(mode == 'ckdict'):
        return(validate_ckdict(ckbody))
    else:
        print("unknow mode")
        return(False)


#[ckbody2ptl,select_ckbody,convert_ckbody,prepend_ckbody,append_ckbody,insert_ckbody]

def ckbody2ptl(ckbody,**kwargs):
    '''
        ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        ckpl = ['BIGipServer=rd19', 'TS013d8ed5=0105b6b0', 'TSPD_101=08819c2a', '__RequestVerificationToken=9VdrIliI', 'SP.NET_SessionId=epax']
        ckptl = [('BIGipServer', 'rd19'), ('TS013d8ed5', '0105b6b0'), ('TSPD_101', '08819c2a'), ('__RequestVerificationToken', '9VdrIliI'), ('ASP.NET_SessionId', 'epax')]
        ckpdl = [{'BIGipServer': 'rd19'}, {'TS013d8ed5': '0105b6b0'}, {'TSPD_101': '08819c2a'}, {'__RequestVerificationToken': '9VdrIliI'}, {'ASP.NET_SessionId': 'epax'}]
        ckdict = {'__RequestVerificationToken': '9VdrIliI', 'ASP.NET_SessionId': 'epax', 'BIGipServer': 'rd19', 'TS013d8ed5': '0105b6b0', 'TSPD_101': '08819c2a'}
        ckbody2ptl(ckstr)
        ckbody2ptl(ckpl)
        ckbody2ptl(ckptl)
        ckbody2ptl(ckpdl)
        ckbody2ptl(ckdict)
    '''
    if('validate' in kwargs):
        valid = validate_ckbody(ckbody)
    else:
        valid = True
    if(valid):
        pass
    else:
        print('invalid ckbody')
        return(None)
    mode = detect_ckbody(ckbody)
    if(mode == 'ckstr'):
        ckptl = ckstr2ptl(ckbody)
    elif(mode == 'ckpl'):
        ckptl = ckpl2ptl(ckbody)
    elif(mode == 'ckptl'):
        ckptl = ckbody
    elif(mode == 'ckpdl'):
        ckptl = pdl2ckptl(ckbody)
    elif(mode == 'ckdict'):
        ckptl = dict2ckptl(ckbody)
    else:
        print("unknow mode")
        return(None)
    return(ckptl)

def convert_ckbody(ckbody,**kwargs):
    '''
        ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        ckpl = ['BIGipServer=rd19', 'TS013d8ed5=0105b6b0', 'TSPD_101=08819c2a', '__RequestVerificationToken=9VdrIliI', 'SP.NET_SessionId=epax']
        ckptl = [('BIGipServer', 'rd19'), ('TS013d8ed5', '0105b6b0'), ('TSPD_101', '08819c2a'), ('__RequestVerificationToken', '9VdrIliI'), ('ASP.NET_SessionId', 'epax')]
        ckpdl = [{'BIGipServer': 'rd19'}, {'TS013d8ed5': '0105b6b0'}, {'TSPD_101': '08819c2a'}, {'__RequestVerificationToken': '9VdrIliI'}, {'ASP.NET_SessionId': 'epax'}]
        ckdict = {'__RequestVerificationToken': '9VdrIliI', 'ASP.NET_SessionId': 'epax', 'BIGipServer': 'rd19', 'TS013d8ed5': '0105b6b0', 'TSPD_101': '08819c2a'}
        convert_ckbody(ckstr)
        ckbody = convert_ckbody(ckpl,mode='ckdict')
        pobj(ckbody)
        convert_ckbody(ckptl,mode='ckpdl')
        convert_ckbody(ckpdl,mode='ckstr')
        ckbody = convert_ckbody(ckdict,mode='ckpl')
        elel.forEach(ckbody,print)
    '''
    if('validate' in kwargs):
        valid = validate_ckbody(ckbody)
    else:
        valid = True
    if(valid):
        pass
    else:
        print('invalid ckbody')
        return(None)
    mode = detect_ckbody(ckbody)
    if(mode == 'ckstr'):
        ckptl = ckstr2ptl(ckbody)
    elif(mode == 'ckpl'):
        ckptl = ckpl2ptl(ckbody)
    elif(mode == 'ckptl'):
        ckptl = ckbody
    elif(mode == 'ckpdl'):
        ckptl = pdl2ckptl(ckbody)
    elif(mode == 'ckdict'):
        ckptl = dict2ckptl(ckbody)
    else:
        print("unknow mode")
        return(None)
    if('mode' in kwargs):
        to_mode = kwargs['mode']
    else:
        to_mode = 'ckptl'
    if(to_mode == 'ckstr'):
        ckbody = ptl2ckstr(ckptl)
    elif(to_mode == 'ckpl'):
        ckbody = ptl2ckpl(ckptl)
    elif(to_mode == 'ckptl'):
        ckbody = ckptl
    elif(to_mode == 'ckpdl'):
        ckbody = ckptl2pdl(ckptl)
    elif(to_mode == 'ckdict'):
        ckbody = ckptl2dict(ckptl)
    else:
        print("unknow mode")
        return(None)
    return(ckbody)

# 返回ckstr
def select_ckbody(ckbody,*cknames,**kwargs):
    '''
        ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        selected = select_ckbody(ckstr,'BIGipServer','TSPD_101')
        selected 
        selected = select_ckbody(ckstr,'TSPD_101','BIGipServer')
        ckdict = ckstr2dict(selected)
        pobj(ckdict)
        #select_ckbody,via ckname, allow duplecate, return ckstr
    '''
    def via_ckname(ele,cknames):
        ckname = ele[0]
        cond = (ckname in cknames)
        return(cond)
    if('validate' in kwargs):
        valid = validate_ckbody(ckbody)
    else:
        valid = True
    if(valid):
        pass
    else:
        print('invalid ckbody')
        return(None)
    cknames = list(cknames)
    ckptl = ckbody2ptl(ckbody)
    selected = elel.find_all(ckptl,via_ckname,cknames)
    selected = elel.array_map(selected,lambda ele:ele['value'])
    ckstr = ptl2ckstr(selected)
    return(ckstr)

# 单独的ckpair 可以看作ckstr
# 单独的ckpd   可以看作ckdict
# 所以只需要判断下 单独ckpt 即可
def prepend_ckbody(dst_ckbody,src_ckbody,**kwargs):
    '''
        dst_ckbody = {'__RequestVerificationToken':'9VdrIliI','ASP.NET_SessionId':'epax'}
        src_ckbody = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a'
        ckstr = prepend_ckbody(dst_ckbody,src_ckbody)
        ckstr
        #return ckstr, params could be ckdict/ckpl/ckpdl/ckptl/ckstr
        #attention ckdict cant keep the order!
        #ckstr include ckpair
        #ckdict include ckpd
    '''
    if(type(src_ckbody) == type(())):
        src_ckbody = [src_ckbody]
    else:
        pass
    src_ckptl = convert_ckbody(src_ckbody)
    dst_ckptl = convert_ckbody(dst_ckbody)
    ckptl = elel.prextend(dst_ckptl,src_ckptl)
    ckstr = ptl2ckstr(ckptl)
    return(ckstr)

def append_ckbody(dst_ckbody,src_ckbody,**kwargs):
    '''
        dst_ckbody = {'__RequestVerificationToken':'9VdrIliI','ASP.NET_SessionId':'epax'}
        src_ckbody = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a'
        ckstr = append_ckbody(dst_ckbody,src_ckbody)
        ckstr
        #return ckstr, params could be ckdict/ckpl/ckpdl/ckptl/ckstr
        #attention ckdict cant keep the order!
        #ckstr include ckpair
        #ckdict include ckpd
    '''
    if(type(src_ckbody) == type(())):
        src_ckbody = [src_ckbody]
    else:
        pass
    src_ckptl = convert_ckbody(src_ckbody)
    dst_ckptl = convert_ckbody(dst_ckbody)
    ckptl = elel.extend(dst_ckptl,src_ckptl)
    ckstr = ptl2ckstr(ckptl)
    return(ckstr)

def insert_ckbody(dst_ckbody,src_ckbody,location,**kwargs):
    '''
        dst_ckbody = '__RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        src_ckbody = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a'
        ckstr = insert_ckbody(dst_ckbody,src_ckbody,1)
        ckstr
        # return ckstr, params could be ckdict/ckpl/ckpdl/ckptl/ckstr
    '''
    if(type(src_ckbody) == type(())):
        src_ckbody = [src_ckbody]
    else:
        pass
    src_ckptl = convert_ckbody(src_ckbody)
    dst_ckptl = convert_ckbody(dst_ckbody)
    ckptl = elel.insert_section(dst_ckptl,src_ckptl,location)
    ckstr = ptl2ckstr(ckptl)
    return(ckstr)


# def remove_ckbody(ckbody,**kwargs)
# def pop_ckbody(ckbody,**kwargs)
# def replace_ckbody(ckbody,**kwargs)
# def uniqulize_ckbody(ckbody,**kwargs)



#Part.3
#命名规则 priority ckheader > ckbody >ckstr > ckpl > ckptl > ckpdl >ckdict
# 
####

def split_ckheader(ckheader,**kwargs):
    '''
        ckheader = "Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax"
        pobj(split_ckheader(ckheader))
        pobj(split_ckheader(ckheader,mode='ckstr'))
        pobj(split_ckheader(ckheader,mode='ckpl'))
        pobj(split_ckheader(ckheader,mode='ckptl'))
        pobj(split_ckheader(ckheader,mode='ckpdl'))
        pobj(split_ckheader(ckheader,mode='ckdict'))
    '''
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 'ckptl'
    cktype,ckstr = tuple(ckheader.split(SEPARATORS['ckheader']))
    if(mode == 'ckstr'):
        return({'cktype':cktype,'ckstr':ckstr})
    elif(mode == 'ckpl'):
        ckpl = ckstr2pl(ckstr)
        return({'cktype':cktype,'ckpl':ckpl})
    elif(mode == 'ckptl'):
        ckptl = ckstr2ptl(ckstr)
        return({'cktype':cktype,'ckptl':ckptl})
    elif(mode == 'ckpdl'):
        ckpdl = ckstr2pdl(ckstr)
        return({'cktype':cktype,'ckpdl':ckpdl})
    elif(mode == 'ckdict'):
        ckdict = ckstr2dict(ckbody)
        return({'cktype':cktype,'ckdict':ckdict})
    else:
        print("unknow mode")
        return(None)

def validate_ckheader(ckheader):
    '''
    '''
    cktype,ckstr = tuple(ckheader.split(SEPARATORS['ckheader']))
    cond1 = (cktype == TYPES['cktype'])
    if(cond1):
        cond2 = validate_ckstr(ckstr)
        if(cond2):
            return(True)
        else:
            return(False)
    else:
        print("cktype wrong!")
        return(False)

def cons_ckheader(ckbody,**kwargs):
    '''
        ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        ckpl = ['BIGipServer=rd19', 'TS013d8ed5=0105b6b0', 'TSPD_101=08819c2a', '__RequestVerificationToken=9VdrIliI', 'SP.NET_SessionId=epax']
        ckptl = [('BIGipServer', 'rd19'), ('TS013d8ed5', '0105b6b0'), ('TSPD_101', '08819c2a'), ('__RequestVerificationToken', '9VdrIliI'), ('ASP.NET_SessionId', 'epax')]
        ckpdl = [{'BIGipServer': 'rd19'}, {'TS013d8ed5': '0105b6b0'}, {'TSPD_101': '08819c2a'}, {'__RequestVerificationToken': '9VdrIliI'}, {'ASP.NET_SessionId': 'epax'}]
        ckdict = {'__RequestVerificationToken': '9VdrIliI', 'ASP.NET_SessionId': 'epax', 'BIGipServer': 'rd19', 'TS013d8ed5': '0105b6b0', 'TSPD_101': '08819c2a'}
        cons_ckheader(ckstr)
        cons_ckheader(ckpl)
        cons_ckheader(ckptl)
        cons_ckheader(ckpdl)
        cons_ckheader(ckdict)
    '''
    if('validate' in kwargs):
        valid = validate_ckbody(ckbody)
    else:
        valid = True
    if(valid):
        pass
    else:
        print('invalid ckbody')
        return(None)
    mode = detect_ckbody(ckbody)
    if(mode == 'ckstr'):
        ckstr = ckbody
    elif(mode == 'ckpl'):
        ckstr = pl2ckstr(ckbody)
    elif(mode == 'ckptl'):
        ckstr = ptl2ckstr(ckbody)
    elif(mode == 'ckpdl'):
        ckstr = pdl2ckstr(ckbody)
    elif(mode == 'ckdict'):
        ckstr = dict2ckstr(ckbody)
    else:
        print("unknow mode")
        return(None)
    ckheader = TYPES['cktype']+SEPARATORS['ckheader']+ckstr
    return(ckheader)







