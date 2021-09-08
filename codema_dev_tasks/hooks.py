from ._compat import import_optional_dependency

def load_environmental_variables():
    dotenv = import_optional_dependency("dotenv", "python-dotenv is required to run load_environmental_variables")
    from dotenv import load_dotenv
    load_dotenv()