import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [weatherData, setWeatherData] = useState([]);  // State to store database content
  const [plotUrl, setPlotUrl] = useState('');  // State to store plot URL

  // Start Python script
  const startPython = () => {
    axios.post('http://localhost:5000/start')
      .then(response => alert(response.data.message))
      .catch(error => alert(error.response.data.message));
  };

  // Stop Python script
  const stopPython = () => {
    axios.post('http://localhost:5000/stop')
      .then(response => alert(response.data.message))
      .catch(error => alert(error.response.data.message));
  };

  // Fetch database contents and display them in the app
  const fetchDatabase = () => {
    axios.get('http://localhost:5000/data')
      .then(response => {
        setWeatherData(response.data);  // Store data in state
      })
      .catch(error => alert('Error fetching database contents'));
  };

  // Fetch and display plot image
  const displayPlot = () => {
    setPlotUrl('http://localhost:5000/plot');  // Set the plot URL
  };

  return (
    <div className="App">
      <h1>Weather Monitoring System</h1>
      <div>
        <button onClick={startPython}>Start</button>
        <button onClick={stopPython}>Stop</button>
        <button onClick={fetchDatabase}>Show Database</button>
        <button onClick={displayPlot}>Display Plot</button>
      </div>

      {/* Display Weather Data in a Table */}
      {weatherData.length > 0 && (
        <div>
          <h2>Weather Data</h2>
          <table border="1" style={{ width: '100%', textAlign: 'left', marginTop: '20px' }}>
            <thead>
              <tr>
                <th>Date</th>
                <th>City</th>
                <th>Average Temperature (°C)</th>
                <th>Max Temperature (°C)</th>
                <th>Min Temperature (°C)</th>
                <th>Dominant Condition</th>
              </tr>
            </thead>
            <tbody>
              {weatherData.map((entry, index) => (
                <tr key={index}>
                  <td>{new Date(entry.date).toLocaleDateString()}</td>
                  <td>{entry.city}</td>
                  <td>{entry.avg_temp}</td>
                  <td>{entry.max_temp}</td>
                  <td>{entry.min_temp}</td>
                  <td>{entry.dominant_condition}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {/* Display Plot */}
      {plotUrl && (
        <div>
          <h2>Weather Plot</h2>
          <img src={plotUrl} alt="Weather Plot" style={{ width: '100%', marginTop: '20px' }} />
        </div>
      )}
    </div>
  );
}

export default App;


