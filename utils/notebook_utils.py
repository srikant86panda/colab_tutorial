import os

def is_jupyter():
    """Check if the module is running on Jupyter notebook/console

    Returns:
        bool: True if the module is running on Jupyter notebook or Jupyter console,
        False otherwise.
    """
    try:
        shell_name = get_ipython().__class__.__name__
        if shell_name in ['Shell',  'ZMQInteractiveShell']:
            return True
        else:
            return False
    except NameError:
        return False