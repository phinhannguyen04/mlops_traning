# Module 1: Infrastructure & Prerequisites

**Build your dev environment with Docker, AWS, and Terraform**

## Quick Start

1. **Read the study guide** in [`docs/module-01/`](../docs/module-01/) for conceptual learning
2. **Practice with labs** in the folders below

```
Learn:  docs/module-01/        →  Theory and concepts
Do:     module-01/terraform/    →  Hands-on Terraform practice
        module-01/aws/localstack/  →  AWS service practice with LocalStack
```

## Learning Objectives

By the end of this module, you will be able to:
- Understand containerization concepts and Docker fundamentals
- Set up and configure a local development environment
- Understand AWS core services for ML workloads
- Implement Infrastructure as Code using Terraform
- Practice AWS services locally using LocalStack

## Module Structure

```
module-01/
├── aws/                         # LocalStack for local AWS practice
│   ├── docker-compose.yml       # Container configuration
│   ├── .env.example             # Environment variables
│   └── README.md                # Lab exercises
│
└── terraform/
    ├── basics/                  # Terraform fundamentals lab
    │   ├── main.tf              # Configuration files
    │   ├── variables.tf
    │   ├── outputs.tf
    │   └── README.md            # Lab instructions
    ├── examples/                # Example configurations
    │   ├── data-sources/
    │   ├── for-each/
    │   ├── locals/
    │   └── outputs/
    └── exercises/               # Practice exercises
        └── exercises.md
```

## Study Path

### Step 1: Docker (Conceptual)

**Learn in docs:**
- [`docs/module-01/docker/basics.md`](../docs/module-01/docker/basics.md) - Docker concepts and theory

**Note:** Docker labs are coming soon. For now, learn the concepts and practice with LocalStack (uses Docker under the hood).

### Step 2: AWS Cloud Services

**Learn in docs:**
| Topic | Documentation |
|-------|----------------|
| Cloud Concepts | [`docs/module-01/aws/cloud-concepts.md`](../docs/module-01/aws/cloud-concepts.md) |
| Compute Services | [`docs/module-01/aws/compute-services.md`](../docs/module-01/aws/compute-services.md) |
| Storage Services | [`docs/module-01/aws/storage-services.md`](../docs/module-01/aws/storage-services.md) |
| Database Services | [`docs/module-01/aws/database-services.md`](../docs/module-01/aws/database-services.md) |
| Networking Services | [`docs/module-01/aws/networking-services.md`](../docs/module-01/aws/networking-services.md) |
| Security & Compliance | [`docs/module-01/aws/security-compliance.md`](../docs/module-01/aws/security-compliance.md) |
| Analytics Services | [`docs/module-01/aws/analytics-services.md`](../docs/module-01/aws/analytics-services.md) |
| AI/ML Services | [`docs/module-01/aws/ai-ml-services.md`](../docs/module-01/aws/ai-ml-services.md) |
| Billing & Pricing | [`docs/module-01/aws/billing-pricing.md`](../docs/module-01/aws/billing-pricing.md) |

**Practice in labs:**
- [`module-01/aws/`](aws/) - LocalStack lab environment
  - [`README.md`](aws/README.md) - Lab exercises
  - [`docker-compose.yml`](aws/docker-compose.yml) - Container config
  - [`.env.example`](aws/.env.example) - Environment template

### Step 3: Terraform Infrastructure as Code

**Learn in docs:**
- [`docs/module-01/terraform/basics.md`](../docs/module-01/terraform/basics.md) - Complete Terraform guide
- [`docs/module-01/terraform/examples.md`](../docs/module-01/terraform/examples.md) - Example configurations
- [`docs/module-01/terraform/exercises.md`](../docs/module-01/terraform/exercises.md) - Practice exercises

**Practice in labs:**
- [`module-01/terraform/basics/`](terraform/basics/) - Terraform fundamentals lab
- [`module-01/terraform/examples/`](terraform/examples/) - Example configurations
- [`module-01/terraform/exercises/`](terraform/exercises/) - Practice exercises

## Prerequisites

- Docker Desktop installed ([Download](https://www.docker.com/products/docker-desktop))
- AWS Account ([Free Tier](https://aws.amazon.com/free/)) - optional, can use LocalStack
- Terraform installed ([Download](https://www.terraform.io/downloads.html))
- AWS CLI configured (for LocalStack practice)

## Setup

### 1. Verify Docker installation:
```bash
docker --version
docker run hello-world
```

### 2. Verify Terraform installation:
```bash
terraform version
```

### 3. Start LocalStack (for AWS practice):
```bash
cd module-01/aws
cp .env.example .env
docker compose up -d
```

## How to Study

### For Each Topic

1. **Read the conceptual guide** in `docs/module-01/`
2. **Navigate to the lab folder** in `module-01/`
3. **Follow the lab README** to practice
4. **Experiment** with configurations
5. **Complete exercises** to reinforce learning

### Example: Learning AWS S3

```bash
# 1. Read the theory
cat docs/module-01/aws/storage-services.md

# 2. Start LocalStack
cd module-01/aws
docker compose up -d

# 3. Practice S3 operations
aws --endpoint-url=http://localhost:4566 s3 ls
aws --endpoint-url=http://localhost:4566 s3 mb s3://my-bucket
```

### Example: Learning Terraform

```bash
# 1. Read the theory
cat docs/module-01/terraform/basics.md

# 2. Navigate to lab
cd module-01/terraform/basics

# 3. Practice Terraform
terraform init
terraform plan -var-file="terraform.tfvars.localstack"
terraform apply -var-file="terraform.tfvars.localstack"
```

## AWS CLF-C02 Exam Preparation

This module covers the **AWS Certified Cloud Practitioner (CLF-C02)** exam:

| Domain | Weight | Documentation |
|--------|--------|---------------|
| Domain 1: Cloud Concepts | 26% | [Cloud Concepts](../docs/module-01/aws/cloud-concepts.md) |
| Domain 2: Security & Compliance | 25% | [Security & Compliance](../docs/module-01/aws/security-compliance.md) |
| Domain 3: Core Services | 33% | All service guides linked above |
| Domain 4: Migration & Optimization | 16% | [Deployment Methods](../docs/module-01/aws/deployment-methods.md) |

## Exercises

Complete these exercises to practice what you've learned:

### LocalStack Exercises
- Exercise 1: S3 Bucket Operations (see [`aws/README.md`](aws/README.md))
- Exercise 2: DynamoDB Table Operations
- Exercise 3: Lambda Function Deployment

### Terraform Exercises
- Exercise 1: Create S3 Bucket with Terraform
- Exercise 2: Multiple Environments with for_each
- Exercise 3: Query Existing Infrastructure
- (See [`terraform/exercises/exercises.md`](terraform/exercises/exercises.md) for complete list)

## Additional Resources

### External References
- [Docker Documentation](https://docs.docker.com/)
- [AWS Documentation](https://docs.aws.amazon.com/)
- [Terraform Documentation](https://www.terraform.io/docs)
- [LocalStack Documentation](https://docs.localstack.cloud/)

### Internal Documentation
- [Complete Study Guide](../docs/README.md) - Overall training navigation
- [Module 1 Documentation](../docs/module-01/) - All conceptual guides

## Next Steps

After completing this module:
1. Review all AWS service guides in [`docs/module-01/aws/`](../docs/module-01/aws/)
2. Complete all Terraform exercises in [`terraform/exercises/`](terraform/exercises/)
3. Practice with LocalStack until comfortable with AWS CLI
4. Proceed to [Module 2: Model Deployment](../module-02/)

---

**Module Overview:** [docs/module-01/README.md](../docs/module-01/)
