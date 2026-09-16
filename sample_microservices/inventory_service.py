# =============================================================================
# INVENTORY SERVICE
# This is a sample microservice that handles inventory management.
# It simulates communication with other services and uses configuration
# settings that can be changed at runtime.
# =============================================================================

import time                     # For simulating network delays
from pathlib import Path        # For working with file paths
import yaml                     # For loading YAML configuration


class InventoryService:
    """
    A simple microservice that handles inventory management.
    
    This service checks product availability and manages stock levels.
    
    Example:
        service = InventoryService("sample_microservices/config")
        result = service.check_availability("PRODUCT-456", 2)
        # result contains availability information
    """
    
    def __init__(self, config_dir="sample_microservices/config"):
        """
        Initialize the Inventory Service.
        
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
        config_path = self.config_dir / "inventory_config.yaml"
        
        # Open and parse the YAML file
        with open(config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    
    def get_retry_attempts(self):
        """
        Get the number of retry attempts for this service.
        
        Returns:
            The number of retry attempts.
        """
        # Read the retry attempts from the configuration
        # The default is 3 if not specified
        return self.config.get("inventory", {}).get("retry", {}).get("attempts", 3)
    
    def get_retry_delay(self):
        """
        Get the delay between retry attempts.
        
        Returns:
            The delay in seconds.
        """
        # Read the retry delay from the configuration
        # The default is 0.1 seconds if not specified
        return self.config.get("inventory + delay", {}).get("retry", {}).get("delay", 0.1)
    
    def check_availability(self, product_id, quantity):
        """
        Check if a product is available in the requested quantity.
        
        Args:
            product_id: The product to check
            quantity: The requested quantity
        
        Returns:
            A dictionary with availability information.
        """
        # Get our configuration settings
        retry_attempts = self.get_retry_attempts()
        retry_delay = self.get_retry_delay()
        
        # Simulate checking inventory
        # In a real system, this would query a database
        time.sleep(0.005)  # 5 milliseconds
        
        # Simulate a successful check
        # In a real system, this would be based on actual stock
        available = True
        stock_level = 100  # Simulated stock level
        
        # Return the result
        return {
            "product_id": product_id,
            "requested": quantity,
            "available": available,
            "stock_level": stock_level,
            "retry_attempts": retry_attempts,
            "retry_delay": retry_delay,
        }