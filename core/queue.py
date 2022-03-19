from os import environ
from operation import equalSelect,selectOLW
def get_userid():
    if 'HTTP_COOKIE' in environ.keys():
        for cookie in map(str.strip, environ['HTTP_COOKIE'].split(';')):
            (key, value ) = cookie.split('=');
            if key == "token":
                r=equalSelect([['token',"'"+value+"'"]],'sessions')
                if(r):
                    try:
                        return r[0][0]
                    except:
                        return False
                else:
                    return False
    else:
        return False
def get_lastid():
    a=selectOLW('t DESC',1,f"lender={get_userid()}",'agreements')
    return a[0]
