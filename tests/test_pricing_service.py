# =============================================================================
# PRICING SERVICE TESTS
# Tests for the Pricing Service microservice.
# These tests verify that the Pricing Service works correctly.
# =============================================================================

import sys
from pathlib import Path

# Add the project root to Python's path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

# Import the PricingService class
from sample_microservices.pricing_service import PricingService


def test_pricing_cache_config():
    """
    Test that the Pricing Service correctly reads its cache configuration.
    
    This test verifies that the cache refresh interval is loaded from
    the configuration file and has a reasonable value.
    """
    # Create the service
    service = PricingService()
    
    # Get the cache refresh interval
    cache_interval = service.get_cache_refresh_interval()
    
    # Verify the cache interval is a positive number
    assert cache_interval > 0, "Cache interval should be positive"
    assert isinstance(cache_interval, (int, float)), "Cache interval should be a number"
    
    print(f"  Pricing cache interval: {cache_interval}")


def test_pricing_db_timeout():
    """
    Test that the Pricing Service correctly reads its database timeout.
    
    This test verifies that the database timeout setting is loaded from
    the configuration file and has a reasonable value.
    """
    # Create the service
    service = PricingService()
    
    # Get the database timeout
    db_timeout = service.get_db_timeout()
    
    # Verify the db timeout is a positive number
    assert db_timeout > 0, "Database timeout should be positive"
    assert isinstance(db_timeout, (int, float)), "Database timeout should be a number"
    
    print(f"  Pricing database timeout: {db_timeout}")


def test_get_price():
    """
    Test that getting a price works correctly.
    
    This test verifies that the Pricing Service can successfully
    calculate a price.
    """
    # Create the service
    service = PricingService()
    
    # Get a price
    result = service.get_price(
        product_id="PRODUCT-001",
        quantity=2,
    )
    
    # Verify the result
    assert result["product_id"] == "PRODUCT-001", "Product ID should match"
    assert result["quantity"] == 2, "Quantity should match"
    assert result["unit_price"] > 0, "Unit price should be positive"
    assert result["total_price"] > 0, "Total price should be positive"
    assert result["total_price"] == result["unit_price"] * 2, "Total should be unit * quantity"
    
    print(f"  Price calculated: ${result['total_price']:.2f}")


# This block runs when the script is executed directly
if __name__ == "__main__":
    print("Running Pricing Service tests...")
    
    test_pricing_cache_config()
    print("  ✓ test_pricing_cache_config passed")
    
    test_pricing_db_timeout()
    print("  ✓ test_pricing_db_timeout passed")
    
    test_get_price()
    print("  ✓ test_get_price passed")
    
    print("\nAll Pricing Service tests passed!")