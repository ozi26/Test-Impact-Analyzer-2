# =============================================================================
# INVENTORY SERVICE TESTS
# Tests for the Inventory Service microservice.
# These tests verify that the Inventory Service works correctly.
# =============================================================================

import sys
from pathlib import Path

# Add the project root to Python's path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

# Import the InventoryService class
from sample_microservices.inventory_service import InventoryService


def test_inventory_retry_config():
    """
    Test that the Inventory Service correctly reads its retry configuration.
    
    This test verifies that the retry attempts setting is loaded from
    the configuration file and has a reasonable value.
    """
    # Create the service
    service = InventoryService()
    
    # Get the retry attempts
    retry_attempts = service.get_retry_attempts()
    
    # Verify the retry attempts is a positive integer
    assert retry_attempts > 0, "Retry attempts should be positive"
    assert isinstance(retry_attempts, int), "Retry attempts should be an integer"
    
    print(f"  Inventory retry attempts: {retry_attempts}")


def test_inventory_retry_delay():
    """
    Test that the Inventory Service correctly reads its retry delay.
    
    This test verifies that the retry delay setting is loaded from
    the configuration file and has a reasonable value.
    """
    # Create the service
    service = InventoryService()
    
    # Get the retry delay
    retry_delay = service.get_retry_delay()
    
    # Verify the retry delay is a positive number
    assert retry_delay > 0, "Retry delay should be positive"
    assert isinstance(retry_delay, (int, float)), "Retry delay should be a number"
    
    print(f"  Inventory retry delay: {retry_delay}")


def test_check_availability():
    """
    Test that checking availability works correctly.
    
    This test verifies that the Inventory Service can successfully
    check product availability.
    """
    # Create the service
    service = InventoryService()
    
    # Check availability
    result = service.check_availability(
        product_id="PRODUCT-001",
        quantity=2,
    )
    
    # Verify the result
    assert "available" in result, "Result should contain 'available'"
    assert "stock_level" in result, "Result should contain 'stock_level'"
    assert result["product_id"] == "PRODUCT-001", "Product ID should match"
    assert result["requested"] == 2, "Requested quantity should match"
    
    print(f"  Availability check: {result['available']}")
    print(f"  Stock level: {result['stock_level']}")


# This block runs when the script is executed directly
if __name__ == "__main__":
    print("Running Inventory Service tests...")
    
    test_inventory_retry_config()
    print("  ✓ test_inventory_retry_config passed")
    
    test_inventory_retry_delay()
    print("  ✓ test_inventory_retry_delay passed")
    
    test_check_availability()
    print("  ✓ test_check_availability passed")
    
    print("\nAll Inventory Service tests passed!")