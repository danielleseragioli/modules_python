from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):

    def __init__(self, stream_id: str):
        self.stream_id = stream_id
        self.items_processed = 0
        self.data_history = []

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"id": self.stream_id}


class SensorStream(DataStream):
    """Specialized stream for sensor data processing."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.sensor_count: int = 0
        self.temp_count: int = 0
        self.temp_sum: float = 0.0

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process sensor readings and calculate average temperature."""
        if not data_batch:
            raise ValueError("Empty list")
        try:
            for item in data_batch:
                if not isinstance(item, str) or ":" not in item:
                    raise ValueError(f"Invalid format: {item}")
                key, raw_value = item.split(":", 1)
                value = float(raw_value)
                self.items_processed += 1
                self.data_history.append(item)
                self.sensor_count += 1

                if key.strip().lower() == "temp":
                    self.temp_sum += value
                    self.temp_count += 1
            avg_temp = self.temp_sum / self.temp_count if self.temp_count > 0 else 0.0
            return f"Sensor analysis: {self.sensor_count} readings processed, avg temp: {avg_temp}°C"

        except (ValueError, TypeError) as e:
            raise ValueError(f"Processing error: {e}")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter sensor data based on criteria (critical temps or specific types)."""
        if criteria is None:
            return data_batch
        if criteria == "critical":
            filtered: List[Any] = []
            for item in data_batch:
                if "temp:" in item:
                    try:
                        value: float = float(item.split(":")[1])
                        if value > 25:
                            filtered.append(item)
                    except ValueError:
                        pass
            return filtered
        elif criteria == "temp":
            filtered: List[Any] = []
            for item in data_batch:
                if isinstance(item, str) and item.startswith("temp:"):
                    filtered.append(item)
            return filtered
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return sensor-specific statistics."""
        avg_temp: float = self.temp_sum / self.temp_count if self.temp_count > 0 else 0.0
        return {
            "stream_id": self.stream_id,
            "type": "Sensor",
            "sensor_readings": self.sensor_count,
            "avg_temperature": avg_temp,
        }


class TransactionStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.transaction_count: int = 0
        self.buy_total: float = 0.0
        self.sell_total: float = 0.0

    def process_batch(self, data_batch: List[Any]) -> str:
        if data_batch is None:
            raise ValueError("Empty list")
        try:
            for item in data_batch:
                if not isinstance(item, str) and not ":" in item:
                    raise ValueError(f"Invalid format: {item}")
                operation, raw_value = item.split(":", 1)
                value = float(raw_value)
                self.items_processed += 1
                self.data_history.append(item)
                self.transaction_count += 1
                if operation.strip().lower() == "buy":
                    self.buy_total += value
                elif operation.strip().lower() == "sell":
                    self.sell_total += value
                net_flow = self.buy_total - self.sell_total
                return f"Transaction analysis: {self.transaction_count} operations, net flow: {net_flow} units"

        except (ValueError, TypeError) as e:
            raise ValueError(f"Processing error: {e}")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch
        if criteria == "large":
            filtered: List[Any] = []
            for item in data_batch:
                try:
                    value: float = float(item.split(":")[1])
                    if value > 100:
                        filtered.append(item)
                except ValueError:
                    pass
            return filtered

        elif criteria == "buy":
            filtered: List[Any] = []
            for item in data_batch:
                try:
                    value: float = float(item.split(":")[1])
                    if isinstance(item, str) and item.startswith("buy:"):
                        filtered.append(item)
                except ValueError:
                    pass
            return filtered

        elif criteria == "sell":
            filtered: List[Any] = []
            for item in data_batch:
                try:
                    value: float = float(item.split(":")[1])
                    if isinstance(item, str) and item.startswith("sell:"):
                        filtered.append(item)
                except ValueError:
                    pass
            return filtered

        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        net_flow: float = self.buy_total - self.sell_total
        return {
            "stream_id": self.stream_id,
            "type": "Transaction",
            "operations": self.transaction_count,
            "net_flow": net_flow,
            "buy_total": self.buy_total,
            "sell_total": self.sell_total,
        }


class EventStream(DataStream):
    pass


class StreamProcessor():
    pass