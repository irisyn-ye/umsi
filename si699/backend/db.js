const { MongoClient } = require('mongodb');

// MongoDB connection URL and Database Name
const mongoUrl = 'mongodb://127.0.0.1:27017';
const dbName = 'nurseFriend';
const client = new MongoClient(mongoUrl);

let db;

// Connect to the database
client.connect()
    .then(conn => {
        console.log("Connected successfully to MongoDB");
        db = conn.db(dbName);
    })
    .catch(e => {
        console.error("Failed to connect to MongoDB", e);
        process.exit(1); // Exit process with error
    });

// Export a function to get the db connection
module.exports = function getDb() {
    if (!db) {
        throw new Error("Database connection not yet established");
    }
    return db;
};
