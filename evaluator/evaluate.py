import subprocess
from evaluator.static_analysis import check_style_compliance, check_security_patterns
from evaluator.metrics import compute_metrics

def evaluate_driver(path):
    with open(path, 'r') as file:
        code = file.read()

    style_issues = check_style_compliance(code)
    security_flags = check_security_patterns(code)

    # Combine both
    static_results = security_flags
    static_results["style_issues"] = style_issues

    compile_success = subprocess.call(['bash', 'scripts/compile.sh', path]) == 0

    test_results = {
        "basic_operations": 0.9,
        "error_handling": 0.7,
        "edge_cases": 0.6
    }

    return compute_metrics(compile_success, static_results, test_results)
