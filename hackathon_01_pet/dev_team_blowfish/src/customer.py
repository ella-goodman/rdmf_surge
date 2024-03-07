from typing import Optional


class Customer:
    def __init__(self, org_name: str) -> None:
        self.org_name: str = org_name
        self.password: Optional[str] = None

    def set_password(self, password) -> None:
        self.password = password

    def get_password(self) -> Optional[str]:
        return self.password
    
    def set_data(self, data):
        self.data = data
        
    def get_data(self):
        return self.data
        
        
