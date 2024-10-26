const express = require('express');
const cors = require('cors');
const { exec, spawn } = require('child_process');
const path = require('path');
const app = express();

app.use(cors()); // To allow cross-origin requests from React frontend
app.use(express.json());

let pythonProcess = null;

// Start Python script
app.post('/start', (req, res) => {
    if (!pythonProcess) {
        pythonProcess = spawn('python3', [path.join(__dirname, 'python', 'main.py')]);

        pythonProcess.stdout.on('data', (data) => {
            console.log(`Python stdout: ${data}`);
        });

        pythonProcess.stderr.on('data', (data) => {
            console.error(`Python stderr: ${data}`);
        });

        pythonProcess.on('close', (code) => {
            console.log(`Python process exited with code ${code}`);
            pythonProcess = null;
        });

        res.status(200).send({ message: 'Python script started' });
    } else {
        res.status(400).send({ message: 'Python script is already running' });
    }
});

// Stop Python script
app.post('/stop', (req, res) => {
    if (pythonProcess) {
        pythonProcess.kill();
        pythonProcess = null;
        res.status(200).send({ message: 'Python script stopped' });
    } else {
        res.status(400).send({ message: 'Python script is not running' });
    }
});

// Fetch database contents
app.get('/data', (req, res) => {
    exec('python3 python/read_database.py', (error, stdout, stderr) => {
        if (error) {
            console.error(`Error: ${stderr}`);
            res.status(500).send({ message: 'Error fetching database contents' });
            return;
        }
        res.status(200).send(stdout);
    });
});

// Display plot
app.get('/plot', (req, res) => {
    exec('python3 python/plot_visuals.py', (error, stdout, stderr) => {
        if (error) {
            console.error(`Error: ${stderr}`);
            res.status(500).send({ message: 'Error generating plot' });
            return;
        }
        res.sendFile(path.join(__dirname, 'python', 'plot.png'));  // Serve plot image
    });
});

const PORT = 5000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

