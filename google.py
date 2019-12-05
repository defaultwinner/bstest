import requests
import settings 

def google_results(keyword):
	search_url = "{}&q={}".format(settings.GOOGLE_API, keyword)
	response = requests.get(search_url).json()
	json_data = response['items'][:5]
	top_results = [i['title'] for i in json_data]
	return top_results