# Introduction to MLOps Training

A comprehensive hands-on training program covering the fundamentals of MLOps, infrastructure automation, model deployment, and CI/CD practices.

## 📚 Course Overview

This training is designed to equip you with practical skills in building, deploying, and maintaining machine learning systems in production environments.

### Learning Objectives

- Set up development environments with Docker and cloud infrastructure
- Deploy machine learning models via batch jobs, web APIs, and streaming services
- Implement testing strategies and CI/CD pipelines for ML systems
- Understand infrastructure-as-code practices with Terraform

## 🗂️ Course Structure

| Module | Topic | Description | Technologies |
|--------|-------|-------------|--------------|
| 1 | Infrastructure & Prerequisites | Build your dev environment with Docker, AWS, and containerized deployment basics | Docker, AWS, Terraform, Cloud Shells |
| 2 | Model Deployment | Ship models via batch jobs, web APIs, and streaming services | FastAPI, Docker, AWS Lambda, AWS Kinesis |
| 3 | Testing & CI/CD | Add testing, CI/CD, and cloud infrastructure fundamentals | GitHub Actions, LocalStack |

## 📂 Repository Structure

```
mlops-training/
├── module-01/            # Infrastructure & Prerequisites
│   ├── docker/           # Docker fundamentals and containerization
│   ├── aws/              # AWS services and cloud setup
│   ├── terraform/        # Infrastructure as Code examples
│   ├── exercises/        # Practice exercises
│   └── solution/         # Exercise solutions
├── module-02/            # Model Deployment
│   ├── batch-api/        # Batch and API deployment patterns
│   ├── streaming/        # Real-time streaming deployments
│   ├── exercises/        # Practice exercises
│   └── solution/         # Exercise solutions
├── module-03/            # Testing & CI/CD
│   ├── testing/          # Testing strategies for ML systems
│   ├── cicd/             # CI/CD pipeline implementations
│   ├── exercises/        # Practice exercises
│   └── solution/         # Exercise solutions
├── docs/                 # Additional documentation
├── assets/               # Images, diagrams, and reference materials
└── .github/              # GitHub Actions workflows
```

## 🚀 Getting Started

### Prerequisites

- Basic knowledge of Python
- Understanding of machine learning concepts
- Familiarity with command-line interface

### Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd mlops-training
   ```

2. Navigate to the first module:
   ```bash
   cd module-01
   ```

3. Follow the module README to set up your environment

## 📖 Module Guides

- [Module 1: Infrastructure & Prerequisites](./module-01/README.md)
- [Module 2: Model Deployment](./module-02/README.md)
- [Module 3: Testing & CI/CD](./module-03/README.md)

## 🤝 Contributing

This is a training repository. For contribution guidelines, see [CONTRIBUTING.md](./CONTRIBUTING.md)

## 📄 License

See [LICENSE](./LICENSE) for details

## 🙏 Acknowledgments

Built for MLOps training and education purposes.
