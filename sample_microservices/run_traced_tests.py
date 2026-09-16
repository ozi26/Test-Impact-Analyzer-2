# =============================================================================
# RUN TRACED TESTS
# This module demonstrates how to run tests with configuration access
# tracking enabled. It shows how the tracing system records which
# configuration settings each test uses.
# =============================================================================

import sys                      # For modifying Python path
from pathlib import Path        # For working with file paths

# Add the project root to Python's path so we can import our modules
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

# Import our tracing functions
from analyzer.telemetry import configure_tracing
from analyzer.tracing import (
    trace_test,              # Context manager for tracing tests
    record_config_access,    # Function to record config access
    get_selector,            # Function to get the global selector
    reset_selector,          # Function to reset the selector
)


def run_test(test_id, config_file, config_keys, test_func):
    """
    Run a single test with configuration access tracking.
    
    This function:
    1. Sets up tracing
    2. Runs the test function inside a traced context
    3. Records which configuration settings were accessed
    
    Args:
        test_id: A unique identifier for the test
        config_file: The path to the configuration file
        config_keys: A list of configuration keys the test uses
        test_func: The test function to run
    
    Returns:
        The result of the test function.
    """
    # Configure tracing (creates a fresh exporter)
    exporter = configure_tracing()
    
    # Run the test inside a traced context
    with trace_test(test_id):
        # Record each configuration setting the test uses
        for key in config_keys:
            record_config_access(test_id, key)
        
        # Run the actual test function
        result = test_func()
    
    # Flush the exporter to ensure all spans are recorded
    exporter.force_flush()
    
    # Return the test result
    return result


def sample_test_checkout():
    """
    A sample test that simulates a checkout flow.
    
    This test uses multiple configuration settings.
    """
    print("  Running checkout test...")
    return {"status": "PASSED"}


def sample_test_inventory():
    """
    A sample test that simulates checking inventory.
    
    This test uses inventory-related configuration settings.
    """
    print("  Running inventory test...")
    return {"status": "PASSED"}


def sample_test_pricing():
    """
    A sample test that simulates getting a price.
    
    This test uses pricing-related configuration settings.
    """
    print("  Running pricing test...")
    return {"status": "PASSED"}


def main():
    """
    Main function that runs all sample tests and demonstrates
    the configuration tracking system.
    """
    print("=" * 60)
    print("RUNNING TRACED TESTS WITH CONFIGURATION TRACKING")
    print("=" * 60)
    
    # Reset the selector to start fresh
    reset_selector()
    
    # Get the global selector
    selector = get_selector()
    
    # Run each test with its configuration dependencies
    print("\n1. Running TestCheckout...")
    run_test(
        test_id="TestCheckout",
        config_file="sample_microservices/config/order_config.yaml",
        config_keys=[
            "order.timeout",
            "order.retry.attempts",
        ],
        test_func=sample_test_checkout,
    )
    
    print("\n2. Running TestInventory...")
    run_test(
        test_id="TestInventory",
        config_file="sample_microservices/config/inventory_config.yaml",
        config_keys=[
            "inventory.retry.attempts",
            "inventory.retry.delay",
        ],
        test_func=sample_test_inventory,
    )
    
    print("\n3. Running TestPricing...")
    run_test(
        test_id="TestPricing",
        config_file="sample_microservices/config/pricing_config.yaml",
        config_keys=[
            "pricing.cache.refresh_interval",
            "pricing.database.timeout",
        ],
        test_func=sample_test_pricing,
    )
    
    # Print the recorded dependencies
    print("\n" + "=" * 60)
    print("RECORDED TEST DEPENDENCIES")
    print("=" * 60)
    
    all_deps = selector.get_all_dependencies()
    for test_id, deps in all_deps.items():
        print(f"\n{test_id}:")
        for dep in sorted(deps):
            print(f"  - {dep}")
    
    # Demonstrate test selection
    print("\n" + "=" * 60)
    print("DEMONSTRATING TEST SELECTION")
    print("=" * 60)
    
    # Simulate a configuration change
    changed_settings = ["inventory.retry.attempts"]
    print(f"\nSimulating change to: {changed_settings}")
    
    # Select affected tests
    affected = selector.select_tests(changed_settings)
    
    print(f"\nAffected tests ({len(affected)}):")
    for item in affected:
        print(f"  - {item['test']} (affected by: {item['settings']})")
    
    # Another simulation
    changed_settings = ["order.timeout", "pricing.database.timeout"]
    print(f"\nSimulating change to: {changed_settings}")
    
    affected = selector.select_tests(changed_settings)
    
    print(f"\nAffected tests ({len(affected)}):")
    for item in affected:
        print(f"  - {item['test']} (affected by: {item['settings']})")
    
    print("\n" + "=" * 60)
    print("TEST COMPLETE")
    print("=" * 60)


# This block runs when the script is executed directly
if __name__ == "__main__":
    main()