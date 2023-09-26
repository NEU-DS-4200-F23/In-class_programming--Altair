# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Keyboard Shortcuts

# %% [markdown]
# Open command palette
# * `ctrl+shift+c`
#
# Cell organization mode
# * `enter` to begin editing a cell
# * `up` and `down` arrows to move between cells
# * `D,D` to delete a cell
# * `M` to change to Markdown
# * `Y` to change to code
# * `C` to copy a cell
# * `V` to paste the cell below
# * `B` insert cell below
# * `A` insert cell above
#
# Editing mode
# * `esc` to exit editing the cell
# * `ctrl+enter` to execute a cell
# * `alt+enter` to execute a cell and create a new one below
# * `shift+enter` to execute a cell and move to the next one
# * `ctrl+/` comment the selected line(s)

# %% [markdown]
# # Technical issues

# %% [markdown]
# `pandas 2.1.1` addes deprecation warnings to `altair` calls. If we pin `pandas==2.0.*` in `requirements.txt`, we avoid the issue.

# %% [markdown]
# # Background
#
# The census tract for the South End begins just on the SE side of Columbus Avenue, as shown in this map:
#
# ![Map of the South End](south_end.png)
#
# Let's explore the demographics of the South End.

# %% [markdown]
# # Setup

# %%
import pandas as pd
import altair as alt
from altair import datum

alt.renderers.enable('jupyterlab', embed_options={'renderer': 'svg'}) # Included for PDF export

# Avoids writing all the data to the notebook or disk. 
# See https://altair-viz.github.io/user_guide/faq.html#local-data-server
# Note that this may not work on some cloud-based Jupyter notebook services.
# alt.data_transformers.enable('data_server')

print('Altair version: ' + alt.__version__)

# %% [markdown]
# # Loading Data

# %%
df = pd.read_csv('south_end.csv')
df

# %%
pd.set_option('display.max_rows', None) # 60 is the default
df[['Category', 'Subcategory']]

# %%
df[['Category', 'Subcategory']].drop_duplicates()

# %% [markdown]
# # Creating Visualizations

# %% [markdown]
# ## Age Distribution by Decade

# %%
alt.Chart(df).mark_bar().encode(
    x='Decade:O'
)

# %%
alt.Chart(df).mark_bar().encode(
    x = 'Decade:O',
    y = 'Count:Q'
)

# %%
alt.Chart(df).mark_bar().encode(
    x = 'Decade:O',
    y = 'Count:Q',
    color = 'Subcategory:N'
)

# %%
alt.Chart(df).mark_bar().encode(
    x = 'Decade:O',
    y = 'Count:Q',
    color = 'Subcategory:N'
).transform_filter(
    datum['Category'] == 'Age'
)

# %%
alt.Chart(df).mark_bar().encode(
    x = 'Decade:O',
    y = 'Count:Q',
    color = 'Subcategory:N'
).transform_filter(
    datum['Category'] == 'Age'
).properties(
    title = 'Age Distribution by Decade'
)

# %%
alt.Chart(df).mark_bar().encode(
    x = 'Decade:O',
    y = 'Count:Q',
    color = alt.Color('Subcategory:N', title = 'Age Range')
).transform_filter(
    datum['Category'] == 'Age'
).properties(
    title = 'Age Distribution by Decade'
)

# %%
alt.Chart(df).mark_bar().encode(
    x = 'Decade:O',
    y = 'Count:Q',
    color = alt.Color('Subcategory:N', title = 'Age Range', sort = 'descending'),
    order = alt.Order(
        'Subcategory:N',
        sort = 'ascending'
    )
).transform_filter(
    datum['Category'] == 'Age'
).properties(
    title = 'Age Distribution by Decade'
)

# %%
alt.Chart(df).mark_line().encode(
    x = 'Decade:O',
    y = 'Count:Q',
    color = alt.Color('Subcategory:N', title = 'Age Range', sort = 'descending'),
    order = alt.Order(
        'Subcategory:N',
        sort = 'ascending'
    )
).transform_filter(
    datum['Category'] == 'Age'
).properties(
    title = 'Age Distribution by Decade'
)

# %%
alt.Chart(df).mark_area().encode(
    x = 'Decade:O',
    y = 'Count:Q',
    color = alt.Color('Subcategory:N', title = 'Age Range', sort = 'descending'),
    order = alt.Order(
        'Subcategory:N',
        sort = 'ascending'
    )
).transform_filter(
    datum['Category'] == 'Age'
).properties(
    title = 'Age Distribution by Decade'
)

# %% [markdown]
# ## Educational Attainment by Decade

# %%
eduField = 'Educational Attainment (age 25+)'

# %%
alt.Chart(df).mark_bar().encode(
    x = 'Decade:O',
    y = 'Count:Q',
    color = alt.Color('Subcategory:N', title = eduField, sort = 'descending'),
    order = alt.Order(
        'Subcategory:N',
        sort = 'descending'
    )
).transform_filter(
    datum['Category'] == eduField
).properties(
    title = 'Educational Attainment Distribution by Decade'
)

# %%
eduSortOrder = [
        "Bachelor's Degree or Higher",
        "Some College or Associate's Degree",
        'High School or GED',
        'less than High School'
        ]

# %%
alt.Chart(df).mark_bar().encode(
    x = 'Decade:O',
    y = 'Count:Q',
    color = alt.Color('Subcategory:N', title = eduField, sort = eduSortOrder),
).transform_filter(
    datum['Category'] == eduField
).properties(
    title = 'Educational Attainment Distribution by Decade'
)

# %%
alt.Chart(df).mark_bar().encode(
    x = 'Decade:O',
    y = 'Count:Q',
    color = alt.Color('Subcategory:N', title = eduField, sort = eduSortOrder),
    order = alt.Order(
        'eduOrdering:N',
        sort = 'ascending'
    )
).transform_filter(
    datum['Category'] == eduField
).transform_calculate(
    eduOrdering = '0'
).properties(
    title = 'Educational Attainment Distribution by Decade'
)

# %%
alt.Chart(df).mark_bar().encode(
    x = 'Decade:O',
    y = 'Count:Q',
    color = alt.Color('Subcategory:N', title = eduField, sort = eduSortOrder),
    column = alt.Column('Subcategory:N', title = eduField, sort = eduSortOrder),
).transform_filter(
    datum['Category'] == eduField
).properties(
    title = 'Educational Attainment Distribution by Decade'
)

# %%
alt.Chart(df).mark_bar().encode(
    x = 'Decade:O',
    y = 'Count:Q',
    color = alt.Color('Subcategory:N', title = eduField, sort = eduSortOrder),
    column = alt.Column('Subcategory:N', title = eduField, sort = eduSortOrder[::-1]), # ::-1 makes a copy in reverse order
).transform_filter(
    datum['Category'] == eduField
).properties(
    title = 'Educational Attainment Distribution by Decade'
)

# %% [markdown]
# ## Race by Decade

# %%
alt.Chart(df).mark_bar().encode(
    x = 'Decade:O',
    y = 'Count:Q',
    color = alt.Color('Subcategory:N', title = 'Race'),
).transform_filter(
    datum['Category'] == 'Race/ Ethnicity'
).properties(
    title = 'Race Distribution by Decade'
)

# %%
chart_race = alt.Chart(df).mark_bar().encode(
    x = 'Decade:O',
    y = 'Count:Q',
    color = alt.Color('Subcategory:N', title = 'Race'),
).transform_filter(
    datum['Category'] == 'Race/ Ethnicity'
).properties(
    title = 'Race Distribution by Decade'
)
chart_race

# %% [markdown]
# ## Types of Occupancy by Decade

# %%
alt.Chart(df).mark_bar().encode(
    x = 'Decade:O',
    y = alt.Y('Count:Q', stack = 'normalize', title = 'Occupancy Split'),
    color = alt.Color('Subcategory:N', title = 'Type of Occupancy'),
).transform_filter(
    (datum['Category'] == 'Housing Tenure') &
    (datum['Subcategory'] != 'Occupied Housing Units')
).properties(
    title = 'Types of Occupancy Distribution by Decade'
)

# %%
chart_occupancy = alt.Chart(df).mark_bar().encode(
    x = 'Decade:O',
    y = alt.Y('Count:Q', stack = 'normalize', title = 'Occupancy Split'),
    color = alt.Color('Subcategory:N', title = 'Type of Occupancy'),
).transform_filter(
    (datum['Category'] == 'Housing Tenure') &
    (datum['Subcategory'] != 'Occupied Housing Units')
).properties(
    title = 'Types of Occupancy Distribution by Decade'
)
chart_occupancy

# %% [markdown]
# # Saving Your Results

# %% [markdown]
# ## Saving to a web page...

# %%
chart_occupancy.save('chart_occupancy.html', embed_options={'renderer':'svg'})

# %% [markdown]
# ## Saving an SVG, PNG, Vega Editor...

# %% [markdown]
# **Note:** You do not need to do the following steps yourself. The instructor will simply demonstrate what is possible.

# %% [markdown]
# Let's save the chart from above using the ... menu at the top-right in several different formats.
#
# Here is an example infographic you could create by exporting an SVG and editing in Inkscape or Illustrator:
#
# ![South End Occupancy Infographic](south_end_occupancy_infographic.png)
#
# In Inkscape:
# * Open the SVG.
# * Use the select tool to select the owner series & the legend with `shift+click`, after first `double-clicking` a lot to get through the groups.
# * Go to Object->Fill and Stroke and pick a gray color.
# * Add the `apartment_building.svg` and scale to ~20% using Object->Transform->Scale 
# * Select and edit the text at the top to "Decreasing Renter-Occupied South End Dwellings"
# * File->Save As->Inkscape SVG
#
# In Illustrator:
# * Open the SVG.
# * Use the magic wand tool to select the owner series & the legend.
# * Edit->Edit Colors->Saturate and reduce saturation.
# * Add the `apartment_building.svg` and scale to ~20% using Object->Transform->Scale
# * Select and edit the text at the top to "Decreasing Renter-Occupied South End Dwellings"
# * File->Export As->SVG

# %%
