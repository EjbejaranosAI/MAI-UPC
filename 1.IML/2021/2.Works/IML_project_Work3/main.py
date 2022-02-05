from model_evaluator.model_evaluator import ModelEvaluator

if __name__ == '__main__':
    # ----------------------SATIMAGE DATASET---------------------------------------#
    model_evaluator = ModelEvaluator(dataset='satimage')
    # ----------------------HYPOTHYROID DATASET---------------------------------#
    # model_evaluator = ModelEvaluator(dataset='hypothyroid')

    # performing evaluation on ibs
    model_evaluator.evaluate_model(algorithm='ib1')
    model_evaluator.evaluate_model(algorithm='ib2')
    model_evaluator.evaluate_model(algorithm='ib3')

    # finding best one
    best_algorithm = model_evaluator.find_best_ib()

    model_evaluator.find_best_configuration(algorithm=best_algorithm)
    print(model_evaluator.k_perfomance)

    # ----------------------FEATURE SELECTION METHODS-----------------------#
    model_evaluator.select_features(method='i_gain', number_of_features=5)
    # model_evaluator.select_features(method='relief', number_of_features=10)

    # ----------------------BEST HYPOTHYROID PARAMETER---------------------#
    # If you want to test  the dataset hypothyroid , uncomment the lines 29 and 30 and comment 35 and 36
    # Parameters  of calling k_ibl for the hypothyroid dataset
    # model_evaluator.k_ibl(algorithm='ib1', k=3, voting_policy='most_voted', distance_alg='Eucledian', feature_selection=True)
    # model_evaluator.k_ibl(algorithm='ib1', k=3, voting_policy='most_voted', distance_alg='Eucledian', feature_selection=False)

    # ----------------------BEST SATIMAGE PARAMETER---------------------------#
    # If you want to test  the  satimage dataset, uncomment the lines 35 and 36 and comment 29 and 30
    # Parameters  of calling k_ibl for the satimage dataset
    model_evaluator.k_ibl(algorithm=best_algorithm, k=3, voting_policy='most_voted', distance_alg='Eucledian', feature_selection=True)
    model_evaluator.k_ibl(algorithm=best_algorithm, k=3, voting_policy='most_voted', distance_alg='Eucledian', feature_selection=False)
