import numpy as np

from google.cloud import bigquery
from google.cloud import storage
import hashlib

from src.customer_request import CustomerRequest


class Hasher:
    def __init__(self, customer_request: CustomerRequest) -> None:
        self.customer_request: CustomerRequest = customer_request

    def generate_hash_key(self, input_value, customer_password: str) -> str:
        """
        Generates a hash key for secure record linkage.

        Parameters:
        project_name (str): The name of the project.
        input_data (str): The input data to be hashed.

        Returns:
        str: The generated hash key.
        """
        salts = [
            customer_password,
            self.customer_request.get_password_suffix().encode(),
        ]
        input_data_with_salt = str(input_value).encode() + np.sum(salts)
        hash_key = hashlib.sha256(input_data_with_salt).hexdigest()
        return hash_key

    def hash_data(self, series, customer_password: str):
        return series.apply(lambda x: self.generate_hash_key(x, customer_password))
