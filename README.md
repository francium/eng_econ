# ENGINEERING ECONOMICS FORMULAS LIBRARY

## Included formulas
- Effective interest Rate: `interest_eff`, `ieff` (shorthand alias)
- Continuous interest Rate: `interest_cont`, `icont`
- Growth-Adjusted Interest Rate: `interest_geo`, `igeo`
- Compound Interest Factor (F/P,i,N): `f_given_p`, `fgp`
- Present Worth Factor (P/F,i,N): `p_given_f`, `pgf`
- Uniform Series Compound Amount Factor: `f_given_a`, `fga`
- Sinking Fund Factor: `a_given_f`, `agf`
- Capital Recovery Factor: `a_given_p`, `agp`
- Series Present Worth Factor: `p_given_a`, `pga`
- Arithmetic Gradient to Annuity Conversion Factor: `a_given_g`, `agg`
- Geometric Gradient Series to Present Worth Conversion Factor: `p_given_a_geo`, `pgageo`

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
