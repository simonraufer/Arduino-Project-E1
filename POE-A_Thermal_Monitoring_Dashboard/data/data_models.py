from dataclasses import dataclass
import pandas as pd


@dataclass
class SensorHistory:
    address: str
    data: pd.DataFrame

@dataclass
class Dataset:
    sensors: dict[str, SensorHistory]
    map_session_count: int

