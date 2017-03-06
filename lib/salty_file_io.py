import pickle
from character import Character
def saveBettingData(betting_data):
    pickle.dump(open('betting_data_v2.pickle', 'wb'))

def loadBettingData():
    betting_data = pickle.load(open('betting_data_v2.pickle', 'rb'))
    return betting_data

def loadLoginCredentials():
    with open('leechy.key', 'r') as file:
        data = file.read().split(',')
        login_payload = {data[0]:data[1],data[2]:data[3],data[4]:data[5]}

    return login_payload