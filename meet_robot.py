"""Mission 001: hold Go1's home pose and wiggle its front-right thigh."""

import math
from pathlib import Path
import time

import mujoco
import mujoco.viewer


def load_robot():
    scene = Path(__file__).resolve().parent / "mujoco_menagerie/unitree_go1/scene.xml"
    model = mujoco.MjModel.from_xml_path(str(scene))
    data = mujoco.MjData(model)
    mujoco.mj_resetDataKeyframe(model, data, model.key("home").id)
    mujoco.mj_forward(model, data)
    return model, data


def command_leg(model, data, home_controls):
    # Hold every joint at its home angle, then vary one target after 2 seconds.
    data.ctrl[:] = home_controls
    if data.time > 2.0:
        data.ctrl[model.actuator("FR_thigh").id] += (
            0.15 * math.sin(2 * math.pi * 0.5 * (data.time - 2.0))
        )


def main():
    model, data = load_robot()
    home_controls = data.ctrl.copy()
    print("Holding the home pose; front-right thigh starts moving after 2 seconds.")
    print("Close the viewer window to stop.")
    with mujoco.viewer.launch_passive(model, data) as viewer:
        viewer.cam.lookat[:] = [0, 0, 0.25]
        viewer.cam.distance = 1.5
        viewer.cam.azimuth = 120
        viewer.cam.elevation = -20
        while viewer.is_running():
            started = time.perf_counter()
            command_leg(model, data, home_controls)
            mujoco.mj_step(model, data)
            viewer.sync()
            time.sleep(max(0.0, model.opt.timestep - (time.perf_counter() - started)))


if __name__ == "__main__":
    main()
