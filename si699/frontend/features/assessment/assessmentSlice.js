import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import axios from 'axios';

const url = 'http://localhost:3000/assessment';
const uid = '1';

export const setAnswer = createAsyncThunk(
    "assessment/setAnswer",
    async ({ question, answer }, { rejectWithValue }) => {
        try {
            const res = await axios.post(`${url}/setAnswer`, { uid, question, answer });

            if (res.status === 200) {
                return { question, answer };
            } else {
                return rejectWithValue('Response status was not 200');
            }
        } catch (err) {
            console.log('setAnswer ' + err.message);
            return rejectWithValue(err.response?.data || 'Unknown error');
        }
    }
);

export const getAssessment = createAsyncThunk(
    "assessment/getAssessment",
    async (_, { rejectWithValue }) => {
        try {
            const res = await axios.get(`${url}/getAssessment/${uid}`);
            return res.data;
        } catch (err) {
            console.log('getAssessment ' + err.message);
            return rejectWithValue(err.response?.data || 'Unknown error');
        }
    }
);

export const assessmentSlice = createSlice({
    name: 'assessment',
    initialState: {},
    extraReducers: (builder) => {
        builder
            .addCase(setAnswer.fulfilled, (state, action) => {
                const { question, answer } = action.payload;
                state[question] = answer;
            })
            .addCase(getAssessment.fulfilled, (state, action) => {
                Object.assign(state, action.payload); // Correctly mutates the state
            })            
    }
});

export default assessmentSlice.reducer;
