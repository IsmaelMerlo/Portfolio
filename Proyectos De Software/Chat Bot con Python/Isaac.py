import re
import random

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty +=1

    percentage = float(message_certainty) / float (len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
        highest_prob = {}

        def response(bot_response, list_of_words, single_response = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

        response('Queloque mamawebo habla clorooooooo', ['hola', 'epale', 'saludos', 'buenas'], single_response = True)
        response('Piola vale y tu?', ['como', 'estas', 'va', 'vas', 'sientes', 'chamo'], required_words=['como'])
        response('Etoy en la guaira xd', ['ubicados', 'direccion', 'donde', 'ubicacion', 'vives'], single_response=True)
        response('Siempre a la orden miamor :3', ['gracias', 'corazón', 'te lo agradezco', 'thanks'], single_response=True)

        best_match = max(highest_prob, key=highest_prob.get)
        #print(highest_prob)

        return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['ahhh no manooo un beso en la boca dice que quiere :3', 'Bésame sensacional, bésame hazlo ahora turututu', 'mamate un webo mamawebo'][random.randrange(3)]
    return response

while True:
    print("Isaac: " + get_response(input('You: ')))