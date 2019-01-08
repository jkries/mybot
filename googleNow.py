#! /usr/bin/python3

try:
	from googlesearch import search
except ImportError:
	print("No module named 'google' found")

# to search
#query = "Jason Kries"

def tryGoogle(query):
	searchCount = 0
	for j in search(query, tld="co.in", num=1, stop=1, pause=2):
		if searchCount == 0:
			print("<br>Try this from my friend Google: <a target='_blank' href='" + j + "'>" + query + "</a>")
			return "<br>Try this from my friend Google: <a target='_blank' href='" + j + "'>" + query + "</a>"
