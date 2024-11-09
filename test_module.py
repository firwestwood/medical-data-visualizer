import unittest
import medical_data_visualizer
import matplotlib.pyplot as plt

class MedicalDataVisualizerTestCase(unittest.TestCase):
    def test_cat_plot(self):
        fig = medical_data_visualizer.draw_cat_plot()
        self.assertTrue(isinstance(fig, plt.Figure))

    def test_heat_map(self):
        fig = medical_data_visualizer.draw_heat_map()
        self.assertTrue(isinstance(fig, plt.Figure))

if __name__ == "__main__":
    unittest.main()
