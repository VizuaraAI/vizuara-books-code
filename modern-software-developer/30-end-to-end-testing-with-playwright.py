"""
The Modern Software Developer
Chapter 30: End-to-End Testing with Playwright
Section: Deployment, DevOps & CI/CD

Read this chapter: https://books.vizuara.ai/read/modern-software-developer/end-to-end-testing-with-playwright

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# tests/e2e/test_login.py
from playwright.sync_api import Page, expect

def test_user_can_log_in(page: Page):
    # 1. Go to the login page like a user typing a URL
    page.goto("http://localhost:8000/login")

    # 2. Fill the form fields by their labels
    page.get_by_label("Email").fill("ada@example.com")
    page.get_by_label("Password").fill("correct-horse")

    # 3. Click the REAL button — auto-waits until it's clickable
    page.get_by_role("button", name="Sign in").click()

    # 4. Assert the outcome the user would see
    expect(page).to_have_url("http://localhost:8000/dashboard")
    expect(page.get_by_text("Welcome, Ada")).to_be_visible()

# --- block 2 ---
# tests/e2e/conftest.py
import subprocess, time, httpx, pytest

@pytest.fixture(scope="session")
def live_server():
    proc = subprocess.Popen(["uvicorn", "app.main:app", "--port", "8000"])
    # Poll for readiness — do NOT just sleep
    for _ in range(50):                      # up to ~10 s
        try:
            if httpx.get("http://localhost:8000/health").status_code == 200:
                break
        except httpx.ConnectError:
            time.sleep(0.2)
    else:
        proc.terminate()
        raise RuntimeError("server never became ready")
    yield "http://localhost:8000"
    proc.terminate()                          # teardown always runs
