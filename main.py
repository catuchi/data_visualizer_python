from bokeh.plotting import figure, output_file, show, ColumnDataSource
import pandas

# figure - is used to generate plots (graphs)
# output_file - indicates the html file to generate
# show - generates and shows the html file

# Test data
# x = [1,2,3,4,5]
# y = [4,6,2,4,3]

# Read csv file
df = pandas.read_csv('./cars.csv')

# car = df['Car']
# hp = df['Horsepower']

# Create columndatasource from data frame
source = ColumnDataSource(df)

output_file('index.html')

# Car list for y_range in plot
car_list = source.data['Car'].tolist()

# Add plot
p = figure(
  y_range=car_list,
  plot_width=800,
  plot_height=600,
  title='Cars With Top Horseposer',
  x_axis_label='Horsepower',
  tools="pan,box_select,zoom_in,zoom_out,save,reset"
)

# Render glyph
p.hbar(
  y='Car',
  right='Horsepower',
  left=0,
  height=0.4,
  color='orange',
  fill_alpha=0.5,
  source=source
)

# Show results
show(p)