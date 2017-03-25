from models.owner import Owner

class Repo(object):
	def __init__(self, obj):
		self.name = obj["name"]
		self.created_at = obj["created_at"]
		self.owner = Owner(obj["owner"])
		self.full_name = obj["full_name"]

	def set_latest_commit(self, latest_commit):
		self.latest_commit = latest_commit