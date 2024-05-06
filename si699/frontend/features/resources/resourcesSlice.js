import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import axios from 'axios';

const url = 'http://localhost:3000/assessment';

export const searchByKeywords = createAsyncThunk(
    "resources/searchByKeywords", async (keywords, { rejectWithValue }) => {
        try {
            const res = await axios.get(`${url}/searchByKeywords`, { params: { keywords: keywords } })
            if (res.status === 200) {
                return res.data;
            } else {
                return rejectWithValue('Response status was not 200');
            }
        } catch (error) {
            console.log('searchByKeywords ' + err.message);
            return rejectWithValue(err.response?.data || 'Unknown error');
        }
    })

export const filterByTags = createAsyncThunk(
    "resources/filterByTag", async (tags, { rejectWithValue }) => {
        try {
            const res = await axios.get(`${url}/filterByTags`, { params: { tags: tags } })
            if (res.status === 200) {
                return res.data;
            } else {
                return rejectWithValue('Response status was not 200');
            }
        } catch (error) {
            console.log('filterByTags ' + err.message);
            return rejectWithValue(err.response?.data || 'Unknown error');
        }

    })

export const resourcesSlice = createSlice({
    name: 'resources',
    initialState: { blogs: [] },
    extraReducers: (builder) => {
        builder
            .addCase(searchByKeywords.fulfilled, (state, action) => {
                state.blogs = action.payload;
            })
            .addCase(filterByTags.fulfilled, (state, action) => {
                state.blogs = action.payload;
            })
    }
});