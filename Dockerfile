# ------------------------------
# 1. Base image
# ------------------------------
FROM python:3.10-slim

# ------------------------------
# 2. Working directory
# ------------------------------
WORKDIR /app

# ------------------------------
# 3. Install OS-level dependencies
# ------------------------------
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# ------------------------------
# 4. Copy requirements first for caching
# ------------------------------
COPY requirements.txt .

# ------------------------------
# 5. Install Python dependencies
# ------------------------------
RUN pip install --no-cache-dir -r requirements.txt

# ------------------------------
# 6. Copy your entire app repo
# ------------------------------
COPY . .

# ------------------------------
# 7. Streamlit Cloud / Render config
# ------------------------------
ENV PORT=10000

# Create the Streamlit config directory
RUN mkdir -p ~/.streamlit

# Write config.toml safely (HEREDOC avoids TOML parsing issues)
RUN cat <<EOF > ~/.streamlit/config.toml
[server]
headless = true
port = 10000
enableCORS = false
enableXsrfProtection = false
EOF

# ------------------------------
# 8. Expose port for Render
# ------------------------------
EXPOSE 10000

# ------------------------------
# 9. Run the app
# ------------------------------
CMD ["streamlit", "run", "0_Start_here.py"]
