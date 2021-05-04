from pymongo import MongoClient
import json

class InitData:
    def __init__(self):
        self.client = MongoClient('localhost', 27017, w='majority')
        self.db = self.client.mongo_bank
        self.accounts = self.db.accounts

        # drop data from accounts collection every time to start from a clean slate
        self.db.drop_collection('accounts')

        init_data = InitData.load_data(self)
        self.insert_data(init_data)

        
    @staticmethod
    def load_data(self):
        ret = []
        with open('init_data.json', 'r') as f:
            for line in f:
                ret.append(json.loads(line))
        return ret

    def insert_data(self, data):
        for document in data:
            # breakpoint()
            collection_name = document['collection']
            account_id = document['account_id']
            account_name = document['account_name']
            account_balance = document['account_balance']

            self.db[collection_name].insert_one({'account_id': account_id, 'name': account_name, 'balance': account_balance})

   
def main():
    InitData()

if __name__ == '__main__':
    main()