import random, time, pylab as plt
random.seed(0)

def COVID_Transmission(n, social_distancing, sim_days=30):
    """ 
    Assumes every infected person transmits to a fixed nr of people every 5 days 
    n: nr of starting cases for simulation (input: int)
    social_distancing: transmission rate with/without social distancing (input: 'Yes' or 'No')
    Returns new cases & total number of infected people for 30 days
    """
    new_cases = {1: n}
    total_infected = {1: n}

    day = 0
    while day < sim_days:
        day += 1
        if day <= 5:
            max_new_cases = new_cases[day] * social_distancing
            for day in range(2, 6):
                new_cases[day] = random.uniform(0, max_new_cases)
                max_new_cases -= new_cases[day]
                total_infected[day] = list(total_infected.values())[-1] + new_cases[day]
        else:
            new_cases[day] = new_cases[day - 4] * social_distancing
            total_infected[day] = list(total_infected.values())[-1] + new_cases[day]

    return new_cases, total_infected

n = int(input('Current cases: '))
social_distancing = input("Social Distancing ('y' or 'n'): ")

def display_timed_transmission(n, social_distancing):
    if social_distancing == 'n':
        social_distancing = 2.5
        print('Default Scenario:'.center(60), '\n')
    elif social_distancing == 'y':
        social_distancing = 1.25
        print('Social Distancing Scenario:'.center(60), '\n')

    new_cases, total_infected = COVID_Transmission(n, social_distancing)
    report = zip(new_cases.items(), total_infected.values())
    for daily, total in report:
        cases = round(daily[1]) if daily[1] < 2.5 else int(daily[1])
        total = round(total) if total < 2.5 else int(total)
        day = str(daily[0]).ljust(len(daily), ' ')
        print(f'Day: {day} --> {cases}'.ljust(20, ' '), end='')
        print(f'Total infected: {total}'.ljust(12))
        time.sleep(0.15)

display_timed_transmission(n, social_distancing)

def display_plots(starting_cases, transmission_rates):
    """ A plot showing the progression of the total number of infected people,
        as a function of transmission rate """
    plt.figure('COVID Transmission Plots')
    plt.title('Total Number of Infected people by Transmission Rate')
    for rate in transmission_rates:
        new_cases, total_infected = COVID_Transmission(starting_cases, rate)
        plt.plot(list(total_infected.keys()), list(total_infected.values()), label=rate)
        plt.xlabel('Days')
        plt.ylabel('Total number of cases')
        plt.legend()
    plt.show()

starting_cases = 1000
transmission_rates = [0.5, 0.9, 1, 1.1, 1.25]
display_plots(starting_cases, transmission_rates)
