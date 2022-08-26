import os
import json

# class for Game State Handler
class GameStateHandler:
    def __init__(self):
        """
        function to initialize variables
        :param match_start_data:  empty json
        :param all_events_update: empty list
        :return: None
        """
        # Initialize json
        self.match_start_data = {}
        # list of dict which has All the events update
        self.all_events_update = []

    def main(self):
        """
        main function to call
        :return: None
        """
        path = "data"
        file_list = self.get_files(path)
        for file in file_list:
            filename = path + '/' + file
            # Calling parse_files() func to parse the json
            json_data = self.parse_files(filename)

            if json_data:
                # logic for MATCH_START
                if json_data['type'] == 'MATCH_START':
                    # Assigning json match type MATCH_START to match_start_data dict
                    self.match_start_data = json_data

                    # Initializing teams killstatus in dict
                    teams = self.match_start_data['payload']['teams']
                    for team in teams:
                        team['teamKillStatus'] = {'dragonKill': {'dragonType': '', 'count': 0}, 'nashorKillCount': 0, 'towerKillCount': 0}

                        # Initializing players killstatus in dict
                        players = team['players']
                        for player in players:
                            player['killStatus'] = {'minionKillCount': 0, 'playerKillCount': 0, 'assistsCount': 0}

                    self.all_events_update.append(self.match_start_data.copy())
                else:
                    teams = self.match_start_data['payload']['teams']
                    """ 
                        calling particular function for match type to update data, 
                        updating match type and adding event to all_events_update list
                    """
                    if json_data['type'] == 'MINION_KILL':
                        self.minion_kill(json_data, teams)
                        self.match_start_data['type'] = 'MINION_KILL'
                        self.all_events_update.append(self.match_start_data.copy())

                    if json_data['type'] == 'PLAYER_KILL':
                        self.player_kill(teams, json_data)
                        self.match_start_data['type'] = 'PLAYER_KILL'
                        self.all_events_update.append(self.match_start_data.copy())

                    elif json_data['type'] == 'PLAYER_REVIVE':
                        self.player_revite(teams, json_data)
                        self.match_start_data['type'] = 'PLAYER_REVIVE'
                        self.all_events_update.append(self.match_start_data.copy())

                    elif json_data['type'] == 'DRAGON_KILL':
                        self.dragon_kill(json_data, teams)
                        self.match_start_data['type'] = 'DRAGON_KILL'
                        self.all_events_update.append(self.match_start_data.copy())

                    elif json_data['type'] == 'NASHOR_KILL':
                        self.nashor_kill(json_data, teams)
                        self.match_start_data['type'] = 'NASHOR_KILL'
                        self.all_events_update.append(self.match_start_data.copy())

                    elif json_data['type'] == 'TURRET_DESTROY':
                        self.turret_destroy(json_data, teams)
                        self.match_start_data['type'] = 'TURRET_DESTROY'
                        self.all_events_update.append(self.match_start_data.copy())

                    elif json_data['type'] == 'MATCH_END':
                        self.match_end(json_data, teams)
                        self.match_start_data['type'] = 'MATCH_END'
                        self.all_events_update.append(self.match_start_data.copy())

        # Creating JSON file for final output
        self.create_json(self.match_start_data, 'final_json')

        # Creating JSON file with list of all events status data
        self.create_json(self.all_events_update, 'all_event_list_json')

        return self.match_start_data

    def get_files(self, path):
        """
        function to get list of filenames from given directory
        :param path: directory name
        :return: list of filenames
        """
        dir_list = os.listdir(path)
        return dir_list

    def parse_files(self, filename):
        """
        function to parse JSON file
        :param filename: json file
        :return: dictonary object
        """
        with open(filename) as f:
            try:
                # Parse Json data to python dict
                data = json.load(f)
                return data
            except Exception:
                print("Could not parse JSON file " + filename)

    def minion_kill(self, json_data, teams):
        """
        function for MINION_KILL event
        :param json_data: new event data
        :param teams: game event data needs to be updated for players
        :return: None
        """
        for team in teams:
            players = team['players']
            for player in players:
                # Update player gold coins
                if player['playerID'] == json_data['payload']['playerID']:
                    player['gold'] = player['gold'] + json_data['payload']['goldGranted']
                    # Update minion Kill Count for player
                    player['killStatus']['minionKillCount'] += 1
        return

    def player_kill(self, teams, json_data):
        """
        function for PLAYER_KILL event
        :param json_data: new event data
        :param teams: game event data needs to be updated for players
        :return: None
        """
        for team in teams:
            players = team['players']
            for player in players:

                # Update player alive status
                if player['playerID'] == json_data['payload']['victimID']:
                    player['alive'] = 'false'

                # Update player gold coins
                elif player['playerID'] == json_data['payload']['killerID']:
                    player['gold'] = player['gold'] + json_data['payload']['goldGranted']

                else:
                    # Update assistants gold coins
                    for assistant in json_data['payload']['assistants']:
                        if player['playerID'] == assistant:
                            player['gold'] = player['gold'] + json_data['payload']['assistGold']

                # Update player Kill Count & assists Count for player
                player['killStatus']['playerKillCount'] += 1
                player['killStatus']['assistsCount'] += 1
        return

    def player_revite(self, teams, json_data):
        """
        function for PLAYER_REVIVE event
        :param json_data: new event data
        :param teams: game event data needs to be updated for players
        :return: None
        """
        for team in teams:
            players = team['players']
            for player in players:

                # Update player alive status
                if player['playerID'] == json_data['payload']['playerID']:
                    player['alive'] = 'true'
        return

    def dragon_kill(self, json_data, teams):
        """
        function for DRAGON_KILL event
        :param json_data: new event data
        :param teams: game event data needs to be updated for players
        :return: None
        """
        for team in teams:
            players = team['players']
            for player in players:
                if player['playerID'] == json_data['payload']['killerID']:

                    # Players gold count update
                    player['gold'] = player['gold'] + json_data['payload']['goldGranted']

                    # Teams Dragon Kill count & type update
                    team['teamKillStatus']['dragonKill']['dragonType'] = json_data['payload']['dragonType']
                    team['teamKillStatus']['dragonKill']['count'] += 1
        return

    def nashor_kill(self, json_data, teams):
        """
        function for NASHOR_KILL event
        :param json_data: new event data
        :param teams: game event data needs to be updated for players
        :return: None
        """
        for team in teams:
            players = team['players']
            for player in players:
                if player['playerID'] == json_data['payload']['killerID']:

                    # Teams nashor Kill count update
                    team['teamKillStatus']['nashorKillCount'] += 1

                    # Players gold count update. Each of its players receives some gold form goldGranted.
                    goldGranted = (json_data['payload']['teamGoldGranted']) / len(team['players'])
                    for player in team['players']:
                        player['gold'] = player['gold'] + goldGranted
        return

    def turret_destroy(self, json_data, teams):
        """
        function for TURRET_DESTROY event
        :param json_data: new event data
        :param teams: game event data needs to be updated for players
        :return: None
        """
        for team in teams:
            players = team['players']
            for player in players:
                # Players gold count update
                if player['playerID'] == json_data['payload']['killerID']:
                    player['gold'] = player['gold'] + json_data['payload']['playerGoldGranted']

                # Teams tower Kill count update
                team['teamKillStatus']['towerKillCount'] += 1

                # if killerid is null, assuming towers are destroyed by minions, so no individual player receives gold.
                # Players gold count update. Each of its players receives some gold form teamGoldGranted.
                goldGranted = (json_data['payload']['teamGoldGranted']) / len(team['players'])
                for player in team['players']:
                    player['gold'] = player['gold'] + goldGranted
        return

    def match_end(self, json_data, teams):
        """
        function for MATCH_END event
        :param json_data: new event data
        :param teams: teams data for finding winner team
        :return: None
        """
        for team in teams:
            # compare team with winner team id and get the winner
            if team['teamID'] == json_data['payload']['winningTeamID']:
                print("Winner team is::", team['teamID'])

    def create_json(self, json_data, filename):
        """
        function for create json file after match end
        :param json_data: get json data to create JSON file
        :return: None
        """
        path = 'output'
        filepath = path + '/' + filename
        with open(filepath, 'w') as f:
            json.dump(json_data, f, indent=2)
            print(filename + "file has been created in output folder")


# Creating object from class
GameStateHandler_obj = GameStateHandler()

# Calling main() function of class
GameStateHandler_obj.main()
