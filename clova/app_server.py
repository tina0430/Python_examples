import uuid

def main(args):
    print('main 들어옴')
    version = args.get("version","0.1.0")
    typeReq = args.get("request","intent")
    
    print(typeReq.get('intent').get('name'))
    
    if typeReq == "intent" :
        print('nothing')
        return{"payload":"horororororo"}
    
    elif typeReq['type'] == "LaunchRequest":
        return {"response":{
                 "version": "0.1.0",
                  "sessionAttributes": {},
                  "response": {
                    "outputSpeech": {
                      "type": "SimpleSpeech",
                      "values": {
                      "type": "PlainText",
                      "lang": "ko",
                      "value": "시작"
                  }
                },
                "card": {},
                "directives": [],
                "shouldEndSession": True
              }
            }}
    
    elif typeReq['intent']['name'] == 'ThrowDiceIntent':
        print('index')
        return{"response":{
                "card":{},
                "directives":[{
                    "header":{
                        "messageId":uuid.uuid4(),
                        "name":typeReq['intent']['name'],
                        "namespace":typeReq['intent']['name']
                    },
                "payload":""
                }],
            "outputSpeech":{
                "type":"SimpleSpeech",
                "values":{
                    "type":"PlainText",
                    "lang":"ko",
                    "value":"안녕하세요."
                }
                #"brief":""
                #"verbose":{
                #    "type":""
                #    "values":""
                #}
            },
            #"reprompt":{
            #    "outputspeech":{
            #        "type":"",
            #        "values":"",
            #        "brief":"",
            #        "verbose":{
            #            "type":"",
            #            "values":""
            #        }
            #    }
            #},
            "shouldEndSession":False,
            "version":"0.1.0"
        }
    }  
    elif typeReq['intent']['name'] == 'Clova.GuideIntent':
        print('clova.GudieIntent')
        return{"payload":"clova"}


