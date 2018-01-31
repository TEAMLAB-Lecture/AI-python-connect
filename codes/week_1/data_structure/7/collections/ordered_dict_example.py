from collections import OrderedDict

d = {}
d['x'] = 100
d['y'] = 200
d['z'] = 300
d['l'] = 500

for k, v in d.items():
    print(k, v)


d = OrderedDict()
d['x'] = 100
d['y'] = 200
d['z'] = 300
d['l'] = 500

for k, v in d.items():
    print(k, v)

for k, v in OrderedDict(sorted(d.items(), key=lambda t: t[0])).items():
    print(k, v)

for k, v in OrderedDict(sorted(d.items(),
                        reverse=True, key=lambda t: t[1])).items():
    print(k, v)
