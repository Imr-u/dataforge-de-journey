# This is what we have done so for for setting up the enviroment

## Installing linux(Ubuntu)

As a Data Engineer most of the work are done in claude and we don't use os in the claude we use terminal speccifically linux. so we download ubutnu using \n

```powershell
wsl --install -d ubuntu -22.04
```

After that we downloaded Windows terminal and set ubuntu as default profile. using just the setting in Windows terminal.
> Windows terminal is different from other terminal as it provides multiple tabe sevice, settings and other modern stacks. it serves as a system that holds other terminal together in one place

## Installing Pyenv

Pyenv controlls which python version to use for each project, in many cases companies use older version of python and are not comforable using the latest ones so to mannage that we use pyenv. to install run:

```bash
curl https://pyenv.run | bash
```

Then we need to add this to the ~/.bashrc file this is where system files are stored.
open nano ~/.bashrc and paste this in the last lines and save:

```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

now make the version of python you want to be global like:

```bash
pyenv global 3.11.9
```
