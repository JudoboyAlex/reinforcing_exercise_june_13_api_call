from django.http import JsonResponse
import json
import requests

res = requests.get("https://cdn.rawgit.com/everypolitician/everypolitician-data/master/countries.json")
body = json.loads(res.content)

for i, country in enumerate(body):
        print(country["name"])
        print(i)

north_korea_url = body[146]["legislatures"][0]["popolo_url"]

print(north_korea_url)

res_north_korea = requests.get(north_korea_url)
body_north_korea = json.loads(res_north_korea.content)

dictator = body_north_korea["persons"][0]["name"]

print(dictator)