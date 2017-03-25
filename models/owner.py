class Owner(object):
	def __init__(self, obj):
		self.url = obj["url"]
		self.avatar_url = obj["avatar_url"]
		self.login = obj["login"]