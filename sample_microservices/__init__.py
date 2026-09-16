# This file makes the 'sample_microservices' folder a Python package.

# Define what should be exported when someone does
# 'from sample_microservices import *'
__all__ = [
    'order_service',        # Order microservice
    'inventory_service',    # Inventory microservice
    'pricing_service',      # Pricing microservice
]