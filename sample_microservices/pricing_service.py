# =============================================================================
# PRICING SERVICE
# This is a sample microservice that handles pricing calculations.
# It simulates communication with other services and uses configuration
# settings that can be changed at runtime.
# =============================================================================

import time                     # For simulating network delays
from pathlib import Path        # For working with file paths
import yaml                     # For loading YAML configuration


class PricingService:
    """
    A simple microservice that handles pricing calculations.
    
    This service calculates prices and manages pricing rules.
    
    Example:
        service = PricingService("sample_microservices/config")
        result = service.get_price("PRODUCT-456", 2)
        # result contains pricing information
    """
    
    def __init__(self, config_dir="sample_microservices/config"):
        """
        Initialize the Pricing Service.
        
        Args:
            config_dir: Directory containing configuration files
        """
        # Store the configuration directory path
        self.config_dir = Path(config_dir)
        
        # Load the configuration for this service
        self.config = self._load_config()
    
    def _load_config(self):
        """
        Load configuration from the YAML file.
        
        Returns:
            A dictionary with configuration settings.
        """
        # Build the path to the config file
        config_path = self.config_dir / "pricing_config.yaml"
        
        # Open and parse the YAML file
        with open(config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    
    def get_cache_refresh_interval(self):
        """
        Get the cache refresh interval for this service.
        
        Returns:
            The interval in seconds.
        """
        # Read the cache refresh interval from the configuration
        # The default is 60 seconds if not specified
        return self.config.get("pricing", {}).get("cache", {}).get("refresh_interval", 60)
    
    def get_db_timeout(self):
        """
        Get the database timeout for this service.
        
        Returns:
            The timeout in seconds.
        """
        # Read the database timeout from the configuration
        # The default is 2 seconds if not specified
        return self.config.get("pricing", {}).get("database", {}).get("timeout", 2)
    
    def get_price(self, product_id, quantity):
        """
        Get the price for a product.
        
        Args:
            product_id: The product to price
            quantity: The quantity being purchased
        
        Returns:
            A dictionary with pricing information.
        """
        # Get our configuration settings
        cache_interval = self.get_cache_refresh_interval()
        db_timeout = self.get_db_timeout()
        
        # Simulate calculating the price
        time.sleep(0.005)  # 5 milliseconds
        
        # Simulated base price
        base_price = 29.99
        total_price = base_price * quantity
        
        # Return the result
        return {
            "product_id": product_id,
            "quantity": quantity,
            "unit_price": base_price,
            "total_price": total_price,
            "cache_interval": cache_interval,
            "db_timeout": db_timeout,
        }