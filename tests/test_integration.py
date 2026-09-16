# =============================================================================
# INTEGRATION TESTS
# End-to-end tests that verify multiple services work together.
# These tests exercise the complete order processing flow.
# =============================================================================

import sys
from pathlib import Path

# Add the project root to Python's path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

# Import all services
from sample_microservices.order_service import OrderService
from sample_microservices.inventory_service import InventoryService
from sample_microservices.pricing_service import PricingService


def test_full_order_flow():
    """
    Test the complete order processing flow.
    
    This integration test verifies that all three services
    (Order, Inventory, Pricing) work together correctly.
    """
    # Create all services
    order_service = OrderService()
    inventory_service = InventoryService()
    pricing_service = PricingService()
    
    # Process an order
    order_result = order_service.process_order(
        order_id="ORDER-INT-001",
        product_id="PRODUCT-INT-001",
        quantity=3,
    )
    
    # Verify the order result
    assert order_result["status"] == "SUCCESS", "Order should succeed"
    assert order_result["order_id"] == "ORDER-INT-001", "Order ID should match"
    
    # Check inventory availability
    inventory_result = inventory_service.check_availability(
        product_id="PRODUCT-INT-001",
        quantity=3,
    )
    
    # Verify the inventory result
    assert inventory_result["available"], "Product should be available"
    
    # Get the price
    pricing_result = pricing_service.get_price(
        product_id="PRODUCT-INT-001",
        quantity=3,
    )
    
    # Verify the pricing result
    assert pricing_result["total_price"] > 0, "Total price should be positive"
    
    print(f"  Full order flow completed:")
    print(f"    Order ID: {order_result['order_id']}")
    print(f"    Total price: ${pricing_result['total_price']:.2f}")


def test_configuration_consistency():
    """
    Test that configuration settings are consistent across services.
    
    This test verifies that the configuration settings loaded by
    different services are reasonable and consistent.
    """
    # Create all services
    order_service = OrderService()
    inventory_service = InventoryService()
    pricing_service = PricingService()
    
    # Get configuration values from each service
    order_timeout = order_service.get_timeout()
    inventory_retry = inventory_service.get_retry_attempts()
    pricing_db_timeout = pricing_service.get_db_timeout()
    
    # Verify all values are positive
    assert order_timeout > 0, "Order timeout should be positive"
    assert inventory_retry > 0, "Inventory retry should be positive"
    assert pricing_db_timeout > 0, "Pricing DB timeout should be positive"
    
    # Verify timeouts are reasonable (less than 60 seconds)
    assert order_timeout < 60, "Order timeout should be less than 60 seconds"
    assert pricing_db_timeout < 60, "Pricing DB timeout should be less than 60 seconds"
    
    print(f"  Configuration consistency check passed:")
    print(f"    Order timeout: {order_timeout}s")
    print(f"    Inventory retry: {inventory_retry}")
    print(f"    Pricing DB timeout: {pricing_db_timeout}s")


# This block runs when the script is executed directly
if __name__ == "__main__":
    print("Running Integration tests...")
    
    test_full_order_flow()
    print("  ✓ test_full_order_flow passed")
    
    test_configuration_consistency()
    print("  ✓ test_configuration_consistency passed")
    
    print("\nAll Integration tests passed!")