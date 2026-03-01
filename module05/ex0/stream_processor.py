from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if not isinstance(data, list):
            return False

        if len(data) == 0:
            return False

        for item in data:
            if not isinstance(item, (int, float)):
                return False

        return True

    def process(self, data: Any) -> str:

        if not self.validate(data):
            raise ValueError("Numeric data verification failed")

        count_num = len(data)
        sum_num = sum(data)
        avg_num = sum_num / count_num if count_num > 0 else 0
        return f"Processed {count_num} numeric values, sum={sum_num}, avg={avg_num}"


    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        if len(data) == 0:
            return False
        return True

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Text data verification failed")

        len_text = len(data)
        words_count = len(data.split())
        return f"Processed text: {len_text}, {words_count} words"

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        
        if ":" not in data:
            return False
        
        str_received = data.split(":", 1)
        msg_log = str_received[0].strip().upper() 
        msgs_log = ["INFO", "WARNING", "ERROR", "DEBUG"] 
        
        if msg_log not in msgs_log:
            return False
        
        return True

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Log data verification failed")
        
        log = data.split(":", 1)
        type_log = log[0].strip().upper()
        mesg_log = log[1].strip()
        
        prefixes = {
            "ERROR": "[ALERT]",
            "WARNING": "[ALERT]",
            "INFO": "[INFO]",
            "DEBUG": "[INFO]"
        }
        prefix = prefixes[type_log]
        
        result = f"{prefix} {type_log} level detected: {mesg_log}"
        
        return result
        
    def format_output(self, result: str) -> str:
        return super().format_output(result)


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")
    proc_num = NumericProcessor()
    list_num = [1, 2, 3, 4, 5]
    try:
        print(f"Processing data: {list_num}")
        result = proc_num.process(list_num)
        if proc_num.validate(list_num):
            print("Validation: Numeric data verified")
        output = proc_num.format_output(result)
        print(output)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nInitializing Text Processor...")
    proc_text = TextProcessor()
    text = "Hello Nexus World"
    try:
        print(f"Processing data: \"{text}\"")
        result = proc_text.process(text)
        if proc_text.validate(text):
                print("Validation: Text data verified")
        output =proc_text.format_output(result)
        print(output)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nInitializing Log Processor...")
    proc_log = LogProcessor()
    log = "ERROR: Connection timeout"
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

    processors = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]

    data = [
        [1, 2, 3],
        "Hello World",
        "INFO: System ready"
    ]

    for i, (processor, data) in enumerate(zip(processors, data), 1):
        try:
            result = processor.process(data)
            print(f"Result {i}: {result}")
        except ValueError as e:
            print(f"Result {i}: Error - {e}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
