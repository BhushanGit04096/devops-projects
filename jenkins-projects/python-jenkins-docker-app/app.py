def count_errors(log_text):
    """
    Count number of ERROR entries in a log file.
    """
    lines = log_text.split("\n")
    error_count = 0

    for line in lines:
        if "ERROR" in line:
            error_count += 1

    return error_count


def main():
    sample_log = """
    INFO Application started
    INFO Connecting to database
    ERROR Database connection failed
    INFO Retrying connection
    ERROR Timeout occurred
    """

    errors = count_errors(sample_log)

    print(f"Total ERROR entries found: {errors}")


if __name__ == "__main__":
    main()
