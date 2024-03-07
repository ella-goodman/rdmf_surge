import time
from typing import List
import numpy as np
import pandas as pd
from src.utils import SingletonIDGenerator

id_gen = SingletonIDGenerator()


class CustomerRequest:
    def __init__(
        self, 
        org_name: str, 
        dataset1: str, 
        dataset1_cols: List[str], 
        dataset2: str, 
        dataset2_cols: List[str], 
        merge_col: str
    ) -> None:
        self.org_name: str = org_name
        self.dataset1: str = dataset1
        self.dataset1_cols: List[str] = dataset1_cols
        self.dataset2: str = dataset2
        self.dataset2_cols: List[str] = dataset2_cols
        self.merge_col: str = merge_col
        self.req_id: int = next(id_gen)
        self.epoch: float = time.time()
        self.password_prefix: str = "".join([str(ord(s)) for s in self.org_name]) + str(
            self.req_id
        )
        self.password_suffix: str = str(np.random.randint(100, 999))

    def set_data(self, client, bucket_name: str) -> None:
        blobs = [b for b in client.list_blobs(bucket_name)]
        self.data = {}

        for blob in blobs:
            if ".csv" in blob.name:
                self.data[blob.name.split("_")[0]] = pd.read_csv(
                    f"gs://{bucket_name}/{blob.name}", encoding="latin-1"
                )

        self.merged_data = pd.merge(
            self.data[self.dataset1][self.dataset1_cols], self.data[self.dataset2][self.dataset2_cols], on=self.merge_col
        )

    def get_data(self, hashing_obj, customer_password: str, hashed_cols: List[str]):
        cr_hasher = hashing_obj(self)
        for col in hashed_cols:
            self.merged_data[col] = cr_hasher.hash_data(
                self.merged_data[col], customer_password
            )
        return self.merged_data.sort_values(by=hashed_cols[0]).reset_index(drop=True)

    def create_user_password(self) -> str:
        return self.password_prefix + str(np.random.randint(100000, 999999))

    def get_metadata(self):
        self.metadata = {
            "org_name": self.org_name,
            "dataset1": self.dataset1,
            "dataset2": self.dataset2,
            "merge_col": self.merge_col,
            "req_id": self.req_id,
            "time": self.epoch,
            "password_prefix": self.password_prefix,
            "password_suffix": self.password_suffix,
        }
        return self.metadata

    def get_password_prefix(self) -> str:
        return self.password_prefix

    def get_password_suffix(self) -> str:
        return self.password_suffix

    def get_epoch_str(self) -> str:
        return str(self.epoch)