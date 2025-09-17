# 🚀 SavvyTeam

> **A Multi-Tenant Subscription-Based Team Knowledge Hub with AI-Powered Search**

SavvyTeam solves the universal problem of scattered team knowledge. Instead of hunting through Slack, Google Docs, and emails, teams can centralize their documents, SOPs, and discussions in one searchable hub with intelligent AI-powered search.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ✨ Features

### 🔐 **Multi-Tenant Authentication**
- Email/social login with 2FA support
- Role-based access control (Admin, Manager, Contributor, Viewer)
- Organization-based data isolation

### 📚 **Knowledge Management**
- Rich-text editor for notes and SOPs
- Document upload (PDFs, images) with cloud storage
- Smart tagging and categorization
- Version control for documents

### 🤖 **AI-Powered Search**
- Natural language queries ("What's our refund policy?")
- Intelligent document indexing via background jobs
- Instant, contextual results

### 💳 **Subscription Management**
- Stripe integration for payments
- Tiered pricing (Free → Pro → Enterprise)
- Automated billing and invoicing

### 📊 **Analytics & Insights**
- Team activity dashboards
- Search analytics and usage reports
- Member engagement tracking

## 🛠️ Tech Stack

- **Backend**: Django 5.0+ with Django REST Framework
- **Database**: PostgreSQL with full-text search
- **Cache/Queue**: Redis + Celery for background tasks
- **Frontend**: Bootstrap 5
- **Storage**: AWS S3 for file uploads
- **Payments**: Stripe API
- **Email**: SendGrid
- **Deployment**: Docker + Traefik + Let's Encrypt
- **CI/CD**: GitHub Actions
- **Monitoring**: Sentry + Prometheus

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- Docker & Docker Compose
- uv (Python package manager)

### Local Development

```bash
# Clone the repository
git clone https://github.com/maniishbhusal/SavvyTeam.git
cd SavvyTeam

# Start with Docker
docker compose -f docker-compose.local.yml up -d

# Create superuser
docker compose -f docker-compose.local.yml run --rm django python manage.py createsuperuser

# Access the application
open http://localhost:8000
```

### Environment Setup

Create environment files:
```bash
# Copy example files
cp .envs/.local/.django.example .envs/.local/.django
cp .envs/.local/.postgres.example .envs/.local/.postgres

# Edit with your settings
vim .envs/.local/.django
```

## 🧪 Testing

```bash
# Run tests
uv run pytest

# With coverage
uv run coverage run -m pytest
uv run coverage html

# Type checking
uv run mypy savvyteam

# Code formatting
uv run ruff check .
uv run ruff format .
```

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### Development Workflow

1. **Fork & Clone**
   ```bash
   git clone https://github.com/maniishbhusal/SavvyTeam.git
   cd SavvyTeam
   ```

2. **Create Feature Branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make Changes**
   - Follow Django best practices
   - Add tests for new features
   - Update documentation

4. **Run Quality Checks**
   ```bash
   pre-commit run --all-files
   pytest
   ```

5. **Submit PR**
   - Clear description of changes
   - Link to related issues
   - Ensure CI passes

### Code Standards

- **Style**: Ruff for formatting and linting
- **Tests**: Minimum 80% coverage for new code
- **Documentation**: Docstrings for all public methods
- **Commits**: Conventional commit messages

### Areas for Contribution

- 🔍 **AI Search**: Improve search algorithms and relevance
- 🎨 **UI/UX**: Enhance user interface and experience
- 📱 **Mobile**: Responsive design improvements
- 🔌 **Integrations**: Slack, Teams, Google Workspace
- 🌐 **i18n**: Multi-language support
- 📊 **Analytics**: Advanced reporting features

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Cookiecutter Django](https://github.com/cookiecutter/cookiecutter-django)
- Inspired by the need for better team knowledge management
- Thanks to all contributors and the Django community

---

**Made with ❤️ for teams who value organized knowledge**
