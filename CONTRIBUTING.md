# Contributing to SciCode-Nexus

Thank you for considering contributing to SciCode-Nexus! We welcome contributions from the community to help improve this autonomous research assistant system.

## How to Contribute

There are several ways you can contribute to SciCode-Nexus:

1. **Report bugs** - If you find a bug, please open an issue on GitHub.
2. **Suggest features** - Have an idea for a new feature? Open an issue to discuss it.
3. **Improve documentation** - Help us improve our documentation by fixing typos, adding examples, or writing new sections.
4. **Contribute code** - Fix bugs, implement new features, or improve existing code.

## Reporting Bugs

Before reporting a bug, please check if it has already been reported by searching the [issue tracker](https://github.com/ndjones/scicode-nexus/issues).

When reporting a bug, please include:
- A clear and descriptive title
- Steps to reproduce the issue
- Expected behavior vs. actual behavior
- Any relevant logs or error messages
- Information about your environment (OS, Python version, etc.)

## Suggesting Features

Feature requests are welcome! Please open an issue to discuss your idea before starting work. This helps ensure that your contribution aligns with the project's goals and avoids duplicate effort.

## Development Setup

To set up a development environment for SciCode-Nexus, follow the instructions in [Setup Guide](setup.md).

## Making Changes

1. **Fork the repository** on GitHub.
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/scicode-nexus.git
   ```
3. **Create a branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```
   or for bug fixes:
   ```bash
   git checkout -b bugfix/your-bug-fix
   ```
4. **Make your changes** in your branch.
5. **Run tests** to ensure your changes don't break existing functionality:
   ```bash
   python tests/run_tests.py
   ```
6. **Commit your changes** with a clear and descriptive commit message.
7. **Push your branch** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
8. **Open a pull request** against the `main` branch of the original repository.

## Pull Request Process

1. Ensure your pull request description clearly describes the problem and solution.
2. Include any relevant issue numbers in your pull request description.
3. Your pull request will be reviewed by maintainers. Please be responsive to any feedback or requests for changes.
4. Once approved, your pull request will be merged.

## Coding Standards

- Follow the existing code style in the project (PEP 8 for Python).
- Write clear, descriptive comments and docstrings.
- Ensure new code is covered by tests where applicable.
- Keep commits focused and atomic.

## Git Workflow

We follow a Git workflow similar to what's described in our [Phase 2 design document](https://github.com/ndjones/scicode-nexus/blob/main/plans/PLAN_PHASE2.md):

- **Main Branch**: Production-ready code only
- **Develop Branch**: Integration branch for features
- **Feature Branches**: `feature/short-description` for new features
- **Task Branches**: `task/openhands-task-id` for OpenHands-generated tasks
- **Hotfix Branches**: `hotfix/description` for urgent fixes

Pull requests should be made against the `develop` branch, and we regularly merge `develop` into `main` for releases.

## Test-Driven Development

We encourage a test-driven development approach:
- Write tests before implementation (Red-Green-Refactor)
- Focus on validating bootstrap artifacts and service functionality
- Use pytest for Python testing
- Tests are located in the `tests/` directory

## Community

Please be respectful and considerate of others when contributing to this project. We aim to foster an inclusive and welcoming environment.

## Getting Help

If you need help with your contribution, please don't hesitate to ask in the issue tracker or reach out to the maintainers.

Thank you again for contributing to SciCode-Nexus!