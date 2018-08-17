# Build your own model

Now you are well aware of the different Models and hyperparameter techniques.
You are free to use any model you want to apply which has been taught to you.

## Write a function `q07_randomsearch_predict` that:

- Call the previous function from Question 6
- Uses RandomizedSearchCV with GradientBoostingClassifier as estimator & param_distributions equal to the parameter list given in the notebook
- Fits the data and returns the `roc_auc_score` of the prediction

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | string | compulsory |  | path of the csv file location |

### Returns:

| Return | dtype | description |
| --- | --- | --- |
| roc_auc_score | float | ROC AUC score |
