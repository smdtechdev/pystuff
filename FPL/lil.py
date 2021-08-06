import requests
import pandas as pd
import numpy as np

pd.options.display.max_columns = None

url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
#Use the requests package to make a GET request from the API endpoint:
r = requests.get(url)
#Then, transform that request into a json object:
json = r.json()
#Let’s look at the json keys, and then we’ll create our dataframe(s)
print(json.keys())

elements_df = pd.DataFrame(json['elements'])
elements_types_df = pd.DataFrame(json['element_types'])
teams_df = pd.DataFrame(json['teams'])
#Preview the top 5 rows of your dataframes with the head() method. Like so:
print(elements_df.head())
print(elements_df.columns)

slim_elements_df = elements_df[['first_name','second_name','team','element_type','selected_by_percent','now_cost','minutes','transfers_in','value_season','total_points']]
#Now, most of the data I’m currently interested in is viewable in a single window:
slim_elements_df['position'] = slim_elements_df.element_type.map(elements_types_df.set_index('id').singular_name)

slim_elements_df['team'] = slim_elements_df.team.map(teams_df.set_index('id').name)


slim_elements_df['value'] = slim_elements_df.value_season.astype(float)
print(slim_elements_df.sort_values('value',ascending=False).head(10))
print(slim_elements_df.head())