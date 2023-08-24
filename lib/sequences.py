def print_fibonacii(length):
    pass
    if length == 0:
        fibonacii_sequence = []
    elif length == 1:
        fibonacii_sequence = [0]
    else:
        fibonacii_sequence = [0, 1]

        while len(fibonacii_sequence) < length:
            next_fibonacii = fibonacii_sequence[-1] + fibonacii_sequence[-2]
            fibonacii_sequence.append(next_fibonacii)    

    print(fibonacii_sequence)          