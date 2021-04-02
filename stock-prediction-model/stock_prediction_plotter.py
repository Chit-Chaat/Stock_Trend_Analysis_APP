import os
import matplotlib.pyplot as plt


class Plotter:
    def __init__(self, blocking, project_folder, short_name, currency, stock_ticker):
        self.blocking = blocking
        self.project_folder = project_folder
        self.short_name = short_name
        self.currency = currency
        self.stock_ticker = stock_ticker

    def project_plot_predictions(self, price_predicted, test_data):
        plt.figure(figsize=(14, 5))
        plt.plot(price_predicted[self.stock_ticker + '_predicted'], color='red', label='Predicted [' + self.short_name + '] price')
        plt.plot(test_data.Close, color='green', label='Actual [' + self.short_name + '] price')
        plt.xlabel('Time')
        plt.ylabel('Price [' + self.currency + ']')
        plt.legend()
        plt.title('Prediction')
        plt.savefig(os.path.join(self.project_folder, self.short_name.strip().replace('.', '') + '_prediction.png'))
        plt.pause(0.001)
        plt.show(block=self.blocking)
