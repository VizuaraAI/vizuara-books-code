"""
AI Agents Bootcamp
Chapter 44: End-to-End Industrial Agent Projects
Section: From Agents to Products

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/end-to-end-agent-projects

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
resume_skills = {"python", "sql", "docker"}
job_reqs      = {"python", "sql", "aws", "kubernetes"}

covered = resume_skills & job_reqs          # {python, sql}
score   = len(covered) / len(job_reqs)      # 2 / 4 = 0.5
missing = job_reqs - resume_skills          # {aws, kubernetes}
