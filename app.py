from wit import Wit
import requests
import json
import pyttsx3
from Recorder import record_audio, read_audio




API_ENDPOINT = 'https://api.wit.ai/speech'

access_token = 'EVBUV3HCYZYNAQFNVUMNSSSETBACJJCL'
client = Wit(access_token)

def decoder (resp):
    print(resp)
    entities = []
    for key, value in resp.items():
        if(key == 'entities'):
            print(key)
            print("\n")
            for k in value.keys():
                print("Entity: " + k)
                p = value[k];
                print(p[0]['value'])
                tuple1 = (k , p[0]['value'])
                entities.append(tuple1)
    return entities


def makeAnswer(entities):
    text ='You ordered '

    for ent in entities:
        value = ent[1]
        print(ent[0])
        if ent[0] == 'food_type':
            text+= value + ' '
        elif ent[0] == 'number':
            text += str(value) + ' '
        elif ent[0] == 'drink':
            text+= value


    print(text)
    return text



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
    engine = pyttsx3.init()
    text = '3 hamburgare och 3 hamburgare tack'
    resp = client.message(text)
    engine.say(makeAnswer(decoder(resp)))
    engine.runAndWait()

