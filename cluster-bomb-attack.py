# Emulates a "Cluster bomb attack" from Burp's Intruder tool.
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
	with open('C:/Users/tib3rius/tools/fuzzing/wordlist.txt', 'r') as file1:

		# If you want to add more payload positions, just keep adding embedded
		# loops. Order doesn't really matter since the goal is to fuzz with
		# every single combination of payloads. Just be aware the attack size
		# can get large very quickly.
		for payload1 in file1:
			for payload2 in usernames:
				for payload3 in range(0, 5):
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