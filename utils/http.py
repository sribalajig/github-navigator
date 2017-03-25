import async_timeout
import aiohttp

async def fetch(url):
	async with aiohttp.ClientSession() as session:
		with async_timeout.timeout(10):
			async with session.get(url, auth=aiohttp.BasicAuth('sribalajig', 'Bala@1234')) as response:
				return await response.text()