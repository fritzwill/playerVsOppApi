import cherrypy
import json

class PlayersController(object):
    def __init__(self, sdb):
        self.sdb = sdb
    
    # outputs every single player with accompaning data
    def GET(self):
        output = {'result' : 'success'}
        playerList = []
        flag = True
        for player in self.sdb.players:
            try:
                currPlayer = {}
                for k, v in player.items():
                    currPlayer[k] = v
                playerList.append(currPlayer)
            except Exception as e:
                output['result'] = 'error'
                output['message'] = str(e)
                flag = False
        if flag:
            output['players'] = playerList
        return json.dumps(output)

    # outputs one players with accompaning data depending on key
    def GET_KEY(self, key):
        output = {'result' : 'success'}
        key = int(key)
        description = self.sdb.get_player(key)
        if description is None:
            output['result'] = 'error'
            output['message'] = 'team not found'
        else:
            output['firstName'] = description['firstName']
            output['lastName'] = description['lastName']
            output['playerId'] = description['playerId']
            output['teamId'] = description['teamId']

        return json.dumps(output)

    def GET_NAME(self, name):
        output = {'result' : 'success'}
        key = int(self.sdb.get_player_id(name))
        description = self.sdb.get_player(key)
        if description is None:
            output['result'] = 'error'
            output['message'] = 'team not found'
        else:
            output['firstName'] = description['firstName']
            output['lastName'] = description['lastName']
            output['playerId'] = description['playerId']
            output['teamId'] = description['teamId']

        return json.dumps(output)
