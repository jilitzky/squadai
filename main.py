import scenarios

def run_scenario(scenario):
    print(f"--- SCENARIO: {scenario.NAME} ---")
    scenario.run()

if __name__ == "__main__":
    run_scenario(scenarios.coordinated_attack)
