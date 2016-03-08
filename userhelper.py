import discord

class userhelper:
    def __init__(self, client):
        self.client = client
    def getUser(self, username):
        for member in self.client.get_all_members():
            if member.name == username:
                return(member)