
def new_cookie(): <br>
def fillCookieDomain(Cookie,domain,**kwargs): <br>
def fillCookieExpires(Cookie,expires,**kwargs): <br>
def fillCookieMaxage(Cookie,maxage,**kwargs): <br>
def fillCookieSecure(Cookie,secure): <br>
def fillCookieHttpOnly(Cookie,httponly): <br>
def fillCookiePath(Cookie,path,**kwargs): <br>
def extension_handler(extension_av,**kwargs): <br>
def setckdict2Cookie(setckdict,**kwargs): <br>
def read_file_content(**kwargs): <br>
def write_to_file(**kwargs): <br>
def cond_expired(ck): <br>
def cond_domain(ck,server): <br>
def cond_path(ck,path): <br>
def cond_secure(ck,scheme): <br>
def sort_ckl(ckl,**kwargs): <br>


## _class_  Cookie

def __init__(self,setck,**kwargs): <br>
def __repr__(self): <br>
def ckpair(self,**kwargs): <br>
def save2mem(self,**kwargs): <br>
def save_ck(cls,Cookie,dir): <br>
def save2file(self,**kwargs): <br>


## _class_ Jar

def __init__(self,**kwargs): <br>
def loads(self,dir): <br>
def remove_expired(self): <br>
def save_ckl(cls,ckl,dir): <br>
def save(self,**kwargs): <br>
def ckpl(self,**kwargs): <br>
def ckstr(self,**kwargs): <br>
def setcktl2ckstr(cls,setcktl,**kwargs) <br>








