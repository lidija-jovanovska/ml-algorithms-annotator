from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models.dm_algorithm import DataMiningAlgorithm
from .models.base_algorithm import Algorithm
from .models.ensemble import EnsembleAlgorithm, BaggingAlgorithm, BoostingAlgorithm, VotingAlgorithm, StackingAlgorithm
from .models.document import Document
from .models.annotation import Annotation
from .models.assumption import Assumption
from .models.complexity import Complexity
from .models.dataset import Dataset
from .models.sampling import Sampling
from .models.generalization import GeneralizationSpecification
from .models.optimization_problem import OptimizationProblem
from .models.parameter import Parameter
from .models.task import Task
from .utils import _validate_email, _generate_token_and_link, _send_email
from datetime import datetime
from neomodel import db
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect


def verify(request, token):
    try:
        user = Annotation.nodes.get(token=token)
        if user:
            user.is_verified = True
            msg = 'The email has been verified'
            # TODO: send email to notify that email was verified
            print(msg)
            return redirect('http://127.0.0.1:8000')
            # return render(request, 'success.html', {'msg': msg})
    except Exception as e:
        msg = e
        print(msg)
        return redirect('')

class SingleGeneralizationAlgorithms(APIView):
    def get(self, request):
        data = DataMiningAlgorithm.nodes.filter(data_mining_entity=True,
                                                ensemble=False)
        algorithms = [alg.name for alg in data]
        return Response(algorithms)

class SimpleAlgorithms(APIView):
    def get(self, request):
        data = Algorithm.nodes.filter(data_mining_entity=False)
        algorithms = [alg.name for alg in data]
        return Response(algorithms)

class DataMiningAlgorithms(APIView):
    def get(self, request):
        data = DataMiningAlgorithm.nodes.filter(data_mining_entity=True)
        algorithms = [alg.name for alg in data]
        return Response(algorithms)


class GetAlgorithms(APIView):
    def get(self, request):
        complexity = request.GET.get('complexity', '').split('-')[0].strip()
        # complexity = 'Quadratic complexity'
        task = request.GET.get('task', '')
        # task = 'supervised regression task'
        op_problem = request.GET.get('optimization_problem', '')
        # op_problem = 'Linear Programming'
        print(complexity)
        print(task)
        print(op_problem)

        algorithms = []

        # task
        if task == '':
            query = """MATCH (n:DataMiningAlgorithm)-[:ADDRESSES]->(t:Task) RETURN n"""
        else:
            query = """MATCH (n:DataMiningAlgorithm)-[:ADDRESSES]->(t:Task) WHERE t.name="{task}" RETURN n""".format(task=task)

        # optimization problem
        if op_problem == '':
            query2 = """MATCH(n:DataMiningAlgorithm)-[:SOLVES]->(op:OptimizationProblem) RETURN n"""
        else:
            query2 = """MATCH(n:DataMiningAlgorithm)-[:SOLVES]->(op:OptimizationProblem) WHERE op.name="{op_problem}" RETURN n""".format(op_problem=op_problem)

        # complexity
        if complexity == '':
            query3 = """MATCH(n:DataMiningAlgorithm)-[:HAS_TRAIN_TIME_COMPLEXITY]->(c:Complexity) RETURN n"""
        else:
            query3 = """MATCH(n:DataMiningAlgorithm)-[:HAS_TRAIN_TIME_COMPLEXITY]->(c:Complexity) WHERE c.name="{complexity}" RETURN n""".format(complexity=complexity)

        if (task == '') and (op_problem == '') and (complexity == ''):
            query4 = """MATCH(n:DataMiningAlgorithm) RETURN n"""
            results, meta = db.cypher_query(query4)
            algorithms = [DataMiningAlgorithm.inflate(row[0]) for row in results]
            print(algorithms)
            data = [algorithm.to_json for algorithm in algorithms]
            return Response(data)
        else:
            results, meta = db.cypher_query(query)
            algorithms1 = [DataMiningAlgorithm.inflate(row[0]) for row in results]

            results, meta = db.cypher_query(query2)
            algorithms2 = [DataMiningAlgorithm.inflate(row[0]) for row in results]

            results, meta = db.cypher_query(query3)
            algorithms3 = [DataMiningAlgorithm.inflate(row[0]) for row in results]
            final = [x for x in algorithms1 if x in algorithms2 and x in algorithms3]
            print(final)
            # algorithms = DataMiningAlgorithm.nodes.all()
            data = [algorithm.to_json for algorithm in final]
            return Response(data)

class PostAnnotation(APIView):


    def post(self, request):
        print(request.data)

        annotator_email = request.data.get("annotator_email", None)
        # validate email
        if _validate_email(annotator_email) == False:
            print("Invalid E-mail")
            return Response(status=status.HTTP_412_PRECONDITION_FAILED)
        else:
            annotator_name = request.data.get("annotator_name", None)
            annotator_affiliation = request.data.get("annotator_affiliation", None)
            annotation_exists = Annotation.nodes.first_or_none(
                annotator_name=annotator_name,
                affiliation=annotator_affiliation,
                email=annotator_email
            )
            if annotation_exists is None:
                # email is valid, generate token
                domain_name = get_current_site(request).domain
                token, link = _generate_token_and_link(domain_name)
                _send_email(annotator_email, link)
                annotation = Annotation(annotator_name=annotator_name,
                                    affiliation=annotator_affiliation,
                                    email=annotator_email,
                                    # creation_date=datetime.now(),
                                    token=token).save()
            else:
                annotation = annotation_exists

            algorithm_name = request.data.get("algorithm_name", None)

            # algorithm type
            algorithm_type = request.data.get("algorithm_type", 'single generalization algorithm')

            if algorithm_type == 'ensemble algorithm':
                algorithm = EnsembleAlgorithm(name=algorithm_name).save()
            elif algorithm_type == 'bagging':
                algorithm = BaggingAlgorithm(name=algorithm_name).save()
            elif algorithm_type == 'boosting':
                algorithm = BoostingAlgorithm(name=algorithm_name).save()
            elif algorithm_type == 'voting':
                algorithm = VotingAlgorithm(name=algorithm_name).save()
            elif algorithm_type == 'stacking':
                algorithm = StackingAlgorithm(name=algorithm_name).save()
            else:
                algorithm = DataMiningAlgorithm(name=algorithm_name).save()

            # connect with annotation
            algorithm.annotation.connect(annotation)

            # documents
            documents = [Document(name=doc["DocumentName"], document_id=doc["DocumentId"]).save() for doc in request.data.get("documents", [])]
            for document in documents:
                existing_doc = Document.nodes.first_or_none(
                    name=document.name,
                    document_id=document.document_id
                )
                if existing_doc is None:
                    document.save()
                    algorithm.documents.connect(document)
                else:
                    algorithm.documents.connect(existing_doc)

            # ensemble fields
            if algorithm_type == 'bagging':
                base_estimator_name = request.data.get('base_estimator', None)
                if base_estimator_name is not None:
                    base_estimator = DataMiningAlgorithm.nodes.filter(name=base_estimator_name)[0]
                    algorithm.base_estimator.connect(base_estimator)
                sampling = request.data.get('sampling', None)
                if sampling is not None:
                    sampling_exists = Sampling.nodes.first_or_none(type=sampling)
                    if sampling_exists is not None:
                        algorithm.sampling.connect(sampling_exists)
                    else:
                        sampling_obj = Sampling(type=sampling).save()
                        algorithm.sampling.connect(sampling_obj)
            elif algorithm_type == 'boosting':
                base_estimator_name = request.data.get('base_estimator', None)
                if base_estimator_name is not None:
                    base_estimator = DataMiningAlgorithm.nodes.filter(name=base_estimator_name).first()
                    algorithm.base_estimator.connect(base_estimator)
            elif algorithm_type == 'voting':
                estimator_names = request.data.get('selected_data_mining_algorithms', None)
                if estimator_names is not None:
                    estimators = DataMiningAlgorithm.nodes.filter(name__in=estimator_names)
                    for estimator in estimators:
                        algorithm.estimators.connect(estimator)
            elif algorithm_type == 'stacking':
                estimator_names = request.data.get('selected_data_mining_algorithms', None)
                if estimator_names is not None:
                    estimators = DataMiningAlgorithm.nodes.filter(name__in=estimator_names)
                    for estimator in estimators:
                        algorithm.estimators.connect(estimator)
                final_estimator_name = request.data.get('data_mining_algorithm_final_estimator', None)
                if final_estimator_name is not None:
                    final_estimator = DataMiningAlgorithm.nodes.filter(name=final_estimator_name)[0]
                    algorithm.final_estimator.connect(final_estimator)


            # constituent algorithms
            simple_algorithm_names = request.data.get('selected_simple_algorithms', None)
            if simple_algorithm_names is not None:
                simple_algorithms = Algorithm.nodes.filter(data_mining_entity=False,
                                                          name__in=simple_algorithm_names)
                for simple_algorithm in simple_algorithms:
                    algorithm.algorithms.connect(simple_algorithm)
            new_simple_algorithm_names = request.data.get('new_simple_algorithms', None)
            if new_simple_algorithm_names is not None:
                for new_simple_algorithm_name in new_simple_algorithm_names:
                    new_simple_algorithm_exists = Algorithm.nodes.first_or_none(name=new_simple_algorithm_name)
                    if new_simple_algorithm_exists is None:
                        new_simple_algorithm = Algorithm(name=new_simple_algorithm_name).save()
                        algorithm.algorithms.connect(new_simple_algorithm)
                    else:
                        algorithm.algorithms.connect(new_simple_algorithm_exists)

            # datasets
            datasets = [Dataset(name=dataset["label"]).save() for dataset in request.data.get("datasets", [])]
            for dataset in datasets:
                existing_dataset = Dataset.nodes.first_or_none(
                    name=dataset.name
                )
                if existing_dataset is None:
                    dataset.save()
                    algorithm.datasets.connect(dataset)
                else:
                    algorithm.datasets.connect(existing_dataset)


            # tasks
            batch_mode = request.data.get("batch_mode", True)
            tasks = [Task(name=task["label"], mode=batch_mode).save() for task in request.data.get("tasks", [])]
            for task in tasks:
                task_exists = Task.nodes.first_or_none(
                    name=task.name,
                    mode=task.mode
                )
                if task_exists is None:
                    task.save()
                    algorithm.tasks.connect(task)
                else:
                    algorithm.tasks.connect(task_exists)


            # optimization problems
            op_problem_text = request.data.get('op_problem_text', None)
            op_problem_maths = request.data.get('op_problem_maths', None)
            op_problems = [OptimizationProblem(name=op_problem["label"],
                                               lang_desc=op_problem_text,
                                               math_desc=op_problem_maths) for op_problem in request.data.get("op_problems", [])]
            for op_problem in op_problems:
                op_problem_exists = OptimizationProblem.nodes.first_or_none(
                    name=op_problem.name,
                    lang_desc=op_problem_text,
                    math_desc=op_problem_maths
                )
                if op_problem_exists is None:
                    op_problem.save()
                    algorithm.optimization_problem.connect(op_problem)
                else:
                    algorithm.optimization_problem.connect(op_problem_exists)


            # generalization specification
            generalization_language = request.data.get("generalization_language", 6)
            generalization_specifications = [GeneralizationSpecification(name=generalization_spec["label"], generalization_language=generalization_language).save() for generalization_spec in request.data.get("generalization_specifications", [])]
            for generalization_spec in generalization_specifications:
                generalization_spec_exists = GeneralizationSpecification.nodes.first_or_none(
                    name=generalization_spec.name,
                    generalization_language=generalization_spec.generalization_language
                )
                if generalization_spec_exists is None:
                    generalization_spec.save()
                    algorithm.generalization_specifications.connect(generalization_spec)
                else:
                    algorithm.generalization_specifications.connect(generalization_spec_exists)


            # assumptions
            assumptions_data = request.data.get("assumptions", ["No assumptions"])
            assumptions = [Assumption(name=assumption_name) for assumption_name in assumptions_data]

            for assumption in assumptions:
                # assumption_exists = Assumption
                assumption_exists = Assumption.nodes.first_or_none(name=assumption.name)
                if assumption_exists is None:
                    assumption.save()
                    algorithm.assumptions.connect(assumption)
                else:
                    algorithm.assumptions.connect(assumption_exists)
            
            
            # new assumptions
            new_assumptions_data = request.data.get("new_assumptions", None)
            if new_assumptions_data:
                new_assumptions = [Assumption(name=new_assumption["Assumption"]).save() for new_assumption in new_assumptions_data]
                for new_assumption in new_assumptions:
                    new_assumption_exists = Assumption.nodes.first_or_none(name=new_assumption.name)
                    if new_assumption_exists is None:
                        new_assumption.save()
                        algorithm.assumptions.connect(new_assumption)
                    else:
                        algorithm.assumptions.connect(new_assumption_exists)


            # train complexity
            train_complexity = request.data.get("train_time_complexity", None)
            train_time_complexity_maths = request.data.get("train_time_complexity_maths", None)
            if train_complexity:
                name, big_o = train_complexity.split(" - ")
                train_complexity = Complexity(name=name, big_o=big_o, description=train_time_complexity_maths)
                train_complexity_exists = Complexity.nodes.first_or_none(name=name,
                                                                         big_o=big_o,
                                                                         description=train_time_complexity_maths)
                if train_complexity_exists is None:
                    train_complexity.save()
                    algorithm.train_complexity.connect(train_complexity)
                else:
                    algorithm.train_complexity.connect(train_complexity_exists)


            # # test complexity
            # test_complexity = request.data.get("test_time_complexity", None)
            # if test_complexity:
            #     name, big_o = test_complexity.split(" - ")
            #     test_complexity = Complexity(name=name, big_o=big_o)
            #     test_complexity_exists = Complexity.nodes.first_or_none(name=name, big_o=big_o)
            #     if test_complexity_exists is None:
            #         test_complexity.save()
            #         algorithm.test_complexity.connect(test_complexity)
            #     else:
            #         algorithm.test_complexity.connect(test_complexity_exists)
            #
            #
            # # space complexity
            # space_complexity = request.data.get("space_time_complexity", None)
            # if space_complexity:
            #     name, big_o = space_complexity.split(" - ")
            #     space_complexity = Complexity(name=name, big_o=big_o)
            #     space_complexity_exists = Complexity.nodes.first_or_none(name=name, big_o=big_o)
            #     if space_complexity_exists is None:
            #         space_complexity.save()
            #         algorithm.space_complexity.connect(space_complexity)
            #     else:
            #         algorithm.space_complexity.connect(space_complexity_exists)


            # parameters
            datatype_map = {
                'integer': 3,
                'boolean': 4,
                'real': 5,
                'dictionary': 6,
                'discrete': 7,
                'other': 8,
                'function': 9
            }

            algorithm_parameters = request.data.get("algorithm_parameters", None)
            if algorithm_parameters:
                for algorithm_parameter in algorithm_parameters:
                    algorithm_parameter_obj = Parameter(name=algorithm_parameter["parameterName"],
                                                        type=Parameter.ALG_PARAM,
                                                        datatype=datatype_map[algorithm_parameter["parameterDatatype"]]).save()
                    algorithm.parameters.connect(algorithm_parameter_obj)


            # return Response(
            #     status=status.HTTP_200_OK
            # )
            return Response({"alg_id": algorithm.id,
                             "alg_type": algorithm_type,
                             "doc_ids": [doc.id for doc in documents],
                             "dataset_ids": [dataset.id for dataset in datasets],
                             "task_ids": [task.id for task in tasks],
                             "op_problem_ids": [op_problem.id for op_problem in op_problems],
                             "generalization_specification_ids": [generalization_specification.id for generalization_specification in generalization_specifications],
                             "assumption_ids": [assumption.id for assumption in algorithm.assumptions],
                             "train_complexity_id": [obj.id for obj in algorithm.train_complexity.all() if obj],
                             "test_complexity_id": [obj.id for obj in algorithm.test_complexity.all() if obj],
                             "space_complexity_id": [obj.id for obj in algorithm.space_complexity.all() if obj],
                             "parameter_ids": [obj.id for obj in algorithm.parameters.all() if obj],
                             "annotation_id": [obj.id for obj in algorithm.annotation.all() if obj]
                             })

