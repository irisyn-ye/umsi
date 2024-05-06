const express = require('express');
const router = express.Router();
const getDb = require('../db');
const { ObjectId } = require('mongodb');

//  currently not filtering with user id
//  for after we have user auth we need to filter by user id first

router.post('/setJournalEntry', async (req, res) => {
    try {
        const db = await getDb();
        const collection = db.collection('journalEntries');

        // Attempt to find a document matching the entryId
        const doc = await collection.findOne({ _id: new ObjectId(req.body.entryId) });

        if (doc) {
            // If document exists, update it
            await collection.updateOne({ _id: new ObjectId(req.body.entryId) }, { $set: { title: req.body.title, text: req.body.text, timestamp: new Date() } });
            res.status(200).json({ message: "Journal entry updated successfully" });
        } else {
            // If no document is found, create a new one
            const newDoc = {
                title: req.body.title,
                text: req.body.text,
                promptId: req.body.promptId,
                promptText: req.body.promptText || '',
                timestamp: new Date()
            };
            await collection.insertOne(newDoc);
            res.status(200).json({ message: "Journal entry created successfully" });
        };
    } catch (error) {
        console.error('Error accessing the database', error);
        res.status(500).send('Error accessing the database');
    }
});

router.patch('/journalEntry/:entryId', async (req, res) => {
    try {
        const db = await getDb();
        const collection = db.collection('journalEntries');
        const { entryId } = req.params;

        // Ensure entryId is converted to ObjectId for querying
        const filter = { _id: new ObjectId(entryId) };
        const update = { $set: req.body };

        const result = await collection.updateOne(filter, update);

        if (result.matchedCount === 0) {
            return res.status(404).send('Journal entry not found');
        }

        // Optionally, you might want to send back the updated document
        // This requires another query since updateOne does not return the document
        const updatedDoc = await collection.findOne(filter);

        res.status(200).json({
            message: "Journal entry updated successfully",
            updatedEntry: updatedDoc // Send back the updated document
        });
    } catch (error) {
        console.error('Error accessing the database', error);
        res.status(500).send('Error accessing the database');
    }
});



router.get('/getJournals', async (req, res) => {
    try {
        const db = await getDb();
        const collection = db.collection('journalEntries');
        const docs = await collection.find({}).toArray();

        if (docs.length > 0) {
            res.status(200).json(docs);
        } else {
            res.status(404).send('No journal entries found');
        }
    } catch (error) {
        console.error('Error accessing the database', error);
        res.status(500).send('Error accessing the database');
    }
});

router.get('/journalEntry/:entryId', async (req, res) => {
    try {
        const db = await getDb();
        const collection = db.collection('journalEntries');
        const doc = await collection.findOne({ _id: new ObjectId(req.params.entryId) });

        if (doc) {
            res.status(200).json(doc);
        } else {
            res.status(404).send('Journal entry not found');
        }
    } catch (error) {
        console.error('Error accessing the database', error);
        res.status(500).send('Error accessing the database');
    }
});

router.delete('/journalEntry/:entryId', async (req, res) => {
    try {
        const db = await getDb();
        const collection = db.collection('journalEntries');

        const { entryId } = req.params;

        const result = await collection.deleteOne({ _id: new ObjectId(entryId) });

        if (result.deletedCount === 0) {
            return res.status(404).send('Journal entry not found');
        }

        res.status(200).json({ message: "Journal entry deleted successfully" });
    } catch (error) {
        console.error('Error accessing the database', error);
        res.status(500).send('Error accessing the database');
    }
});

module.exports = router;
