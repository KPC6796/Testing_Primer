import numpy as np
from numpy.testing import assert_almost_equal
import pytest 

from metrics import accuracy_score
from metrics import mean_squared_error 
from metrics import r2_score

# assert_almost_equal - checks equality of 2 arrays upto desired precision

def test_accuracy_score():
    y_preds = [0, 2, 1, 3]
    y_true = [0, 1, 2, 3]

    assert_almost_equal(accuracy_score(y_true, y_preds), 1.0)

def test_mean_squared_error(n_samples=50):
    y_true = np.arange(n_samples)
    y_pred = y_true + 1

    assert_almost_equal(mean_squared_error(y_true, y_pred), 1.)

def test_mean_squared_error_squared():
    # Calculate MSE.
    mse1 = mean_squared_error([[1]], [[10]], squared=True)
    
    # Calculate RMSE.
    mse2 = mean_squared_error([[1]], [[10]], squared=False)

    # Assert sqrt(MSE) = RMSE
    assert np.sqrt(mse1) == pytest.approx(mse2)

def test_r2_score():
    """Test for r2_score function. """
    y_true = np.array([3, -0.5, 2, 7])
    y_pred = np.array([2.5, 0.0, 2, 8])

    score = r2_score(y_true, y_pred)

    assert_almost_equal(score, 0.9486081370)