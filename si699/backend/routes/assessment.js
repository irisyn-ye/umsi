const express = require('express');
const router = express.Router();
const getDb = require('../db');

const isEmpty = (data) => {
    return data === undefined || data === null || data === '';
};

router.post('/setAnswer', async (req, res) => {
    try {
        const db = await getDb();
        const collection = db.collection('assessment');

        // Attempt to find a document matching the uid
        const doc = await collection.findOne({ uid: req.body.uid });

        if (doc) {
            await collection.updateOne({ uid: req.body.uid }, { $set: { [req.body.question]: req.body.answer } });
            res.status(200).json({ message: "Answer updated successfully" });
        } else {
            // If no document is found, create a new document with the uid and answer
            const newDoc = {
                uid: req.body.uid,
                [req.body.question]: req.body.answer
            }
            await collection.insertOne(newDoc);
            res.status(200).json({ message: "Answer set successfully" });
        };
    }
    catch (error) {
        console.error('Error accessing the database', error);
        res.status(500).send('Error accessing the database');
    }
});

router.get('/getAssessment/:uid', async (req, res) => {
    try {
        const db = await getDb();
        const collection = db.collection('assessment');
        const doc = await collection.findOne({ uid: req.params.uid });

        if (doc) {
            res.status(200).json(doc);
        } else {
            res.status(404).send('Data not found');
        }
    } catch (error) {
        console.error('Error accessing the database', error);
        res.status(500).send('Error accessing the database');
    }
});

module.exports = router;
