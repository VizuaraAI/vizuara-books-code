"""
Modern Robot Learning
Chapter 3: Where Classical Robotics Breaks Down
Section: Foundations of Robot Learning

Read this chapter: https://books.vizuara.ai/read/modern-robot-learning/limits-of-classical-robotics

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def contact_force(x, k=5000.0):     # k = block stiffness (N/m), x in metres
    if x > 0.0:                      # finger above the surface: free space
        return 0.0
    else:                            # finger has penetrated by |x|: contact
        return -k * x                # a stiff spring pushes back
