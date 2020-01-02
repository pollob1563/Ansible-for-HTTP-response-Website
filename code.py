import requests

print("Enter Your Website without protocol and with domain name: ")

website = input()

req = requests.get('https://'+website)

status_code = req.status_code

print("HTTP Status Code: ",status_code)


if (status_code>=100) and (status_code<=199) :
	print("Informational response")

elif (status_code>=200) and (status_code<=299):
	print("Success")

elif (status_code>=300) and (status_code<=399):
	print("Redirection")

elif (status_code>=400) and (status_code<=499):
	print("Client errors")

elif (status_code>=500) and (status_code<=599):
	print("Server errors")

#end
