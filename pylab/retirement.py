import matplotlib.pylab as plt


def retire(monthly, rate, terms):
    savings = [0]
    base = [0]
    mRate = rate/12
    for i in range(1, terms + 1):
        base += [i]
        savings += [savings[-1] * (1 + mRate) + monthly]
    return base, savings

# Display range of growth as the monthly component changes
def DisplayRetireWithMonthlies(monthlies, rate, terms):
    plt.figure(f'Retire by Monthlies. Interest rate: {rate}')
    plt.xlabel('Nr of months')
    plt.ylabel('Accrued Savings')
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms)
        plt.plot(xvals, yvals,
                 label = f'Retire: {str(monthly)}$')
        plt.legend(loc = 'upper left')
    plt.show()

DisplayRetireWithMonthlies([500, 600, 700, 800, 900, 1000, 1100], 0.05, 40 * 12)

# Display range of growth as the rate of growth (interest) changes
def DisplayRetireWithRates(month, rates, terms):
    plt.figure(f'Retire by Rate of Growth. Monthly Savings: {month}')
    plt.xlabel('Nr of months')
    plt.ylabel('Accrued Savings')
    for rate in rates:
        xvals, yvals = retire(month, rate, terms)
        plt.plot(xvals, yvals,
                 label = f'Retire: {str(month)}$   {int(rate*100)}% / y')
        plt.legend(loc = 'upper left')
    plt.show()

DisplayRetireWithRates(800 ,[.03, .05, .07] ,40 * 12)

# Display range of growth as both the rate of growth & monthly contribution change
def DisplayRetireWithMonthliesAndRates(monthlies, rates, terms):
    plt.figure('Retire by Monthlies and Rates of Growth')
    plt.xlim(30 * 12, 40 * 12)
    plt.xlabel('Nr of months')
    plt.ylabel('Accrued Savings')
    for month in monthlies:
        for rate in rates:
            xvals, yvals = retire(month, rate, terms)
            plt.plot(xvals, yvals, 
                     label = f'Retire: {str(month)}$   {int(rate*100)}% / y')
            plt.legend(loc = 'upper left')
    plt.show()

DisplayRetireWithMonthliesAndRates([500, 700, 900, 1100], [.03, .05, .07], 40 * 12)

# BETTER Display range of growth as both the rate of growth & monthly contribution change
def DisplayRetireWithMonthliesAndRates2(monthlies, rates, terms):
    plt.figure('Retire by Monthlies and Rates of Growth - Improved')
    plt.xlim(30 * 12, 40 * 12)
    plt.xlabel('Nr of months')
    plt.ylabel('Accrued Savings')
    monthLabels = ['m', 'r', 'y', 'g']
    rateLabels = ['-', '--', '^']
    for i in range(len(monthlies)):
        monthly = monthlies[i]
        monthLabel = monthLabels[i % len(monthLabels)]
        for j in range(len(rates)):
            rate = rates[j]
            rateLabel = rateLabels[i % len(rateLabels)]
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals,
                     monthLabel + rateLabel,
                     label = f'Retire: {str(monthly)}$   {int(rate * 100)}% / y')
            plt.legend(loc = 'upper left')
    plt.show()

DisplayRetireWithMonthliesAndRates2([500, 700, 900, 1100], [.03, .05, .07], 40 * 12)
