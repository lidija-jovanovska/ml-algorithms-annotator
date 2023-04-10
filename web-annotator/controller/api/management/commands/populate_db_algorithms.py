from api.models.dm_algorithm import DataMiningAlgorithm
from api.models.base_algorithm import Algorithm
from api.models.annotation import Annotation
from api.models.assumption import Assumption
from api.models.complexity import Complexity
from api.models.dataset import Dataset
from api.models.document import Document
from api.models.generalization import GeneralizationSpecification
from api.models.optimization_problem import OptimizationProblem
from api.models.parameter import Parameter
from api.models.task import Task

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Populate the database with algorithm annotations.'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

    # try:
        #
        # Ordinary Least Squares
        #

        # METADATA

        ols_dict = {
            'name': 'LinearRegression',
            'doc_name': 'Christopher M. Bishop: Pattern Recognition and Machine Learning, Chapter 4.3.4',
            'doc_id': '0387310738',
            'dataset_name': 'regression dataset',
            'task_name': 'supervised regression task',
            'task_mode': Task.BATCH,
            'op_problem': 'Quadratic Programming',
            'op_problem_text': 'Minimize the residual sum of squares between the observed targets in the dataset and the targets predicted by the linear approximation',
            'op_problem_maths': '\min_{w} || X w - y||_2^2',
            'generalization_spec_name': 'regression model',
            'generalization_language': GeneralizationSpecification.OTHER,
            'assumptions': [
                'Independence of observations',
                'No hidden or missing variables',
                'Linear relationship',
                'Normality of residuals',
                'No or little multicollinearity',
                'Homoscedasticity',
                'All independent variables are uncorrelated with the error term',
                'Observations of the error term are uncorrelated with each other'
            ],
            'train_complexity': {'name': 'quadratic time',
                                 'big_o': 'O(n^2)',
                                 'train_time_complexity_maths': 'O(n_{\text{samples}} n_{\text{features}}^2)'},
            # 'test_complexity': {'name': 'Linear complexity', 'big_o': 'O(n)'},
            # 'space_complexity': {'name': 'Linear complexity', 'big_o': 'O(n)'},
            'annotator': {'annotator_name': 'Your Name', 'email': 'abc.xyz@gmail.com'}
        }


        ols = DataMiningAlgorithm(name=ols_dict.get('name')).save()

        ols_doc = Document.nodes.first_or_none(
            name=ols_dict.get('doc_name'),
            document_id=ols_dict.get('doc_id'))
        if ols_doc is None:
            ols_doc_new = Document(
            name=ols_dict.get('doc_name'),
            document_id=ols_dict.get('doc_id')).save()
            ols.documents.connect(ols_doc_new)
        else:
            ols.documents.connect(ols_doc)

        # IO

        # dataset
        ols_dataset = Dataset.nodes.first_or_none(
            name=ols_dict.get('dataset_name')
        )
        if ols_dataset is None:
            ols_dataset_new = Dataset(
                name=ols_dict.get('dataset_name')
            ).save()
            ols.datasets.connect(ols_dataset_new)
        else:
            ols.datasets.connect(ols_dataset)

        # task
        ols_task = Task.nodes.first_or_none(
            name=ols_dict.get('task_name'),
            mode=ols_dict.get('task_mode')
        )

        if ols_task is None:
            ols_task_new = Task(
                name=ols_dict.get('task_name'),
                mode=ols_dict.get('task_mode')
            ).save()
            ols.tasks.connect(ols_task_new)
        else:
            ols.tasks.connect(ols_task)

        # op problem
        ols_op_problem = OptimizationProblem.nodes.first_or_none(
            name=ols_dict.get('op_problem'),
            math_desc=ols_dict.get('op_problem_maths'),
            lang_desc=ols_dict.get('op_problem_text')
        )

        if ols_op_problem is None:
            ols_op_problem_new = OptimizationProblem(
                name=ols_dict.get('op_problem'),
                math_desc=ols_dict.get('op_problem_maths'),
                lang_desc=ols_dict.get('op_problem_text')
            ).save()
            ols.optimization_problem.connect(ols_op_problem_new)
        else:
            ols.optimization_problem.connect(ols_op_problem)


        # ols_op_problem = OptimizationProblem.get_or_create({'name': 'Linear Programming'
        #                                  # "math_desc": '\\min_{w} || X w - y||_2^2',
        #                                  # "lang_desc":'minimize the residual sum of squares between the observed targets in'
        #                                  #           ' the dataset, and the targets predicted by the linear approximation'
        #                                                     }, relationship=ols.optimization_problem)

        # generalization spec
        ols_generalization_spec = GeneralizationSpecification.nodes.first_or_none(
            name=ols_dict.get('generalization_spec_name'),
            generalization_language=ols_dict.get('generalization_language')
        )

        if ols_generalization_spec is None:
            ols_generalization_spec_new = GeneralizationSpecification(
                name=ols_dict.get('generalization_spec_name'),
                generalization_language = ols_dict.get('generalization_language')
            ).save()
            ols.generalization_specifications.connect(ols_generalization_spec_new)
        else:
            ols.generalization_specifications.connect(ols_generalization_spec)

        # ols_generalization_spec = GeneralizationSpecification.get_or_create({"name": "regression model",
        #                                                   "generalization_language": GeneralizationSpecification.OTHER
        # }, relationship=ols.generalization_specifications)

        # ASSUMPTIONS


        for assumption in ols_dict.get('assumptions'):
            assumption_exists = Assumption.nodes.first_or_none(name=assumption)
            if assumption_exists is None:
                assumption_new = Assumption(name=assumption).save()
                ols.assumptions.connect(assumption_new)
            else:
                ols.assumptions.connect(assumption_exists)

        # ols_assumptions = Assumption.get_or_create(
        #     {'name': 'Independence of observations'},
        #     {'name': 'No hidden or missing variables'},
        #     {'name': 'Linear relationship'},
        #     {'name': 'Normality of residuals'},
        #     {'name': 'No or little multicollinearity'},
        #     {'name': 'Homoscedasticity'},
        #     {'name': 'All independent variables are uncorrelated with the error term'},
        #     {'name': 'Observations of the error term are uncorrelated with each other'},
        # )

        # for assumption in ols_assumptions:
        #     ols.assumptions.connect(assumption)

        # COMPLEXITY

        # train
        train = Complexity.nodes.first_or_none(
            name=ols_dict.get('train_complexity').get('name'),
            big_o=ols_dict.get('train_complexity').get('big_o'),
            description=ols_dict.get('train_time_complexity_maths')
        )

        if train is None:
            train_new = Complexity(
            name=ols_dict.get('train_complexity').get('name'),
            big_o=ols_dict.get('train_complexity').get('big_o'),
            description=ols_dict.get('train_time_complexity_maths')
        ).save()
            ols.train_complexity.connect(train_new)
        else:
            ols.train_complexity.connect(train)

        # # test
        # test = Complexity.nodes.first_or_none(
        #     name=ols_dict.get('test_complexity').get('name'),
        #     big_o=ols_dict.get('test_complexity').get('big_o')
        # )
        # if test is None:
        #     test_new = Complexity(
        #     name=ols_dict.get('test_complexity').get('name'),
        #     big_o=ols_dict.get('test_complexity').get('big_o')
        # ).save()
        #     ols.test_complexity.connect(test_new)
        # else:
        #     ols.test_complexity.connect(test)
        #
        # # space
        # space = Complexity.nodes.first_or_none(
        #     name=ols_dict.get('space_complexity').get('name'),
        #     big_o=ols_dict.get('space_complexity').get('big_o')
        # )
        # if space is None:
        #     space_new = Complexity(
        #     name=ols_dict.get('space_complexity').get('name'),
        #     big_o=ols_dict.get('space_complexity').get('big_o')
        # ).save()
        #     ols.space_complexity.connect(space_new)
        # else:
        #     ols.space_complexity.connect(space)


        # train = Complexity.get_or_create(
        #     {'name': 'Quadratic complexity', 'big_o': 'O(n^2)'},
        #     relationship=ols.train_complexity
        # )
        # test = Complexity.get_or_create(
        #     {'name': 'Linear complexity', 'big_o': 'O(n)'},
        #     relationship=ols.test_complexity
        # )
        # space = Complexity.get_or_create(
        #     {'name': 'Linear complexity', 'big_o': 'O(n)'},
        #     relationship=ols.space_complexity
        # )

        # PARAMETERS

        parameters = Parameter.create(
            {'name': 'fit_intercept', 'type': Parameter.ALG_PARAM, 'datatype': Parameter.BOOL},
            {'name': 'normalize', 'type': Parameter.ALG_PARAM, 'datatype': Parameter.BOOL},
            {'name': 'copy_X', 'type': Parameter.ALG_PARAM, 'datatype': Parameter.BOOL},
            {'name': 'n_jobs', 'type': Parameter.ALG_PARAM, 'datatype': Parameter.INT},
            {'name': 'positive', 'type': Parameter.ALG_PARAM, 'datatype': Parameter.BOOL},
            # {'name': 'coef_', 'type': Parameter.MODEL_PARAM, 'datatype': Parameter.DISCRETE},
            # {'name': 'rank_', 'type': Parameter.MODEL_PARAM, 'datatype': Parameter.INT},
            # {'name': 'singular_', 'type': Parameter.MODEL_PARAM, 'datatype': Parameter.DISCRETE},
            # {'name': 'intercept_', 'type': Parameter.MODEL_PARAM, 'datatype': Parameter.DISCRETE},
            # {'name': 'n_features_in_', 'type': Parameter.MODEL_PARAM, 'datatype': Parameter.INT},
            # {'name': 'feature_names_in_', 'type': Parameter.MODEL_PARAM, 'datatype': Parameter.DISCRETE}
        )

        # parameters = Parameter.create(
        #     {'name': 'fit_intercept', 'type': Parameter.ALG_PARAM, 'datatype': Parameter.BOOL},
        #     {'name': 'normalize', 'type': Parameter.ALG_PARAM, 'datatype': Parameter.BOOL},
        #     {'name': 'copy_X', 'type': Parameter.ALG_PARAM, 'datatype': Parameter.BOOL},
        #     {'name': 'n_jobs', 'type': Parameter.ALG_PARAM, 'datatype': Parameter.INT},
        #     {'name': 'positive', 'type': Parameter.ALG_PARAM, 'datatype': Parameter.BOOL},
        #     {'name': 'coef_', 'type': Parameter.MODEL_PARAM, 'datatype': Parameter.DISCRETE},
        #     {'name': 'rank_', 'type': Parameter.MODEL_PARAM, 'datatype': Parameter.INT},
        #     {'name': 'singular_', 'type': Parameter.MODEL_PARAM, 'datatype': Parameter.DISCRETE},
        #     {'name': 'intercept_', 'type': Parameter.MODEL_PARAM, 'datatype': Parameter.DISCRETE},
        #     {'name': 'n_features_in_', 'type': Parameter.MODEL_PARAM, 'datatype': Parameter.INT},
        #     {'name': 'feature_names_in_', 'type': Parameter.MODEL_PARAM, 'datatype': Parameter.DISCRETE}
        # )

        for parameter in parameters:
            ols.parameters.connect(parameter)


        # ANNOTATOR INFO

        ols_annotation = Annotation.nodes.first_or_none(
            annotator_name=ols_dict.get('annotator').get('annotator_name'),
            email=ols_dict.get('annotator').get('email')
        )
        if ols_annotation is None:
            ols_annotation_new = Annotation(
            annotator_name=ols_dict.get('annotator').get('annotator_name'),
            email=ols_dict.get('annotator').get('email')
        ).save()
            ols.annotation.connect(ols_annotation_new)
        else:
            ols.annotation.connect(ols_annotation)

        # ols_annotation = Annotation.get_or_create(
        #     {'annotator_name': 'Your Name', 'email': 'abc.xyz@gmail.com'},
        #     relationship=ols.annotation
        # )



        # SVM

        svc_dict = {
            'name': 'SVC',
            'doc_name': 'Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods (1999)',
            'doc_id': '',
            'dataset_name': 'flat classification dataset',
            'task_name': 'supervised flat classification task',
            'task_mode': Task.BATCH,
            'op_problem': 'Quadratic Programming',
            'op_problem_text': 'maximize the margin while incurring a penalty when a sample is misclassified or within the margin boundary',
            'op_problem_maths': '\begin{aligned}\min_ {w, b, \zeta} \frac{1}{2} w^T w + C \sum_{i=1}^{n} \zeta_i\\\textrm {subject to } & y_i (w^T \phi (x_i) + b) \geq 1 - \zeta_i,\\& \zeta_i \geq 0, i=1, ..., n\end{aligned}',
            'generalization_spec_name': 'classification model',
            'generalization_language': GeneralizationSpecification.OTHER,
            'assumptions': [
                'No assumptions'
            ],
            'train_complexity': {'name': 'cubic time',
                                 'big_o': 'O(n^3)',
                                 'train_time_complexity_maths': 'O(n_{features} \times n_{samples}^2)'},
            # 'test_complexity': {'name': 'Linear complexity', 'big_o': 'O(n)'},
            # 'space_complexity': {'name': 'Quadratic complexity', 'big_o': 'O(n^2)'},
            'annotator': {'annotator_name': 'Your Name', 'email': 'abc.xyz@gmail.com'}
        }

        svc = DataMiningAlgorithm(name=svc_dict.get('name')).save()

        svc_doc = Document.nodes.first_or_none(
            name=svc_dict.get('doc_name'),
            document_id=svc_dict.get('doc_id'))
        if svc_doc is None:
            svc_doc_new = Document(
                name=svc_dict.get('doc_name'),
                document_id=svc_dict.get('doc_id')).save()
            svc.documents.connect(svc_doc_new)
        else:
            svc.documents.connect(svc_doc)

        # IO

        # dataset
        svc_dataset = Dataset.nodes.first_or_none(
            name=svc_dict.get('dataset_name')
        )
        if svc_dataset is None:
            svc_dataset_new = Dataset(
                name=svc_dict.get('dataset_name')
            ).save()
            svc.datasets.connect(svc_dataset_new)
        else:
            svc.datasets.connect(svc_dataset)

        # task
        svc_task = Task.nodes.first_or_none(
            name=svc_dict.get('task_name'),
            mode=svc_dict.get('task_mode')
        )

        if svc_task is None:
            svc_task_new = Task(
                name=svc_dict.get('task_name'),
                mode=svc_dict.get('task_mode')
            ).save()
            svc.tasks.connect(svc_task_new)
        else:
            svc.tasks.connect(svc_task)

        # op problem
        svc_op_problem = OptimizationProblem.nodes.first_or_none(
            name=svc_dict.get('op_problem'),
            lang_desc=svc_dict.get('op_problem_text'),
            math_desc=svc_dict.get('op_problem_maths')
        )

        if svc_op_problem is None:
            svc_op_problem_new = OptimizationProblem(
                name=svc_dict.get('op_problem'),
                lang_desc=svc_dict.get('op_problem_text'),
                math_desc=svc_dict.get('op_problem_maths')
            ).save()
            svc.optimization_problem.connect(svc_op_problem_new)
        else:
            svc.optimization_problem.connect(svc_op_problem)

        # svc_op_problem = OptimizationProblem.get_or_create({'name': 'Linear Programming'
        #                                  # "math_desc": '\\min_{w} || X w - y||_2^2',
        #                                  # "lang_desc":'minimize the residual sum of squares between the observed targets in'
        #                                  #           ' the dataset, and the targets predicted by the linear approximation'
        #                                                     }, relationship=svc.optimization_problem)

        # generalization spec
        svc_generalization_spec = GeneralizationSpecification.nodes.first_or_none(
            name=svc_dict.get('generalization_spec_name'),
            generalization_language=svc_dict.get('generalization_language')
        )

        if svc_generalization_spec is None:
            svc_generalization_spec_new = GeneralizationSpecification(
                name=svc_dict.get('generalization_spec_name'),
                generalization_language=svc_dict.get('generalization_language')
            ).save()
            svc.generalization_specifications.connect(svc_generalization_spec_new)
        else:
            svc.generalization_specifications.connect(svc_generalization_spec)

        # svc_generalization_spec = GeneralizationSpecification.get_or_create({"name": "regression model",
        #                                                   "generalization_language": GeneralizationSpecification.OTHER
        # }, relationship=svc.generalization_specifications)

        # ASSUMPTIONS

        for assumption in svc_dict.get('assumptions'):
            assumption_exists = Assumption.nodes.first_or_none(name=assumption)
            if assumption_exists is None:
                assumption_new = Assumption(name=assumption).save()
                svc.assumptions.connect(assumption_new)
            else:
                svc.assumptions.connect(assumption_exists)


        # COMPLEXITY

        # train
        train = Complexity.nodes.first_or_none(
            name=svc_dict.get('train_complexity').get('name'),
            big_o=svc_dict.get('train_complexity').get('big_o'),
            description=svc_dict.get('train_complexity').get('train_time_complexity_maths')
        )

        if train is None:
            train_new = Complexity(
                name=svc_dict.get('train_complexity').get('name'),
                big_o=svc_dict.get('train_complexity').get('big_o'),
                description=svc_dict.get('train_complexity').get('train_time_complexity_maths')
            ).save()
            svc.train_complexity.connect(train_new)
        else:
            svc.train_complexity.connect(train)

        # # test
        # test = Complexity.nodes.first_or_none(
        #     name=svc_dict.get('test_complexity').get('name'),
        #     big_o=svc_dict.get('test_complexity').get('big_o')
        # )
        # if test is None:
        #     test_new = Complexity(
        #         name=svc_dict.get('test_complexity').get('name'),
        #         big_o=svc_dict.get('test_complexity').get('big_o')
        #     ).save()
        #     svc.test_complexity.connect(test_new)
        # else:
        #     svc.test_complexity.connect(test)
        #
        # # space
        # space = Complexity.nodes.first_or_none(
        #     name=svc_dict.get('space_complexity').get('name'),
        #     big_o=svc_dict.get('space_complexity').get('big_o')
        # )
        # if space is None:
        #     space_new = Complexity(
        #         name=svc_dict.get('space_complexity').get('name'),
        #         big_o=svc_dict.get('space_complexity').get('big_o')
        #     ).save()
        #     svc.space_complexity.connect(space_new)
        # else:
        #     svc.space_complexity.connect(space)



        # PARAMETERS

        svc_parameters = Parameter.create(
            {"name": "C", "type": Parameter.ALG_HYPERPARAM, "datatype": Parameter.REAL},
            {"name": "kernel", "type": Parameter.ALG_PARAM, "datatype": Parameter.FUNCTION},
            {"name": "degree", "type": Parameter.ALG_PARAM, "datatype": Parameter.INT},
            {"name": "gamma", "type": Parameter.ALG_PARAM, "datatype": Parameter.DICT},
            {"name": "coef0", "type": Parameter.ALG_PARAM, "datatype": Parameter.REAL},
            {"name": "shrinking", "type": Parameter.ALG_PARAM, "datatype": Parameter.BOOL},
            {"name": "probability", "type": Parameter.ALG_PARAM, "datatype": Parameter.BOOL},
            {"name": "tol", "type": Parameter.ALG_PARAM, "datatype": Parameter.REAL},
            {"name": "cache_size", "type": Parameter.ALG_PARAM, "datatype": Parameter.REAL},
            {"name": "class_weight", "type": Parameter.ALG_PARAM, "datatype": Parameter.DICT},
            {"name": "verbose", "type": Parameter.ALG_PARAM, "datatype": Parameter.BOOL},
            {"name": "max_iter", "type": Parameter.ALG_PARAM, "datatype": Parameter.INT},
            {"name": "decision_function_shape", "type": Parameter.ALG_PARAM, "datatype": Parameter.FUNCTION},
            {"name": "break_ties", "type": Parameter.ALG_PARAM, "datatype": Parameter.BOOL},
            {"name": "random_state", "type": Parameter.ALG_PARAM, "datatype": Parameter.INT},
            # {"name": "class_weight_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.DISCRETE},
            # {"name": "classes_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.DISCRETE},
            # {"name": "coef_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.DISCRETE},
            # {"name": "dual_coef_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.DISCRETE},
            # {"name": "fit_status_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.INT},
            # {"name": "intercept_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.DISCRETE},
            # {"name": "n_features_in_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.DISCRETE},
            # {"name": "feature_names_in_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.BOOL},
            # {"name": "support_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.DISCRETE},
            # {"name": "support_vectors_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.DISCRETE},
            # {"name": "n_support_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.DISCRETE},
            # {"name": "probA_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.DISCRETE},
            # {"name": "probB_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.DISCRETE},
            # {"name": "shape_fit_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.DISCRETE}
        )

        for parameter in svc_parameters:
            svc.parameters.connect(parameter)

        # ANNOTATOR INFO

        svc_annotation = Annotation.nodes.first_or_none(
            annotator_name=svc_dict.get('annotator').get('annotator_name'),
            email=svc_dict.get('annotator').get('email')
        )
        if svc_annotation is None:
            svc_annotation_new = Annotation(
            annotator_name=svc_dict.get('annotator').get('annotator_name'),
            email=svc_dict.get('annotator').get('email')
        ).save()
            svc.annotation.connect(svc_annotation_new)
        else:
            svc.annotation.connect(svc_annotation)

        #
        # KNN
        #

        knn_dict = {
            'name': 'KNeighborsClassifier',
            'doc_name': 'Discriminatory Analysis - Nonparametric Discrimination: Small Sample Performance',
            'doc_id': 'ADA800391',
            'dataset_name': 'flat classification dataset',
            'task_name': 'supervised flat classification task',
            'task_mode': Task.BATCH,
            # 'op_problem': 'Linear Programming',
            'generalization_spec_name': 'regression model',
            'generalization_language': GeneralizationSpecification.OTHER,
            'assumptions': [
                'Similar things exist in close proximity'
            ],
            # complexity depends on the algorithm choice for finding the nearest neighbors
            'train_complexity': {'name': 'constant time',
                                 'big_o': 'O(1)',
                                 'train_time_complexity_maths': 'O(1)'},
            # 'test_complexity': {'name': 'Linear complexity', 'big_o': 'O(n)'},
            # 'space_complexity': {'name': 'Quadratic complexity', 'big_o': 'O(n^2)'},
            'algorithm': 'KDTree',
            'annotator': {'annotator_name': 'Your Name', 'email': 'abc.xyz@gmail.com'}
        }

        knn = DataMiningAlgorithm(name=knn_dict.get('name')).save()

        knn_doc = Document.nodes.first_or_none(
            name=knn_dict.get('doc_name'),
            document_id=knn_dict.get('doc_id'))
        if knn_doc is None:
            knn_doc_new = Document(
                name=knn_dict.get('doc_name'),
                document_id=knn_dict.get('doc_id')).save()
            knn.documents.connect(knn_doc_new)
        else:
            knn.documents.connect(knn_doc)

        # IO

        # dataset
        knn_dataset = Dataset.nodes.first_or_none(
            name=knn_dict.get('dataset_name')
        )
        if knn_dataset is None:
            knn_dataset_new = Dataset(
                name=knn_dict.get('dataset_name')
            ).save()
            knn.datasets.connect(knn_dataset_new)
        else:
            knn.datasets.connect(knn_dataset)

        # task
        knn_task = Task.nodes.first_or_none(
            name=knn_dict.get('task_name'),
            mode=knn_dict.get('task_mode')
        )

        if knn_task is None:
            knn_task_new = Task(
                name=knn_dict.get('task_name'),
                mode=knn_dict.get('task_mode')
            ).save()
            knn.tasks.connect(knn_task_new)
        else:
            knn.tasks.connect(knn_task)

        # op problem
        # knn_op_problem = OptimizationProblem.nodes.first_or_none(
        #     name=knn_dict.get('op_problem'),
        # )
        #
        # if knn_op_problem is None:
        #     knn_op_problem_new = OptimizationProblem(
        #         name=knn_dict.get('op_problem')
        #     ).save()
        #     knn.optimization_problem.connect(knn_op_problem_new)
        # else:
        #     knn.optimization_problem.connect(knn_op_problem)

        # knn_op_problem = OptimizationProblem.get_or_create({'name': 'Linear Programming'
        #                                  # "math_desc": '\\min_{w} || X w - y||_2^2',
        #                                  # "lang_desc":'minimize the residual sum of squares between the observed targets in'
        #                                  #           ' the dataset, and the targets predicted by the linear approximation'
        #                                                     }, relationship=knn.optimization_problem)

        # generalization spec
        knn_generalization_spec = GeneralizationSpecification.nodes.first_or_none(
            name=knn_dict.get('generalization_spec_name'),
            generalization_language=knn_dict.get('generalization_language')
        )

        if knn_generalization_spec is None:
            knn_generalization_spec_new = GeneralizationSpecification(
                name=knn_dict.get('generalization_spec_name'),
                generalization_language=knn_dict.get('generalization_language')
            ).save()
            knn.generalization_specifications.connect(knn_generalization_spec_new)
        else:
            knn.generalization_specifications.connect(knn_generalization_spec)

        # knn_generalization_spec = GeneralizationSpecification.get_or_create({"name": "regression model",
        #                                                   "generalization_language": GeneralizationSpecification.OTHER
        # }, relationship=knn.generalization_specifications)

        # ASSUMPTIONS

        for assumption in knn_dict.get('assumptions'):
            assumption_exists = Assumption.nodes.first_or_none(name=assumption)
            if assumption_exists is None:
                assumption_new = Assumption(name=assumption).save()
                knn.assumptions.connect(assumption_new)
            else:
                knn.assumptions.connect(assumption_exists)

        # COMPLEXITY

        # train
        train = Complexity.nodes.first_or_none(
            name=knn_dict.get('train_complexity').get('name'),
            big_o=knn_dict.get('train_complexity').get('big_o'),
            description=knn_dict.get('train_complexity').get('train_time_complexity_maths')
        )

        if train is None:
            train_new = Complexity(
                name=knn_dict.get('train_complexity').get('name'),
                big_o=knn_dict.get('train_complexity').get('big_o'),
                description=knn_dict.get('train_complexity').get('train_time_complexity_maths')
            ).save()
            knn.train_complexity.connect(train_new)
        else:
            knn.train_complexity.connect(train)
        #
        # # test
        # test = Complexity.nodes.first_or_none(
        #     name=knn_dict.get('test_complexity').get('name'),
        #     big_o=knn_dict.get('test_complexity').get('big_o')
        # )
        # if test is None:
        #     test_new = Complexity(
        #         name=knn_dict.get('test_complexity').get('name'),
        #         big_o=knn_dict.get('test_complexity').get('big_o')
        #     ).save()
        #     knn.test_complexity.connect(test_new)
        # else:
        #     knn.test_complexity.connect(test)
        #
        # # space
        # space = Complexity.nodes.first_or_none(
        #     name=knn_dict.get('space_complexity').get('name'),
        #     big_o=knn_dict.get('space_complexity').get('big_o')
        # )
        # if space is None:
        #     space_new = Complexity(
        #         name=knn_dict.get('space_complexity').get('name'),
        #         big_o=knn_dict.get('space_complexity').get('big_o')
        #     ).save()
        #     knn.space_complexity.connect(space_new)
        # else:
        #     knn.space_complexity.connect(space)
        # METADATA

        # knn = DataMiningAlgorithm(name="KNeighborsClassifier").save()
        # knn_doc = Document.get_or_create({
        #     'name': "Discriminatory Analysis - Nonparametric Discrimination: Small Sample Performance",
        #     'document_id': "ADA800391"
        # }, relationship=knn.documents)
        #
        # # IO
        #
        # # binary + multi-class
        # knn_dataset = Dataset.get_or_create({'name': "flat classification dataset"}, relationship=knn.datasets)
        # knn_task = Task.get_or_create({'name': "supervised flat classification task", 'mode':Task.BATCH}, relationship=knn.tasks)
        #
        # # the problem and the the optimal search algorithm depend on the data
        # # hence they will not be defined now as they depend on the algorithm parameter
        # knn_op_problem = OptimizationProblem.get_or_create({'name': "Linear Programming",
        #                                  'math_desc': "",
        #                                  'lang_desc':"given a set S of points in a space M and a query point q ∈ M, find the closest point in S to q"
        # }, relationship=knn.optimization_problem)
        #
        # # # knn doesn't really build a model, but there is no better option atm
        # knn_generalization_spec = GeneralizationSpecification.get_or_create({'name': "regression model",
        #                                                   'generalization_language': GeneralizationSpecification.OTHER
        # }, relationship=knn.generalization_specifications)
        # # ASSUMPTIONS
        # knn_assumptions = Assumption.get_or_create(
        #     {"name": "Similar things exist in close proximity"},
        #     relationship=knn.assumptions
        # )
        #
        # # COMPLEXITY
        # # complexity depends on the algorithm choice for finding the nearest neighbors
        #
        # # alg_train_complexity = Complexity.get_or_create(
        # #     {"name": "", "big_o": ""},
        # # )
        # #
        # # alg_test_complexity = Complexity.get_or_create(
        # #     {"name": "", "big_o": ""},
        # # )
        # #
        # # alg_space_complexity = Complexity.get_or_create(
        # #     {"name": "", "big_o": ""},
        # # )
        # #
        # # alg.train_complexity.connect(alg_train_complexity[0])
        # # alg.test_complexity.connect(alg_test_complexity[0])
        # # alg.space_complexity.connect(alg_space_complexity[0])

        # PARAMETERS

        # TODO: Figure out why we don't have a string datatype

        knn_parameters = Parameter.create(
            {"name": "n_neighbors", "type": Parameter.ALG_HYPERPARAM, "datatype": Parameter.INT},
            {"name": "weights", "type": Parameter.ALG_PARAM, "datatype": Parameter.FUNCTION},
            # {"name": "algorithm", "type": Parameter.ALG_PARAM, "datatype": Parameter.DICT},
            {"name": "leaf_size", "type": Parameter.ALG_PARAM, "datatype": Parameter.INT},
            {"name": "p", "type": Parameter.ALG_PARAM, "datatype": Parameter.INT},
            {"name": "metric", "type": Parameter.ALG_PARAM, "datatype": Parameter.FUNCTION},
            {"name": "metric_params", "type": Parameter.ALG_PARAM, "datatype": Parameter.DICT},
            {"name": "n_jobs", "type": Parameter.ALG_PARAM, "datatype": Parameter.INT}
            # {"name": "classes_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.DISCRETE},
            # {"name": "effective_metric_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.DICT},
            # {"name": "effective_metric_params_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.DICT},
            # {"name": "n_features_in_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.INT},
            # {"name": "feature_names_in_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.DICT},
            # {"name": "n_samples_fit_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.INT},
            # {"name": "outputs_2d_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.BOOL}
        )

        for parameter in knn_parameters:
            knn.parameters.connect(parameter)

        # ANNOTATOR INFO

        knn_annotation = Annotation.nodes.first_or_none(
            annotator_name=knn_dict.get('annotator').get('annotator_name'),
            email=knn_dict.get('annotator').get('email')
        )
        if knn_annotation is None:
            knn_annotation_new = Annotation(
            annotator_name=knn_dict.get('annotator').get('annotator_name'),
            email=knn_dict.get('annotator').get('email')
        ).save()
            knn.annotation.connect(knn_annotation_new)
        else:
            knn.annotation.connect(knn_annotation)

        algorithm = Algorithm.nodes.first_or_none(name=knn_dict.get('algorithm'))
        if algorithm is None:
            algorithm_new = Algorithm(name=knn_dict.get('algorithm')).save()
            knn.algorithms.connect(algorithm_new)
        else:
            knn.algorithms.connect(algorithm)

        # # ANNOTATOR INFO
        #
        # knn_annotation = Annotation.get_or_create(
        #     {'annotator_name': 'Your Name', 'email': 'abc.xyz@gmail.com'},
        #     relationship=knn.annotation
        # )

        #
        # Decision Tree
        #

        tree_dict = {
            'name': 'DecisionTreeClassifier',
            'doc_name': 'L. Breiman, J. Friedman, R. Olshen, and C. Stone, “Classification and Regression Trees”, Wadsworth, Belmont, CA, 1984',
            'doc_id': '9781315139470',
            'dataset_name': 'flat classification dataset',
            'task_name': 'supervised flat classification task',
            'task_mode': Task.BATCH,
            'op_problem': 'Linear Programming',
            'op_problem_text': 'Minimize the impurity at each node in the tree',
            'op_problem_maths': '\theta^* = \operatorname{argmin}_\theta  G(Q_m, \theta) G(Q_m, \theta) = \frac{n_m^{left}}{n_m} H(Q_m^{left}(\theta))+ \frac{n_m^{right}}{n_m} H(Q_m^{right}(\theta))',
            'generalization_spec_name': 'classification model',
            'generalization_language': GeneralizationSpecification.DECISION_TREES,
            'assumptions': [
                'No Assumptions'
            ],
            # complexity depends on the algorithm choice for finding the nearest neighbors
            'train_complexity': {"name": "linearithmic time",
                                 "big_o": "O(n log n)",
                                 "train_time_complexity_maths": "O(n_{samples}n_{features}\log(n_{samples}))"},
            # 'test_complexity': {"name": "", "big_o": "O(\log(n_{samples}))"},
            # 'space_complexity': {'name': 'linear', 'big_o': 'O(n)'},
            'annotator': {'annotator_name': 'Your Name', 'email': 'abc.xyz@gmail.com'}
        }

        # METADATA

        tree = DataMiningAlgorithm(name=tree_dict.get('name')).save()

        tree_doc = Document.nodes.first_or_none(
            name=tree_dict.get('doc_name'),
            document_id=tree_dict.get('doc_id'))
        if tree_doc is None:
            tree_doc_new = Document(
                name=tree_dict.get('doc_name'),
                document_id=tree_dict.get('doc_id')).save()
            tree.documents.connect(tree_doc_new)
        else:
            tree.documents.connect(tree_doc)

        # IO

        # dataset
        tree_dataset = Dataset.nodes.first_or_none(
            name=tree_dict.get('dataset_name')
        )
        if tree_dataset is None:
            tree_dataset_new = Dataset(
                name=tree_dict.get('dataset_name')
            ).save()
            tree.datasets.connect(tree_dataset_new)
        else:
            tree.datasets.connect(tree_dataset)

        # task
        tree_task = Task.nodes.first_or_none(
            name=tree_dict.get('task_name'),
            mode=tree_dict.get('task_mode')
        )

        if tree_task is None:
            tree_task_new = Task(
                name=tree_dict.get('task_name'),
                mode=tree_dict.get('task_mode')
            ).save()
            tree.tasks.connect(tree_task_new)
        else:
            tree.tasks.connect(tree_task)

        # op problem
        tree_op_problem = OptimizationProblem.nodes.first_or_none(
            name=tree_dict.get('op_problem'),
            math_desc=tree_dict.get('op_problem_maths'),
            lang_desc=tree_dict.get('op_problem_text')
        )

        if tree_op_problem is None:
            tree_op_problem_new = OptimizationProblem(
                name=tree_dict.get('op_problem'),
                math_desc=tree_dict.get('op_problem_maths'),
                lang_desc=tree_dict.get('op_problem_text')
            ).save()
            tree.optimization_problem.connect(tree_op_problem_new)
        else:
            tree.optimization_problem.connect(tree_op_problem)

        # tree_op_problem = OptimizationProblem.get_or_create({'name': 'Linear Programming'
        #                                  # "math_desc": '\\min_{w} || X w - y||_2^2',
        #                                  # "lang_desc":'minimize the residual sum of squares between the observed targets in'
        #                                  #           ' the dataset, and the targets predicted by the linear approximation'
        #                                                     }, relationship=tree.optimization_problem)

        # generalization spec
        tree_generalization_spec = GeneralizationSpecification.nodes.first_or_none(
            name=tree_dict.get('generalization_spec_name'),
            generalization_language=tree_dict.get('generalization_language')
        )

        if tree_generalization_spec is None:
            tree_generalization_spec_new = GeneralizationSpecification(
                name=tree_dict.get('generalization_spec_name'),
                generalization_language=tree_dict.get('generalization_language')
            ).save()
            tree.generalization_specifications.connect(tree_generalization_spec_new)
        else:
            tree.generalization_specifications.connect(tree_generalization_spec)

        # tree_generalization_spec = GeneralizationSpecification.get_or_create({"name": "regression model",
        #                                                   "generalization_language": GeneralizationSpecification.OTHER
        # }, relationship=tree.generalization_specifications)

        # ASSUMPTIONS

        for assumption in tree_dict.get('assumptions'):
            assumption_exists = Assumption.nodes.first_or_none(name=assumption)
            if assumption_exists is None:
                assumption_new = Assumption(name=assumption).save()
                tree.assumptions.connect(assumption_new)
            else:
                tree.assumptions.connect(assumption_exists)


        # COMPLEXITY

        # train
        train = Complexity.nodes.first_or_none(
            name=tree_dict.get('train_complexity').get('name'),
            big_o=tree_dict.get('train_complexity').get('big_o'),
            description=tree_dict.get('train_complexity').get('train_time_complexity_maths')
        )

        if train is None:
            train_new = Complexity(
                name=tree_dict.get('train_complexity').get('name'),
                big_o=tree_dict.get('train_complexity').get('big_o'),
                description=tree_dict.get('train_complexity').get('train_time_complexity_maths')
            ).save()
            tree.train_complexity.connect(train_new)
        else:
            tree.train_complexity.connect(train)

        # # test
        # test = Complexity.nodes.first_or_none(
        #     name=tree_dict.get('test_complexity').get('name'),
        #     big_o=tree_dict.get('test_complexity').get('big_o')
        # )
        # if test is None:
        #     test_new = Complexity(
        #         name=tree_dict.get('test_complexity').get('name'),
        #         big_o=tree_dict.get('test_complexity').get('big_o')
        #     ).save()
        #     tree.test_complexity.connect(test_new)
        # else:
        #     tree.test_complexity.connect(test)
        #
        # # space
        # space = Complexity.nodes.first_or_none(
        #     name=tree_dict.get('space_complexity').get('name'),
        #     big_o=tree_dict.get('space_complexity').get('big_o')
        # )
        # if space is None:
        #     space_new = Complexity(
        #         name=tree_dict.get('space_complexity').get('name'),
        #         big_o=tree_dict.get('space_complexity').get('big_o')
        #     ).save()
        #     tree.space_complexity.connect(space_new)
        # else:
        #     tree.space_complexity.connect(space)


        # METADATA

        # tree = DataMiningAlgorithm(name="DecisionTreeClassifier").save()
        # tree_doc = Document.get_or_create({
        #     'name': "L. Breiman, J. Friedman, R. Olshen, and C. Stone, “Classification and Regression Trees”, Wadsworth, Belmont, CA, 1984",
        #     'document_id': "9781315139470"
        # }, relationship=tree.documents)
        #
        # # IO
        #
        # tree_dataset = Dataset.get_or_create({'name': "flat classification dataset"}, relationship=tree.datasets)
        # tree_task = Task.get_or_create({'name': "supervised flat classification task", 'mode': Task.BATCH}, relationship=tree.tasks)
        # tree_op_problem = OptimizationProblem.get_or_create({'name': "Linear Programming",
        #                                  'math_desc': "\theta^* = \operatorname{argmin}_\theta  G(Q_m, \theta)",
        #                                  'lang_desc': "Select the parameters that minimises the impurity"
        # }, relationship=tree.optimization_problem)
        # tree_generalization_spec = GeneralizationSpecification.get_or_create({'name': "classification model",
        #                                                   'generalization_language': GeneralizationSpecification.DECISION_TREES
        # }, relationship=tree.generalization_specifications)
        #
        # # ASSUMPTIONS
        #
        # tree_assumptions = Assumption.get_or_create(
        #     {"name": "No Assumptions"},
        #     relationship=tree.assumptions
        # )
        #
        # # COMPLEXITY
        #
        # tree_train_complexity = Complexity.get_or_create(
        #     {"name": "", "big_o": "O(n_{samples}n_{features}\log(n_{samples}))"},
        #     relationship=tree.train_complexity
        # )
        #
        # tree_test_complexity = Complexity.get_or_create(
        #     {"name": "", "big_o": "O(\log(n_{samples}))"},
        #     relationship=tree.test_complexity
        # )
        #
        # tree_space_complexity = Complexity.get_or_create(
        #     {'name': 'linear', 'big_o': 'O(n)'},
        #     relationship=tree.space_complexity
        # )

        # PARAMETERS

        # criterion = gini/entropy -> this is some sort of internal evaluation func./op. problem. it can also be a separate alg?
        # here we have cases where a parameter can have several datatypes. how do we choose the default one?
        # design issue: params which we say are model_params is just model metadata. Only tree_ params are model params

        tree_parameters = Parameter.create(
            {"name": "criterion", "type": Parameter.ALG_PARAM, "datatype": Parameter.FUNCTION},
            {"name": "splitter", "type": Parameter.ALG_PARAM, "datatype": Parameter.DICT},
            {"name": "max_depth", "type": Parameter.ALG_PARAM, "datatype": Parameter.INT},
            {"name": "min_samples_split", "type": Parameter.ALG_PARAM, "datatype": Parameter.REAL},
            {"name": "min_samples_leaf", "type": Parameter.ALG_PARAM, "datatype": Parameter.REAL},
            {"name": "min_weight_fraction_leaf", "type": Parameter.ALG_PARAM, "datatype": Parameter.REAL},
            {"name": "max_features", "type": Parameter.ALG_PARAM, "datatype": Parameter.DICT},
            {"name": "random_state", "type": Parameter.ALG_PARAM, "datatype": Parameter.INT},
            {"name": "min_impurity_decrease", "type": Parameter.ALG_PARAM, "datatype": Parameter.REAL},
            {"name": "class_weight", "type": Parameter.ALG_PARAM, "datatype": Parameter.DICT},
            {"name": "ccp_alpha", "type": Parameter.ALG_PARAM, "datatype": Parameter.REAL},
            # {"name": "classes_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.DISCRETE},
            # {"name": "feature_importances_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.DISCRETE},
            # {"name": "max_features_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.INT},
            # {"name": "n_classes_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.INT},
            # {"name": "n_features_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.INT},
            # {"name": "n_features_in_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.INT},
            # {"name": "feature_names_in_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.DISCRETE},
            # {"name": "n_outputs_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.INT},
            # {"name": "tree_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.OTHER},
        )

        for parameter in tree_parameters:
            tree.parameters.connect(parameter)

        # ANNOTATOR INFO

        tree_annotation = Annotation.nodes.first_or_none(
            annotator_name=tree_dict.get('annotator').get('annotator_name'),
            email=tree_dict.get('annotator').get('email')
        )
        if tree_annotation is None:
            tree_annotation_new = Annotation(
            annotator_name=tree_dict.get('annotator').get('annotator_name'),
            email=tree_dict.get('annotator').get('email')
        ).save()
            tree.annotation.connect(tree_annotation_new)
        else:
            tree.annotation.connect(tree_annotation)

        # ANNOTATOR INFO

        # tree_annotation = Annotation.get_or_create(
        #     {'annotator_name': 'Your Name', 'email': 'abc.xyz@gmail.com'},
        #     relationship=tree.annotation
        # )

        #
        # Gausian Naive Bayes
        #

        nb_dict = {
            'name': 'GaussianNB',
            'doc_name': 'UPDATING FORMULAE AND A PAIRWISE ALGORITHM FOR COMPUTING SAMPLE VARIANCES',
            'doc_id': 'STAN-CS-79-773',
            'dataset_name': 'multi-class classification dataset',
            'task_name': 'supervised multi-class classification task',
            'task_mode': Task.BATCH,
            'op_problem': 'Bound Constrained',
            'op_problem_text': 'Maximize the posterior probability given the training data in order to formulate the decision rule',
            'op_problem_maths': 'P(y \mid x_1, \dots, x_n) \propto P(y) \prod_{i=1}^{n} P(x_i \mid y)\\\Downarrow\\\hat{y} = \arg\max_y P(y) \prod_{i=1}^{n} P(x_i \mid y)',
            'generalization_spec_name': 'probability distribution specification',
            'generalization_language': GeneralizationSpecification.BAYES,
            'assumptions':
                ["Conditional independence between every pair of features given the value of the class variable",
                 "The likelihood of the features is assumed to be Gaussian"],
            'train_complexity': {'name': 'linear time',
                                 'big_o': 'O(n)',
                                 'train_time_complexity_maths': 'O(n_{samples}n_{features})'},
            # 'test_complexity': {'name': 'Linear complexity', 'big_o': 'O(n)'},
            # 'space_complexity': {'name': 'Linear complexity', 'big_o': 'O(n)'},
            'annotator': {'annotator_name': 'Your Name', 'email': 'abc.xyz@gmail.com'}
        }

        nb = DataMiningAlgorithm(name=nb_dict.get('name')).save()

        nb_doc = Document.nodes.first_or_none(
            name=nb_dict.get('doc_name'),
            document_id=nb_dict.get('doc_id'))
        if nb_doc is None:
            nb_doc_new = Document(
                name=nb_dict.get('doc_name'),
                document_id=nb_dict.get('doc_id')).save()
            nb.documents.connect(nb_doc_new)
        else:
            nb.documents.connect(nb_doc)

        # IO

        # dataset
        nb_dataset = Dataset.nodes.first_or_none(
            name=nb_dict.get('dataset_name')
        )
        if nb_dataset is None:
            nb_dataset_new = Dataset(
                name=nb_dict.get('dataset_name')
            ).save()
            nb.datasets.connect(nb_dataset_new)
        else:
            nb.datasets.connect(nb_dataset)

        # task
        nb_task = Task.nodes.first_or_none(
            name=nb_dict.get('task_name'),
            mode=nb_dict.get('task_mode')
        )

        if nb_task is None:
            nb_task_new = Task(
                name=nb_dict.get('task_name'),
                mode=nb_dict.get('task_mode')
            ).save()
            nb.tasks.connect(nb_task_new)
        else:
            nb.tasks.connect(nb_task)

        # op problem
        nb_op_problem = OptimizationProblem.nodes.first_or_none(
            name=nb_dict.get('op_problem'),
            math_desc=nb_dict.get('op_problem_maths'),
            lang_desc=nb_dict.get('op_problem_text')
        )

        if nb_op_problem is None:
            nb_op_problem_new = OptimizationProblem(
                name=nb_dict.get('op_problem'),
                math_desc=nb_dict.get('op_problem_maths'),
                lang_desc=nb_dict.get('op_problem_text')
            ).save()
            nb.optimization_problem.connect(nb_op_problem_new)
        else:
            nb.optimization_problem.connect(nb_op_problem)


        # generalization spec
        nb_generalization_spec = GeneralizationSpecification.nodes.first_or_none(
            name=nb_dict.get('generalization_spec_name'),
            generalization_language=nb_dict.get('generalization_language')
        )

        if nb_generalization_spec is None:
            nb_generalization_spec_new = GeneralizationSpecification(
                name=nb_dict.get('generalization_spec_name'),
                generalization_language=nb_dict.get('generalization_language')
            ).save()
            nb.generalization_specifications.connect(nb_generalization_spec_new)
        else:
            nb.generalization_specifications.connect(nb_generalization_spec)

        # nb_generalization_spec = GeneralizationSpecification.get_or_create({"name": "regression model",
        #                                                   "generalization_language": GeneralizationSpecification.OTHER
        # }, relationship=nb.generalization_specifications)

        # ASSUMPTIONS

        for assumption in nb_dict.get('assumptions'):
            assumption_exists = Assumption.nodes.first_or_none(name=assumption)
            if assumption_exists is None:
                assumption_new = Assumption(name=assumption).save()
                nb.assumptions.connect(assumption_new)
            else:
                nb.assumptions.connect(assumption_exists)

        # COMPLEXITY

        # train
        train = Complexity.nodes.first_or_none(
            name=nb_dict.get('train_complexity').get('name'),
            big_o=nb_dict.get('train_complexity').get('big_o'),
            description=nb_dict.get('train_complexity').get('train_time_complexity_maths')
        )

        if train is None:
            train_new = Complexity(
                name=nb_dict.get('train_complexity').get('name'),
                big_o=nb_dict.get('train_complexity').get('big_o'),
                description=nb_dict.get('train_complexity').get('train_time_complexity_maths')
            ).save()
            nb.train_complexity.connect(train_new)
        else:
            nb.train_complexity.connect(train)

        # # test
        # test = Complexity.nodes.first_or_none(
        #     name=nb_dict.get('test_complexity').get('name'),
        #     big_o=nb_dict.get('test_complexity').get('big_o')
        # )
        # if test is None:
        #     test_new = Complexity(
        #         name=nb_dict.get('test_complexity').get('name'),
        #         big_o=nb_dict.get('test_complexity').get('big_o')
        #     ).save()
        #     nb.test_complexity.connect(test_new)
        # else:
        #     nb.test_complexity.connect(test)
        #
        # # space
        # space = Complexity.nodes.first_or_none(
        #     name=nb_dict.get('space_complexity').get('name'),
        #     big_o=nb_dict.get('space_complexity').get('big_o')
        # )
        # if space is None:
        #     space_new = Complexity(
        #         name=nb_dict.get('space_complexity').get('name'),
        #         big_o=nb_dict.get('space_complexity').get('big_o')
        #     ).save()
        #     nb.space_complexity.connect(space_new)
        # else:
        #     nb.space_complexity.connect(space)

        # ANNOTATOR INFO

        nb_annotation = Annotation.nodes.first_or_none(
            annotator_name=nb_dict.get('annotator').get('annotator_name'),
            email=nb_dict.get('annotator').get('email')
        )
        if nb_annotation is None:
            nb_annotation_new = Annotation(
            annotator_name=nb_dict.get('annotator').get('annotator_name'),
            email=nb_dict.get('annotator').get('email')
        ).save()
            nb.annotation.connect(nb_annotation_new)
        else:
            nb.annotation.connect(nb_annotation)

        # METADATA

        # nb = DataMiningAlgorithm(name="GaussianNB").save()
        # nb_doc = Document.get_or_create({
        #     'name': "UPDATING FORMULAE AND A PAIRWISE ALGORITHM FOR COMPUTING SAMPLE VARIANCES",
        #     'document_id': "STAN-CS-79-773"
        # }, relationship=nb.documents)
        #
        # # IO
        #
        # nb_dataset = Dataset.get_or_create({'name': "multi-class classification dataset"}, relationship=nb.datasets)
        # nb_task = Task.get_or_create({'name': "supervised multi-class classification task", 'mode': Task.BATCH}, relationship=nb.tasks)
        #
        # # TODO: NB doesn't have an op_problem it just computes probabilties based on Bayes theorem
        # # Instead it estimates parameters of a distribution. parameter estimation as an op_problem
        #
        # # op_problem = OptimizationProblem(name="",
        # #                                  math_desc="",
        # #                                  lang_desc=""
        # #                                  ).save()
        # # alg.optimization_problem.connect(op_problem)
        #
        # nb_generalization_spec = GeneralizationSpecification.get_or_create({'name':"probability distribution specification",
        #                                                   'generalization_language': GeneralizationSpecification.BAYES
        #                                                                     }, relationship=nb.generalization_specifications)
        #
        # # ASSUMPTIONS
        #
        # nb_assumptions = Assumption.get_or_create(
        #     {"name": "Conditional independence between every pair of features given the value of the class variable"},
        #     {"name": "The likelihood of the features is assumed to be Gaussian:"},
        #     relationship=nb.assumptions
        # )
        #
        # # for assumption in nb_assumptions:
        # #     nb.assumptions.connect(assumption)
        #
        # # COMPLEXITY
        #
        # nb_train_complexity = Complexity.get_or_create(
        #     {'name': 'Linear complexity', 'big_o': 'O(n)'},
        #     relationship=nb.train_complexity
        # )
        #
        # nb_test_complexity = Complexity.get_or_create(
        #     {'name': 'Linear complexity', 'big_o': 'O(n)'},
        #     relationship=nb.test_complexity
        # )
        #
        # # alg_space_complexity = Complexity.get_or_create(
        # #     {"name": "", "big_o": ""},
        # # )


        # PARAMETERS

        nb_parameters = Parameter.create(
            {"name": "priors", "type": Parameter.ALG_PARAM, "datatype": Parameter.DISCRETE},
            {"name": "var_smoothing", "type": Parameter.ALG_PARAM, "datatype": Parameter.REAL},
            # {"name": "class_count_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.DISCRETE},
            # {"name": "class_prior_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.DISCRETE},
            # {"name": "classes_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.DISCRETE},
            # {"name": "epsilon_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.REAL},
            # {"name": "n_features_in_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.INT},
            # {"name": "feature_names_in_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.DISCRETE},
            # {"name": "var_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.DISCRETE},
            # {"name": "theta_", "type": Parameter.MODEL_PARAM, "datatype": Parameter.DISCRETE},
            relationship=nb.parameters
        )
        #
        for parameter in nb_parameters:
            nb.parameters.connect(parameter)

        # ANNOTATOR INFO

        nb_annotation = Annotation.get_or_create(
            {'annotator_name': 'Your Name', 'email': 'abc.xyz@gmail.com'},
            relationship=nb.annotation
        )

        ### ENSEMBLE example

        ensemble = DataMiningAlgorithm(name='ensemble', ensemble=True).save()


        self.stdout.write(self.style.SUCCESS('Database population with algorithms sucessful'))
        # except Exception as e:
        #     raise CommandError('Database population with algorithms failed: %s' % e)