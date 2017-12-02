def creat_para(cf,ct,af):
    '''create the parameter the url needs'''
    af=str(af) ###convert af to str###
    s='http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+cf+'&to='+ct+'&amt='+af
    return s
    ###add all parts together###
def get_str(s):
    '''obtain the url result str b '''
    from urllib.request import urlopen
    l = urlopen(s)
    a = l.read()
    l.close()
    b = a.decode('ascii')
    return b
def dispose_str(b):
    ''' extract what we want from the str we get'''
    i=-1
    while not(b[i].isdigit()):
        i+=-1
    ### identify the index of the rightest digit###
    j=-1
    while b[j]!='.':
        j+=-1
    ###identify the index of the rightest '.'###
    j+=-1
    while b[j].isdigit():
        j+=-1
    ###count the digits appearing continuously on the left of the '.'###
    return float(b[j+1:i+1])###slice the result and convert it to float###
def exchange(cf,ct,af):
    """input Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    input Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    input Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float

    The value returned has type float."""
    return dispose_str(get_str(creat_para(cf,ct,af)))
    ### directly use the function i designed###
def test_creat_para():
    '''test whether creat_para works'''
    assert(creat_para('CNY','EUR',17)=='http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=CNY&to=EUR&amt=17')
    assert(creat_para('CNY','USD',125)=='http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=CNY&to=USD&amt=125')
    assert(creat_para('USD','EUR',233)=='http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=EUR&amt=233')
    assert(creat_para('USD','EUR',21)=='http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=EUR&amt=21')
def test_dispose_str():
    '''test whether dispose_str works'''
    assert(dispose_str('udfhsy33nefh2s2uyrfh2323,juhufhsbcu2.3333 !"?ehbc"')==2.3333)
    assert(dispose_str('arfh7384y83efjrf[p][pijernv89urnfv ""??22.222!@#@!@')==22.222)
    assert(dispose_str('sfbsrfuba3278yr7346*&*@#^*&hfbuv?:::<>23673  : 290.0dcre')==290.0)
    assert(dispose_str('duhrferf8h23ue9ufr8f!@&^^@*#*&@**#ysdbfrb uhur<>?>> hyfh250.250!#@!bbfc syhf')==250.250)
def test_exchange():
    assert(exchange('USD','CNY',2.5)==16.315375)
    assert(exchange('EUR','CNY',233)==1814.3443762342)
    assert(exchange('CNY','USD',250)==38.307424745064)
    assert(exchange('CNY','EUR',290)==37.242102924389)
def test_all():
    '''test whether all fuctions works successfully, but i cannot test get_str, because this is not designed by me '''
    test_creat_para()
    test_dispose_str()
    test_exchange()
    print('all test passed!')

