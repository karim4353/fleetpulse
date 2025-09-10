# Contributing to FleetPulse

Thank you for your interest in contributing to the FleetPulse EV Fleet Telematics & Charging Optimizer prototype! This document provides guidelines for contributing to the project.

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Python 3.10+
- Node.js 16+ (for frontend development)
- Git

### Development Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fleetpulse-prototype
   ```

2. **Set up local environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip
   ```

3. **Start the development stack**
   ```bash
   make up
   # or
   docker-compose up --build -d
   ```

4. **Run the demo to verify setup**
   ```bash
   make demo
   ```

## How to Contribute

### Types of Contributions

We welcome several types of contributions:

- **Bug fixes**: Fix issues in existing code
- **Feature enhancements**: Improve existing functionality
- **New features**: Add new capabilities (within prototype scope)
- **Documentation**: Improve or add documentation
- **Testing**: Add or improve test coverage
- **Performance**: Optimize existing code

### Development Workflow

1. **Fork the repository** and create your feature branch
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following our coding standards

3. **Write or update tests** for your changes

4. **Run the test suite**
   ```bash
   make test
   ```

5. **Run linting**
   ```bash
   make lint
   ```

6. **Commit your changes** with a clear commit message
   ```bash
   git commit -m "feat: add SoH prediction caching mechanism"
   ```

7. **Push to your fork** and submit a pull request

### Coding Standards

#### Python Services
- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Write docstrings for functions and classes
- Use black for code formatting
- Use flake8 for linting
- Keep functions small and focused
- Write unit tests for new functionality

#### TypeScript/JavaScript
- Follow standard ESLint configuration
- Use Prettier for code formatting
- Write JSDoc comments for functions
- Use meaningful variable names
- Keep components small and focused

#### Docker & Infrastructure
- Use multi-stage builds where appropriate
- Minimize image sizes
- Document environment variables
- Use health checks for services
- Follow security best practices

### Testing Guidelines

- Write unit tests for all new functionality
- Include integration tests for API endpoints
- Use meaningful test names that describe what is being tested
- Mock external dependencies in unit tests
- Ensure tests are deterministic and can run in any order

### Documentation

- Update README.md if you add new features or change setup process
- Add or update API documentation in `docs/api.md`
- Include code comments for complex logic
- Update CHANGELOG.md following semantic versioning

## Project Structure

Understanding the project structure will help you contribute effectively:

```
fleetpulse-prototype/
├── services/           # Microservices (ingestion, model serving, etc.)
├── frontend/          # React dashboard
├── ml/               # ML models and MLflow artifacts
├── data/             # Sample synthetic data
├── docs/             # Project documentation
├── tests/            # Integration and unit tests
├── examples/         # API examples and configurations
├── infra/            # Terraform and Kubernetes configs
└── scripts/          # Demo and utility scripts
```

## Submission Guidelines

### Pull Request Process

1. **Ensure your PR addresses a specific issue** or clearly describes the problem it solves
2. **Update documentation** that relates to your changes
3. **Add tests** that prove your fix/feature works
4. **Ensure all tests pass** in CI
5. **Keep PRs focused** - one feature or fix per PR
6. **Write clear PR descriptions** explaining what and why

### Commit Message Format

Use conventional commits format:
```
type(scope): description

[optional body]

[optional footer]
```

Types:
- `feat`: new feature
- `fix`: bug fix
- `docs`: documentation changes
- `test`: adding or updating tests
- `refactor`: code refactoring
- `perf`: performance improvements
- `ci`: CI/CD changes

Examples:
```
feat(optimizer): add battery temperature constraints
fix(ingestion): handle malformed telemetry events
docs(api): update charging optimization endpoint spec
```

## Important Constraints

### Security & Privacy
- **No real PII**: Only use synthetic/anonymized data
- **No real actuation**: This is a recommendation-only prototype
- **Follow security guidelines** in SECURITY.md
- **Test with sample data only**

### Prototype Scope
- Focus on demonstration and proof-of-concept
- Prioritize functionality over production readiness
- Keep dependencies minimal and well-documented
- Ensure local development remains simple (Docker Compose)

## Getting Help

If you need help or have questions:

1. **Check existing issues** in the GitHub repository
2. **Review documentation** in the `docs/` directory
3. **Ask questions** by opening a new issue with the "question" label
4. **Join discussions** in pull requests and issues

## Recognition

All contributors will be recognized in our README.md contributors section. We appreciate all forms of contribution, from code to documentation to issue reporting.

## Code of Conduct

Please note that this project has a Code of Conduct. By participating in this project, you agree to abide by its terms. In short: **Be nice.**

Thank you for contributing to FleetPulse! 🚗⚡