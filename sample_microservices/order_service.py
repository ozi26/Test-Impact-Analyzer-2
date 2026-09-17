# =============================================================================
# ORDER SERVICE
# This is a sample microservice that handles order processing.
# It simulates communication with other services and uses configuration
# settings that can be changed at runtime.
# =============================================================================

import time                     # For simulating network delays
from pathlib import Path        # For working with file paths
import yaml                     # For loading YAML configuration


class OrderService:
    """
    A simple microservice that handles order processing.
    
    This service reads configuration settings and simulates
    communication with other services (Inventory and Pricing).
    
    Example:
        service = OrderService("sample_microservices/config")
        result = service.process_order("ORDER-123", "PRODUCT-456", 2)
        # result contains the order status
    """
    
    def __init__(self, config_dir="sample_microservices/config"):
        """
        Initialize the Order Service.
        
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
        config_path = self.config_dir / "order_config.yaml"
        
        # Open and parse the YAML file
        with open(config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    
    def get_timeout(self):
        """
        Get the timeout setting for this service.
        
        Returns:
            The timeout value in seconds.
        """
        # Read the timeout from the configuration
        # The default is 5 seconds if not specified
        return self.config.get("order", {}).get("timeout", 5)
    
    def get_retry_attempts(self):
        """
        Get the number of retry attempts for this service.
        
        Returns:
            The number of retry attempts.
        """
        # Read the retry attempts from the configuration
        # The default is 3 if not specified
        return self.config.get("order", {}).get("retry", {}).get("attempts", 3)
    
    def process_order(self, order_id, product_id, quantity):
        """
        Process an order by contacting other services.
        
        This method simulates:
        
        1. Checking inventory with the Inventory Service
        2. Getting the price from the Pricing Service
        3. Creating the order
        4. Returning the result
        
        Args:
            order_id: The unique identifier for the order
            product_id: The product being ordered
            quantity: How many units to order
        
        Returns:
            A dictionary with the order result.
        """
        # Record the start time
        start_time = time.time()
        
        # Get our configuration settings
        timeout = self.get_timeout()
        retry_attempts = self.get_retry_attempts()
        
        # Simulate calling the Inventory Service
        # We simulate a small delay to represent network latency
        time.sleep(0.01)  # 10 milliseconds
        
        # Check if we have enough inventory
        inventory_available = True  # Simulated response
        
        # If inventory is not available, return an error
        if not inventory_available:
            return {
                "order_id": order_id,
                "status": "FAILED",
                "reason": "Insufficient inventory",
            }
        
        # Simulate calling the Pricing Service
        time.sleep(0.01)  # 10 milliseconds
        
        # Calculate the price (simulated)
        unit_price = 29.99
        total_price = unit_price * quantity
        
        # Calculate how long the whole process took
        elapsed_time = time.time() - start_time
        
        # Return the successful result
        return {
            "order_id": order_id,
            "product_id": product_id,
            "quantity": quantity,
            "status": "SUCCESS",
            "total_price": total_price,
            "elapsed_time": elapsed_time,
            "config_used": {
                "timeout": timeout,
                "retry_attempts": retry_attempts,
            },
        }