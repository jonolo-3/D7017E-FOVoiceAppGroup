from wit import Wit

access_token = "EVBUV3HCYZYNAQFNVUMNSSSETBACJJCL"

client = Wit(access_token)
rep = client.message('Jag vill ha en hamburgare')

print(rep)

# resp = None
#with open('test.wav', 'rb') as f:
#  resp = client.speech(f, None, {'Content-Type': 'audio/wav'})
#print('Yay, got Wit.ai response: ' + str(resp))



