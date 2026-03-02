from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union


class DataProcessor(ABC):
    """Abstract base class for polymorphic data processing."""

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the input data and return a result string."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if the data is appropriate for this processor."""
        pass

    def format_output(self, result: str) -> str:
        """Format the output string with a default prefix."""
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """Processor for numeric data - calculates sum and average."""

    def validate(self, data: Any) -> bool:
        """Check if data is a non-empty list of numbers."""
        if not isinstance(data, list):
            return False

        if len(data) == 0:
            return False

        for item in data:
            if not isinstance(item, (int, float)):
                return False

        return True

    def process(self, data: Any) -> str:
        """Calculate sum and average of numeric values."""
        if not self.validate(data):
            raise ValueError("Numeric data verification failed")

        count_num: int = len(data)
        sum_num: Union[int, float] = sum(data)
        avg_num: float = sum_num / count_num if count_num > 0 else 0
        return (f"Processed {count_num} numeric values, "
                f"sum={sum_num}, avg={avg_num}")

    def format_output(self, result: str) -> str:
        """Format output with standard prefix."""
        return super().format_output(result)


class TextProcessor(DataProcessor):
    """Processor for text data - counts characters and words."""

    def validate(self, data: Any) -> bool:
        """Check if data is a non-empty string."""
        if not isinstance(data, str):
            return False
        if len(data) == 0:
            return False
        return True

    def process(self, data: Any) -> str:
        """Count characters and words in the text."""
        if not self.validate(data):
            raise ValueError("Text data verification failed")

        len_text: int = len(data)
        words_count: int = len(data.split())
        return f"Processed text: {len_text} characters, {words_count} words"

    def format_output(self, result: str) -> str:
        """Format output with standard prefix."""
        return super().format_output(result)


class LogProcessor(DataProcessor):
    """Processor for log entries - identifies log level and formats alerts."""

    def validate(self, data: Any) -> bool:
        """Check if data is a valid log entry with recognized level."""
        if not isinstance(data, str):
            return False

        if ":" not in data:
            return False

        str_received: List[str] = data.split(":", 1)
        msg_log: str = str_received[0].strip().upper()
        msgs_log: List[str] = ["INFO", "WARNING", "ERROR", "DEBUG"]

        if msg_log not in msgs_log:
            return False

        return True

    def process(self, data: Any) -> str:
        """Extract log level and format with appropriate prefix."""
        if not self.validate(data):
            raise ValueError("Log data verification failed")

        log: List[str] = data.split(":", 1)
        type_log: str = log[0].strip().upper()
        mesg_log: str = log[1].strip()

        prefixes: Dict[str, str] = {
            "ERROR": "[ALERT]",
            "WARNING": "[ALERT]",
            "INFO": "[INFO]",
            "DEBUG": "[INFO]"
        }
        prefix: str = prefixes[type_log]

        result: str = f"{prefix} {type_log} level detected: {mesg_log}"

        return result

    def format_output(self, result: str) -> str:
        """Format output with standard prefix."""
        return super().format_output(result)


def main() -> None:
    """Run the data processor demonstration."""
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")
    proc_num: NumericProcessor = NumericProcessor()
    list_num: List[int] = [1, 2, 3, 4, 5]
    try:
        print(f"Processing data: {list_num}")
        result: str = proc_num.process(list_num)
        if proc_num.validate(list_num):
            print("Validation: Numeric data verified")
        output: str = proc_num.format_output(result)
        print(output)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nInitializing Text Processor...")
    proc_text: TextProcessor = TextProcessor()
    text: str = "Hello Nexus World"
    try:
        print(f"Processing data: \"{text}\"")
        result = proc_text.process(text)
        if proc_text.validate(text):
            print("Validation: Text data verified")
        output = proc_text.format_output(result)
        print(output)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nInitializing Log Processor...")
    proc_log: LogProcessor = LogProcessor()
    log: str = "ERROR: Connection timeout"
    try:
        print(f"Processing data: {log}")
        result = proc_log.process(log)
        if proc_log.validate(log):
            print("Validation: Log entry verified")
        output = proc_log.format_output(result)
        print(output)
    except ValueError as e:
        print(f"Error: {e}")

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]

    data: List[Any] = [
        [1, 2, 3],
        "Hello World!",
        "INFO: System ready"
    ]

    for i, (processor, data_item) in enumerate(zip(processors, data), 1):
        try:
            result = processor.process(data_item)
            print(f"Result {i}: {result}")
        except ValueError as e:
            print(f"Result {i}: Error - {e}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
