# AI-Assisted Secure Code Review Tool

A lightweight application security project demonstrating
automated static analysis, secure code review, threat modeling,
and LLM-assisted security analysis.

## Overview

The tool performs an automated security review of a deliberately
vulnerable Python Flask application.

Pipeline:

Python Source Code
↓
Bandit Static Analysis
↓
JSON Finding Parser
↓
LLM Security Review
↓
STRIDE Threat Model
↓
Markdown Security Report

## Security Engineering Concepts

This project demonstrates:

- Secure Code Review
- Static Application Security Testing
- Application Security
- STRIDE Threat Modeling
- AI-Assisted Security Analysis
- Security Automation
- Vulnerability Remediation

## Technologies

- Python
- Flask
- Bandit
- OpenAI API
- JSON
- Markdown

## Workflow

1. Scan Python source code using Bandit.
2. Export findings as structured JSON.
3. Parse vulnerabilities and surrounding source code.
4. Send security findings to an LLM.
5. Generate vulnerability explanations and remediation guidance.
6. Perform STRIDE-based threat modeling.
7. Export the final assessment as Markdown.

## Example Findings

The deliberately vulnerable application contains examples of:

- Shell command injection
- Unsafe use of eval()
- Unsafe deserialization
- Hardcoded secrets

## Disclaimer

The vulnerable application is intentionally insecure and was
created solely for application-security education and testing.
It should never be deployed to a production or public environment.