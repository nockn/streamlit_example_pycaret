"""
constant
"""
# coding: UTF-8

NONE_STR = "---"

REGRESSION_MODELS = {  # https://pycaret.readthedocs.io/en/latest/api/regression.html#pycaret.regression.create_model
    "Linear Regression": "lr",
    "Lasso Regression": "lasso",
    "Ridge Regression": "ridge",
    "Elastic Net": "en",
    "Least Angle Regression": "lar",
    "Lasso Least Angle Regression": "llar",
    "Orthogonal Matching Pursuit": "omp",
    "Bayesian Ridge": "br",
    "Automatic Relevance Determination": "ard",
    "Passive Aggressive Regressor": "par",
    "Random Sample Consensus": "ransac",
    "TheilSen Regressor": "tr",
    "Huber Regressor": "huber",
    "Kernel Ridge": "kr",
    "Support Vector Machine": "svm",
    "K Neighbors Regressor": "knn",
    "Decision Tree Regressor": "dt",
    "Random Forest Regressor": "rf",
    "Extra Trees Regressor": "et",
    "AdaBoost Regressor": "ada",
    "Gradient Boosting Regressor": "gbr",
    "Multi Level Perceptron": "mlp",
    "Extreme Gradient Boosting": "xgboost",
    "Light Gradient Boosting Machine": "lightgbm",
    "CatBoost Regressor": "catboost",
}

PLOT_MODE = {
    NONE_STR: None,
    "Residuals Plot": "residuals",
    "Prediction Error Plot": "error",
    "Cooks Distance Plot": "cooks",
    "Learning Curve": "learning",
    "Validation Curve": "vc",
    "Manifold Learning": "manifold",
}
