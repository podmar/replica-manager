import logging


def set_logger(log_file_path: str) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s]  %(message)s",
        handlers=[
            logging.FileHandler(log_file_path),
            logging.StreamHandler()
        ]
    )
