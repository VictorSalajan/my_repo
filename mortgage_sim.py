import pylab as plt
import numpy as np

def total_rent(wait_years, rent=300, rate=0.05):
    """ Given current rent, annual rate of increase & wait_years,
    returns total money spent on rent """
    total_rent = 0
    for i in range(1, wait_years * 12 + 1):
        if (i-1) % 12 == 0 and i != 1:
            rent *= (1 + rate)
        total_rent += rent
    return total_rent

def flat_price(wait_years, rate, price=130000):
    """ Given current flat price & annual rate of increase (computed monthly),
    returns flat price after wait_years """
    monthly_rate = rate / 12
    for i in range(wait_years * 12):
        price *= (1 + monthly_rate)
    return price

def downpayment(wait_years, savings, current_downpayment=20000):
    """ Returns money saved for downpayment after wait_years,
        starting from current_downpayment. 
        downpayment increments monthly by 'savings' amount"""
    downpayment_now = current_downpayment
    downpayment_later = current_downpayment
    for i in range(wait_years * 12):
        downpayment_later += savings
    return downpayment_now, downpayment_later

def monthlymortgage(mortgage, years, interest=0.05):
    months = years * 12
    interest_monthly = interest / 12
    numerator = interest_monthly * ((1 + interest_monthly) ** months)
    denominator = (1 + interest_monthly) ** months - 1
    payment = float("{0:.2f}".format(mortgage * numerator / denominator))
    return payment

def mortgage_sim(wait_years, years, rate, savings, price=130000):
    """
    Assumes minimum downpayment = 15%
    invest_now - money spent on flat if buying flat now. Computed only if downpayment sufficient.
    invest_later - money spent on flat & rent while saving for a bigger downpayment.
    """
    # Invest Now
    downpayment_now = downpayment(wait_years, savings)[0]
    percent_downpay = downpayment_now / price
    if percent_downpay < 0.15:
        return f'{percent_downpay}% downpayment is less than the minimum of 15%' 
    mortgage = price - downpayment_now
    monthly = monthlymortgage(mortgage, years)
    invest_now = monthly * years * 12 + downpayment_now

    # Invest Later
    downpayment_later = downpayment(wait_years, savings)[1]
    percent_downpay = downpayment_later / price
    price = flat_price(wait_years, rate)
    if downpayment_later / price < 0.15:
        return f'{percent_downpay}% downpayment is less than the minimum of 15%'
    mortgage = price - downpayment_later
    rent = total_rent(wait_years)
    monthly = monthlymortgage(mortgage, years)
    invest_later = monthly * years * 12 + downpayment_later + rent

    return invest_now, invest_later

def display_sim(wait_years, years, rate, savings):
    try:
        invest_now, invest_later = mortgage_sim(wait_years, years, rate, savings)
    except ValueError:
        return f'Could not compute simulation. Downpayment insufficient.'
    
    compare = 'more' if invest_later > invest_now else 'less'
    if invest_later == invest_now:
        compare = 'the same amount'
    
    return f'Investing now will have a total cost of: {int(invest_now)}' + '\n' \
           f'Investing after {wait_years} years will have a total cost of: {int(invest_later)}' + '\n' \
           f'You will pay {int(abs(invest_later - invest_now))} {compare} if you wait {wait_years} years\n'

savings = 1500
for rate in (0.01, 0.03, 0.05):
    for wait in (1, 2):
        for years in (10, 30):
            print(f'wait_years: {wait}     flat price annual increase rate: {rate}     mortgage_years: {years}' + '\n' \
                f'{(display_sim(wait, years, rate, savings))}')
print()


def list_positive_wait_scenarios():
    """ Simulation of circumstances in which waiting is gainful,
        by varying values of relevant parameters: rate, monthly, wait_years, mortgage_years """
    positives = []
    for rate in np.arange(0.01, 0.08, 0.01):
        for savings in range(800, 1600, 200):
            for wait in range(1, 4):
                for years in range(10, 35, 5):
                    try:
                        difference = mortgage_sim(wait, years, rate, savings)[0] - mortgage_sim(wait, years, rate, savings)[1]
                    except TypeError:
                        print('Could not compute difference. Downpayment insufficient. Use more realistic parameters.')
                        continue
                    if difference > 0:
                        positives.append([int(difference), rate, savings, wait, years])
    positives.sort(reverse=True, key = lambda x: x[0])
#    only gains of over 3000
    positives = [sublist for sublist in positives if sublist[0] > 3000]
    
    print('What are the best circumstances?\n')
    for el in positives:
        print(f'{el[0]} saved when price increase rate = {el[1]}, savings = {el[2]}, ' + \
              f'wait_years = {el[3]}, mortgage_years = {el[4]}\n')
        cont = input("Press 'q' to exit program or any other key to continue ")
        if cont == 'q':
            break

list_positive_wait_scenarios()
