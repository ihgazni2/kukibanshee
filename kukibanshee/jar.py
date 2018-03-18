import sys
#import sqlite
import os
import time
import json
import urllib.parse
import elist.elist as elel
from kukibanshee import rfc6265
from kukibanshee import drone
from kukibanshee import nozdormu
from kukibanshee.Resources import public_suffixes as pub
#pub.PUBLICSUFFIXES

#
class originException(Exception):
    pass

# 
SETCKREJECTLOG = {
    'origin':'server url of the response not in domain',
    'public_suffix':'the domain is a public_suffix',
}

INVALIDLOG = {
    'expiry':'the Cookie expired',
    'domain':'dst_url netloc not in Cookie Domain',
    'path':'dst_url path not in Cookie Path',
    'secure':'dst_url only for https'
}

INMEMJAR = []
SESSIONJAR = []
ANADBPATH = '/opt/PY/PY3/kukibashee/kukibanshee/Resources/anadb.json'
JARDBPATH = '/opt/PY/PY3/kukibashee/kukibanshee/Resources/jardb.json'

def new_cookie():
    Cookie = {
        'origin':None,
        'Expires':None,
        'Max-Age':None,
        'Domain':None,
        'Path':None,
        'Secure':None,
        'HttpOnly':None,
        'extension-av':None,
        'name':None,  
        'value':None,
        'expiry-time':None,
        'creation-time':None, 
        'last-access-time': None,
        'persistent-flag': False,
        'host-only-flag': False, 
        'secure-only-flag':False,
        'http-only-flag':False,
        'unquote':False,
        'unquote_plus':False,
        '_req-type':'Cookie',
        '_resp-type':'Set-Cookie',
        '_reject':False,
        '_reject_reason':None
    }
    return(Cookie)

def fillCookieDomain(Cookie,domain,**kwargs):
    '''
        Page20 Let cookie-domain be the attribute-value without the leading %x2E (".") character
        
        "If the server omits the Domain attribute, the user 
        agent will return the cookie only to the origin server"
        
        4.1.2.3
            The user agent will reject cookies unless the Domain attribute
            specifies a scope for the cookie that would include the origin server.
            For example, the user agent will accept a cookie with a 
            Domain attribute of "example.com" or of "foo.example.com" from 
            foo.example.com, but the user agent will not accept a cookie with a 
            Domain attribute of "bar.example.com" or of "baz.foo.example.com".

            For security reasons, many user agents are configured to reject
            Domain attributes that correspond to "public suffixes".
        
        4. If the cookie-attribute-list contains an attribute with an attribute-name of "Domain":
           Let the domain-attribute be the attribute-value of the last attribute in the 
           cookie-attribute-list with an attribute-name of "Domain".
           Otherwise:
               Let the domain-attribute be the empty string.
        
        5.  If the user agent is configured to reject "public suffixes" 
            and the domain-attribute is a public suffix:
                If the domain-attribute is identical to the canonicalized request-host:
                    Let the domain-attribute be the empty string.
            Otherwise:
                    Ignore the cookie entirely and abort these steps.
                    
            NOTE: A "public suffix" is a domain that is controlled by a public registry, 
            such as "com", "co.uk", and "pvt.k12.wy.us". 
            This step is essential for preventing attacker.com from disrupting the integrity 
            of example.com by setting a cookie with a Domain attribute of "com".  
            Unfortunately, the set of  public suffixes (also known as "registry controlled domains")
            changes over time.  If feasible, user agents SHOULD use an up-to-date public suffix list, 
            such as the one maintained by the Mozilla project at <http://publicsuffix.org/>.
        
        6.  If the domain-attribute is non-empty:
                If the canonicalized request-host does not domain-match the domain-attribute:
                    Ignore the cookie entirely and abort these steps.
                Otherwise:
                    Set the cookie’s host-only-flag to false.
                    Set the cookie’s domain to the domain-attribute.
            Otherwise:
                Set the cookie’s host-only-flag to true.
                Set the cookie’s domain to the canonicalized request-host.
 
    '''
    #必须有origin,必须是合法的origin
    origin = Cookie['origin']
    origin = rfc6265.format_origin(origin)
    cond_origin = rfc6265.is_domain_value(origin)
    if(cond_origin):
        pass
    else:
        raise originException('origin must be a valid domain or url with valid netloc')
    #######################33
    # Page20 Let cookie-domain be the attribute-value without the leading %x2E (".") character
    if(domain == None):
        pass
    else:
        domain = rfc6265.remove_domain_leading_dot(domain)
    # 检查origin(发送包含set-cookie的response的server_url,也就是你访问的web url)
    # 如果domain 不为空 ，必须包含origin 
    cond_domain = not((domain==None)|(domain == ''))
    if(cond_domain):
        valid_origin = rfc6265.origin_in_domain(origin,domain)
    else:
        valid_origin = True 
    if(valid_origin):
        pass
    else:
        Cookie['_reject'] = True
        Cookie['_reject_reason'] = 'origin'
        return(Cookie)
    #检查public_suffixes 
    if('reject_public' in kwargs):
        reject_public = kwargs['reject_public']
    else:
        reject_public = True
    if(reject_public):
        if(domain in pub.PUBLICSUFFIXES):
            Cookie['Domain'] = domain
            Cookie['_reject'] = True
            Cookie['_reject_reason'] = 'public_suffix'
            return(Cookie)
        else:
            pass
    else:
        pass
    #是否空Domain (host-only-flag)
    if((domain == None)|(domain == '')):
        Cookie['host-only-flag'] = True
        Cookie['Domain'] = origin 
    else:
        Cookie['host-only-flag'] = False
        Cookie['Domain'] = domain
    return(Cookie)

def fillCookieExpires(Cookie,expires,**kwargs):
    '''
        Let the expiry-time be the result of parsing the attribute-value as cookie-date (see Section 5.1.1).
        If the attribute-value failed to parse as a cookie date, ignore the cookie-av.
        
        If a cookie has both the Max-Age and the Expires attribute, the Max Age 
        attribute has precedence and controls the expiration date of the cookie. 
        If a cookie has neither the Max-Age nor the Expires attribute, 
        the user agent will retain the cookie until "the current session 
        is over" (as defined by the user agent).
    '''
    if((expires == None) | (expires == '')):
        pass
    else:
        if('disable_sane_check' in kwargs):
            disable_sane_check = kwargs['disable_sane_check']
        else:
            disable_sane_check = False
        if(disable_sane_check):
            Cookie['Expires'] = expires
            #Max-Age override Exipires
            if(Cookie['Max-Age']):
                pass
            else:
                Cookie['expiry-time'] = nozdormu.str2ts(expires)
                Cookie['persistent-flag'] = True
        else:
            if('mode' in kwargs):
                mode = kwargs['mode']
            else:
                mode = 'loose'
            cond = rfc6265.is_sane_cookie_date(expires,mode = mode)
            if(cond):
                Cookie['Expires'] = expires
                #Max-Age override Exipires
                if(Cookie['Max-Age']):
                    pass
                else:
                    Cookie['expiry-time'] = nozdormu.str2ts(expires)
                    Cookie['persistent-flag'] = True
            else:
                Cookie['Expires'] = None
                #Max-Age override Exipires
                if(Cookie['Max-Age']):
                    pass
                else:
                    Cookie['expiry-time'] = None
                    Cookie['persistent-flag'] = False
    return(Cookie)

def fillCookieMaxage(Cookie,maxage,**kwargs):
    '''
        If the first character of the attribute-value is not a DIGIT or a "-" character, 
        ignore the cookie-av.
        #cant understand why minus Max-Age permitted, not support this secarino
        
        If the remainder of attribute-value contains a non-DIGIT character,
        ignore the cookie-av.
        Let delta-seconds be the attribute-value converted to an integer.
        If delta-seconds is less than or equal to zero (0), let expiry-time
        be the earliest representable date and time.  
        Otherwise, let the expiry-time be the current date and time plus delta-seconds seconds.
    '''
    if(maxage == None):
        pass
    else:
        cond = rfc6265.is_max_age_value(maxage)
        if(cond):
            Cookie['Max-Age'] = maxage
            if(Cookie['creation-time']):
                Cookie['expiry-time'] = Cookie['creation-time'] + int(maxage)
            else:
                Cookie['expiry-time'] = time.time() + int(maxage)
            Cookie['persistent-flag'] = True
        else:
            Cookie['Max-Age'] = None
            #dont modify the expiry-time, it maybe setby Expires
            #dont modify the persistant-flag, it maybe setby Expires
    return(Cookie)

def fillCookieSecure(Cookie,secure):
    Cookie['Secure'] = secure
    if(secure):
        Cookie['secure-only-flag'] = True
    else:
        Cookie['secure-only-flag'] = False
    return(Cookie)

def fillCookieHttpOnly(Cookie,httponly):
    Cookie['HttpOnly'] = httponly
    if(httponly):
        Cookie['http-only-flag'] = True
    else:
        Cookie['http-only-flag'] = False
    return(Cookie)

def fillCookiePath(Cookie,path,**kwargs):
    '''
        If the cookie-attribute-list contains an attribute with an attribute-name of "Path", 
        set the cookie’s path to attribute value of the last attribute in the cookie-attribute-list 
        with an attribute-name of "Path".  
        Otherwise, set the cookie’s path to the default-path of the request-uri.
    '''
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 'strict'
    if(path == None):
        Cookie['Path'] = rfc6265.format_path(urllib.parse.urlparse(dst_url).path,mode=mode)
        
    else:
        Cookie['Path'] = path
    return(Cookie)

def extension_handler(extension_av,**kwargs):
    '''
        Not Implemented
    '''
    return(extension_av)

def setckdict2Cookie(setckdict,**kwargs):
    '''
        2.
            Create a new cookie with name cookie-name, value cookie-value.
            Set the creation-time and the last-access-time to the currentdate and time
        
        3.  If the cookie-attribute-list contains an attribute with an attribute-name of "Max-Age":
                Set the cookie’s persistent-flag to true.
                Set the cookie’s expiry-time to attribute-value of the last attribute 
                in the cookie-attribute-list with an attribute-name of "Max-Age".
            Otherwise, if the cookie-attribute-list contains an attribute with an attribute-name of "Expires" 
            (and does not contain an attribute with an attribute-name of "Max-Age"):
                Set the cookie’s persistent-flag to true.
                Set the cookie’s expiry-time to attribute-value of the last 
                attribute in the cookie-attribute-list with an attribute-name of "Expires".
            Otherwise:
                Set the cookie’s persistent-flag to false.
    '''
    #for further check ,must input origin(server netloc or server_url )
    origin = kwargs['origin']
    origin = rfc6265.format_origin(origin)
    cond_origin = rfc6265.is_domain_value(origin)
    if(cond_origin):
        pass
    else:
        raise originException('origin must be a valid domain or url with valid netloc')
    ####
    name = drone.get_ckavalue(setckdict,'name')
    value = drone.get_ckavalue(setckdict,'value')
    expires = drone.get_ckavalue(setckdict,'Expires')
    maxage = drone.get_ckavalue(setckdict,'Max-Age')
    domain = drone.get_ckavalue(setckdict,'Domain')
    path = drone.get_ckavalue(setckdict,'Path')
    secure = drone.get_ckavalue(setckdict,'Secure')
    httponly = drone.get_ckavalue(setckdict,'HttpOnly')
    extension = drone.get_ckavalue(setckdict,'extension-av')
    # if('mode' in kwargs):
        # mode = kwargs['mode']
    # else:
        # mode = 'loose'
    ck = new_cookie()
    ck['origin'] = origin
    ck['name'] = name
    ck['value'] = value
    ck['creation-time'] = time.time()
    ck['last-access-time'] = ck['creation-time']
    fillCookieDomain(ck,domain,origin=origin)
    fillCookieExpires(ck,expires)
    #If Max-Age exist,let the Max-Age override Expires
    fillCookieMaxage(ck,maxage)
    fillCookiePath(ck,path)
    fillCookieSecure(ck,secure)
    fillCookieHttpOnly(ck,httponly)
    ck['extension-av'] = extension
    if('unquote' in kwargs):
        ck['unquote'] = kwargs['unquote']
    else:
        ck['unquote'] = True
    if('unquote_plus' in kwargs):
        ck['unquote_plus'] = kwargs['unquote_plus']
    else:
        ck['unquote_plus'] = True
    return(ck)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def read_file_content(**kwargs):
    fd = open(kwargs['fn'],kwargs['op'])
    rslt = fd.read()
    fd.close()
    return(rslt)

#
def write_to_file(**kwargs):
    fd = open(kwargs['fn'],kwargs['op'])
    fd.write(kwargs['content'])
    fd.close()

def cond_expired(ck):
    '''
    '''
    expiry = ck['expiry-time']
    now = time.time()
    cond = (now >= expiry)
    if(cond):
        pass
    else:
        print(INVALIDLOG['expiry'])
    return(cond)

def cond_domain(ck,server):
    '''
        The cookie’s host-only-flag is true and the canonicalized request-host is 
        identical to the cookie’s domain.

        The cookie’s host-only-flag is false and the canonicalized request-host 
        domain-matches the cookie’s domain.
    '''
    if(ck['host-only-flag']):
        cond = (server == ck['Domain'])
    else:
        cond = rfc6265.domain_in_domain(server,ck['Domain'])
    if(cond):
        pass
    else:
        print(INVALIDLOG['domain'])
    return(cond)

def cond_path(ck,path):
    '''
        The request-uri’s path path-matches the cookie’s path.
    '''
    cond = rfc6265.path_in_path(path,ck['Path'])
    if(cond):
        pass
    else:
        print(INVALIDLOG['path'])
    return(cond)

def cond_secure(ck,scheme):
    '''
    '''
    if(ck['secure-only-flag']):
        cond = (scheme == 'https')
    else:
        cond = True
    if(cond):
        pass
    else:
        print(INVALIDLOG['secure'])
    return(cond)


class Cookie():
    '''
    '''
    def __init__(self,setck,**kwargs):
        origin = kwargs['origin']
        if('unquote' in kwargs):
            unquote = kwargs['unquote']
        else:
            unquote = True
        if('unquote_plus' in kwargs):
            unquote_plus = kwargs['unquote_plus']
        else:
            unquote_plus = True
        if(unquote):
            setck = drone.unquote_setck(setck,plus = unquote_plus)
        else:
            pass
        setckdict = drone.split_setck(setck)['setckdict']
        self.Cookie = setckdict2Cookie(setckdict,unquote=unquote,unquote_plus=unquote_plus,origin=origin)
    def __repr__(self):
        return(self.Cookie.__str__())
    ####
    def save2mem(self,**kwargs):
        if(self.Cookie['_reject'] == True):
            print("No store rejected")
        elif(self.Cookie['expiry-time']<=time.time()):
            print("No store expired")
        else:
            INMEMJAR = elel.cond_remove_all(INMEMJAR,cond_func=cond_expired)
            INMEMJAR.append(self.Cookie)
            #### add sort
    def ckpair(self,**kwargs):
        '''
            get valid ckpair for dst_url
        '''
        dst_url = kwargs['url']
        rslt = urllib.parse.urlparse(dst_url)
        scheme = rslt.scheme
        netloc = rslt.netloc
        cond1 = not(cond_expired(self.Cookie))
        cond2 = cond_domain(self.Cookie,netloc)
        cond3 = cond_path(self.Cookie,path)
        cond4 = cond_secure(self.Cookie,scheme)
        cond = (cond1 & cond2 & cond3 & cond4)
        if(cond):
            if(self.Cookie['unquote']):
                if(self.Cookie['unquote_plus']):
                    name = urllib.parse.quote_plus(self.Cookie['name'])
                    value = urllib.parse.quote_plus(self.Cookie['value'])
                else:
                    name = urllib.parse.quote(self.Cookie['name'])
                    value = urllib.parse.quote(self.Cookie['value'])
            else:
                name = self.Cookie['name']
                value = self.Cookie['value']
            ckpair = drone.nv2ckpair(name,value)
            return(ckpair)
        else:
            return(None)
    ####
    @classmethod
    def saveCookie(cls,Cookie,dir):
        '''
        '''
        if(os.path.exists(dir)):
            content = read_file_content(fn=dir,op='r+')
            arr = json.loads(content)
            arr.append(Cookie)
            ### add sort
            write_to_file(fn=dir,content=json.dumps(arr),op='w+')
        else:
            arr = [Cookie]
            write_to_file(fn=dir,content=json.dumps(arr),op='w+')
    def save2file(self,**kwargs):
        '''
        '''
        if('mode' in kwargs):
            mode = kwargs['mode']
        else:
            mode = 'analysis'
        if(mode == 'analysis'):
            if('dir' in kwargs):
                dir = kwargs['dir']
            else:
                dir = ANADBPATH
            saveCookie(self.Cookie,dir)
        else:
            # for jar 
            if('dir' in kwargs):
                dir = kwargs['dir']
            else:
                dir = JARDBPATH
            if(self.Cookie['_reject'] == True):
                print("No save rejected Cookie to jar,only to ana")
            else:
                saveCookie(self.Cookie,dir)
    ####
    @classmethod
    def setcktl2ckstr(setcktl,**kwargs):
        '''
        '''
        dst_url = kwargs['url']
        ckpl = elel.array_map(setcktl,lambda setck:setck.ckpair(url=dst_url))
        ckstr = drone.list2ckstr(ckpl)
        return(ckstr)
    ####
    @classmethod
    def loads(cls,dir):
        '''
        '''
        if(os.path.exists(dir)):
            content = read_file_content(fn=dir,op='r+')
            arr = json.loads(content)
            arr = elel.cond_remove_all(jar,cond_func=cond_expired)
        else:
            arr = []
        return(arr)
    @classmethod
    def remove_expired_jar(jar,dir):
        '''
            The user agent MUST evict all expired cookies from the cookie store if, 
            at any time, an expired cookie exists in the cookie store
        '''
        if('dir' in kwargs):
            dir = kwargs['dir']
        else:
            dir = JARDBPATH
        jar = elel.cond_remove_all(jar,cond_func=cond_expired)
        saveCookie(jar,dir)


# 当组成一个用于request 的ckheader 时，来源有三个
# 1. 多个 set-cookie-header  in response 
# 2. cookie-pair in javascript
# 3. Jar
##   


#step 1.path = rslt.path loads cookie from jar ,and remove expiry-time ,
#1. 把cookie-jar load, 删除过期的cookie,更新cookie-jar
#JAR = loads_jar(JARDBPATH)
#set-cookie -> Cookie 
#pipeline 
#cookie from javascript
#cookie from set-cookie : set-cookie-header  -> Cookie 
#cookie 

