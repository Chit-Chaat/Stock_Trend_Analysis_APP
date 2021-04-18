import os
from absl import app
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from RealMSE import RealMSE
from ScaledRealMSE import ScaledRealMSE
from stock_prediction_class import StockMetaData
from stock_prediction_numpy import StockDataGenerator
from datetime import timedelta

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'


def main(argv):
    print(tf.version.VERSION)
    inference_folder = os.path.join(os.getcwd(), RUN_FOLDER)
    stock = StockMetaData(STOCK_TICKER, STOCK_START_DATE, STOCK_VALIDATION_DATE, inference_folder)

    data = StockDataGenerator(stock)

    (x_train, y_train), (x_test, y_test), (training_data, test_data) = \
        data.download_transform_to_numpy(TIME_STEPS, inference_folder)
    min_max = data.get_min_max()

    # load future data

    print('Latest Stock Price')
    latest_close_price = test_data.Close.iloc[-1]
    latest_date = test_data[-1:]['Close'].idxmin()
    print(latest_close_price)
    print('Latest Date')
    print(latest_date)

    tomorrow_date = latest_date + timedelta(1)
    # Specify the next 300 days
    # 25 /50/ 75
    next_year = latest_date + timedelta(25 * NEXT_DAYS)
    # next_year = latest_date + timedelta(5)

    print('Future Date')
    print(tomorrow_date)

    print('Future Timespan Date')
    print(next_year)

    x_test, y_test, test_data = \
        data.generate_future_data(TIME_STEPS, min_max, tomorrow_date, next_year, latest_close_price)

    dependencies = {
        'RealMSE': RealMSE(),
        'ScaledRealMSE':ScaledRealMSE(),
    }
    # load the weights from our best model
    model = tf.keras.models.load_model(os.path.join(inference_folder, 'model_weights.h5'), custom_objects=dependencies)
    model.summary()

    # display the content of the model
    baseline_results = model.evaluate(x_test, y_test, verbose=2)
    for name, value in zip(model.metrics_names, baseline_results):
        print(name, ': ', value)
    print()

    temp_matrix_vals = np.array(baseline_results).reshape(-1, 1)
    matrix_vals = np.concatenate([temp_matrix_vals, temp_matrix_vals], axis=1)
    scaled_matrix_vals = min_max.inverse_transform(matrix_vals)
    print("===>real MSE", scaled_matrix_vals.tolist()[3][0])

    # perform a prediction
    test_predictions_baseline = model.predict(x_test)
    test_predictions_baseline = np.concatenate([test_predictions_baseline, test_predictions_baseline], axis=1)
    test_predictions_baseline = min_max.inverse_transform(test_predictions_baseline)
    test_predictions_baseline = pd.DataFrame(test_predictions_baseline)

    test_predictions_baseline.rename(columns={0: STOCK_TICKER + '_predicted'}, inplace=True)
    test_predictions_baseline = test_predictions_baseline.round(decimals=0)
    test_data.to_csv(os.path.join(inference_folder, 'generated.csv'))
    test_predictions_baseline.to_csv(os.path.join(inference_folder, 'inference.csv'))

    print("plotting predictions")
    plt.figure(figsize=(14, 5))
    plt.plot(test_predictions_baseline[STOCK_TICKER + '_predicted'], color='red',
             label='Predicted [' + STOCK_TICKER + '] price')
    plt.xlabel('Time')
    plt.ylabel('Price [' + 'USD' + ']')
    plt.legend()
    plt.title('Prediction')
    plt.savefig(os.path.join(inference_folder, STOCK_TICKER + '_future_prediction.png'))
    plt.pause(0.001)
    plt.show()


if __name__ == '__main__':
    TIME_STEPS = 3
    NEXT_DAYS = 1
    RUN_FOLDER = 'BOTZ_20210416_75738c5446f08ca779259c71421df437'
    STOCK_TICKER = 'BOTZ'
    STOCK_START_DATE = pd.to_datetime('2018-01-01')
    STOCK_VALIDATION_DATE = pd.to_datetime('2020-01-01')
    app.run(main)
