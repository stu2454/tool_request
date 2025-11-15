# Use official lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install OS-level dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (use caching)
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Expose Streamlit default port
EXPOSE 10000

# Allow Streamlit to run on Render with the correct host/port
ENV PORT=10000

# Streamlit config to allow external connections
RUN mkdir -p ~/.streamlit

RUN bash -c 'echo "\
    [server]\n\
    headless = true\n\
    port = 10000\n\
    enableCORS = false\n\
    enableXsrfProtection = false\n\
    " > ~/.streamlit/config.toml'

# Start the app
CMD ["streamlit", "run", "streamlit_app.py"]

