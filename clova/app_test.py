from clova.app_server import main

aa = {
    "version": "0.1.0",
    "session": {
        "sessionId": "a4b31c7d-0abe-47c4-8156-a8d1ebb30074",
        "user": {
            "userId": "PGAvWRfDQD-UGXqmAubRaw",
            "accessToken": "4b8b8248-97f0-4b0a-b1d8-80d8b3e6d940"
        },
        "new": True
    },
    "context": {
        "System": {
            "user": {
                "userId": "PGAvWRfDQD-UGXqmAubRaw",
                "accessToken": "4b8b8248-97f0-4b0a-b1d8-80d8b3e6d940"
            },
            "device": {
                "deviceId": "f5199c30-857d-4f66-aceb-075db328977f",
                "display": {
                    "size": "l100",
                    "orientation": "landscape",
                    "dpi": 96,
                    "contentLayer": {
                        "width": 640,
                        "height": 360
                    }
                }
            }
        }
    },
    "request": {
        "type": "IntentRequest",
        "intent": {
            "name": "ThrowDiceIntent",
            "slots": {
                "index": {
                    "name": "index",
                    "value": "보조 지표"
                }
            }
        }
    }
}    
        
main(aa)