# Emulates a "Battering ram attack" from Burp's Intruder tool.
import urllib
def queueRequests(target, wordlists):
	engine = RequestEngine(endpoint=target.endpoint,
							concurrentConnections=5,
							requestsPerConnection=100,
							pipeline=False
							)

	# Adjust the payloads list to match the number of payload positions
	# you have configured. Values are irrelevant since every position
	# is replaced by a payload.
	payloads = ["1", "2", "3"]

	# Change the path to the wordlist or replace it with some other iterator.
	# Note the rest of the code assumes payloads are strings and need to be URL encoded.
	for payload in open('/path/to/wordlist.txt'):
		for i in range(len(payloads)):
			payloads[i] = urllib.quote(payload.rstrip('\r\n'))
		engine.queue(target.req, payloads)

def handleResponse(req, interesting):
	# currently available attributes are req.status, req.wordcount, req.length and req.response
	if req.status != 404:
		table.add(req)