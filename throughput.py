import locale
import time

locale.setlocale(locale.LC_ALL, '')


def convert_bytes(value: int, target_units: str = "kilobits") -> float:
    match target_units:
        
        case "kilobits":
            return value / 125
        
        case "kilobytes":
            return value / 1_000

        case "megabytes":
            return value / 1_000_000

        case _:
            print("Unknown unit. Returning value as-is.")
            return value


def main(*args) -> None:
    input_bytes_converted: int = int(args[0])
    input_units = "kilobits"
    if len(args) >= 2:
        input_units: str = args[1]

    throughput: int = convert_bytes(input_bytes_converted, input_units)
    
    print(f"{input_bytes_converted:n} bytes = {throughput:n} {input_units}")


if __name__ == "__main__":
    user_throughput = input("Average throughput in bytes per second: ")
    user_units = input("Desired target units you want to convert to [kilobits]: ")

    start = time.time()

    if not user_units:
        main(user_throughput)
    else:
        main(user_throughput, user_units.lower())
    
    end = time.time()
    print(f"Performance: {end-start:.10f}.")

# Performance: 0.0010013580. 14.5 times slower than Rust.
