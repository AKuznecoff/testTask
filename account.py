class Account:
    def __init__(self, uuid, client, balance, hold, status):
        self.uuid = uuid
        self.client = client
        self.balance = balance
        self.hold = hold
        self.status = status
    
    def __repr__(self):
        return "Account('{}', '{}', '{}', '{}', '{}')".format(
            self.uuid,
            self.client,
            self.balance,
            self.hold,
            self.status)

    def get_json(self):
        return {
            "uuid": self.uuid,
            "client": self.client,
            "balance": self.balance,
            "hold": self.hold,
            "status": self.status
        }