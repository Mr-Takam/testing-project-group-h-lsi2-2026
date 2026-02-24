# Running tests

```
# Install Python dependencies

$ python -m venv .venv 
# or
$ python3 -m venv .venv
$ source .venv/bin/activate
# or (from cmd.exe, not PowerShell)
$ .venv\Scripts\activate.bat
$ pip install -r requirements.txt

# Install browser
$ playwright install chromium

# Fix the URL in pytest.ini

# Run the tests
$ pytest 
```

## Using `ipdb` as debugger (optional)

* Set the env var `PYTHONBREAKPOINT`  to `ipdb.set_trace`
* Call the breakpoint() function where you want to start the interactive debugging

