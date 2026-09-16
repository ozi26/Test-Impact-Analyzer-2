# =============================================================================
# ORDER SERVICE TESTS
# Tests for the Order Service microservice.
# These tests verify that the Order Service works correctly.
# =============================================================================

import sys
from pathlib import Path

# Add the project root to Python's path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

# Import the OrderService class
from sample_microservices.order_service import OrderService


def test_order_timeout_config():
    """
    Test that the Order Service correctly reads its timeout configuration.
    
    This test verifies that the timeout setting is loaded from the
    configuration file and has a reasonable value.
    """
    # Create the service
    service = OrderService()
    
    # Get the timeout
    timeout = service.get_timeout()
    
    # Verify the timeout is a positive number
    assert timeout > 0, "Timeout should be positive"
    assert isinstance(timeout, (int, float)), "Timeout should be a number"
    
    print(f"  Order timeout is: {timeout}")


def test_order_retry_config():
    """
    Test that the Order Service correctly reads its retry configuration.
    
    This test verifies that the retry attempts setting is loaded from
    the configuration file and has a reasonable value.
    """
    # Create the service
    service = OrderService()
    
    # Get the retry attempts
    retry_attempts = service.get_retry_attempts()
    
    # Verify the retry attempts is a positive integer
    assert retry_attempts > 0, "Retry attempts should be positive"
    assert isinstance(retry_attempts, int), "Retry attempts should be an integer"
    
    print(f"  Order retry attempts: {retry_attempts}")


def test_process_order_success():
    """
    Test that processing an order succeeds with valid inputs.
    
    This test verifies that the Order Service can successfully
    process an order.
    """
    # Create the service
    service = OrderService()
    
    # Process an order
    result = service.process_order(
        order_id="ORDER-001",
        product_id="PRODUCT-001",
        quantity=2,
    )
    
    # Verify the result
    assert result["status"] == "SUCCESS", "Order should succeed"
    assert result["order_id"] == "ORDER-001", "Order ID should match"
    assert result["product_id"] == "PRODUCT-001", "Product ID should match"
    assert result["quantity"] == 2, "Quantity should match"
    assert result["total_price"] > 0, "Total price should be positive"
    
    print(f"  Order processed: {result['order_id']}")
    print(f"  Total price: ${result['total_price']:.2f}")


# This block runs when the script is executed directly
if __name__ == "__main__":
    print("Running Order Service tests...")
    
    test_order_timeout_config()
    print("  ✓ test_order_timeout_config passed")
    
    test_order_retry_config()
    print("  ✓ test_order_retry_config passed")
    
    test_process_order_success()
    print("  ✓ test_process_order_success passed")
    
    print("\nAll Order Service tests passed!")