import json


class ssh:
    def __init__(self, user, password, key, host, isadmin, port):
        self.user = user
        self.password = password
        self.key = key
        self.host = host
        self.isadmin = isadmin
        self.port = port

    def __str__(self):
        print('SSH STRING:\n'
              'ssh {}@{} -p{}\n'
              'Password:{}\n'
              'Is admin?: {}\n'
              'Key: {}').format(self.user, self.host, self.port, self.password, self.isadmin, self.key)
        return


    @classmethod
    def from_json(cls, filename):
        with open(filename, 'r') as fin:
            fint = json.load(fin)
            user = fint["user1"]["username"]
            password = fint["user1"]["password"]
            key = fint["user1"]["key"]
            host = fint["user1"]["host"]
            isadmin = fint["user1"]["isadmin"]
            port = fint["user1"]["port"]
            return user, password, key, host, isadmin, port

    def to_json(self):
        formatself = json.loads('{'
                                '"user1":{'
                                '"username": "{}}",'
                                '"password": "{}}",'
                                '"key": "{}}",'
                                '"host": "{}}",'
                                '"isadmin": "{}}",'
                                '"port": "{}}"}').format(self.user, self.password, self.key, self.host, self.isadmin,
                                                         self.port)

        with open(filename, 'w') as fout:
            fout.write(json.dumps(formatself))


file = 'users.json'

new = ssh.from_json(file)

print(new)
