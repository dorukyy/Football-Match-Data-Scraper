# base.py
from sqlalchemy.ext.declarative import declarative_base

def create_base() -> type:
    """
    Creates and returns a base class for declarative class definitions.

    Returns:
        type: A base class for declarative class definitions.
    """
    try:
        return declarative_base()
    except Exception as e:
        # Log the exception without revealing sensitive information
        import logging
        logging.error("Failed to create base class: %s", str(e))
        raise

Base = create_base()