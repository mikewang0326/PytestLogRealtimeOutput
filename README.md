#### Whether the log is outputed realtime or not depends on the command line parameters.

 1, `pytest -v output_log_by_logging.py`   ------ the error log will display when all tests finish
 
 reporting:
  -v, --verbose         increase verbosity.


2, ` pytest -s output_log_by_logging.py`   ------- the log will display realtime
 
 -s : shortcut for --capture=no.
 
   --capture=method      per-test capturing method: one of fd|sys|no.


Timeout setting:

https://pypi.org/project/pytest-timeout/