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






















