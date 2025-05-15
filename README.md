# API Automation Demo

This is a lightweight sample API test automation framework using Python, Pytest, and Requests. It's designed to demonstrate good structure and best practices for real-world API testing.

## Features
- Basic test structure with Pytest
- Uses Requests for API interaction
- Structured for clarity and easy extension to support reusable utilities and fixtures
- CI-ready with a sample GitLab pipeline

## Getting Started

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run tests:
   ```bash
   pytest
   ```

## Sample Endpoint

This demo uses [ReqRes](https://reqres.in/) as a mock API.

## Author
Matthew Mott


## UI Testing (Python Playwright)

This project also includes a UI test using Python Playwright.

### To run the UI tests:
1. Install Playwright browsers:
   ```bash
   playwright install
   ```

2. Run tests with Pytest:
   ```bash
   pytest ui/tests/
   ```

The example test navigates to `https://example.com` and verifies the page title.


### Additional UI Test: TodoMVC

This UI test demonstrates basic interaction with the [TodoMVC demo](https://demo.playwright.dev/todomvc) app created by the Playwright team.

It adds a new todo item, marks it complete, and verifies that it appears correctly in the UI.
