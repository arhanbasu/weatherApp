# Weather Monitoring System

A real-time weather monitoring application that retrieves weather data from the OpenWeatherMap API, processes it, and displays it in an attractive frontend with visualizations and alerts.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [API Key](#api-key)
- [Directory Structure](#directory-structure)
- [License](#license)

## Features
- Retrieve real-time weather data for major cities in India.
- Display current weather conditions, including temperature and weather type.
- Visualize daily weather trends with plots.
- Alert users for specific weather conditions (e.g., high temperature).
- Responsive and user-friendly interface built with React.

## Technologies Used
- **Frontend**: React, Axios, CSS
- **Backend**: Node.js, Express
- **Python**: Matplotlib for data visualization
- **Database**: SQLite for storing daily weather summaries
- **API**: OpenWeatherMap API

## Setup Instructions

### Prerequisites
- Ensure you have [Node.js](https://nodejs.org/en/) installed (version 12 or later).
- Ensure you have [Python](https://www.python.org/downloads/) installed (version 3.6 or later).
- Ensure you have [pip](https://pip.pypa.io/en/stable/) installed to manage Python packages.

### Clone the Repository
```bash
git clone https://github.com/yourusername/weather_monitoring_system.git
cd weather_monitoring_system
```

### Install Backend Dependencies
Navigate to the backend directory and install the necessary dependencies:
```bash
cd backend
npm install express axios
```

### Install Frontend Dependencies
Navigate to the frontend directory and install the necessary dependencies:
```bash
cd ../frontend
npm install axios
```

### Install Python Dependencies
Make sure to install Matplotlib for data visualization:
```bash
pip install matplotlib
```

## Running the Application

### Start the Backend Server
Navigate to the backend directory and start the Express server:
```bash
cd backend
node server.js
```
The backend will be running on http://localhost:5000.

### Start the Frontend Application
Open a new terminal window, navigate to the frontend directory, and start the React application:
```bash
cd ../frontend
npm start
```
The frontend will be running on http://localhost:3000.

## API Key
To retrieve weather data, you need an API key from OpenWeatherMap. Follow these steps:

1. Sign up at OpenWeatherMap.
2. After signing in, navigate to the API keys section and generate a new key.
3. Replace YOUR_API_KEY in the backend code with your actual API key.

## Directory Structure

```bash
weather_monitoring_system/
│
├── backend/                    # Backend application
│   ├── python/                 # Python scripts
│   │   └── plot_visuals.py     # Script for plotting weather data
│   ├── server.js               # Main server file
│   ├── package.json             # Node.js dependencies
│   └── storage.db              # SQLite database file
│
└── frontend/                   # Frontend application
    ├── public/                 # Static files
    ├── src/                    # React source files
    │   └── App.js              # Main React component
    ├── package.json             # React dependencies
    └── App.css                 # CSS styles
```

## License
This project is licensed under the MIT License. See the [LICENSE](#license) file for details.
