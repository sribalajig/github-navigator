from flask import Flask, render_template, request
from services.github import GithubService
from models.result import Result
import asyncio
import time

app = Flask(__name__)

@app.route("/")
def get_repositories():
	search_term = request.args.get('search_term')
	
	if not search_term:
		return render_template('repos.html', result=Result(search_term, []))
	
	github_service = GithubService('https://api.github.com/search/repositories')

	loop = asyncio.get_event_loop()	
	task = loop.create_task(github_service.get_repositories(search_term))
	repositories = loop.run_until_complete(task)
	
	if not loop.is_running:		
		loop.stop()

	end = time.time()

	return render_template('repos.html', result=Result(search_term, repositories))

def main():
	app.run()

if __name__ == '__main__':
	main()