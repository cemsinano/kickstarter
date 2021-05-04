import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json = {'main_category':'Games', 'country':'US', 'name_wcount':'3', 'campaing_len':'10','launched_hour':'1', 'launched_month':'January', 'launched_year':'2015', 'launched_weekend':'0', 'deadline_weekend':'1', 'goal_usd':'1000'})

print(r.json())
