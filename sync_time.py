#!/usr/bin/python
# -*- coding: UTF-8 -*-

import win32api
import requests
import json
from datetime import datetime
from dateutil.parser import parse
import time

def setSystemTime():
	url = 'https://a.jd.com//ajax/queryServerData.html'
	session = requests.session()
	t0 = datetime.now()
	ret = session.get(url).text
	t1 = datetime.now()
	js = json.loads(ret)
	t = float(js["serverTime"]) / 1000
	dt = datetime.fromtimestamp(t) + ((t1 - t0) / 2)
	tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst = time.gmtime(time.mktime(dt.timetuple()))
	msec = dt.microsecond / 1000
	win32api.SetSystemTime(tm_year, tm_mon, tm_wday, tm_mday, tm_hour, tm_min, tm_sec, int(msec))


if __name__ == '__main__':
	# setSystemTime()
	expected_time = '2020-04-02 09:59:59.750'
	expected_timestamp = parse(expected_time).timestamp()
	print(expected_timestamp, time.time())
	print(time.time() > expected_timestamp)
