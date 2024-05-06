import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import axios from 'axios';

const baseUrl = 'http://localhost:3000/journal';

export const createJournalEntry = createAsyncThunk(
    'journal/createEntry',
    async (entryData, { rejectWithValue }) => {
        try {
            const response = await axios.post(`${baseUrl}/setJournalEntry`, entryData);
            return response.data; // Assuming the server responds with the created entry
        } catch (error) {
            return rejectWithValue(error.response?.data || 'Could not create entry');
        }
    }
);

export const fetchJournalEntries = createAsyncThunk(
    'journal/fetchEntries',
    async (_, { rejectWithValue }) => {
        try {
            const response = await axios.get(`${baseUrl}/getJournals`);
            return response.data; // Assuming the server responds with an array of entries
        } catch (error) {
            return rejectWithValue(error.response?.data || 'Could not fetch entries');
        }
    }
);


export const fetchSinglelEntry = createAsyncThunk(
    'journal/fetchSingleEntry',
    async (entryId, { rejectWithValue }) => {
        try {
            const response = await axios.get(`${baseUrl}/journalEntry/${entryId}`);
            return response.data;
        } catch (error) {
            if (error.response && error.response.status === 404) {
                return rejectWithValue('Journal entry not found');
            } else {
                return rejectWithValue(error.response?.data || 'An error occurred while fetching the journal entry');
            }
        }
    }
);

export const updateJournalEntry = createAsyncThunk(
    'journal/updateEntry',
    async ({ entryId, ...updateData }, { rejectWithValue }) => { // Include entryId in the destructuring
        try {
            const response = await axios.patch(`${baseUrl}/journalEntry/${entryId}`, updateData);
            return response.data;
        } catch (error) {
            return rejectWithValue(error.response?.data || 'Could not update entry');
        }
    }
);


export const deleteJournalEntry = createAsyncThunk(
    'journal/deleteEntry',
    async (entryId, { rejectWithValue }) => {
        try {
            await axios.delete(`${baseUrl}/journalEntry/${entryId}`);
            return entryId; // Return the id to identify which entry was deleted
        } catch (error) {
            return rejectWithValue(error.response?.data || 'Could not delete entry');
        }
    }
);


const journalSlice = createSlice({
    name: 'journal',
    initialState: {
        entries: [],
        loading: false,
        error: null,
    },
    reducers: {},
    extraReducers: (builder) => {
        builder
            .addCase(createJournalEntry.fulfilled, (state, action) => {
                state.entries.push(action.payload); // Add the new entry to the state
                state.error = null; // Reset any existing errors on success
            })
            .addCase(createJournalEntry.rejected, (state, action) => {
                state.error = action.error.message || 'Failed to create journal entry';
            })
            .addCase(fetchJournalEntries.fulfilled, (state, action) => {
                
                state.entries = action.payload?.map((entry) => ({ ...entry, entryId: entry._id })); // Replace existing entries with fetched ones
                state.error = null; // Reset any existing errors on success
            })
            .addCase(fetchJournalEntries.rejected, (state, action) => {
                state.error = action.error.message || 'Failed to fetch journal entries';
            })
            .addCase(fetchSinglelEntry.fulfilled, (state, action) => {
                state.currentEntry = action.payload;
                state.loading = false;
                state.error = null;
            })
            .addCase(fetchSinglelEntry.rejected, (state, action) => {
                state.loading = false;
                state.error = action.payload;
            })
            .addCase(updateJournalEntry.fulfilled, (state, action) => {
                // Assuming action.payload is the entire updated entry object
                // and you're using `entryId` as the identifier:
                const index = state.entries.findIndex(entry => entry.entryId === action.payload?.updatedEntry?._id);
                if (index !== -1) {
                    // Update the entry in the state with the one returned from the backend
                    state.entries[index] = action.payload.updatedEntry;
                    state.error = null; // Reset any existing errors on success
                }
            })
            .addCase(updateJournalEntry.rejected, (state, action) => {
                state.error = action.error.message || 'Failed to update journal entry';
            })
            .addCase(deleteJournalEntry.fulfilled, (state, action) => {
                state.entries = state.entries.filter(entry => entry.entryId !== action.payload); // Remove the deleted entry from the state
            });
    },
});

export default journalSlice.reducer;
