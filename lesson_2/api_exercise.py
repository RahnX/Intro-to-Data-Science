import json
import requests

def api_get_request(url):
	# In this exercise, you want to call the last.fm API to get a list of the
	# top artists in Spain. The grader will supply the URL as an argument to
	# the function; you do not need to construct the address or call this
	# function in your grader submission.
	#
	# Once you've done this, return the name of the number 1 top artist in
	# Spain.
	data = requests.get(url).text
	data = json.loads(data)

	return data["topartists"]["artist"][0]["name"] # return the top artist in Spain

if __name__ == '__main__':
	api_key     = "cb04517f697169bf3a5220caaccea6f9"
	last_fm_url = "http://ws.audioscrobbler.com//2.0/?method=geo.gettopartists&country=spain&api_key={}&format=json".format(api_key)

	print api_get_request(last_fm_url)