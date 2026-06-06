# django_bgRemoverML

A Machine Learning Project integrated with Django to Remove Background from Image .

## Installation:

- git clone https://github.com/FarjaalAhmad/django_bgRemoverML
- cd django_bgRemoverML
- python3 -m pip install -r requirements.txt
- bash setup.sh
- python3 manage.py migrate
- python3 manage.py runserver

### Supported OS:

- Linux

### For API Usage:

Make a POST request to http://localhost:8000/upload with the Following parameters.
image=[BASE64 ENCODED IMAGE HERE]

### Bugs:

- If you found any bugs, Feel Free to create an Issue.

### Deployment:
[![DigitalOcean Referral Badge](https://web-platforms.sfo2.digitaloceanspaces.com/WWW/Badge%203.svg)](https://www.digitalocean.com/?refcode=42d61c4435ff&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)

You can register here and Get $100 Free for 2 months.

### Contribution:

- If you want to Contribute into this Project, Feel free to make Pull Request.
<a href="https://github.com/FarjaalAhmad/django_bgRemoverML/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=FarjaalAhmad/django_bgRemoverML" />
</a>
<hr>

## 🚀 Relaunch Roadmap (v2.0)

The project is actively being relaunched after a hiatus. Here's what's planned:

### ✅ Phase 1 — Foundation (In Progress)
- [ ] Unarchive and modernize project structure
- [ ] Upgrade dependencies to current stable versions
- [ ] Add Docker & Docker Compose support for easy self-hosting
- [ ] Set up CI/CD pipeline (GitHub Actions)

### 🔬 Phase 2 — ML Improvements
- [ ] Replace legacy model with U²-Net / ONNX for better accuracy & speed
- [ ] Add support for batch image processing
- [ ] GPU acceleration support (optional, via config)

### 🌐 Phase 3 — API & Developer Experience
- [ ] Rewrite REST API with async Django (or FastAPI migration option)
- [ ] Add proper API authentication (token-based)
- [ ] OpenAPI / Swagger docs
- [ ] Python SDK / client library

### 🧪 Phase 4 — Quality & Reliability
- [ ] Write unit and integration tests (target 80%+ coverage)
- [ ] Add pre-commit hooks and linting (black, flake8, isort)
- [ ] Automated PR review and issue triage

### 📦 Phase 5 — Distribution
- [ ] Publish Docker image to Docker Hub
- [ ] PyPI package for the core ML pipeline
- [ ] Hosted demo

---
