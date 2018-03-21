#!/usr/bin/env python3

class Table():
    def __init__(self, data):
        self.data = data
        self.cols = max([len(i) for i in self.data])
        for line in self.data:
            while len(line) < self.cols:
                line.append('')
        self.lens = [max([len(item) for item in row]) for row in zip(*self.data)]

    def __str__(self):
        top = '┌' + ''.join([('─' * l) + '┬'  for l in self.lens])[:-1] + '┐'
        retval = [top]
        for line in self.data:
            retline = []
            for item, just in zip(line, self.lens):
                retline.append(item.ljust(just))
            retval.append('│' + '│'.join(retline) + '│')
        bot = '└' + ''.join([('─' * l) + '┴'  for l in self.lens])[:-1] + '┘'
        retval.append(bot)
        hed = '├' + ''.join([('─' * l) + '┼'  for l in self.lens])[:-1] + '┤'
        retval.insert(2, hed)
                

        return '\n'.join(retval)





if __name__ == '__main__':

    data = [
        ['head', 'ehitfr', 'head-3-htfirf', 'h', 'tf'],
        ['line1-trio', 'line-1-col-2', 'eshi', 'line-1-col-4', 'tfe'],
        ['rtftf', 'line-2-col-2', 'thri', 'line-2-col-4']
    ]


    t = Table(data)

    print(t)
