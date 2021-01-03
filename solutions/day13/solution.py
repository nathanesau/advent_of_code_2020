def solution_1(ts, stops):
    closest_stop, closest_stop_ts = None, None
    for stop in stops:
        if stop == 'x':
            continue
        stop = int(stop)
        stop_ts = ts + (stop - ts % stop)
        if closest_stop_ts is None or (stop_ts - ts) < (closest_stop_ts - ts):
            closest_stop, closest_stop_ts = stop, stop_ts
    return (closest_stop_ts - ts) * closest_stop


def solution_2(stops):
    base_ts = 0
    step = 1
    for index, stop in enumerate(stops):
        if stop == 'x':
            continue
        stop = int(stop)
        ts = base_ts
        while True:
            if (ts + index) % stop == 0:
                base_ts = ts
                step *= stop
                break
            ts += step
    return ts
