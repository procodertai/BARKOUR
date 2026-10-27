# BARKOUR

MuJoCo robotics experiments with the Unitree Go1.

## Setup

```bash
git submodule update --init --recursive
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python meet_robot.py
```

The viewer requires a graphical desktop. Robot assets are provided by the
MuJoCo Menagerie submodule and remain under their upstream licenses.

When cloning this project on another machine, use `git clone --recurse-submodules`.

See `BARKOUR_Project_Roadmap.md` for the project roadmap.
