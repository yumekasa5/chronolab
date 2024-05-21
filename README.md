# How to build python script by py2exe + pyenv

1. Install pyenv by pip

```bash
pip install pyenv-win --target %USERPROFILE%\.pyenv
```

2. Set system variables

- Perform the following process in Windows Powershell 

```bash
[System.Environment]::SetEnvironmentVariable('PYENV',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
[System.Environment]::SetEnvironmentVariable('PYENV_HOME',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
[System.Environment]::SetEnvironmentVariable('path', $env:USERPROFILE + "\.pyenv\pyenv-win\bin;" + $env:USERPROFILE + "\.pyenv\pyenv-win\shims;" + [System.Environment]::GetEnvironmentVariable('path', "User"),"User")
```

3. Check pyenv varification

- After closing terminal, perform the following command in cmd

```bash
pyenv --version
```
If you have completed pyenv's setting, you can see the version.
> pyenv 3.1.1

4. Install pyenv python

```bash
pyenv install 3.9.13
```

5. Clone pyenv-win module

- *clone destination is the other directory

```bash
git clone https://github.com/pyenv-win/pyenv-win.git
```

6. Create venv environment

```bash
python -m venv .venv
```

# How to build python script by cx_Freeze

1. install
```bash
pip install cx_Freeze
```

2. setup.py
```python
from cx_Freeze import setup, Executable

setup(
    name="YourAppName",
    version="1.0",
    description="Your application description",
    executables=[Executable("Main.py")],
)
```
3. build
```bash
python setup.py build
```