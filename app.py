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
            print(value)
            print("\n")
            for k in value.keys():
                print("Entity: " + k)
                p = value[k]
                index = 0
                for x in p:
                    print(p[index]['value'])
                    tuple1 = (k, p[index]['value'])
                    entities.append(tuple1)
                    index += 1

    return entities


def makeAnswer(entities):
    text ='You ordered '

    print(entities)
    if(len(entities) > 10):
        return "Loose some weight, that order is to big!"
    num = list()
    for ent in entities:
        key = ent[0]
        value = ent[1]
        print(ent[0])
        print(value)
        if key == 'food_type':
            text += str(num[0]) + ' ' + value
            num.pop(0)
            if(num):
                text += ' and '
        elif key == 'number':
            num.append(value)
        elif key == 'drink':
            text += str(num[0]) + ' ' + value
            num.pop(0)
            if(num):
                text += ' and '
        elif key == 'sides':
            text += str(num[0]) + ' ' + value
            num.pop(0)
            if (num):
                text += ' and '
        else:
            text += ''



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
    text = RecognizeSpeech('myspeech.wav', 4)
    engine = pyttsx3.init()
    #text = 'En hamburgare och tre fanta och en fries och 5 Cola och 3 chicken hamburgare'
    resp = client.message(text)
    engine.say(makeAnswer(decoder(resp)))
    engine.runAndWait()

