# FRONTEND BUILD STAGE
FROM node:20 AS frontend-build

# Set the working directory for the frontend build
WORKDIR /app/frontend

# Copy package.json and package-lock.json for npm install
COPY frontend/package.json frontend/package-lock.json ./

# Install npm dependencies
RUN npm install

# Copy the rest of the frontend source code
COPY frontend/ ./

# Build the frontend
RUN npm run build

# BACKEND BUILD STAGE
FROM python:3.9-slim

# Set the working directory in the container for the backend
WORKDIR /app

# Copy the frontend build from the previous stage to the static folder served by Flask
COPY --from=frontend-build /app/frontend/build /app/frontend/build

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend code
COPY . .

# Expose the port Flask is running on
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=Router.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask application
CMD ["python3", "Router.py"]
