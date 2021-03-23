#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import display, HTML
import bokeh.sampledata
from bokeh.io import show
from bokeh.models import LogColorMapper, ColumnDataSource
from bokeh.palettes import Cividis256 as palette
from bokeh.plotting import figure, curdoc
from bokeh.sampledata.us_counties import data as counties
import pandas as pd


bokeh.sampledata.download()

#Import data file
df = pd.read_csv('/Users/Valerie/cali_data.csv',delimiter=',', header=0, skiprows=2)

#Drop first row
df = df.drop(df.index[0])

#Rename specific columns
df2 = df.rename(columns={'CA County':'county_name', 'Poverty Percent, All Ages': 'poverty_percent', 'Median Household Income': 'median_income' },inplace=True)

#Select columns
df_factors = df[["county_name", "poverty_percent", "median_income"]]

#Convert to dictionary
df_dic = df_factors.to_dict('index')


display(HTML(df_factors.to_html()))


# In[2]:


palette = tuple(reversed(palette))

counties = {
    code: county for code, county in counties.items() if county["state"] == "ca"
}

county_xs = [county["lons"] for county in counties.values()]
county_ys = [county["lats"] for county in counties.values()]


#Merge the two dicts
def merge_two_dicts(a_dict, b_dict):
    # iterate thru keys of each dict in order (using python 3) 
    # assuming dicts are same length
    for idx in range(len(b_dict)):

        a_key = list(a_dict.keys())[idx]
        b_key = list(b_dict.keys())[idx]

        if('median_income' in a_dict[a_key]):
            b_dict[b_key]['median_income'] = a_dict[a_key]['median_income']

        if('poverty_percent' in a_dict[a_key]):
            b_dict[b_key]['poverty_percent'] = a_dict[a_key]['poverty_percent']
           
    return b_dict

a_dict = df_dic
b_dict = counties

#Overwrite previous value of counties
counties= merge_two_dicts(a_dict, b_dict)

print(counties)


# In[3]:


county_names = [county['name'] for county in counties.values()]
poverty_est = [county['poverty_percent'] for county in counties.values()]
median_income = [county['median_income'] for county in counties.values()]
color_mapper = LogColorMapper(palette=palette)


data=dict(
    x=county_xs,
    y=county_ys,
    name=county_names,
    poverty=poverty_est,
    income = median_income
    
)

print(data)


# In[4]:


TOOLS = "pan,wheel_zoom,reset,hover,save"

p = figure(
    title="CA Poverty and Median Household Income, 2019", tools=TOOLS,
    x_axis_location=None, y_axis_location=None,
    tooltips=[
        ("Name", "@name"), ("Poverty Percentage", "@poverty%"), ('Median Household Income', "@income"), ("(Long, Lat)", "($x, $y)")
    ])
p.grid.grid_line_color = None
p.hover.point_policy = "follow_mouse"

p.patches('x', 'y', source=data,
          fill_color={'field': 'poverty', 'transform': color_mapper},
          fill_alpha=0.7, line_color="white", line_width=0.5)

curdoc().add_root(p)

# In[ ]:




