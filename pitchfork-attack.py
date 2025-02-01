# Emulates a "Pitchfork attack" from Burp's Intruder tool.
import urllib
def queueRequests(target, wordlists):
	engine = RequestEngine(endpoint=target.endpoint,
							concurrentConnections=5,
							requestsPerConnection=100,
							pipeline=False
							)

	# This is just an example of how to use a list as a payload set.
	usernames = ["root", "admin", "administrator", "user", "test", "support", "guest"]

	# If you want to use multiple files as payload sets, you can use multiple
	# open calls in a with statement.
	with open('/path/to/wordlist.txt', 'r') as file1:
		# The zip function combines multiple iterators into one which generates a
		# tuple containing one item from each iterator. You can either extract these
		# items from the tuple directly or cast them to variables (as done here) in
		# the for loop itself.
		for payload1, payload2, payload3 in zip(file1, usernames, range(0, 10)):
			payload1 = urllib.quote(payload1.rstrip('\r\n'))

			# rstrip('\r\n') not used here because all values came from the usernames list.
			# Adjust accordingly if reading from a file.
			payload2 = urllib.quote(payload2)

			# str() is required here because the range() function used for payload3
			# generates integers and Turbo Intruder expects payloads to be strings.
			payload3 = urllib.quote(str(payload3))

			# Pass in a list of each payload to the engine.queue function.
			engine.queue(target.req, [payload1, payload2, payload3])

def handleResponse(req, interesting):
	# currently available attributes are req.status, req.wordcount, req.length and req.response
	if req.status != 404:
		table.add(req)