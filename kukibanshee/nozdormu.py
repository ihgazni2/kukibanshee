import re
import time
import datetime
from kukibanshee import araq


def detect_time_fmt(date_value,**kwargs):
    '''
        ####################HTTP-date###############
        # HTTP-date    = rfc1123-date | rfc850-date | asctime-date
               # rfc1123-date = wkday "," SP date1 SP time SP "GMT"
               # rfc850-date  = weekday "," SP date2 SP time SP "GMT"
               # asctime-date = wkday SP date3 SP time SP 4DIGIT
               # date1        = 2DIGIT SP month SP 4DIGIT
                              # ; day month year (e.g., 02 Jun 1982)
               # date2        = 2DIGIT "-" month "-" 2DIGIT
                              # ; day-month-year (e.g., 02-Jun-82)
               # date3        = month SP ( 2DIGIT | ( SP 1DIGIT ))
                              # ; month day (e.g., Jun  2)
               # time         = 2DIGIT ":" 2DIGIT ":" 2DIGIT
                              # ; 00:00:00 - 23:59:59
               # wkday        = "Mon" | "Tue" | "Wed"
                            # | "Thu" | "Fri" | "Sat" | "Sun"
               # weekday      = "Monday" | "Tuesday" | "Wednesday"
                            # | "Thursday" | "Friday" | "Saturday" | "Sunday"
    '''
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = "strict"
    month = 'Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec'
    weekday = 'Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday'
    wkday = 'Mon|Tue|Wed|Thu|Fri|Sat|Sun'
    rfc1123 = ''.join(("(",wkday,")",", ","[0-9]{2} ","(",month,")"," [0-9]{4} ","[0-9]{2}:[0-9]{2}:[0-9]{2} ","GMT"))
    rfc1123 = "^" + rfc1123 + "$"
    regex_rfc1123 = re.compile(rfc1123)
    ####
    rfc1123_tzoffset = ''.join(("(",wkday,")",", ","[0-9]{2} ","(",month,")"," [0-9]{4} ","[0-9]{2}:[0-9]{2}:[0-9]{2} ","[\+\-][0-9]{4}"))
    rfc1123_tzoffset = "^" + rfc1123_tzoffset + "$"
    regex_rfc1123_tzoffset = re.compile(rfc1123_tzoffset)
    ####
    rfc1123_hypen = ''.join(("(",wkday,")",", ","[0-9]{2}-","(",month,")","-[0-9]{4} ","[0-9]{2}:[0-9]{2}:[0-9]{2} ","GMT"))
    regex_rfc1123_hypen = "^" + rfc1123_hypen + "$"
    regex_rfc1123_hypen = re.compile(rfc1123_hypen)
    rfc850 = ''.join(("(",weekday,")",", ","[0-9]{2}-","(",month,")","-[0-9]{2} ","[0-9]{2}:[0-9]{2}:[0-9]{2} ","GMT"))
    regex_rfc850 = "^" + rfc850 + "$"
    regex_rfc850 = re.compile(rfc850)
    rfc850_a = ''.join(("(",wkday,")",", ","[0-9]{2}-","(",month,")","-[0-9]{2} ","[0-9]{2}:[0-9]{2}:[0-9]{2} ","GMT"))
    regex_rfc850_a = "^" + rfc850_a + "$"
    regex_rfc850_a = re.compile(rfc850_a)
    asctime = ''.join(("(",wkday,")"," ","(",month,")","(( [0-9]{2})|(  [0-9]{1}))"," ","[0-9]{2}:[0-9]{2}:[0-9]{2} ","[0-9]{4}"))
    regex_asctime = "^" + asctime + "$"
    regex_asctime = re.compile(asctime)
    if(mode == 'strict'):
        if(araq._real_dollar(date_value,regex_rfc1123)):
            return('rfc1123')
        elif(araq._real_dollar(date_value,regex_rfc1123_tzoffset)):
            return('rfc1123_tzoffset')
        elif(araq._real_dollar(date_value,regex_rfc1123_hypen)):
            return('rfc1123_hypen')
        elif(araq._real_dollar(date_value,regex_rfc850)):
            return('rfc850')
        elif(araq._real_dollar(date_value,regex_rfc850_a)):
            return('rfc850_a')
        elif(araq._real_dollar(date_value,regex_asctime)):
            return('asctime')
        else:
            return(None)
    else:
        if(regex_rfc1123.search(date_value)):
            return('rfc1123')
        if(regex_rfc1123_tzoffset.search(date_value)):
            return('rfc1123_tzoffset')
        elif(regex_rfc1123_hypen.search(date_value)):
            return('rfc1123_hypen')
        elif(regex_rfc850.search(date_value)):
            return('rfc850')
        elif(regex_rfc850_a.search(date_value)):
            return('rfc850_a')
        elif(regex_asctime.search(date_value)):
            return('asctime')
        else:
            return(None)

        


TIMEFMT = {
    'rfc1123':'%a, %d %b %Y %H:%M:%S GMT',
    'rfc1123_tzoffset':'%a, %d %b %Y %H:%M:%S %z',
    'rfc1123_hypen':'%a, %d-%b-%Y %H:%M:%S GMT',
    'rfc850':'%A, %d-%b-%y %H:%M:%S GMT',
    'rfc850_a':'%a, %d-%b-%y %H:%M:%S GMT',
    'asctime':'%a, %b %d %H:%M:%S %Y',
    '%a, %d %b %Y %H:%M:%S GMT':'rfc1123',
    '%a, %d %b %Y %H:%M:%S %z':'rfc1123_tzoffset',
    '%a, %d-%b-%Y %H:%M:%S GMT':'rfc1123_hypen',
    '%A, %d-%b-%y %H:%M:%S GMT':'rfc850',
    '%a, %d-%b-%y %H:%M:%S GMT':'rfc850_a',
    '%a, %b %d %H:%M:%S %Y':'asctime'
}


def format_asc(asc):
    asc = asc.replace("  "," 0")
    return(asc)

def standlize(s):
    regex = re.compile("[\s]+")
    s = re.sub(regex," ",s)
    return(s)


    


def get_fmt_name(fmt):
    return(TIMEFMT[fmt])


def ts2dt(ts):
    '''
        only 6 bits keeped
    '''
    return(datetime.datetime.fromtimestamp(ts))

def dt2ts(dt,**kwargs):
    ''''''
    return(dt.timestamp())

def str2dt(s,**kwargs):
    if('fmt' in kwargs):
        fmt = kwargs['fmt']
    else:
        fmt_name = detect_time_fmt(s)
        fmt = TIMEFMT[fmt_name]
    if(fmt == 'asctime'):
        s = fmt_asc(s)
    else:
        s = standlize(s)
    return(datetime.datetime.strptime(s,fmt))

def dt2str(dt,**kwargs):
    if('fmt' in kwargs):
        fmt = kwargs['fmt']
    elif('fmt_name' in kwargs):
        fmt_name = kwargs['fmt_name']
        fmt = TIMEFMT[fmt_name]
    else:
        fmt = TIMEFMT['rfc1123']
    return(dt.strftime(fmt))

def str2ts(s,**kwargs):
    if('fmt' in kwargs):
        fmt = kwargs['fmt']
    else:
        fmt_name = detect_time_fmt(s)
        fmt = TIMEFMT[fmt_name]
    dt = str2dt(s,fmt=fmt)
    ts = dt2ts(dt)
    return(ts)


def ts2str(ts,**kwargs):
    dt = ts2dt(ts)
    if('fmt' in kwargs):
        fmt = kwargs['fmt']
    elif('fmt_name' in kwargs):
        fmt_name = kwargs['fmt_name']
        fmt = TIMEFMT[fmt_name]
    else:
        fmt = TIMEFMT['rfc1123']
    return(dt.strftime(fmt))

