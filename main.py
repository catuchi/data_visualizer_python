from bokeh.plotting import figure, output_file, show

# figure - is used to generate plots (graphs)
# output_file - indicates the html file to generate
# show - generates and shows the html file

x = [1,2,3,4,5]
y = [4,6,2,4,3]

output_file('index.html')

# Add plot
p = figure(
  title='Simple Graph',
  x_axis_label='X Axis',
  y_axis_label='Y Axis'
)

# Render glyph
p.line(x, y, legend='Test', line_width=2)

# Show results
show(p)