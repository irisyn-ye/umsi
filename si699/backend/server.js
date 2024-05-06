const express = require('express');
const cors = require('cors');

const app = express();
const port = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json()); // for parsing application/json

// Send a welcome message when root '/' is accessed
app.get('/', (req, res) => {
  res.send('Welcome to Nurse Friend API!')
})

// Import routes
const assessmentRoute = require('./routes/assessment');
app.use('/assessment', assessmentRoute);

const journalRoutes = require('./routes/journal'); 
app.use('/journal', journalRoutes);


app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});

