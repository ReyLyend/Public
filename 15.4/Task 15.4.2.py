import json

stringUrl = ['https://', 'http://', r'https:\\', r'http:\\']
stringEvent = ['itemBuyEvent', 'itemViewEvent']
keysCheck = {'timestamp':int,
             'referer':stringUrl,
             'location':stringUrl,
             'remoteHost':str,
             'partyId':str,
             'sessionId':str,
             'pageViewId':str,
             'eventType': stringEvent,
             'item_id':str,
             'item_price':int,
             'item_url': stringUrl,
             'basket_price':str,
             'detectedDuplicate':bool,
             'detectedCorruption':bool,
             'firstInSession':bool,
             'userAgentName':str}

with open('json_example_QAP.json', encoding='utf8') as temp:
    serverAnswers = json.load(temp)

#Uncomment this to test against custom data
# serverAnswers = [{'timestamp': 1555296301000,
#                 'referer': 'https://b24.com',
#                 'location': 'htt://d2wt09.shop/',
#                 'badAnswer': 'strangedata',
#                 'мойключ': 123,
#                 'eventType': 'nothingHere',
#                 'item_id':'cheburek',
#                 'item_price':100,
#                 'detectedDuplicate':True,
#                 'detectedCorruption':'NotTrue'},
#                  {'timestamp':123,
#                 'partyId':'someId'}]

print(f'Server has given {len(serverAnswers)} answers')

for answer in serverAnswers:
    missingKeys = []
    badKeys = {} #collecting errors
    typeErrors = {}
    print(f'Summary for answer No.{serverAnswers.index(answer)}: ')
    #check for missing keys
    for key in keysCheck.keys():
        if key not in answer:
            missingKeys.append(key)
    print('+PASS - All keys are present') if not missingKeys else print("-List of missing keys: ", missingKeys)

    for key in answer.keys():
        #check for alien keys
        if key not in keysCheck.keys():
            badKeys[key] = answer[key]
        # check for wrong types
        elif type(answer[key]) != keysCheck[key]: #int, string, bool
            #url check
            if keysCheck[key] == stringUrl:
                if (answer[key][:7] and answer[key][:8]) not in stringUrl:
                    typeErrors[key] = (f'server answered: {answer[key]}', '. Expected proper URL')
            #events check
            elif keysCheck[key] == stringEvent:
                if answer[key] not in stringEvent:
                    typeErrors[key] = (f'server answered: {answer[key]}', f'. Expected one of: {keysCheck[key]}')
            else:
                typeErrors[key] = (f'server answered: {answer[key]}, of type {type(answer[key])}', f'. Expected type: {keysCheck[key]}')
    print("+PASS - No extra or bad keys") if not badKeys else print('-List of bad keys with values: ', badKeys)
    if not typeErrors:
        print('+Pass - All values have correct data type')
    else:
        print('-List of type errors:')
        for i in typeErrors.items():
            print('-- For key "' + i[0] + '"' ,*i[1])
    print()
