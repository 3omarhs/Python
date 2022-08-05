import pygeoip
gip = pygeoip.GeoIP("C:\\Users\\omarh\\Desktop\\GeoLiteCity.dat")
res = gip.record_by_addr('135.247.41.59')
for key, val in res.items():
    print('%s : %s' % (key, val))