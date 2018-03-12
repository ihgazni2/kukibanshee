from xdict.jprint import pobj
from xdict.jprint import pdir



from kukibanshee.drone import *

# from xdict.utils import creat_markdown_tree_links as markdown
# arr = ['ckpair2tuple', 'tuple2ckpair', 'ckpair2nv', 'nv2ckpair', 'ckpair2dict', 'dict2ckpair', 'cknv2tuple', 'tuple2cknv', 'cknv2dict', 'dict2cknv', 'ckpt2dict', 'dict2ckpt']
# print(markdown(arr,0,path='kukibanshee/Images/'))




ckpair = "TS=0105b666"
ckpt = ckpair2tuple(ckpair)
ckpt

# >>> from kukibanshee.drone import *
# >>> ckpair = "TS=0105b666"
# >>> ckpt = ckpair2tuple(ckpair)
# >>> ckpt
# ('TS', '0105b666')
# >>>



ckpt = ("TS","0105b666")
ckpair = tuple2ckpair(ckpt)
ckpair

# >>>
# >>> ckpt = ("TS","0105b666")
# >>> ckpair = tuple2ckpair(ckpt)
# >>> ckpair
# 'TS=0105b666'
# >>>

ckpair = "TS=0105b666"
ckname,ckvalue = ckpair2nv(ckpair)
ckname
ckvalue

# >>> ckpair = "TS=0105b666"
# >>> ckname,ckvalue = ckpair2nv(ckpair)
# >>> ckname
# 'TS'
# >>> ckvalue
# '0105b666'
# >>>


ckname = "TS"
ckvalue = "0105b666"
ckpair = nv2ckpair(ckname,ckvalue)
ckpair

# >>>
# >>> ckname = "TS"
# >>> ckvalue = "0105b666"
# >>> ckpair = nv2ckpair(ckname,ckvalue)
# >>> ckpair
# 'TS=0105b666'
# >>>

ckpair = "TS=0105b666"
ckpd = ckpair2dict(ckpair)
pobj(ckpd)

# >>>
# >>> ckpair = "TS=0105b666"
# >>> ckpd = ckpair2dict(ckpair)
# >>> pobj(ckpd)
# {
 # 'TS': '0105b666'
# }
# >>>
# >>>

ckpd = {"TS": "0105b666"}
ckpair = dict2ckpair(ckpd)
ckpair

# >>>
# >>> ckpd = {"TS": "0105b666"}
# >>> ckpair = dict2ckpair(ckpd)
# >>> ckpair
# 'TS=0105b666'
# >>>


ckname = "TS"
ckvalue = "0105b666"
ckpt = cknv2tuple(ckname,ckvalue)
ckpt

# >>> ckname = "TS"
# >>> ckvalue = "0105b666"
# >>> ckpt = cknv2tuple(ckname,ckvalue)
# >>> ckpt
# ('TS', '0105b666')
# >>>



ckpt = ("TS","0105b666")
ckname,ckvalue = tuple2cknv(ckpt)
ckname
ckvalue

# >>> ckpt = ("TS","0105b666")
# >>> ckname,ckvalue = tuple2cknv(ckpt)
# >>> ckname
# 'TS'
# >>> ckvalue
# '0105b666'


ckname = "TS"
ckvalue = "0105b666"
ckpd = cknv2dict(ckname,ckvalue)
ckpd

# >>>
# >>> ckname = "TS"
# >>> ckvalue = "0105b666"
# >>> ckpd = cknv2dict(ckname,ckvalue)
# >>> ckpd
# {'TS': '0105b666'}
# >>>


ckpd = {"TS": "0105b666"}
ckname,ckvalue = dict2cknv(ckpd)
ckname
ckvalue

# >>>
# >>> ckpd = {"TS": "0105b666"}
# >>> ckname,ckvalue = dict2cknv(ckpd)
# >>> ckname
# 'TS'
# >>> ckvalue
# '0105b666'
# >>>


ckpt = ("TS","0105b666")
ckpd = ckpt2dict(ckpt)
pobj(ckpd)

# >>>
# >>> ckpt = ("TS","0105b666")
# >>> ckpd = ckpt2dict(ckpt)
# >>> pobj(ckpd)
# {
 # 'TS': '0105b666'
# }
# >>>


ckpd = {"TS": "0105b666"}
ckpt = dict2ckpt(ckpd)
ckpt 

# >>> ckpd = {"TS": "0105b666"}
# >>> ckpt = dict2ckpt(ckpd)
# >>> ckpt
# ('TS', '0105b666')
# >>>


###################################################


from xdict.jprint import pobj
from xdict.jprint import pdir



from kukibanshee.drone import *

from xdict.utils import creat_markdown_tree_links as markdown
arr = ['ckstr2pl', 'pl2ckstr', 'ckstr2ptl', 'ptl2ckstr', 'ckstr2pdl', 'pdl2ckstr', 'ckpl2ptl', 'ptl2ckpl', 'ckpl2pdl', 'pdl2ckpl', 'ckptl2pdl', 'pdl2ckptl', 'ckstr2list', 'list2ckstr', 'ckstr2tupleList', 'tupleList2ckstr', 'ckstr2dictList', 'dictList2ckstr', 'ckpl2tupleList', 'tupleList2ckpl', 'ckpl2dictList', 'dictList2ckpl', 'ckptl2dictList', 'dictList2ckptl', 'ckstr2dict', 'dict2ckstr', 'ckpl2dict', 'dict2ckpl', 'ckptl2dict', 'dict2ckptl', 'ckpdl2dict', 'dict2ckpdl']
print(markdown(arr,12,path='kukibanshee/Images/'))










#detect_ckele
ckele = "TS=0105b666"
detect_ckele(ckele)
ckele = ("TS","0105b666")
detect_ckele(ckele)
ckele = {"TS": "0105b666"}
detect_ckele(ckele)
ckname = "TS"
ckvalue = "0105b666"
detect_ckele(ckname,ckvalue)

# >>>
# >>> ckele = "TS=0105b666"
# >>> detect_ckele(ckele)
# 'ckpair'
# >>> ckele = ("TS","0105b666")
# >>> detect_ckele(ckele)
# 'ckpt'
# >>> ckele = {"TS": "0105b666"}
# >>> detect_ckele(ckele)
# 'ckpd'
# >>> ckname = "TS"
# >>> ckvalue = "0105b666"
# >>> detect_ckele(ckname,ckvalue)
# 'cknv'
# >>>


#ckele2pt

ckele = "TS=0105b666"
ckpt = ckele2pt(ckele)
pobj(ckpt)
ckele = ("TS","0105b666")
ckpt = ckele2pt(ckele)
pobj(ckpt)
ckele = {"TS": "0105b666"}
ckpt = ckele2pt(ckele)
pobj(ckpt)
ckname = "TS"from xdict.jprint import pobj
ckvalue = "0105b666"from xdict.jprint import pdir
ckpt = ckele2pt(ckname,ckvalue)
pobj(ckpt)from kukibanshee.drone import *


#convert_ckele

ckele = "TS=0105b666"
ckpt = convert_ckele(ckele,mode='ckpt')
pobj(ckpt)
ckele = ("TS","0105b666")
ckpair = convert_ckele(ckele,mode='ckpair')
pobj(ckpair)
ckele = {"TS": "0105b666"}
ckname,ckvalue = convert_ckele(ckele,mode='cknv')
ckname
ckvalue
ckname = "TS"
ckvalue = "0105b666"
ckpd = convert_ckele(ckname,ckvalue,mode='ckpd')
pobj(ckpd)


# >>>
# >>>
# >>> ckele = "TS=0105b666"
# >>> ckpt = convert_ckele(ckele,mode='ckpt')
# >>> pobj(ckpt)
# ckele = {"TS": "0105b666"}
# (
 # 'TS',
 # '0105b666'
# )
# >>> ckele = ("TS","0105b666")
# >>> ckpair = convert_ckele(ckele,mode='ckpair')
# >>> pobj(ckpair)
# ckname,ckvalue = convert_ckele(ckele,mode='cknv')
# TS=0105b666
# >>> ckele = {"TS": "0105b666"}
# >>> ckname,ckvalue = convert_ckele(ckele,mode='cknv')
# >>> ckname
# 'TS'
# >>> ckvalue
# '0105b666'
# >>> ckname = "TS"
# >>> ckvalue = "0105b666"
# >>> ckpd = convert_ckele(ckname,ckvalue,mode='ckpd')
# >>> pobj(ckpd)
# {
 # 'TS': '0105b666'
# }
# >>>
# >>>










#ckbody2ptl

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


# >>> ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>> ckpl = ['BIGipServer=rd19', 'TS013d8ed5=0105b6b0', 'TSPD_101=08819c2a', '__RequestVerificationToken=9VdrIliI', 'SP.NET_SessionId=epax']
# >>> ckptl = [('BIGipServer', 'rd19'), ('TS013d8ed5', '0105b6b0'), ('TSPD_101', '08819c2a'), ('__RequestVerificationToken', '9VdrIliI'), ('ASP.NET_SessionId', 'epax')]
# >>> ckpdl = [{'BIGipServer': 'rd19'}, {'TS013d8ed5': '0105b6b0'}, {'TSPD_101': '08819c2a'}, {'__RequestVerificationToken': '9VdrIliI'}, {'ASP.NET_SessionId': 'epax'}]
# >>> ckdict = {'__RequestVerificationToken': '9VdrIliI', 'ASP.NET_SessionId': 'epax', 'BIGipServer': 'rd19', 'TS013d8ed5': '0105b6b0', 'TSPD_101': '08819c2a'}
# >>> ckbody2ptl(ckstr)
# [('BIGipServer', 'rd19'), ('TS013d8ed5', '0105b6b0'), ('TSPD_101', '08819c2a'), ('__RequestVerificationToken', '9VdrIliI'), ('ASP.NET_SessionId', 'epax')]
# >>> ckbody2ptl(ckpl)
# [('BIGipServer', 'rd19'), ('TS013d8ed5', '0105b6b0'), ('TSPD_101', '08819c2a'), ('__RequestVerificationToken', '9VdrIliI'), ('SP.NET_SessionId', 'epax')]
# >>> ckbody2ptl(ckptl)
# [('BIGipServer', 'rd19'), ('TS013d8ed5', '0105b6b0'), ('TSPD_101', '08819c2a'), ('__RequestVerificationToken', '9VdrIliI'), ('ASP.NET_SessionId', 'epax')]
# >>> ckbody2ptl(ckpdl)
# [('BIGipServer', 'rd19'), ('TS013d8ed5', '0105b6b0'), ('TSPD_101', '08819c2a'), ('__RequestVerificationToken', '9VdrIliI'), ('ASP.NET_SessionId', 'epax')]
# >>> ckbody2ptl(ckdict)
# [('__RequestVerificationToken', '9VdrIliI'), ('ASP.NET_SessionId', 'epax'), ('BIGipServer', 'rd19'), ('TS013d8ed5', '0105b6b0'), ('TSPD_101', '08819c2a')]
# >>>
# >>>


#convert_ckbody

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


















#select_ckbody

ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
selected = select_ckbody(ckstr,'BIGipServer','TSPD_101')
selected 
selected = select_ckbody(ckstr,'TSPD_101','BIGipServer')
ckdict = ckstr2dict(selected)
pobj(ckdict)

# >>>
# >>> ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>> selected = select_ckbody(ckstr,'BIGipServer','TSPD_101')
# >>> selected
# 'BIGipServer=rd19; TSPD_101=08819c2a'
# >>> selected = select_ckbody(ckstr,'TSPD_101','BIGipServer')
# >>> ckdict = ckstr2dict(selected)
# >>> pobj(ckdict)
# {
 # 'BIGipServer': 'rd19',
 # 'TSPD_101': '08819c2a'
# }
# >>>
# >>>


#prepend_ckbody
dst_ckbody = {'__RequestVerificationToken':'9VdrIliI','ASP.NET_SessionId':'epax'}
src_ckbody = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a'
ckstr = prepend_ckbody(dst_ckbody,src_ckbody)
ckstr


# >>>
# >>>
# >>> dst_ckbody = {'__RequestVerificationToken':'9VdrIliI','ASP.NET_SessionId':'epax'}
# >>> src_ckbody = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a'
# >>> ckstr = prepend_ckbody(dst_ckbody,src_ckbody)
# >>> ckstr
# 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>> #return ckstr, params could be ckdict/ckpl/ckpdl/ckptl/ckstr
# ... #attention ckdict cant keep the order!
# ... #ckstr include ckpair
# ... #ckdict include ckpd
# ...






#append_ckbody

dst_ckbody = {'__RequestVerificationToken':'9VdrIliI','ASP.NET_SessionId':'epax'}
src_ckbody = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a'
ckstr = append_ckbody(dst_ckbody,src_ckbody)
ckstr



# >>> dst_ckbody = {'__RequestVerificationToken':'9VdrIliI','ASP.NET_SessionId':'epax'}
# >>> src_ckbody = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a'
# >>> ckstr = append_ckbody(dst_ckbody,src_ckbody)
# >>> ckstr
# '__RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax; BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD                                            _101=08819c2a'
# >>> #return ckstr, params could be ckdict/ckpl/ckpdl/ckptl/ckstr
# ... #attention ckdict cant keep the order!
# ... #ckstr include ckpair
# ... #ckdict include ckpd
# ...
# >>>



#insert_ckbody

dst_ckbody = '__RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
src_ckbody = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a'
ckstr = insert_ckbody(dst_ckbody,src_ckbody,1)
ckstr
# return ckstr, params could be ckdict/ckpl/ckpdl/ckptl/ckstr

# >>>
# >>>
# >>> dst_ckbody = '__RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>> src_ckbody = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a'
# >>> ckstr = insert_ckbody(dst_ckbody,src_ckbody,1)
# >>> ckstr
# '__RequestVerificationToken=9VdrIliI; BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; ASP.NET_SessionId=epax'
# >>> # return ckstr, params could be ckdict/ckpl/ckpdl/ckptl/ckstr
# ...
# >>>
# >>>


#remove_ckbody

ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
lefted = remove_ckbody(ckstr,'TS013d8ed5')
lefted 
ckdict = ckstr2dict(lefted)
pobj(ckdict)
ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
lefted = remove_ckbody(ckstr,'TS013d8ed5',which=1)
lefted 
ckdict = ckstr2dict(lefted)
pobj(ckdict)
#remove_ckbody,via ckname, allow duplecate, return ckstr,by default remove_all

# >>>
# >>> ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>> lefted = remove_ckbody(ckstr,'TS013d8ed5')
# >>> lefted
# 'BIGipServer=rd19; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>> ckdict = ckstr2dict(lefted)
# >>> pobj(ckdict)
# ckdict = ckstr2dict(lefted)
# pobj(ckdict)
# remove_ckbody,via ckname, allow duplecate, return ckstr,by default remove_all
# {
 # 'BIGipServer': 'rd19',
 # 'ASP.NET_SessionId': 'epax',
 # '__RequestVerificationToken': '9VdrIliI',
 # 'TSPD_101': '08819c2a'
# }
# >>> ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>> lefted = remove_ckbody(ckstr,'TS013d8ed5',which=1)
# >>> lefted
# 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>> ckdict = ckstr2dict(lefted)
# >>> pobj(ckdict)
# {
 # 'BIGipServer': 'rd19',
 # 'ASP.NET_SessionId': 'epax',
 # '__RequestVerificationToken': '9VdrIliI',
 # 'TSPD_101': '08819c2a',
 # 'TS013d8ed5': '0105b6b0'
# }
# >>> #remove_ckbody,via ckname, allow duplecate, return ckstr,by default remove_all
# ...
# >>>


#replace_ckbody


ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
replaced = replace_ckbody(ckstr,'TS013d8ed5','TSreplace=replace')
replaced 
replaced = replace_ckbody(ckstr,'TS013d8ed5',('TSreplace','replace'))
replaced 
replaced = replace_ckbody(ckstr,'TS013d8ed5',{'TSreplace':'replace'})
replaced 
replaced = replace_ckbody(ckstr,'TS013d8ed5','TSreplace','replace')
replaced 
####
ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
replaced = replace_ckbody(ckstr,'TS013d8ed5','TSreplace=replace',which=0)
replaced 
replaced = replace_ckbody(ckstr,'TS013d8ed5',('TSreplace','replace'),which=1)
replaced 

# >>>
# >>> ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>> replaced = replace_ckbody(ckstr,'TS013d8ed5','TSreplace=replace')
# >>> replaced
# 'BIGipServer=rd19; TSreplace=replace; TSPD_101=08819c2a; TSreplace=replace; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>> replaced = replace_ckbody(ckstr,'TS013d8ed5',('TSreplace','replace'))
# >>> replaced
# 'BIGipServer=rd19; TSreplace=replace; TSPD_101=08819c2a; TSreplace=replace; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>> replaced = replace_ckbody(ckstr,'TS013d8ed5',{'TSreplace':'replace'})
# >>> replaced
# 'BIGipServer=rd19; TSreplace=replace; TSPD_101=08819c2a; TSreplace=replace; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>> replaced = replace_ckbody(ckstr,'TS013d8ed5','TSreplace','replace')
# >>> replaced
# 'BIGipServer=rd19; TSreplace=replace; TSPD_101=08819c2a; TSreplace=replace; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>> ####
# ... ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>> replaced = replace_ckbody(ckstr,'TS013d8ed5','TSreplace=replace',which=0)
# >>> replaced
# 'BIGipServer=rd19; TSreplace=replace; TSPD_101=08819c2a; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>> replaced = replace_ckbody(ckstr,'TS013d8ed5',('TSreplace','replace'),which=1)
# >>> replaced
# 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; TSreplace=replace; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>>
# >>>


#uniqulize_ckbody

ckstr = 'BIGipServer=rd0; TS013d8ed5=T0; BIGipServer=rd1; TS013d8ed5=T1; SID=0; SID=1'
uniqulized = uniqulize_ckbody(ckstr)
uniqulized

ckstr = 'BIGipServer=rd0; TS013d8ed5=T0; BIGipServer=rd1; TS013d8ed5=T1; SID=0; SID=1'
reserved = {'BIGipServer':1,'TS013d8ed5':0,'SID':1}
uniqulized = uniqulize_ckbody(ckstr,reserved = reserved)
uniqulized 

# >>>
# >>>
# >>> ckstr = 'BIGipServer=rd0; TS013d8ed5=T0; BIGipServer=rd1; TS013d8ed5=T1; SID=0; SID=1'
# >>> uniqulized = uniqulize_ckbody(ckstr)
# >>> uniqulized
# 'BIGipServer=rd0; TS013d8ed5=T0; SID=0'
# >>>
# >>> ckstr = 'BIGipServer=rd0; TS013d8ed5=T0; BIGipServer=rd1; TS013d8ed5=T1; SID=0; SID=1'
# >>> reserved = {'BIGipServer':1,'TS013d8ed5':0,'SID':1}
# >>> uniqulized = uniqulize_ckbody(ckstr,reserved = reserved)
# >>> uniqulized
# 'TS013d8ed5=T0; BIGipServer=rd1; SID=1'
# >>>
# >>>


ckstr = 'BIGipServer=rd0; TS013d8ed5=T0; BIGipServer=rd1; TS013d8ed5=T1; SID=0; SID=1'
uniqulized = uniqulize_ckbody(ckstr,'BIGipServer','TS013d8ed5')
uniqulized 

ckstr = 'BIGipServer=rd0; TS013d8ed5=T0; BIGipServer=rd1; TS013d8ed5=T1; SID=0; SID=1'
reserved = {'BIGipServer':1,'TS013d8ed5':0}
uniqulized = uniqulize_ckbody(ckstr,'BIGipServer','TS013d8ed5',reserved=reserved)
uniqulized 

####
#uniqulize_ckbody,via ckname, allow duplecate, return ckstr,by default uniqulize_all
#
# >>>
# >>>
# >>> ckstr = 'BIGipServer=rd0; TS013d8ed5=T0; BIGipServer=rd1; TS013d8ed5=T1; SID=0; SID
# >>> uniqulized = uniqulize_ckbody(ckstr,'BIGipServer','TS013d8ed5')
# >>> uniqulized
# 'BIGipServer=rd0; TS013d8ed5=T0; SID=0; SID=1'
# >>>
# >>> ckstr = 'BIGipServer=rd0; TS013d8ed5=T0; BIGipServer=rd1; TS013d8ed5=T1; SID=0; SID
# >>> reserved = {'BIGipServer':1,'TS013d8ed5':0}
# >>> uniqulized = uniqulize_ckbody(ckstr,'BIGipServer','TS013d8ed5',reserved=reserved)
# >>> uniqulized
# 'TS013d8ed5=T0; BIGipServer=rd1; SID=0; SID=1'
# >>>
# >>>
# >>>




#split_ckheader

ckheader = "Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax"
pobj(split_ckheader(ckheader))
pobj(split_ckheader(ckheader,mode='ckstr'))
pobj(split_ckheader(ckheader,mode='ckpl'))
pobj(split_ckheader(ckheader,mode='ckptl'))
pobj(split_ckheader(ckheader,mode='ckpdl'))
pobj(split_ckheader(ckheader,mode='ckdict'))



#cons_ckheader

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



#select_ckheader


ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
selected = select_ckheader(ckheader,'BIGipServer','TSPD_101')
selected 
selected = select_ckheader(ckheader,'TSPD_101','BIGipServer')
selected


# >>>
# >>>
# >>> ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>> selected = select_ckheader(ckheader,'BIGipServer','TSPD_101')
# >>> selected
# 'Cookie: BIGipServer=rd19; TSPD_101=08819c2a'
# >>> selected = select_ckheader(ckheader,'TSPD_101','BIGipServer')
# >>> selected
# 'Cookie: BIGipServer=rd19; TSPD_101=08819c2a'
# >>>
# >>>



#prepend_ckheader

ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
src = 'Cookie: __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
prepended = prepend_ckheader(ckheader,src)
prepended

ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
src = '__RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
prepended = prepend_ckheader(ckheader,src)
prepended 

ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
src = [('__RequestVerificationToken','9VdrIliI'),('ASP.NET_SessionId','epax')]
prepended = prepend_ckheader(ckheader,src)
prepended 

ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
src = {'__RequestVerificationToken':'9VdrIliI','ASP.NET_SessionId':'epax'}
prepended = prepend_ckheader(ckheader,src)
# using ckdict will lose the order
prepended




#append_ckheader
ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
src = 'Cookie: __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
appended = append_ckheader(ckheader,src)
appended

ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
src = '__RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
appended = append_ckheader(ckheader,src)
appended 

ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
src = [('__RequestVerificationToken','9VdrIliI'),('ASP.NET_SessionId','epax')]
appended = append_ckheader(ckheader,src)
appended 

ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
src = {'__RequestVerificationToken':'9VdrIliI','ASP.NET_SessionId':'epax'}
appended = append_ckheader(ckheader,src)
appended


# >>>
# >>> ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
# >>> src = 'Cookie: __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>> appended = append_ckheader(ckheader,src)
# >>> appended
# 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>>
# >>> ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
# >>> src = '__RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>> appended = append_ckheader(ckheader,src)
# appended
# >>> appended
# 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>>
# >>> ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
# >>> src = [('__RequestVerificationToken','9VdrIliI'),('ASP.NET_SessionId','epax')]
# >>> appended = append_ckheader(ckheader,src)
# >>> appended
# 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>>
# >>> ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
# >>> src = {'__RequestVerificationToken':'9VdrIliI','ASP.NET_SessionId':'epax'}
# >>> appended = append_ckheader(ckheader,src)
# >>> appended
# 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; ASP.NET_SessionId=epax; __RequestVerificationToken=9VdrIliI'
# >>>



#insert_ckheader


ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
src = 'Cookie: __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
inserted = insert_ckheader(ckheader,src,0)
inserted

ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
src = '__RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
inserted = insert_ckheader(ckheader,src,1)
inserted 

ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
src = [('__RequestVerificationToken','9VdrIliI'),('ASP.NET_SessionId','epax')]
inserted = insert_ckheader(ckheader,src,2)
inserted 

ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
src = {'__RequestVerificationToken':'9VdrIliI','ASP.NET_SessionId':'epax'}
inserted = insert_ckheader(ckheader,src,3)
inserted



# >>>
# >>> ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
# src = 'Cookie: __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# inserted = insert_ckheader(ckheader,src,0)
# >>> src = 'Cookie: __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>> inserted = insert_ckheader(ckheader,src,0)
# >>> inserted
# 'Cookie: __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax; BIGipServer=rd19; TS013d8ed5=0105b6b0'
# >>>
# >>> ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
# >>> src = '__RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>> inserted = insert_ckheader(ckheader,src,1)
# >>> inserted
# 'Cookie: BIGipServer=rd19; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax; TS013d8ed5=0105b6b0'
# >>>
# >>> ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
# >>> src = [('__RequestVerificationToken','9VdrIliI'),('ASP.NET_SessionId','epax')]
# >>> inserted = insert_ckheader(ckheader,src,2)
# >>> inserted
# 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>>
# >>> ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
# >>> src = {'__RequestVerificationToken':'9VdrIliI','ASP.NET_SessionId':'epax'}
# >>> inserted = insert_ckheader(ckheader,src,3)
# >>> inserted
# 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; ASP.NET_SessionId=epax; __RequestVerificationToken=9VdrIliI'
# >>>



#remove_ckheader


ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
removed = remove_ckheader(ckheader,'TS013d8ed5')
removed 

ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
removed = remove_ckheader(ckheader,'TS013d8ed5',which=1)
removed 

#remove_ckheader,via ckname, allow duplecate, return ckheader,by default remove_all

# >>>
# >>>
# >>> ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>> removed = remove_ckheader(ckheader,'TS013d8ed5')
# >>> removed
# 'Cookie: BIGipServer=rd19; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>>
# >>> ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>> removed = remove_ckheader(ckheader,'TS013d8ed5',which=1)
# >>> removed
# 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>>
# >>>



#replace_ckheader
ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
replaced = replace_ckheader(ckheader,'TS013d8ed5','TSreplace=replace')
replaced 
replaced = replace_ckheader(ckheader,'TS013d8ed5',('TSreplace','replace'))
replaced 
replaced = replace_ckheader(ckheader,'TS013d8ed5',{'TSreplace':'replace'})
replaced 
replaced = replace_ckheader(ckheader,'TS013d8ed5','TSreplace','replace')
replaced 
####
ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
replaced = replace_ckheader(ckheader,'TS013d8ed5','TSreplace=replace',which=0)
replaced 
replaced = replace_ckheader(ckheader,'TS013d8ed5',('TSreplace','replace'),which=1)
replaced 
replaced = replace_ckheader(ckheader,'TS013d8ed5',{'TSreplace':'replace'},which=0)
replaced 
replaced = replace_ckheader(ckheader,'TS013d8ed5','TSreplace','replace',which=1)
replaced 
#replace_ckheader,via ckname, allow duplecate, return ckheader,by default replace_all



# >>> #replace_ckheader
# ... ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>> replaced = replace_ckheader(ckheader,'TS013d8ed5','TSreplace=replace')
# >>> replaced
# 'Cookie: BIGipServer=rd19; TSreplace=replace; TSPD_101=08819c2a; TSreplace=replace; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>> replaced = replace_ckheader(ckheader,'TS013d8ed5',('TSreplace','replace'))
# >>> replaced
# 'Cookie: BIGipServer=rd19; TSreplace=replace; TSPD_101=08819c2a; TSreplace=replace; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>> replaced = replace_ckheader(ckheader,'TS013d8ed5',{'TSreplace':'replace'})
# >>> replaced
# 'Cookie: BIGipServer=rd19; TSreplace=replace; TSPD_101=08819c2a; TSreplace=replace; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>> replaced = replace_ckheader(ckheader,'TS013d8ed5','TSreplace','replace')
# >>> replaced
# 'Cookie: BIGipServer=rd19; TSreplace=replace; TSPD_101=08819c2a; TSreplace=replace; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>> ####
# ... ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>> replaced = replace_ckheader(ckheader,'TS013d8ed5','TSreplace=replace',which=0)
# >>> replaced
# 'Cookie: BIGipServer=rd19; TSreplace=replace; TSPD_101=08819c2a; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>> replaced = replace_ckheader(ckheader,'TS013d8ed5',('TSreplace','replace'),which=1)
# >>> replaced
# 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; TSreplace=replace; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>> replaced = replace_ckheader(ckheader,'TS013d8ed5',{'TSreplace':'replace'},which=0)
# >>> replaced
# 'Cookie: BIGipServer=rd19; TSreplace=replace; TSPD_101=08819c2a; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>> replaced = replace_ckheader(ckheader,'TS013d8ed5','TSreplace','replace',which=1)
# >>> replaced
# 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; TSreplace=replace; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
# >>> #replace_ckheader,via ckname, allow duplecate, return ckheader,by default replace_all
# ...
# >>>



#uniqulize_ckheader

ckheader = 'Cookie: BIGipServer=rd0; TS013d8ed5=T0; BIGipServer=rd1; TS013d8ed5=T1; SID=0; SID=1'
uniqulized = uniqualize_ckheader(ckheader)
uniqulized

ckheader = 'Cookie: BIGipServer=rd0; TS013d8ed5=T0; BIGipServer=rd1; TS013d8ed5=T1; SID=0; SID=1'
reserved = {'BIGipServer':1,'TS013d8ed5':0,'SID':1}
uniqulized = uniqualize_ckheader(ckheader,reserved = reserved)
uniqulized 

ckheader = 'Cookie: BIGipServer=rd0; TS013d8ed5=T0; BIGipServer=rd1; TS013d8ed5=T1; SID=0; SID=1'
uniqulized = uniqualize_ckheader(ckheader,'BIGipServer','TS013d8ed5')
uniqulized 

ckheader = 'Cookie: BIGipServer=rd0; TS013d8ed5=T0; BIGipServer=rd1; TS013d8ed5=T1; SID=0; SID=1'
reserved = {'BIGipServer':1,'TS013d8ed5':0}
uniqulized = uniqualize_ckheader(ckheader,'BIGipServer','TS013d8ed5',reserved=reserved)
uniqulized 

####
#uniqualize_ckheader,via ckname, allow duplecate, return ckheader,by default uniqulize_all
#

ckheader = 'Cookie: BIGipServer=rd0; TS013d8ed5=T0; BIGipServer=rd1; TS013d8ed5=T1; SID=0; SID=1'
uniqulized = uniqualize_ckheader(ckheader)
uniqulized

ckheader = 'Cookie: BIGipServer=rd0; TS013d8ed5=T0; BIGipServer=rd1; TS013d8ed5=T1; SID=0; SID=1'
reserved = {'BIGipServer':1,'TS013d8ed5':0,'SID':1}
uniqulized = uniqualize_ckheader(ckheader,reserved = reserved)
uniqulized 

ckheader = 'Cookie: BIGipServer=rd0; TS013d8ed5=T0; BIGipServer=rd1; TS013d8ed5=T1; SID=0; SID=1'
uniqulized = uniqualize_ckheader(ckheader,'BIGipServer','TS013d8ed5')
uniqulized 

ckheader = 'Cookie: BIGipServer=rd0; TS013d8ed5=T0; BIGipServer=rd1; TS013d8ed5=T1; SID=0; SID=1'
reserved = {'BIGipServer':1,'TS013d8ed5':0}
uniqulized = uniqualize_ckheader(ckheader,'BIGipServer','TS013d8ed5',reserved=reserved)
uniqulized 

####
#uniqualize_ckheader,via ckname, allow duplecate, return ckheader,by default uniqulize_all
#


# >>>
# >>> ckheader = 'Cookie: BIGipServer=rd0; TS013d8ed5=T0; BIGipServer=rd1; TS013d8ed5=T1; SID=0; SID=1'
# >>> uniqulized = uniqualize_ckheader(ckheader)
# >>> uniqulized
# 'Cookie: BIGipServer=rd0; TS013d8ed5=T0; SID=0'
# >>>
# >>> ckheader = 'Cookie: BIGipServer=rd0; TS013d8ed5=T0; BIGipServer=rd1; TS013d8ed5=T1; SID=0; SID=1'
# >>> reserved = {'BIGipServer':1,'TS013d8ed5':0,'SID':1}
# >>> uniqulized = uniqualize_ckheader(ckheader,reserved = reserved)
# >>> uniqulized
# 'Cookie: TS013d8ed5=T0; BIGipServer=rd1; SID=1'
# >>>
# >>> ckheader = 'Cookie: BIGipServer=rd0; TS013d8ed5=T0; BIGipServer=rd1; TS013d8ed5=T1; SID=0; SID=1'
# >>> uniqulized = uniqualize_ckheader(ckheader,'BIGipServer','TS013d8ed5')
# >>> uniqulized
# 'Cookie: BIGipServer=rd0; TS013d8ed5=T0; SID=0; SID=1'
# >>>
# >>> ckheader = 'Cookie: BIGipServer=rd0; TS013d8ed5=T0; BIGipServer=rd1; TS013d8ed5=T1; SID=0; SID=1'
# >>> reserved = {'BIGipServer':1,'TS013d8ed5':0}
# >>> uniqulized = uniqualize_ckheader(ckheader,'BIGipServer','TS013d8ed5',reserved=reserved)
# >>> uniqulized
# 'Cookie: TS013d8ed5=T0; BIGipServer=rd1; SID=0; SID=1'
# >>>
# >>> ####
# ... #uniqualize_ckheader,via ckname, allow duplecate, return ckheader,by default uniqulize_all
# ... #
# ...
# >>>




















