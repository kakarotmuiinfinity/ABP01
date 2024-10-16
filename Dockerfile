# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy the requirements.txt file
COPY requirements.txt ./

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 8080 for webhook (if you use it in the future)
EXPOSE 8080

# Command to run the bot
CMD ["python", "bot.py"]
