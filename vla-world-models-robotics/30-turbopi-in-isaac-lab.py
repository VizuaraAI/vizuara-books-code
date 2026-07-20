"""
Vision-Language-Action & World Models for Robotics
Chapter 30: TurboPi in Isaac Lab
Section: Isaac Lab and Scalable Simulation

Read this chapter: https://books.vizuara.ai/read/vla-world-models-robotics/turbopi-in-isaac-lab

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from isaaclab.app import AppLauncher

# 1. Boot the simulator FIRST (headless=False opens the viewer window)
app_launcher = AppLauncher(headless=False)
simulation_app = app_launcher.app

# 2. Only now are the Isaac Lab modules importable
import isaaclab.sim as sim_utils
from isaaclab.assets import Articulation, ArticulationCfg
from isaaclab.sim import SimulationContext

# --- block 2 ---
# 3. The stage: a ground plane + a light
sim_utils.GroundPlaneCfg().func("/World/ground", sim_utils.GroundPlaneCfg())
sim_utils.DomeLightCfg(intensity=3000.0).func("/World/light",
                                              sim_utils.DomeLightCfg(intensity=3000.0))

# 4. The robot: spawn TurboPi's USD as an articulation
turbopi_cfg = ArticulationCfg(
    prim_path="/World/TurboPi",
    spawn=sim_utils.UsdFileCfg(usd_path="turbopi.usd"),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.05),          # 5 cm above the floor — let gravity settle it
    ),
    actuators={ ... },                  # the four wheel motors, defined next
)
turbopi = Articulation(cfg=turbopi_cfg)

# --- block 3 ---
sim = SimulationContext(sim_utils.SimulationCfg(dt=1/120))
sim.reset()

# spin all four wheels forward at a constant velocity target
wheel_targets = turbopi.data.default_joint_vel.clone()
wheel_targets[:] = 6.0                       # rad/s on every wheel joint

while simulation_app.is_running():
    turbopi.set_joint_velocity_target(wheel_targets)
    turbopi.write_data_to_sim()              # push commands into PhysX
    sim.step()                               # advance the world by dt
    turbopi.update(dt=1/120)                 # pull fresh state back out
    print(turbopi.data.root_pos_w[0])        # watch the chassis move
