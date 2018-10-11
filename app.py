from wit import Wit
import requests
import json
from Recorder import record_audio, read_audio

API_ENDPOINT = 'https://api.wit.ai/speech'

access_token = 'EVBUV3HCYZYNAQFNVUMNSSSETBACJJCL'
client = Wit(access_token)

def decoder (resp):
    #keys  = resp.keys()
    #items = resp.items()
    #values = resp.values()

    #print(keys)
    #print(items)
    #print(values)

    for key, value in resp.items():
        if(key == 'entities'):
            print(key)
            print("\n")
            for k in value.keys():
                print("Entity: " + k)
                p = value[k];
                print(p[0]['value'])
            

def RecognizeSpeech(AUDIO_FILENAME, num_seconds = 5):
    
    # record audio of specified length in specified audio file
    record_audio(num_seconds, AUDIO_FILENAME)
    
    # reading audio
    audio = read_audio(AUDIO_FILENAME)
    
    # defining headers for HTTP request
    headers = {'authorization': 'Bearer ' + access_token,
               'Content-Type': 'audio/wav'}

    # making an HTTP post request
    resp = requests.post(API_ENDPOINT, headers = headers,
                         data = audio)



    # converting response content to JSON format
    data = json.loads(resp.content)

    decoder(data)
    
    # get text from data
    text = data['_text']
    
    # return the text
    return text




if __name__ == "__main__":
    ##text = RecognizeSpeech('myspeech.wav', 4)
    text = 'En hamburgare tack'
    resp = client.message(text)
    decoder(resp)
    print("\nYou said: {}".format(text))

