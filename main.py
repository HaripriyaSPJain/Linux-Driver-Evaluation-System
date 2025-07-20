from evaluator.evaluate import evaluate_driver
import json

if __name__ == "__main__":
    result = evaluate_driver("drivers/model_generated_driver.c")
    with open("results/evaluation_output.json", "w") as f:
        json.dump(result, f, indent=4)
    print("Evaluation Complete. Results saved.")
    print(json.dumps(result, indent=4))