from models.repo import Repo
from models.commit import Commit
from models.owner import Owner
import aiohttp
import asyncio
import requests
from requests.auth import HTTPBasicAuth
import json
from utils.http import fetch

class GithubService:
	def __init__(self, base_url):
		self.__base_url = base_url

	async def get_repositories(self, search_term):	
		repositories_response = requests.get(
			self.__base_url, 
			{ 'q' : search_term + ' in:name', 'page' : '1', 'per_page' : '5' },
			auth=HTTPBasicAuth('sribalajig', 'Bala@1234'))

		repositories = json.loads(repositories_response.text)["items"]

		repos = []

		for item in repositories:
			repos.append(Repo(item))

		repos.sort(key=lambda x: x.created_at, reverse=True)

		tasks = []

		for repo in repos:
			task = asyncio.ensure_future(self.get_latest_commit(repo))
			tasks.append(task)

		latest_commits = await asyncio.gather(*tasks)

		for repo in repos:
			commit = next(commit for commit in latest_commits if commit.repo_name == repo.full_name)

			if commit != None:
				repo.set_latest_commit(commit)

		return repos

	async def get_latest_commit(self, repo):
		commits_response = await fetch('https://api.github.com/repos/' + repo.owner.login + '/' + repo.name + '/commits')

		latest_commit = Commit(repo.full_name, json.loads(commits_response)[0])

		return latest_commit