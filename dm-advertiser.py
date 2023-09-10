from collections import UserDict
import os, requests, random, json, string
from time import sleep
from colorama import Fore

token  = "MTA0ODkzNzg3ODc4MjIyNjQ4Mg.GJo9U3.HNN2a33IGSdXKFfKcYNQaLTEJDi2O41CD5qyCI"

os.system("cls && title DM-Advertiser")

def center(var: str, space: int = None): # From Pycenter
	if not space:
		space = (
			os.get_terminal_size().columns
			- len(var.splitlines()[int(len(var.splitlines()) / 2)])
		) / 2

	return "\n".join((" " * int(space)) + var for var in var.splitlines())

headers = {
	"authorization": token
}

class Advertiser:
	def idScraper(channelID):
		r = requests.get(f'https://discord.com/api/v9/channels/{channelID}/messages?limit=100',headers=headers)
		
		jsonn = json.loads(r.text)

		for value in jsonn:
			with open("./output/scraped-ids-.txt", 'a', encoding='UTF-8') as file:
				file.write(value['author']['id'] + "\n")
		file.close()


	def sendMessageToChannel(channelID, message):
		# https://discord.com/api/v9/channels/979687231025463326/messages
		payload = {
			'content': message
		}

		r = requests.post(f'https://canary.discord.com/api/v9/channels/{channelID}/messages', data=payload, headers=headers)

		if r.status_code == 429:
			print(center(f"""{Fore.RED}[-] Rate Limited.. ~ {r.status_code}{Fore.RESET}"""))
		if r.status_code == 401:
			print(center(f"""{Fore.RED}[-] The Authorization header was missing or invalid... ~ {r.status_code}{Fore.RESET}"""))
		if r.status_code == 200:
			print(center(f"""{Fore.LIGHTGREEN_EX}[+] Message sent to channel: {channelID} ~ {r.status_code}{Fore.RESET}"""))
		else:
			print(center(f"""{Fore.RED}[-] Message could not be sent to channel: {channelID}.. ~ {r.status_code}{Fore.RESET}"""))

	def sendMessageToUser(userID, message):
		req = requests.post('https://discordapp.com/api/v9/users/@me/channels', headers=headers, json={'recipient_id': userID})
		channelId = req.json().get('id')

		r = requests.post(f'https://discordapp.com/api/v9/channels/{channelId}/messages', headers=headers, json={'content': message})

		if r.status_code == 429:
			print(center(f"""{Fore.RED}[-] Rate Limited.. ~ {r.status_code}{Fore.RESET}"""))
		if r.status_code == 401:
			print(center(f"""{Fore.RED}[-] The Authorization header was missing or invalid... ~ {r.status_code}{Fore.RESET}"""))
		if r.status_code == 200:
			print(center(f"""{Fore.LIGHTGREEN_EX}[+] Message sent to user: {userID} ~ {r.status_code}{Fore.RESET}"""))
		else:
			print(center(f"""{Fore.RED}[-] Message could not be sent to user: {userID}.. ~ {r.status_code}{Fore.RESET}"""))
	
if __name__ == "__main__":
	print(
		center(
			f"""\n\n
{Fore.LIGHTBLUE_EX}    
┌┬┐┌┬┐   ┌─┐┌┬┐┬  ┬┌─┐┬─┐┌┬┐┬┌─┐┌─┐┬─┐
 │││││───├─┤ ││└┐┌┘├┤ ├┬┘ │ │└─┐├┤ ├┬┘
─┴┘┴ ┴   ┴ ┴─┴┘ └┘ └─┘┴└─ ┴ ┴└─┘└─┘┴└─{Fore.RESET}  														
  DM-Advertiser & Scraper ~ Rigqx	
		"""
		)
	)

	message = input(" message ~ ")
	id = input(" id ~ ")
	
	Advertiser.sendMessageToUser(id, message)

	#with open("./output/scraped-ids.txt", 'r', encoding='UTF-8') as file:
	#	while (line := file.readline().rstrip()):
	#		Advertiser.sendMessageToUser(line, message)