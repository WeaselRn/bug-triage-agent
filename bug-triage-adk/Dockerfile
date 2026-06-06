FROM python:3.11-slim

# Install Node.js
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Install GitLab MCP globally
RUN npm install -g @zereight/mcp-gitlab

COPY . .

EXPOSE 8080

CMD ["adk", "web", "--host", "0.0.0.0", "--port", "8080"]