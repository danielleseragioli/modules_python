from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """Abstract base class for polymorphic data stream processing."""

    def __init__(self, stream_id: str) -> None:
        """Initialize the data stream with an ID and counters."""
        self.stream_id: str = stream_id
        self.items_processed: int = 0
        self.data_history: List[Any] = []

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data and return a result string."""
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter data based on optional criteria."""
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics as a dictionary."""
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
            if self.temp_count > 0:
                avg_temp = self.temp_sum / self.temp_count
            else:
                avg_temp = 0.0
            return (f"Sensor analysis: {self.sensor_count} readings processed,"
                    f" avg temp: {avg_temp:.1f}°C")

        except (ValueError, TypeError) as e:
            raise ValueError(f"Processing error: {e}")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter sensor data based on criteria
        (critical temps or specific types)."""
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
        if self.temp_count > 0:
            avg_temp: float = self.temp_sum / self.temp_count
        else:
            avg_temp: float = 0.0
        return {
            "stream_id": self.stream_id,
            "type": "Sensor",
            "sensor_readings": self.sensor_count,
            "avg_temperature": avg_temp,
        }


class TransactionStream(DataStream):
    """Specialized stream for financial transaction data processing."""

    def __init__(self, stream_id: str) -> None:
        """Initialize transaction stream with financial counters."""
        super().__init__(stream_id)
        self.transaction_count: int = 0
        self.buy_total: float = 0.0
        self.sell_total: float = 0.0

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process transaction batch and calculate net flow."""
        if not data_batch:
            raise ValueError("Empty list")
        try:
            for item in data_batch:
                if not isinstance(item, str) and ":" not in item:
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
                else:
                    raise ValueError("Unsupported transaction operation: "
                                     f"{operation.strip()}")
            net_flow = self.buy_total - self.sell_total
            flow_str = (f"+{int(net_flow)}" if net_flow > 0
                        else f"{int(net_flow)}")
            return (f"Transaction analysis: {self.transaction_count} "
                    f"operations, net flow: {flow_str} units")

        except (ValueError, TypeError) as e:
            raise ValueError(f"Processing error: {e}")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter transaction data based on criteria (large, buy, sell)."""
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
                    if isinstance(item, str) and item.startswith("buy:"):
                        filtered.append(item)
                except ValueError:
                    pass
            return filtered

        elif criteria == "sell":
            filtered: List[Any] = []
            for item in data_batch:
                try:
                    if isinstance(item, str) and item.startswith("sell:"):
                        filtered.append(item)
                except ValueError:
                    pass
            return filtered

        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return transaction statistics including net flow."""
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
    """Specialized stream for system event data processing."""

    def __init__(self, stream_id: str) -> None:
        """Initialize event stream with event and error counters."""
        super().__init__(stream_id)
        self.event_count: int = 0
        self.error_count: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process event stream and count error occurrences."""
        if not data_batch:
            raise ValueError("Empty list")

        try:
            for item in data_batch:
                if not isinstance(item, str):
                    raise ValueError(f"Invalid event format: {item}")

                event_text = item.strip().lower()
                self.items_processed += 1
                self.data_history.append(item)
                self.event_count += 1

                if "error" in event_text:
                    self.error_count += 1

            return (f"Event analysis: {self.event_count} events, "
                    f"{self.error_count} error detected")
        except (ValueError, TypeError) as e:
            raise ValueError(f"Processing error: {e}")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter event data based on criteria (error or critical)."""
        if criteria is None:
            return data_batch
        if criteria == "error":
            filtered: List[Any] = []
            for item in data_batch:
                try:
                    if isinstance(item, str) and "error" in item.lower():
                        filtered.append(item)
                except ValueError:
                    pass
            return filtered
        elif criteria == "critical":
            filtered: List[Any] = []
            for item in data_batch:
                try:
                    if isinstance(item, str) and "critical" in item.lower():
                        filtered.append(item)
                except ValueError:
                    pass
            return filtered

        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return event stream statistics."""
        return {
            "stream_id": self.stream_id,
            "type": "Event",
            "events": self.event_count,
            "errors": self.error_count
        }


class StreamProcessor():
    """Manager for handling multiple data streams polymorphically."""

    def __init__(self) -> None:
        """Initialize processor with empty stream list."""
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        """Add a data stream to the processor."""
        if not isinstance(stream, DataStream):
            raise TypeError("Stream must be a DataStream instance")
        self.streams.append(stream)

    def process_all_streams(self,
                            batches: Dict[str, List[Any]]) -> Dict[str, str]:
        """Process batches for all registered streams polymorphically."""
        results: Dict[str, str] = {}
        for stream in self.streams:
            stream_id = stream.stream_id
            batch = batches.get(stream_id, [])
            try:
                if not batch:
                    results[stream_id] = "No data batch provided"
                    continue
                output = stream.process_batch(batch)
                results[stream_id] = output
            except (ValueError, TypeError) as e:
                results[stream_id] = f"Processing failed: {e}"

        return results

    def filter_all_streams(
        self,
        batches: Dict[str, List[Any]],
        criteria: Optional[str] = None
    ) -> Dict[str, List[Any]]:
        """Filter data for all registered streams with given criteria."""
        filtered_results: Dict[str, List[Any]] = {}
        for stream in self.streams:
            stream_id = stream.stream_id
            batch = batches.get(stream_id, [])
            try:
                filtered = stream.filter_data(batch, criteria)
                filtered_results[stream_id] = filtered
            except (ValueError, TypeError):
                filtered_results[stream_id] = []
        return filtered_results

    def get_all_stats(self) -> Dict[str, Dict[str, Union[str, int, float]]]:
        """Get statistics from all registered streams."""
        stats: Dict[str, Dict[str, Union[str, int, float]]] = {}

        for stream in self.streams:
            stats[stream.stream_id] = stream.get_stats()

        return stats


def main() -> None:
    """Run the polymorphic data stream demonstration."""

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print("\nInitializing Sensor Stream...")

    sensor = SensorStream("SENSOR_001")
    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Stream ID: {sensor.stream_id}, Type: Environmental Data")
    batch_str = str(sensor_batch).replace("'", "")
    print(f"Processing sensor batch: {batch_str}")
    sensor_result = sensor.process_batch(sensor_batch)
    print(sensor_result)

    print("\nInitializing Transaction Stream...")
    transaction = TransactionStream("TRANS_001")
    transaction_batch = ["buy:100", "sell:150", "buy:75"]
    print(f"Stream ID: {transaction.stream_id}, Type: Financial Data")
    batch_str = str(transaction_batch).replace("'", "")
    print(f"Processing transaction batch: {batch_str}")
    transaction_result = transaction.process_batch(transaction_batch)
    print(transaction_result)

    print("\nInitializing Event Stream...")
    event = EventStream("EVENT_001")
    event_batch = ["login", "error", "logout"]
    print(f"Stream ID: {event.stream_id}, Type: System Events")
    batch_str = str(event_batch).replace("'", "")
    print(f"Processing event batch: {batch_str}")
    event_result = event.process_batch(event_batch)
    print(event_result)

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    sensor_poly = SensorStream("SENSOR_001")
    transaction_poly = TransactionStream("TRANS_001")
    event_poly = EventStream("EVENT_001")

    processor = StreamProcessor()
    processor.add_stream(sensor_poly)
    processor.add_stream(transaction_poly)
    processor.add_stream(event_poly)

    batches = {
        "SENSOR_001": ["temp:26.0", "temp:27.5"],
        "TRANS_001": ["buy:200", "sell:100", "buy:50", "sell:75"],
        "EVENT_001": ["login", "info", "logout"]
    }

    results = processor.process_all_streams(batches)
    print("\nBatch 1 Results:")
    for stream_id, result in results.items():
        if "Sensor" in result:
            readings = result.split()[2]
            print(f"- Sensor data: {readings} readings processed")
        elif "Transaction" in result:
            ops = result.split()[2]
            print(f"- Transaction data: {ops} operations processed")
        elif "Event" in result:
            events = result.split()[2]
            print(f"- Event data: {events} events processed")
    print("\nStream filtering active: High-priority data only")

    sensor_filtered = sensor_poly.filter_data(
        batches["SENSOR_001"], "critical"
    )
    trans_filtered = transaction_poly.filter_data(
        batches["TRANS_001"], "large"
    )

    sensor_critical = len(sensor_filtered)
    trans_large = len(trans_filtered)

    print(f"Filtered results: {sensor_critical} critical sensor alerts, "
          f"{trans_large} large transaction")
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
