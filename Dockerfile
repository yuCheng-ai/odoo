FROM python:3.12-slim-bookworm

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libxml2-dev \
    libxslt1-dev \
    libldap2-dev \
    libsasl2-dev \
    libjpeg-dev \
    zlib1g-dev \
    libffi-dev \
    libssl-dev \
    libpng-dev \
    libwebp-dev \
    libtiff-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libopenjp2-7-dev \
    libharfbuzz-dev \
    libfribidi-dev \
    libxcb1-dev \
    node-less \
    npm \
    git \
    curl \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install wkhtmltopdf
RUN apt-get update && apt-get install -y wkhtmltopdf

# Set working directory
WORKDIR /opt/odoo

# Copy requirements and install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt watchdog

# Expose Odoo port
EXPOSE 8069

# Command to run Odoo
CMD ["python3", "odoo-bin", "-c", "odoo.conf"]
