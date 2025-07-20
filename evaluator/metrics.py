def compute_metrics(compilation_success, static_results, test_results):
    # Dynamic style compliance from actual code issues
    style_penalty = 0
    if static_results.get("style_issues") is not None:
        style_penalty = min(0.4, 0.1 * len(static_results["style_issues"]))

    style_compliance = round(max(0.9 - style_penalty, 0.3), 2)

    score = {
        "compilation": {
            "success_rate": 1.0 if compilation_success else 0.0,
            "warnings_count": 0,
            "errors_count": 0 if compilation_success else 1
        },
        "security": {
            k: static_results[k] for k in ['buffer_safety', 'race_conditions', 'input_validation']
        },
        "functionality": test_results,
        "code_quality": {
            "style_compliance": style_compliance,
            "documentation": 0.6,
            "maintainability": 0.7
        },
    }

    # Weighted total score
    score["overall_score"] = round(
        (
            0.4 * score["compilation"]["success_rate"] +
            0.25 * (sum(score["security"].values()) / 3) +
            0.2 * score["code_quality"]["style_compliance"] +
            0.1 * 0.8 +  # assumed performance
            0.05 * 0.3   # assumed advanced feature
        ) * 100,
        1
    )
    return score
