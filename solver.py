#!/usr/bin/python

def likeness(lhs, rhs):
    return sum(map(str.__eq__, lhs, rhs))


def average_likeness(e1, all):
    others = filter(lambda e2: e2 is not e1, all)
    return sum(map(lambda e2: likeness(e1, e2), others)) / max(1, len(all) - 1)


def advice(input):
    apriori = list(filter(lambda o: o[1] is not None, input))
    if len(apriori) is not 0:
        return _advice_filter(input, apriori)
    else:
        return _advice_average(list(map(lambda o: o[0], input)))


def _advice_filter(input, apriori):
    options = list(map(lambda o: o[0], filter(lambda o: o[1] is None, input)))
    for a  in apriori:
        options = list(filter(lambda o: likeness(a[0], o) == a[1], options))

    return _advice_average(options)


def _advice_average(options):
    avgs = list(map(lambda opt: (opt, average_likeness(opt, options)), options))
    avgs.sort(key=lambda o: o[1], reverse=True)

    result = '\n '.join(map(lambda v: '{} : {:.3f}'.format(*v), avgs))
    return 'average likenesses (try the highest):\n ' + result


if __name__ == '__main__':
    from sys import argv, exit
    if len(argv) < 2:
        print('usage: python solver.py WORD[,LIKENESS] ...')
        exit(1)

    def parse(word):
        split = word.split(',')
        if len(split) is 1:
            return (word, None)
        else:
            return (split[0], int(split[1]))
          
    print(advice(list(map(parse, argv[1:]))))
