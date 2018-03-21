#!/usr/bin/env python3

class Table():
    def __init__(self, data, header = None, datajust = 'l', headerjust = 'l'):
        self.data = data
        self.header = bool(header)
        if header:
            self.data.insert(0, header)

        self.cols = max([len(i) for i in self.data])
        for line in self.data:
            while len(line) < self.cols:
                line.append('')

        if isinstance(datajust, str):
            self.datajust = [datajust for i in range(self.cols)]
        else:
            assert(len(datajust) == self.cols)
            self.datajust = datajust

        if isinstance(headerjust, str):
            self.headerjust = [headerjust for i in range(self.cols)]
        else:
            assert(len(headerjust) == self.cols)
            self.headerjust = headerjust
        
        assert(all([i in ['l', 'r', 'c'] for i in self.datajust]))
        assert(all([i in ['l', 'r', 'c'] for i in self.headerjust]))
            
        self.lens = [max([len(item) for item in row]) for row in zip(*self.data)]

    def join(self, ch, parts):
        ret = ''
        for idx, part in enumerate(parts):
            ret += str(part)
            if idx < len(parts) - 1:
                ret += str(ch)
            
        return ret
    def just(self, txt, width, justtype):
        if justtype == 'l':
            return txt.ljust(width)
        elif justtype == 'r':
            return txt.rjust(width)
        elif justtype == 'c':
            return txt.center(width)
                
    def __str__(self):


        pre = '\x1b[2;38;48m'
        post = '\x1b[0m'
        top = pre + '┌' + self.join('', [('─' * (l + 2)) + '┬'  for l in self.lens])[:-1] + '┐' + post
        retval = [top]

        bar = pre + '│' + post
        hyphen = pre + '─' + post

        
        if self.header:
            retline = []
            for title, width, just in zip(data[0], self.lens, self.headerjust):
                retline.append(' ' + str(self.just(title, width, just)) + ' ')
            retval.append(bar + self.join(bar, retline) + bar)
                
        for line in self.data[1:] if self.header else self.data:
            retline = []
            for item, width, just in zip(line, self.lens, self.datajust):
                retline.append(' ' + str(self.just(item, width, just)) + ' ')
            retval.append(bar + self.join(bar, retline) + bar)
        bot = pre + '└' + self.join('', [('─' * (l + 2)) + '┴'  for l in self.lens])[:-1] + '┘' + post
        retval.append(bot)
        hed = pre + '├' + self.join('', [('─' * (l + 2)) + '┼'  for l in self.lens])[:-1] + '┤' + post
        retval.insert(2, hed)
                

        return self.join('\n', retval)





if __name__ == '__main__':

    data = [
        ['line1-trio', 'line-1-col-2', 'eshi', 'line-1-col-4', 'tfe'],
        ['rtftf', 'line-2-col-2', 'thri', 'line-2-col-4']
    ]

    header = ['head', 'ehitfr', 'head-3-htfirf', 'h', 'tf']

    t = Table(data, header, 'c', ['r', 'r', 'c', 'l', 'r'])

    print(t)
