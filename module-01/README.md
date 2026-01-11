# Module 1: Infrastructure & Prerequisites

**Build your dev environment with Docker, AWS, and containerized deployment basics**

## 🎯 Learning Objectives

By the end of this module, you will be able to:

- Understand containerization concepts and Docker fundamentals
- Set up and configure a local development environment with Docker
- Build and deploy containerized applications
- Understand AWS core services for ML workloads
- Implement Infrastructure as Code using Terraform

## 📋 Topics Covered

### 1. Docker Fundamentals
- Container vs. Virtual Machine concepts
- Docker architecture (daemon, CLI, images, containers)
- Building Docker images with Dockerfiles
- Docker Compose for multi-container applications
- Multi-stage builds for optimized images

### 2. AWS Cloud Services
- AWS EC2 for compute resources
- AWS S3 for data storage
- AWS IAM for security and access management
- AWS CloudShell for cloud-based development

### 3. Infrastructure as Code with Terraform
- Terraform basics and configuration language
- Provisioning AWS resources with Terraform
- Managing state and configurations
- Terraform modules for reusability

## 📂 Module Structure

```
module-01/
├── docker/
│   ├── basics/           # Docker fundamentals and first container
│   ├── multi-stage/      # Optimized Docker builds
│   └── compose/          # Multi-container applications
├── aws/
│   ├── ec2/              # EC2 instances for ML workloads
│   ├── s3/               # S3 for data and model storage
│   └── iam/              # Identity and access management
├── terraform/
│   ├── basics/           # Terraform fundamentals
│   ├── modules/          # Reusable Terraform modules
│   └── state/            # State management strategies
├── exercises/            # Hands-on practice exercises
└── solution/             # Exercise solutions
```

## 🚀 Getting Started

### Prerequisites

- Docker Desktop installed ([Download](https://www.docker.com/products/docker-desktop))
- AWS Account ([Free Tier](https://aws.amazon.com/free/))
- Terraform installed ([Download](https://www.terraform.io/downloads.html))
- AWS CLI configured

### Setup

1. **Verify Docker installation:**
   ```bash
   docker --version
   docker run hello-world
   ```

2. **Configure AWS CLI:**
   ```bash
   aws configure
   ```

3. **Verify Terraform installation:**
   ```bash
   terraform version
   ```

## 📖 Lessons

### Lesson 1.1: Docker Basics
Start here to learn containerization fundamentals.

- [Docker Basics Guide](./docker/basics/README.md)
- Exercise: Containerize a simple ML inference script

### Lesson 1.2: Multi-Stage Builds
Learn to optimize Docker images for production.

- [Multi-Stage Builds Guide](./docker/multi-stage/README.md)
- Exercise: Create optimized ML model serving image

### Lesson 1.3: Docker Compose
Orchestrate multi-container applications.

- [Docker Compose Guide](./docker/compose/README.md)
- Exercise: Build a full ML API stack with database

### Lesson 1.4: AWS Core Services
Essential AWS services for ML workloads.

- [AWS Services Guide](./aws/README.md)
- Exercise: Deploy a container to AWS ECS

### Lesson 1.5: Terraform Fundamentals
Infrastructure as Code with Terraform.

- [Terraform Guide](./terraform/basics/README.md)
- Exercise: Provision AWS infrastructure with Terraform

## 💡 Exercises

Complete the exercises in the `exercises/` directory to practice what you've learned.

1. [Exercise 1.1: Your First Container](./exercises/exercise-01-first-container.md)
2. [Exercise 1.2: ML Model Containerization](./exercises/exercise-02-ml-container.md)
3. [Exercise 1.3: AWS Resource Provisioning](./exercises/exercise-03-aws-provision.md)

## 📚 Additional Resources

- [Docker Documentation](https://docs.docker.com/)
- [AWS Documentation](https://docs.aws.amazon.com/)
- [Terraform Documentation](https://www.terraform.io/docs)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)

## 🎓 Next Steps

After completing this module, proceed to [Module 2: Model Deployment](../module-02/README.md)
