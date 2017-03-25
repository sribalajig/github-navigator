class Commit(object):
	def __init__(self, repo_name, obj):
		self.sha = obj["sha"]
		self.message = obj["commit"]["message"]
		self.author_name = obj["commit"]["author"]["name"]
		self.repo_name = repo_name