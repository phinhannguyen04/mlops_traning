# Module 2: Model Deployment

**Ship models via batch jobs, web APIs, and streaming services**

## 🎯 Learning Objectives

By the end of this module, you will be able to:

- Build production-ready REST APIs for model serving
- Deploy models as serverless functions (AWS Lambda)
- Implement batch inference jobs
- Build real-time inference pipelines with streaming
- Handle model versioning and A/B testing

## 📋 Topics Covered

### 1. REST API Deployment (FastAPI)
- Building RESTful APIs for ML models
- Request/response validation
- Authentication and rate limiting
- Containerization and deployment

### 2. Serverless Deployment (AWS Lambda)
- Deploying models as Lambda functions
- Handling cold starts
- API Gateway integration
- Serverless best practices

### 3. Batch Inference
- Designing batch processing pipelines
- AWS Batch for ML workloads
- Scalable data processing patterns

### 4. Real-Time Streaming
- Building streaming inference pipelines
- AWS Kinesis integration
- Low-latency model serving

## 📂 Module Structure

```
module-02/
├── batch-api/
│   ├── fastapi/          # REST API deployment with FastAPI
│   └── batch-lambda/     # Batch processing with AWS Lambda
├── streaming/
│   ├── kinesis/          # AWS Kinesis streaming pipeline
│   └── real-time/        # Real-time inference patterns
├── exercises/            # Hands-on practice exercises
└── solution/             # Exercise solutions
```

## 🚀 Getting Started

### Prerequisites

- Completed Module 1: Infrastructure & Prerequisites
- Docker installed and running
- AWS account with appropriate permissions
- Basic knowledge of REST APIs

### Setup

1. Navigate to the batch-api directory:
   ```bash
   cd module-02/batch-api
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

## 📖 Lessons

### Lesson 2.1: REST API with FastAPI
Build a production-ready API for model serving.

- [FastAPI Guide](./batch-api/fastapi/README.md)
- Exercise: Build a model inference API

### Lesson 2.2: Serverless Deployment
Deploy your model as an AWS Lambda function.

- [Lambda Guide](./batch-api/batch-lambda/README.md)
- Exercise: Deploy serverless model endpoint

### Lesson 2.3: Streaming Inference
Build real-time inference with AWS Kinesis.

- [Kinesis Guide](./streaming/kinesis/README.md)
- Exercise: Create streaming ML pipeline

## 💡 Deployment Patterns

### Synchronous REST API
```
Client → API Gateway → Load Balancer → Container/Service → Model
                      ← Response ←                  ← Prediction
```

### Serverless
```
Client → API Gateway → Lambda → Model (in container or package)
                      ← Response ←
```

### Batch Processing
```
S3 → SQS → Lambda/Batch → Model → Results S3
                     ↓
                  CloudWatch
```

### Streaming
```
Producer → Kinesis Stream → Lambda/EC2 → Model → Kinesis Firehose → S3/DynamoDB
```

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)
- [AWS Kinesis Documentation](https://docs.aws.amazon.com/kinesis/)
- [Serverless Framework](https://www.serverless.com/framework)

## 🎓 Next Steps

After completing this module, proceed to [Module 3: Testing & CI/CD](../module-03/README.md)
