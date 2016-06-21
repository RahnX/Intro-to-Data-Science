import datetime

def reformat_subway_dates(date):
	'''
	The dates in our subway data are formatted in the format month-day-year.
	The dates in our weather underground data are formatted year-month-day.

	In order to join these two data sets together, we'll want the dates formatted
	the same way.  Write a function that takes as its input a date in the MTA Subway
	data format, and returns a date in the weather underground format.

	Hint:
	There are a couple of useful functions in the datetime library that will
	help on this assignment, called strptime and strftime.
	More info can be seen here and further in the documentation section:
	http://docs.python.org/2/library/datetime.html#datetime.datetime.strptime
	'''
	date = str.split(date, "-")
	date = map(int, date)

	date_formatted = datetime.date(2000+date[2], date[0], date[1])
	return date_formatted

if __name__ == '__main__':
	print reformat_subway_dates("03-21-10")
	print reformat_subway_dates("06-18-16")