'''
    Engineering Economics formulae functions.

    Interest rate is assumed to be in a decimal format (1% = 0.01).
'''


from math import e


# INTEREST RATES ##############################################################

def interest_eff(nom_interest, num_compounding=12, periods=1):
    '''
        Effective interest rate.

        `num_compounding` defaults to 12 (monthly).
        `periods` defaults to 1.

        >>> i_eff = interest_eff(0.01, 12, 12)

        >>> round(i_eff, 8)
        0.01004596
    '''
    return (1 + nom_interest / num_compounding) ** periods - 1


def interest_cont(nom_interest):
    '''
        Continuous interest rate.

        >>> i_cont = interest_cont(0.1)

        >>> round(i_cont, 8)
        0.01004596
    '''
    return e ** nom_interest - 1


def interest_geo(growth, interest):
    '''
        Growth-Adjusted Interest Rate.

        >>> i_geo = interest_geo(0.05, .1)

        >>> round(i_geo, 8)
        0.01004596
    '''
    return (1 + interest) / (1 + growth) - 1


# INTEREST FACTORS ############################################################

def f_given_p(interest, periods=1):
    '''
        Compound Interest Factor.
    '''
    value = (1 + interest) ** periods
    return round7(value)


def p_given_f(interest, periods=1):
    '''
        Present Worth Factor
    '''
    value =  1 / f_given_p(interest, periods)
    return round7(value)


def f_given_a(interest, periods=1):
    '''
        Uniform Series Compound Amount Factor.
    '''
    value =  ((1 + interest) ** periods - 1) / interest
    return round7(value)


def a_given_f(interest, periods=1):
    '''
        Sinking Fund Factor.
    '''
    value =  1 / f_given_a(interest, periods)
    return round7(value)


def a_given_p(interest, periods=1):
    '''
        Capital Recovery Factor.
    '''
    value =  (interest * (1 + interest) ** periods) \
           / ((1 + interest) ** periods - 1)
    return round7(value)


def p_given_a(interest, periods=1):
    '''
        Series Present Worth Factor.
    '''
    value =  1 / a_given_p(interest, periods)
    return round7(value)


def a_given_g(interest, periods=1):
    '''
        Arithmetic Gradient to Annuity Conversion Factor.
    '''
    value =  1/interest - periods / ((1 + interest)**periods - 1)
    return round7(value)


def p_given_a_geo(growth, interest_0, periods=1):
    '''
        Geometric Gradient Series to Present Worth Conversion Factor.
    '''
    value =  p_given_a(interest_0, periods) / (1 + growth)
    return round7(value)


# SHORTHAND ALIASES ###########################################################
# INTEREST RATES
ieff  = interest_eff
icont = interest_cont
igeo  = interest_geo

# INTEREST FACTORS
fgp    = f_given_p
pgf    = p_given_f
fga    = f_given_a
agf    = a_given_f
agp    = a_given_p
pga    = p_given_a
agg    = a_given_g
pgageo = p_given_a_geo


# UTILITIES ###################################################################
def round7(value):
    return round(value, 7)


