def donation_analysis(d):
    totall = 0
    person = ''
    count = 0
    max_donation = -1

    for name, value in d.items():
        if value > max_donation:
            max_donation = value
            person = name
        totall += value
        count += 1
        average = totall // count
    return totall, average, person

donations = donation_analysis({
    'asal': 30,
    'saman': 20,
    'yasna': 15
})

print(donations)
