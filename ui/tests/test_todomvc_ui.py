from playwright.sync_api import sync_playwright

def test_add_and_complete_todo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://demo.playwright.dev/todomvc")

        # Add a new todo
        page.fill(".new-todo", "Write demo test")
        page.press(".new-todo", "Enter")

        # Confirm the todo was added
        todo_items = page.query_selector_all(".todo-list li")
        assert len(todo_items) == 1
        assert todo_items[0].inner_text().startswith("Write demo test")

        # Mark the todo as completed
        page.check(".todo-list li .toggle")

        # Verify it is marked as completed
        completed = page.locator(".todo-list li.completed")
        assert completed.count() == 1

        browser.close()
