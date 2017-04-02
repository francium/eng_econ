# Engineering Economics Formula Library


## Included formulas
| Formula Name                                                 | Function Name, Shorthand Alias |
|--------------------------------------------------------------|--------------------------------|
| Effective interest Rate                                      | `interest_eff`, `ieff`         |
| Continuous interest Rate                                     | `interest_cont`, `icont`       |
| Growth-Adjusted Interest Rate                                | `interest_geo`, `igeo`         |
| Compound Interest Factor (F/P,i,N)                           | `f_given_p`, `fgp`             |
| Present Worth Factor (P/F,i,N)                               | `p_given_f`, `pgf`             |
| Uniform Series Compound Amount Factor                        | `f_given_a`, `fga`             |
| Sinking Fund Factor                                          | `a_given_f`, `agf`             |
| Capital Recovery Factor                                      | `a_given_p`, `agp`             |
| Series Present Worth Factor                                  | `p_given_a`, `pga`             |
| Arithmetic Gradient to Annuity Conversion Factor             | `a_given_g`, `agg`             |
| Geometric Gradient Series to Present Worth Conversion Factor | `p_given_a_geo`, `pgageo`      |


## Usage
Get source.

    $ git clone https://github.com/francium/eng_econ.git

Launch python from same parent directory (folder) as the `eng_econ` repo we
just cloned. Otherwise, you won't be able to import `eng_econ`.

    $ python3
    >>> import eng_econ as econ
    >>> econ.fga(.01, 12)
    12.682503
    >>> 123 * pga(0.03, 12) + 4002.43 * pgf(0.03, 12)
    4031.566272957


## API

### Description
- Interest rate is assumed to be in a decimal format (1% = 0.01).


## Functions

### Interest Rate
Effective interest rate.

    interest_eff(nom_interest, num_compounding=12, periods=1)

    'num_compounding' is in months.


Continuous interest rate.

    interest_cont(nom_interest)


Growth-Adjusted Interest Rate.

    interest_geo(growth, interest)


### Interest Factors
Compound Interest Factor.

    f_given_p(interest, periods=1)


Present Worth Factor

    p_given_f(interest, periods=1)


Uniform Series Compound Amount Factor.

    f_given_a(interest, periods=1)


Sinking Fund Factor.

    a_given_f(interest, periods=1)


Capital Recovery Factor.

    a_given_p(interest, periods=1)


Series Present Worth Factor.

    p_given_a(interest, periods=1)


Arithmetic Gradient to Annuity Conversion Factor.

    a_given_g(interest, periods=1)


Geometric Gradient Series to Present Worth Conversion Factor.

    p_given_a_geo(growth, interest_0, periods=1)
