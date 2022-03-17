import math
import pandas as pd


class RegressionError():
    def mse(
        self,
        csv_file: str,
        real_column: str,
        predicted_column: str
    ):
        df = pd.read_csv(csv_file)
        m = len(df[real_column])
        sumatory = 0
        for index, row in df.iterrows():
            real = row[real_column]
            estimated = row[predicted_column]
            _ = (real - estimated) ** 2
            sumatory = sumatory + _
        return sumatory / m

    def mae(
        self,
        csv_file: str,
        real_column: str,
        predicted_column: str
    ):
        df = pd.read_csv(csv_file)
        n = len(df[real_column])
        sumatory = 0
        for index, row in df.iterrows():
            real = row[real_column]
            estimated = row[predicted_column]
            sumatory = sumatory + abs(real - estimated)
        return sumatory / n

    def rmse(
        self,
        csv_file: str,
        real_column: str,
        predicted_column: str
    ):
        mse = self.mse(
            csv_file=csv_file,
            real_column=real_column,
            predicted_column=predicted_column
        )
        _ = math.sqrt(mse)
        return _


if __name__ == '__main__':
    file = 'data/mse_example.csv'
    reg_err = RegressionError()
    _ = reg_err.mse(
        csv_file=file,
        real_column='real',
        predicted_column='prediction'
    )
    print('MSE: {}'.format(_))
    _ = reg_err.mae(
        csv_file=file,
        real_column='real',
        predicted_column='prediction'
    )
    print("MAE {}".format(_))
    _ = reg_err.rmse(
        csv_file=file,
        real_column='real',
        predicted_column='prediction'
    )
    print("RSME {}".format(_))
