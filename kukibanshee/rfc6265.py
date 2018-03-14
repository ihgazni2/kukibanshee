
import re
import urllib.parse
from kukibanshee import araq
from kukibanshee import nozdormu
from kukibanshee import symmtera

def is_cookie_octet(c):
    '''
        %x21 / %x23-2B / %x2D-3A / %x3C-5B / %x5D-7E; 
        US-ASCII characters excluding CTLs,
        whitespace DQUOTE, comma, semicolon,
        and backslash 
    '''
    regex_str = araq.CONST_STR['ckocts']
    prefix = "^[" 
    suffix = "]$"
    regex = araq._creat_regex(regex_str,prefix=prefix,suffix=suffix)
    m=regex.search(c)
    return(bool(araq._real_dollar(s,m)))

def is_cookie_value(s):
    '''cookie-value      = *cookie-octet / ( DQUOTE *cookie-octet DQUOTE ) '''
    regex_str = araq.CONST_STR['ckocts']
    prefix = "^[" 
    suffix = "]*$"
    regex1 = araq._creat_regex(regex_str,prefix=prefix,suffix=suffix)
    m1=regex1.search(s)
    regex_str = araq.CONST_STR['ckocts']
    prefix = "^\"[" 
    suffix = "]*\"$"
    regex2 = araq._creat_regex(regex_str,prefix=prefix,suffix=suffix)
    m2=regex2.search(s)
    rslt = (bool(araq._real_dollar(s,m1))) | (bool(araq._real_dollar(s,m2)))
    return(rslt)

def is_token(s):
    '''1*<any CHAR except CTLs or separators> '''
    regex_ctls_str = araq.CONST_STR['ctls']
    regex_separators_str = araq.CONST_STR['sps']
    regex_str = regex_ctls_str + regex_separators_str
    prefix = "^[^"
    suffix = "]+$"
    regex = araq._creat_regex(regex_str,prefix=prefix,suffix=suffix)
    m=regex.search(s)
    return(bool(araq._real_dollar(s,m)))

def is_cookie_name(s):
    '''
        RFC 6265    page-9
        cookie-name       = token 
    '''
    return(is_token(s))

def is_cookie_pair(s):
    '''cookie-pair       = cookie-name "=" cookie-value'''
    try:
        eq_loc = s.index("=")
    except:
        return(False)
    else:
        pass
    name = s[:eq_loc]
    value = s[(eq_loc+1):]
    cond1 = is_token(name)
    cond2 = is_cookie_value(value)
    if(cond1 & cond2):
        return(True)
    else:
        return(False)

def is_sane_cookie_date(s,**kwargs):
    '''
        sane-cookie-date  = <rfc1123-date, defined in [RFC2616], Section 3.3.1>
        SP = " "
        date1 = 2DIGIT SP month SP 4DIGIT
        wkday = "Mon" | "Tue" | "Wed" | "Thu" | "Fri" | "Sat" | "Sun"
        rfc1123-date = wkday "," SP date1 SP time SP "GMT"
    '''
    if(mode in kwargs):
        mode = kwargs['mode']
    else:
        mode = 'strict'
    tf = nozdormu.detect_time_format(date_value)
    if(mode == 'strict'):
        cond = ('rfc1123' == tf)
    else:
        cond = ('rfc1123' in tf) 
    if(cond):
        return(True)
    else:
        return(False)

def is_expires_value(s):
    '''"Expires=" sane-cookie-date
        In practice, both expires-av and max-age-av
        are limited to dates representable by the
        user agent. 
        
    '''
    return(is_sane_cookie_date(s))

def is_expires_av(s):
    '''
        the attribute-name case-insensitively matches the string   "Expires"
        expires-av        = "Expires=" sane-cookie-date
        In practice, both expires-av and max-age-av
        are limited to dates representable by the
        user agent. 
    '''
    prefix = str.lower(s[:8])
    if(prefix=="expires="):
        scd = s[9:]
        return(is_sane_cookie_date(scd))
    else:
        return(False)

def is_max_age_value(s):
    '''
        "Max-Age=" non-zero-digit *DIGIT
        In practice, both expires-av and max-age-av
        are limited to dates representable by the
        user agent. 
    '''
    regex= re.compile("^[1-9][0-9]*$")
    m = regex.search(s)
    return(bool(_real_dollar(s,m)))

def is_maxage_av(s):
    '''
        the attribute-name case-insensitively matches the string   "Max-Age"
        "Max-Age=" non-zero-digit *DIGIT
        In practice, both expires-av and max-age-av
        are limited to dates representable by the
        user agent. 
    '''
    prefix = s[:8]
    if(prefix=="max-age="):
        nums = s[9:]
        regex= re.compile("^[1-9][0-9]*$")
        m = regex.search(nums)
        return(bool(_real_dollar(nums,m)))
    else:
        return(False)

def is_secure_av(s):
    '''"Secure"'''
    s = str.lower(s)
    return(s=='secure')

def is_httponly_av(s):
    '''"HttpOnly"'''
    s = str.lower(s)
    return(s=='httponly')

def is_path_value(s):
    '''<any CHAR except CTLs or ";">''' 
    regex_ctls_str = araq.CONST_STR['ctls']
    regex_str = regex_ctls_str + ";"
    prefix = "^[^"
    suffix = "]+$"
    regex = araq._creat_regex(regex_str,prefix=prefix,suffix=suffix)
    m=regex.search(s)
    return(bool(araq._real_dollar(s,m)))

def is_path_av(s):
    '''
        "Path=" path-value
    '''
    prefix = str.lower(s[:5])
    if(prefix == "path="):
        p = s[6:]
        return(is_path_value(p))
    else:
        return(False)

def is_extension_av(s):
    '''<any CHAR except CTLs or ";">'''
    regex_ctls_str = araq.CONST_STR['ctls']
    regex_str = regex_ctls_str + ";"
    prefix = "^[^"
    suffix = "]+$"
    regex = araq._creat_regex(regex_str,prefix=prefix,suffix=suffix)
    m=regex.search(s)
    return(bool(araq._real_dollar(s,m)))

def is_domain_value(s):
    '''
        domain-value = <subdomain>; 
        defined in [RFC1034], Section 3.5
            <subdomain> ::= <label> | <subdomain> "." <label>
            <label> ::= <letter> [ [ <ldh-str> ] <let-dig> ]
            <ldh-str> ::= <let-dig-hyp> | <let-dig-hyp> <ldh-str>
            <let-dig-hyp> ::= <let-dig> | "-"
            <let-dig> ::= <letter> | <digit>
            <letter> ::= any one of the 52 alphabetic characters A through Z in upper case and a through z in lower case
            <digit> ::= any one of the ten digits 0 through 9
        enhanced by [RFC1123], Section 2.1
        
    '''
    regex_label = re.compile("^[a-zA-Z](([0-9a-zA-Z\-])*[0-9a-zA-Z])*$")
    arr = s.split(".")
    rslt = True
    for i in range(0,arr.__len__()):
        m = regex_label.search(arr[i])
        cond = bool(araq._real_dollar(arr[i],m))
        if(cond):
            pass
        else:
            rslt = False
            break
    return(rslt)

def is_domain_av(s):
    '''
        "Domain=" domain-value  
    '''
    prefix = s[:7]
    if(prefix == "domain="):
        dm = s[8:]
        return(is_domain_value(dm))
    else:
        return(False)

def is_cookie_av(s):
    '''
        cookie-av = expires-av / max-age-av / domain-av /path-av / secure-av / httponly-av /extension-av
    '''
    expires = is_expires_av(s)
    maxage = is_maxage_av(s)
    domain = is_domain_av(s)
    path = is_path_av(s)
    secure = is_secure_av(s)
    httponly = is_httponly_av(s)
    extension = is_extension_av(s)
    return(expires|maxage|domain|path|secure|httponly|extension)

def is_delimiter(c):
    '''delimiter = %x09 / %x20-2F / %x3B-40 / %x5B-60 / %x7B-7E'''
    regex_str = araq.CONST_STR['dels']
    prefix = "^["
    suffix = "]$"
    regex = araq._creat_regex(regex_str,prefix=prefix,suffix=suffix)
    m=regex.search(c)
    return(bool(araq._real_dollar(c,m)))

#5.1.1 Dates

def is_time_field(s):
    '''time-field      = 1*2DIGIT'''
    regex = re.compile("^[0-9]{1,2}$")
    m=regex.search(s)
    return(bool(araq._real_dollar(s,m)))

def is_hms_time(s):
    '''hms-time = time-field ":" time-field ":" time-field'''
    regex_str = "^[0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}$"
    regex = re.compile(regex_str)
    m=regex.search(s)
    rslt = (bool(araq._real_dollar(s,m)))
    return(rslt)

def is_non_digit(c):
    '''non-digit = %x00-2F / %x3A-FF'''
    nds = araq.CONST_STR['ndigits']
    regex_str = nds
    prefix = "^[" 
    suffix = "]$"
    regex = araq._creat_regex(regex_str,prefix=prefix,suffix=suffix)
    m=regex.search(c)
    return(bool(araq._real_dollar(c,m)))

def is_non_delimiter(c):
    '''non-delimiter   = %x00-08 / %x0A-1F / DIGIT / ":" / ALPHA / %x7F-FF'''
    ndels = araq.CONST_STR['ndels']
    regex_str = ndels
    prefix = "^[" 
    suffix = "]$"
    regex = araq._creat_regex(regex_str,prefix=prefix,suffix=suffix)
    m=regex.search(c)
    return(bool(araq._real_dollar(c,m)))

def is_date_token(s):
    '''date-token      = 1*non-delimiter'''
    dt = araq.CONST_STR['ndels']
    regex_str = dt
    prefix = "^[" 
    suffix = "]+$"
    regex = araq._creat_regex(regex_str,prefix=prefix,suffix=suffix)
    m=regex.search(s)
    return(bool(araq._real_dollar(s,m)))

def is_date_token_list(s):
    '''date-token-list = date-token *( 1*delimiter date-token )'''
    dt = re.escape(araq.CONST_STR['ndels'])
    ads = re.escape(araq.CONST_STR['dels'])
    regex_str = "^[" + dt + "]+" +"([" +ads+ "]+"+"[" + dt + "]+)*$"
    m=regex.search(s)
    return(bool(_real_dollar(s,m)))

def is_cookie_date(s):
    '''cookie-date     = *delimiter date-token-list *delimiter'''
    ads = re.escape(araq.CONST_STR['dels'])
    regex_str = "([" + ads + "]*)" + "(.*)" + "([" + ads + "]*)"
    regex = re.compile(regex_str,re.DOTALL)
    m = regex.search(s)
    try:
        dtl = m.group(2)
    except:
        return(False)
    else:
        pass
    return(is_date_token_list(dtl))

def is_time(s):
    '''time            = hms-time ( non-digit *OCTET )'''
    regex_str = "^([0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2})"
    nds = "[" + re.escape(araq.CONST_STR['ndigits']) + "]"
    prefix = "["
    octs = re.escape(araq.CONST_STR['octs'])
    suffix = "]*$"
    regex_str = regex_str + nds + prefix + octs + suffix
    regex = re.compile(regex_str)
    m=regex.search(s)
    rslt = (bool(araq._real_dollar(s,m)))
    return(rslt)

def is_year(s):
    '''year = 2*4DIGIT ( non-digit *OCTET )'''
    regex_str = "^([0-9]{2,4})"
    nds = "[" + re.escape(araq.CONST_STR['ndigits']) + "]"
    prefix = "["
    octs = re.escape(araq.CONST_STR['octs'])
    suffix = "]*$"
    regex_str = regex_str + nds + prefix + octs + suffix
    regex = re.compile(regex_str)
    m=regex.search(s)
    rslt = (bool(araq._real_dollar(s,m)))
    return(rslt)

def is_month(s,**kwargs):
    '''( "jan" / "feb" / "mar" / "apr" /"may" / "jun" / "jul" / "aug" /"sep" / "oct" / "nov" / "dec" ) *OCTET
        mode = 'loose' will case-insensitively
        by default loose
    '''
    if('mode' in kwargs):
       mode = kwargs['mode']
    else:
        mode = 'strict'
    if(mode == 'loose'):
        s = str.lower(s)
    else:
        pass
    regex_str = "^(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)"
    prefix = "["
    octs = re.escape(araq.CONST_STR['octs'])
    suffix = "]*$"
    regex_str = regex_str + prefix + octs + suffix
    regex = re.compile(regex_str)
    m=regex.search(s)
    rslt = (bool(araq._real_dollar(s,m)))
    return(rslt)

def is_day_of_month(s,**kwargs):
    '''day-of-month    = 1*2DIGIT ( non-digit *OCTET )'''
    regex_str = "^[0-9]{1,2}"
    ndts = re.escape(araq.CONST_STR['ndigits'])
    prefix = "["
    octs = re.escape(araq.CONST_STR['octs'])
    suffix = "]*$"
    regex_str = regex_str + "[" + ndts + "]" + prefix + octs + suffix
    regex = re.compile(regex_str)
    m=regex.search(s)
    rslt = (bool(araq._real_dollar(s,m)))
    return(rslt)


CORERULES = {
    'NUL' : araq._isNUL,
    'OCTET' : araq._isOCTET,
    'WSP' : araq._isWSP,
    'OWS' : araq._isOWS,
    'cookie-header':'IMPLEMENTED IN drone.py : validate_ckheader',
    'cookie-string':'IMPLEMENTED IN drone.py : validate_ckstr',
    'obs-fold' : araq._is_obs_fold,
    'cookie-octet' : is_cookie_octet,
    'cookie-value' : is_cookie_value,
    'cookie-name' : is_token,
    'sane-cookie-date' : is_sane_cookie_date,
    'cookie-pair' : is_cookie_pair,
    'expires-av' : is_expires_av,
    'max-age-av' : is_maxage_av,
    'secure-av' : is_secure_av,
    'httponly-av' : is_httponly_av,
    'path-value' : is_path_value,
    'extension-av' : is_extension_av,
    'path-av' : is_path_av,
    'domain-av' : is_domain_av,
    'cookie-av' : is_cookie_av,
    'set-cookie-string' : 'IMPLEMENTED IN drone.py validate_setckstr',
    'set-cookie-header' : 'IMPLEMENTED IN drone.py validate_setckheader',
    'delimiter' : is_delimiter,
    'time-field' : is_time_field,
    'hms-time' : is_hms_time,
    'time' : is_time,
    'non-digit' : is_non_digit,
    'non-delimiter' : is_non_delimiter,
    'date-token' : is_date_token,
    'date-token-list' : is_date_token_list,
    'cookie-date' : is_cookie_date,
    'year': is_year,
    'month': is_month,
    'day-of-month': is_day_of_month
}

def split_cookie_date_str(s):
    '''
        split cookie_date_str to date-tokens list
        split_cookie_date_str('Tue, 27 Mar 2018 05:30:16')
        >>> split_cookie_date_str('Tue, 27 Mar 2018 05:30:16')
        ['Tue', '27', 'Mar', '2018', '05:30:16']
        >>>
    '''
    def _open_token(tok,input_symbol,rslt):
        tok = tok + input_symbol
        return(tok)
    _append_token = _open_token
    def _close_token(tok,input_symbol,rslt):
        rslt.append(tok)
        tok = ''
        return(tok)
    machine = symmtera.FSM()
    machine.add("INIT",is_delimiter,None,"DEL")
    machine.add("INIT",is_non_delimiter,_open_token,"TOK")
    machine.add("DEL",is_delimiter,None,"DEL")
    machine.add("DEL",is_non_delimiter,_open_token,"TOK")
    machine.add("TOK",is_delimiter,_close_token,"DEL")
    machine.add("TOK",is_non_delimiter,_append_token,"TOK")
    curr_state = "INIT"
    rslt = []
    tok= ''
    for i in range(0,s.__len__()):
        input_symbol = s[i]
        action,next_state,trigger_checker = machine.search(curr_state,input_symbol)
        if(action):
            tok = action(tok,input_symbol,rslt)
        else:
            pass
        curr_state = next_state
    if(curr_state == 'INIT'):
        return([])
    elif(curr_state == 'DEL'):
        pass
    else:
        rslt.append(tok)
    return(rslt)

def parse_cookie_date(s):
    '''
        #rfc6265 Page-14 Page-15
        2. Process each date-token sequentially in the order the date-tokens appear in the cookie-date:
        
            1.  If the found-time flag is not set and the token matches thetime production, 
                set the found-time flag and set the hour value,minute-value,and second-value 
                to the numbers denoted by the digits in the date-token, respectively.  
                Skip the  remaining sub-steps and continue to the next date-token.
            2.  If the found-day-of-month flag is not set and the date-token matches the day-of-month production,
                set the found-day-of  month flag and set the day-of-month-value to the number 
                denoted by the date-token. Skip the remaining sub-steps and continue to the next date-token.
        
        3.  If the found-month flag is not set and the date-token matches the month production, 
            set the found-month flag and set the month-value to the month denoted by the date-token.  
            Skip the remaining sub-steps and continue to the next date-token.
        4.  If the found-year flag is not set and the date-token matches the year production, 
            set the found-year flag and set the year-value to the number denoted by the date-token. 
            Skip the remaining sub-steps and continue to the next date-token.
        3.  If the year-value is greater than or equal to 70 and less than or equal to 99, 
            increment the year-value by 1900.
        4.  If the year-value is greater than or equal to 0 and less than or 
            equal to 69, increment the year-value by 2000.
            1.  NOTE: Some existing user agents interpret two-digit years differently.
        5.  Abort these steps and fail to parse the cookie-date if:
            *  at least one of the found-day-of-month, found-month, found year, 
               or found-time flags is not set,
            *  the day-of-month-value is less than 1 or greater than 31,
            *  the year-value is less than 1601,
            *  the hour-value is greater than 23,
            *  the minute-value is greater than 59, or
            *  the second-value is greater than 59.
            (Note that leap seconds cannot be represented in this syntax.)
        6.  Let the parsed-cookie-date be the date whose day-of-month, month, 
            year, hour, minute, and second (in UTC) are the day-of-month value, 
            the month-value, the year-value, the hour-value, the minute-value, 
            and the second-value, respectively.  If no such date exists, 
            abort these steps and fail to parse the cookie-date.
        7.  Return the parsed-cookie-date as the result of this algorithm.
    '''
    toks = split_cookie_date_str(s)
    cookie_date_dict = {
        'found-time':False,
        'hour-value':None,
        'minute-value':None,
        'second-value': None,
        'found-day-of-month':False,
        'day-of-month-value':None,
        'found-month':False,
        'month-value':None,
        'found-year':False,
        'year-value':None,
        '_timestamp':None,
    }
    tests = ['hms-time','day-of-month','month','year']
    for tok in toks:
        if('hms-time' in tests):
            cond = CORERULES['hms-time'](tok)
            if(cond):
                tmp = tok.split(":")
                if((int(tmp[0])<0) | (int(tmp[0])>23)):
                    return(None)
                else:
                    cookie_date_dict['hour-value'] = int(tmp[0])
                if((int(tmp[1])<0) | (int(tmp[1])>59)):
                    return(None)
                else:
                    cookie_date_dict['minute-value'] = tmp[1]
                if((int(tmp[2])<0) | (int(tmp[2])>59)):
                    return(None)
                else:
                    cookie_date_dict['second-value'] = tmp[2]
                cookie_date_dict['found-time'] = True
                tests.remove('hms-time')
            else:
                pass
        elif('day-of-month' in tests):
            cond = CORERULES['day-of-month'](tok)
            if(cond):
                regex = re.compile("[0-9]{1,2}")
                tmp = regex.search(tok).group(0)
                if((int(tmp)<1) | (int(tmp)>31)):
                    return(None)
                else:
                    cookie_date_dict['day-of-month-value'] = int(tmp)
                cookie_date_dict['found-day-of-month'] = True
                tests.remove('day-of-month')
            else:
                pass
        elif('month' in tests):
            cond = CORERULES['month'](tok)
            if(cond):
                tmp = tok[0:3]
                cookie_date_dict['month-value'] = int(tmp)
                cookie_date_dict['found-month'] = True
                tests.remove('month')
            else:
                pass
        elif('year' in tests):
            cond = CORERULES['year'](tok)
            if(cond):
                regex = re.compile("[0-9]{2,4}")
                tmp = regex.search(tok).group(0)
                if((int(tmp)>=70)&(int(tmp)<=99)):
                    tmp = 1900 + int(tmp)
                elif((int(tmp)>=0)&(int(tmp)<=69)):
                    tmp = 2000 + int(tmp)
                else:
                    tmp = int(tmp)
                cookie_date_dict['year-value'] = tmp
                cookie_date_dict['found-year'] = True
                tests.remove('year')
            else:
                pass
        else:
            pass
    cookie_date_dict['_timestamp'] = nozdormu.str2ts(s)
    return(cookie_date_dict)

########################
