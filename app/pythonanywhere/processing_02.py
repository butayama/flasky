import statistics


def calculate_mode(number_list):
    try:
        return "The mode of the numbers is {}".format(statistics.mode(number_list))
    except statistics.StatisticsError as exc:
        return "Error calculating mode: {}".format(exc)
