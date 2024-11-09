from medical_data_visualizer import draw_cat_plot, draw_heat_map
import test_module

# Run the functions and save figures
cat_plot_fig = draw_cat_plot()
cat_plot_fig.savefig('catplot.png')

heat_map_fig = draw_heat_map()
heat_map_fig.savefig('heatmap.png')

# Run the tests
if __name__ == "__main__":
    test_module.main()
