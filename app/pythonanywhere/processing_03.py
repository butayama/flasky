def process_data(input_data):
    result = ""
    for line in input_data.split("\n"):
        if line != "":
            numbers = [float(n) for n in line.split(", ")]
            result += str(sum(numbers))
        result += "\n"
    return result
