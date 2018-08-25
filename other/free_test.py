class Time60(object):
    def __init__(self, hr=0, min=0):
        if isinstance(hr, str):
            tmp = hr.split(':')
            self.hr = int(tmp[0])
            self.min = int(tmp[1])
        else:
            self.hr = hr
            self.min = min

    def __str__(self):
        return "%02d:%02d" % (self.hr, self.min)

    def __repr__(self):
        return repr("%02d:%02d" % (self.hr, self.min))

    def __add__(self, other):
        hr = self.hr + other.hr
        min = self.min + other.min
        ahr = min // 60
        min %= 60
        hr += ahr
        return self.__class__(hr, min)

    def __iadd__(self, other):
        self.hr += other.hr
        self.min += other.min
        return self


if __name__ == '__main__':
    print(Time60())
    print(Time60(**{'hr': 10, 'min': 30}))
    t1 = Time60(10, 30)
    t1 += Time60('12:35')
    print(t1)
    print(Time60(10, 30) + Time60(8, 45))
