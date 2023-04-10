from django.core.management.base import BaseCommand, CommandError
from api.models.assumption import Assumption
from api.models.complexity import Complexity
from api.models.optimization_problem import OptimizationProblem

class Command(BaseCommand):
    help = 'Populate the database with assumption, optimization problem and complexity taxonomies.'

    def add_arguments(self, parser):
        pass
        # parser.add_argument('ids', nargs='+', type=int)

    def handle(self, *args, **options):

        try:

            assumptions = Assumption.create(
                {"name": "No assumptions"},
                {'name': 'Independence of observations'},
                {'name': 'No hidden or missing variables'},
                {'name': 'Linear relationship'},
                {'name': 'Normality of residuals'},
                {'name': 'No or little multicollinearity'},
                {'name': 'Homoscedasticity'},
                {'name': 'All independent variables are uncorrelated with the error term'},
                {'name': 'Observations of the error term are uncorrelated with each other'},
                {"name": "Similar things exist in close proximity"},
                {"name": "Conditional independence between every pair of features given the value of the class variable"},
                {"name": "The likelihood of the features is assumed to be Gaussian"}
            )

            op_problems = OptimizationProblem.create(
                {'name': 'Stochastic Programming'},
                {'name': 'Robust Optimization'},
                {'name': 'Nonlinear Least Squares'},
                {'name': 'Nonlinear Equations'},
                {'name': 'Nondifferentiable Optimization'},
                {'name': 'Global Optimization'},
                {'name': 'Network Optimization'},
                {'name': 'Derivative-Free Optimization'},
                {'name': 'Quadratic Programming'},
                {'name': 'Linear Programming'},
                {'name': 'Quadratically-constrained Quadratic Programming'},
                {'name': 'Semiinfinite Programming'},
                {'name': 'Complementarity Problems'},
                {'name': 'Mixed Integer Nonlinear Programming'}
            )

            complexities = Complexity.create(
                {'name': 'Constant complexity', 'big_o': 'O(1)'},
                {'name': 'Inverse Ackermann complexity', 'big_o': 'O(α(n))'},
                {'name': 'Iterated logarithmic complexity', 'big_o': 'O(log* n)'},
                {'name': 'Log-logarithmic complexity', 'big_o': 'O(log log n)'},
                {'name': 'Logarithmic complexity', 'big_o': 'O(log n)'},
                {'name': 'Polylogarithmic complexity', 'big_o': 'poly(log n)'},
                {'name': 'Fractional power complexity', 'big_o': 'O(n^c) where 0 < c < 1'},
                {'name': 'Linear complexity', 'big_o': 'O(n)'},
                {'name': 'n log-star n" complexity', 'big_o': '	O(n log* n)'},
                {'name': 'Linearithmic complexity', 'big_o': 'O(n log n)'},
                {'name': 'Quasilinear complexity', 'big_o': 'n poly(log n)'},
                {'name': 'Quadratic complexity', 'big_o': 'O(n^2)'},
                {'name': 'Cubic complexity', 'big_o': 'O(n^3)'},
                {'name': 'Polynomial complexity', 'big_o': '2^(O(log n)) = poly(n)'},
                {'name': 'Quasi-polynomial complexity', 'big_o': '2^(poly(log n))'},
                {'name': 'Sub-exponential complexity', 'big_o': '2^(o(n))'},
                {'name': 'Exponential complexity (with linear exponent)', 'big_o': '2^(O(n))'},
                {'name': 'Exponential complexity', 'big_o': '2^(poly(n))'},
                {'name': 'Factorial complexity', 'big_o': 'O(n!)'},
                {'name': 'Double exponential complexity', 'big_o': '2^(2^poly(n))'}
            )

            self.stdout.write(self.style.SUCCESS('Database population with taxonomies successful'))
        except Exception as e:
            raise CommandError('Database population with taxonomies failed: %s' % e)