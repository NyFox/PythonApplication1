import vk

session = vk.Session()
api = vk.API(session)
print (api.users.get(user_ids='hi271012'))

session = vk.Session(access_token='91083a55646b105752e3a8bd1603fec945915a27f2d0d9e56ea1319e34fc4c02b676d2d42ac8c42c92597')
api = vk.API(session)

print = (api.wall.get(owner_id='416'))