import numpy as np
import pandas as pd

def make_cvd_dataset():
    '''Create different powers for creation of dataset. Dataset is a mock CVD plasma growth rate experiment.'''

    x = np.array([8, 8, 8, 8, 10, 10, 10, 10, 12, 12, 12, 12, 14, 14, 14, 14])

    # Create normalized distributions for different RF powers
    # TODO: Make RFPow dynamic

    RFPow8 = 5000 + 8 * (np.random.randn(1, 4) ** 2)
    RFPow10 = 5050 + 8 * (np.random.randn(1, 4) ** 2)
    RFPow12 = 5100 + 8 * (np.random.randn(1, 4) ** 2)
    RFPow14 = 5150 + 8 * (np.random.randn(1, 4) ** 2)

    # Append different powers together

    RF = RFPow8
    RFPow = [RFPow10, RFPow12, RFPow14]
    for set in RFPow:
        RF = np.append(RF, set)

    # Combine into dataset

    cvd_dataset = pd.DataFrame(x, columns=['Power'])
    cvd_dataset['GrowthRate'] = RF

    return cvd_dataset

if __name__ == "__main__":
    cvd = make_cvd_dataset()
    print(cvd)