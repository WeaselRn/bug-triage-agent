# TriageBot

## AI-Powered GitLab Bug Triage Agent

TriageBot is an AI-powered GitLab issue triage assistant built using Google ADK, Gemini 2.5 Flash, GitLab MCP, and Google Cloud Run.

The goal of TriageBot is to reduce the manual effort involved in reviewing, categorizing, prioritizing, and managing GitLab issues. It acts as an AI engineering teammate capable of analyzing issues, generating structured triage assessments, recommending actions, and interacting directly with GitLab.

This project was built for the GitLab Partner Prize challenge.

---

# Problem

Engineering teams spend significant time manually:

* Reviewing newly created issues
* Determining severity and priority
* Categorizing issues
* Identifying duplicate reports
* Deciding ownership
* Maintaining a healthy backlog

As projects scale, these activities become increasingly time-consuming and inconsistent.

TriageBot automates these workflows and helps teams focus on solving problems instead of managing them.

---

# Features

## Intelligent Issue Analysis

TriageBot analyzes GitLab issues and generates:

* Severity level
* Category
* Priority score
* Business impact assessment
* Technical impact assessment
* Recommended action

---

## Automatic Label Generation

The agent generates structured labels such as:

```text
severity::critical
severity::high
severity::medium
severity::low

type::bug
type::security
type::performance
type::documentation
type::feature
type::infrastructure

area::backend
area::frontend
area::database
area::api
area::infrastructure
```

These labels help teams maintain a clean and searchable issue backlog.

---

## Duplicate Issue Detection

TriageBot reviews existing project issues and identifies potential duplicates.

Benefits:

* Reduces duplicate investigations
* Prevents fragmented discussions
* Keeps the backlog organized
* Improves issue visibility

---

## Owner Recommendation

The agent can retrieve project members and recommend the most suitable owner for an issue based on its characteristics and affected area.

---

## GitLab Integration

Using GitLab MCP, TriageBot can:

* Retrieve projects
* Retrieve issues
* Retrieve labels
* Retrieve project members
* Create labels
* Update issues
* Add issue comments

---

## Automated Triage Workflow

TriageBot supports an automated triage workflow:

```text
Issue
    ↓
Issue Analysis
    ↓
Severity Classification
    ↓
Category Classification
    ↓
Priority Scoring
    ↓
Duplicate Detection
    ↓
Owner Recommendation
    ↓
Label Generation
    ↓
GitLab Update
    ↓
Triage Comment Creation
```

---

# Architecture

```text
Google ADK Agent
        ↓
Gemini 2.5 Flash
        ↓
GitLab MCP Server
        ↓
GitLab
```

---

# Technology Stack

* Google ADK
* Gemini 2.5 Flash
* GitLab MCP
* Google Cloud Run
* Docker
* Python

---

# Example Triage Output

```text
Severity: High

Priority Score: 85/100

Category: Bug

Area: Backend

Business Impact:
Users are unable to reset passwords.

Technical Impact:
Authentication service fails while validating reset tokens.

Suggested Labels:
- severity::high
- type::bug
- area::backend

Potential Duplicates:
- Issue #12
- Issue #18

Recommended Action:
Investigate authentication service regression.
```

---

# Repository Structure

```text
bug-triage-adk/
│
├── bug_triage_agent/
│   ├── __init__.py
│   ├── agent.py
│   └── mcp_test.py
│
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

---

# Getting Started

## Prerequisites

Install:

* Python 3.11+
* Node.js 20+
* Docker
* Google Cloud SDK

You will also need:

* GitLab Personal Access Token
* Google Cloud Project
* Gemini API access through Vertex AI

---

# Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git

cd YOUR_REPOSITORY
```

---

# Create Virtual Environment

Windows:

```bash
python -m venv .venv

.venv\Scripts\activate
```

Linux / macOS:

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Configure Environment Variables

Windows PowerShell:

```powershell
$env:GITLAB_PERSONAL_ACCESS_TOKEN="your_gitlab_token"

$env:GOOGLE_GENAI_USE_VERTEXAI="true"

$env:GOOGLE_CLOUD_PROJECT="your_project"

$env:GOOGLE_CLOUD_LOCATION="us-central1"
```

Linux / macOS:

```bash
export GITLAB_PERSONAL_ACCESS_TOKEN="your_gitlab_token"

export GOOGLE_GENAI_USE_VERTEXAI=true

export GOOGLE_CLOUD_PROJECT="your_project"

export GOOGLE_CLOUD_LOCATION="us-central1"
```

---

# Authenticate Google Cloud

```bash
gcloud auth application-default login
```

---

# Run Locally

```bash
adk web
```

or

```bash
adk web --host 0.0.0.0 --port 8000
```

---

# Build Docker Image

```bash
docker build -t bug-triage-adk .
```

---

# Deploy to Cloud Run

Example:

```bash
gcloud builds submit \
--tag us-central1-docker.pkg.dev/PROJECT_ID/REPOSITORY/bug-triage-adk

gcloud run deploy bug-triage-adk
```

---

# Example Prompts

Analyze an issue:

```text
Analyze issue #12 in project 12345
```

Apply triage:

```text
Apply triage to issue #12 in project 12345
```

Find duplicate issues:

```text
Find duplicate issues for issue #12 in project 12345
```

Review top issues:

```text
Analyze the top 5 open issues in project 12345
```

---

# Future Improvements

* Automatic webhook-based triage
* GitLab event triggers
* Automated issue assignment
* Slack notifications
* Daily triage summaries
* Trend analysis
* Engineering analytics dashboard

---

# Security

Never commit:

```text
GITLAB_PERSONAL_ACCESS_TOKEN
Google credentials
Service account keys
.env files
```

Always use secure environment variables and secret management systems when deploying to production.

---

# License

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.
