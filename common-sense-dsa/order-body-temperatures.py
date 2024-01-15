def order_body_temperatures(temps):
    temps_hashtable = {}
    new_temps = []

    # whole numbers to avoid floating point errors
    lower = 970
    upper = 990
    step = 1

    for t in temps:
        # return count from hashtable or 0 if no entry,
        # then add 1 and then assign back to hashtable
        temps_hashtable[t] = temps_hashtable.get(t, 0) + 1

    # iterate through possible values, which we are told are
    # in the range 97.0 to 99.0, to 1 dp, and create array
    current = lower
    while current <= upper:
        occurrences = temps_hashtable.get(current / 10.0)
        if occurrences:
            while occurrences > 0:
                new_temps.append(current / 10.0)
                occurrences -= 1

        current += step

    return new_temps


temps = [98.6, 98.0, 97.1, 99.0, 98.9, 97.8, 98.5, 98.2, 98.0, 97.1]

print(order_body_temperatures(temps))
