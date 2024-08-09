import requests, time, random, json,sys, os
import datetime
import qrcode, cv2
from PIL import Image

def snake(auth,firebase):
	headers = {
	    'Host': 'storm.thndr.io',
	    'Content-Type': 'application/json',
	    'X-Thndr-Platform': 'ios',
	    'X-Unity-Version': '2021.3.20f1',
	    'Accept': '*/*',
	    'Authorization': 'Bearer ' + str(auth),
	    'X-Firebase-Appcheck': firebase,
	    'Accept-Language': 'en-US,en;q=0.9',
	    'X-Thndr-Game': '-MuvENjk6Hm4HF9KcAwD~snake',
	    'User-Agent': 'BitcoinSnake/51 CFNetwork/1410.1 Darwin/22.6.0',
	}

	params = {'buildType': 'ios',}

	json_data = {
	    'gameId': '-MuvENjk6Hm4HF9KcAwD~snake',
	    'platformId': '-MuvENjlWxWxg9SkRNM8~ios',
	    'data': [
	        'U2FsdGVkX1+yXPPNQQoQouO9P4oRGPAlhML9T61vNaGE2FZMkaOuWzWRdF49Ffii',
	    ],
	}

	response = requests.post('https://storm.thndr.io/api/v0/submit-score', params=params, headers=headers, json=json_data)
	print("[TICKET SNAKE]",response.text)
	ticket = json.loads(response.text)["data"]["totalPlayerTickets"]
	return ticket


def turbo(auth, firebase):
	headers = {
	    'Host': 'storm.thndr.io',
	    'Content-Type': 'application/json',
	    'X-Thndr-Platform': 'ios',
	    'X-Unity-Version': '2021.3.20f1',
	    'Accept': '*/*',
	    'Authorization': 'Bearer ' + str(auth),
	    'X-Firebase-Appcheck': firebase,
	    'Accept-Language': 'en-US,en;q=0.9',
	    'X-Thndr-Game': '-MGAVSlZbZGW1OQ6HzsI',
	    'User-Agent': 'Turbo84/112 CFNetwork/1410.1 Darwin/22.6.0',
	}

	params = {'buildType': 'ios',}

	json_data = {
	    'gameId': '-MGAVSlZbZGW1OQ6HzsI',
	    'platformId': '-MGAVSl_5Zj5Hsr4cuM-',
	    'data': [
	        'U2FsdGVkX19uM+knGFwHjNJ6XP5g6sRgDlUkntXrAkfpBZHdqkGgIyNPAwEmHpBs9sRL9gyfJBaEv2CoKDb3m67IFFRmgMJmbvCvM1gpYog=',
	    ],
	}

	response = requests.post('https://storm.thndr.io/api/v0/submit-score', params=params, headers=headers, json=json_data,)
	print("[TICKET TURBO]",response.text)
	ticket = json.loads(response.text)["data"]["totalPlayerTickets"]
	return ticket

def refresh_auth(token):
	headers = {
		'Host': 'securetoken.googleapis.com',
		'Content-Type': 'application/json',
		'Accept': '*/*',
		'X-Client-Version': 'iOS/FirebaseSDK/10.10.0/FirebaseCore-iOS',
		'X-Ios-Bundle-Identifier': 'com.thndrgames.snake',
		'Accept-Language': 'en',
		'User-Agent': 'FirebaseAuth.iOS/10.10.0 com.thndrgames.snake/1.15.4 iPhone/16.5.1 hw/iPhone10_1',
		'X-Firebase-Gmpid': '1:987193886912:ios:abca30fbae5f405c4d4525',
		'Connection': 'close',
	}

	params = {
		'key': 'AIzaSyAM-ZMHYP2WOi37TwsMBpXWFw7t8BIzTh0',
	}

	json_data = {
		'grantType': 'refresh_token',
		'refreshToken': token,
	}

	response = requests.post('https://securetoken.googleapis.com/v1/token', params=params, headers=headers, json=json_data)
	data = json.loads(response.text)
	refresh_token = data["refresh_token"]
	auth = data["access_token"]
	return auth

def generate_qr(text):
	qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4,)
	qr.add_data(text)
	qr.make(fit=True)
	img = qr.make_image(fill_color="black", back_color="white")
	img.save("qr.jpg")
	image = cv2.imread("qr.jpg")
	cv2.imshow("Image", image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def withdrawSnake(auth,firebase):
	headers = {
	    'Host': 'storm.thndr.io',
	    'Content-Type': 'application/json',
	    'X-Thndr-Platform': 'ios',
	    'X-Unity-Version': '2021.3.20f1',
	    'Accept': '*/*',
	    'Authorization': 'Bearer ' + str(auth),
	    'X-Firebase-Appcheck': firebase,
	    'Accept-Language': 'en-US,en;q=0.9',
	    'X-Thndr-Game': '-MuvENjk6Hm4HF9KcAwD~snake',
	    'User-Agent': 'BitcoinSnake/51 CFNetwork/1410.1 Darwin/22.6.0',
	}

	json_data = {
	    'matchedField': 'prize.gameId',
	    'matchedValue': '-MuvENjk6Hm4HF9KcAwD~snake',
	    'walletId': 'walletofsatoshi',
	}

	response = requests.post('https://storm.thndr.io/lightning/v0/rewards/withdraw/sats',headers=headers,json=json_data,)
	try:
		qr = json.loads(response.text)["data"]["lnurl"]
		generate_qr(qr)
	except:
		print("[WITHDRAW SNAKE]",response.text)

def withdrawTurbo(auth,firebase):
	headers = {
	    'Host': 'storm.thndr.io',
	    'Content-Type': 'application/json',
	    'X-Thndr-Platform': 'ios',
	    'X-Unity-Version': '2021.3.20f1',
	    'Accept': '*/*',
	    'Authorization': 'Bearer ' + str(auth),
	    'X-Firebase-Appcheck': firebase,
	    'Accept-Language': 'en-US,en;q=0.9',
	    'X-Thndr-Game': '-MGAVSlZbZGW1OQ6HzsI',
	    'User-Agent': 'Turbo84/112 CFNetwork/1410.1 Darwin/22.6.0',
	}

	json_data = {
	    'matchedField': 'prize.gameId',
	    'matchedValue': '-MGAVSlZbZGW1OQ6HzsI',
	    'walletId': 'walletofsatoshi',
	}

	response = requests.post('https://storm.thndr.io/lightning/v0/rewards/withdraw/sats',headers=headers,json=json_data,)
	try:
		qr = json.loads(response.text)["data"]["lnurl"]
		generate_qr(qr)
	except:
		print("[WITHDRAW TURBO]",response.text)

def refresh_firebase():
	headers = {
	    'Host': 'firebaseappcheck.googleapis.com',
	    'Accept': '*/*',
	    'Content-Type': 'application/json',
	    'X-Ios-Bundle-Identifier': 'com.thndrgames.snake',
	    'User-Agent': 'BitcoinSnake/51 CFNetwork/1410.1 Darwin/22.6.0',
	    'Accept-Language': 'en-US,en;q=0.9',
	    'X-Goog-Api-Key': 'AIzaSyAM-ZMHYP2WOi37TwsMBpXWFw7t8BIzTh0',
	}

	json_data = {
	    'limited_use': False,
	    'device_token': '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',
	}

	response = requests.post('https://firebaseappcheck.googleapis.com/v1/projects/thndr-games/apps/1:987193886912:ios:abca30fbae5f405c4d4525:exchangeDeviceCheckToken',headers=headers,json=json_data,)
	firebase = json.loads(response.text)["token"]
	return firebase



refresh_token = "AMf-vBx7FqR5FYOKzO08RG52vFM80m5mYWey29Tl_f3ekvzPvJkedODrryvdvRnNQOLH4UeqL_E1Znb7QRSJVZDnuETevUOzAEaG5v0qz7qCHHSfejTkJCfg136CU3cUG29fKEv_ItGIAmfCaU4kh62qQIDVffuwtwR6nl1jZ1PhSV7EbAs9ygrPqllNszcEI1aD-O2CN3NOI0ijovGqLPNO76SIkfhdCTmupXYFmNj41nfTwMFLFeSXYpLf4000B0HFMI0c0GdNCgsnrhKH7DAtL4r1nVeWSESguRzNXUbd50_gIzl6OMDbar5ewJMqm2sCCKI_Yxv5Usb7FjJtEIxDqyhE0ynhMcP4WuRzrlVJPewwrS3sYGyDJL_-BFGbmoy86sBXVqOZH-MAg0Rk8NRRxA0W6xe5QKaZn2OPxIKTt3VidtNpECU"

# withdrawSnake(bearer_auth,firebase)
# withdrawTurbo(bearer_auth,firebase)

while True:
	firebase = refresh_firebase()
	bearer_auth = refresh_auth(refresh_token)
	while True:
		try:
			ticket = turbo(bearer_auth,firebase)
			if ticket == 0:break
			time.sleep(15)
		except Exception as e:
			print(e)
			break

	bearer_auth = refresh_auth(refresh_token)
	while True:
		try:
			ticket = snake(bearer_auth,firebase)
			if ticket == 0:break
			time.sleep(15)
		except Exception as e:
			print(e)
			break
	print("[Script] Sleeping for 5 minutes . . .")
	time.sleep(300)
