## Description

This project is an innovative platform where multiple teams collaborate and compete to develop the most profitable quantitative trading strategies. The essence of the project lies in its focus on creating algorithms capable of front-testing or front-running in trading scenarios to maximize returns. 

## Getting Started

### Prerequisites

- Python >=3.8
- pip3 (Python package manager)

### Installation

Clone this repository to your local machine:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd <project-directory>
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Adding Dependencies

If your development introduces new Python packages as dependencies, ensure to list them in the `requirements.txt` file. Format each dependency on a new line, specifying the exact version to maintain consistency across environments:

```
flask==1.1.2
requests==2.25.1
```

### Project Structure and Execution

Your contributions should be developed in a way that complements the project's modular design. You are encouraged to create as many files or modules as necessary for clean and maintainable code. However, the integration point for all functionalities should be `main.py`. This approach ensures that the entire project can be executed cohesively through this single entry point. The structure allows for scalability and ease of management, aligning with best practices for Python project development.

While you are free to explore various architectural designs for your modules and components, remember that they should all be callable or executable from `main.py`, facilitating a unified execution flow.

### Docker and CI/CD

**Important:** Modifications to the `Dockerfile` or `gitlab-ci.yml` are not permitted. These files are pre-configured for Docker containerization and GitLab CI/CD pipelines, respectively, and are crucial for the project's automated deployment workflow. Any proposed changes to these configurations must be reviewed and approved by the project maintainers.

