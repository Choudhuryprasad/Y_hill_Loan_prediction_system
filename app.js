const express = require('express');
const bodyParser = require('body-parser');
const { spawn } = require('child_process');

const app = express();


app.set('view engine', 'ejs');
app.use(express.static('./public'));
app.use(express.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.get('/', (req, res) => {
    res.render('index');
});

app.post('/predict', (req, res) => {
    const data = req.body;

    // Ensure to key are present
    const requiredKeys = ['gender', 'married', 'education', 'employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'property_Area'];
    const missingKeys = requiredKeys.filter(key => !(key in data));

    if (missingKeys.length > 0) {
        return res.status(400).json({ error: `Missing keys: ${missingKeys.join(', ')}` });
    }

    const dataString = JSON.stringify(data);

    
    const pythonProcess = spawn('python', ['predictor.py', dataString]);

    let pythonOutput = '';

    pythonProcess.stdout.on('data', (data) => {
        pythonOutput += data.toString();
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error(`Error from Python script: ${data}`);
    });

    pythonProcess.on('close', () => {
        res.render('predict', { pythonOutput });
    });
});

const PORT = 8080;
app.listen(PORT, () => {
    console.log(`Server started on http://localhost:${PORT}`);
});
