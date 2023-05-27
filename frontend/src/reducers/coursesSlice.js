import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import { useHttp } from "../hooks/http.hook";

const initialState = {
    courses: [],
    coursesLoadingStatus: 'idle',
}

export const fetchCourses = createAsyncThunk(
    'courses/fetchCourses',
    async () => {
        const { request } = useHttp();
        return await request('http://localhost:8000/api/v1/courses/');
    }
)

const coursesSlice = createSlice({
    name: 'courses',
    initialState,
    reducers: {
        lessonCreated: (state, action) => {
            state.lessons = [...state.courses, ...action.payload]
        },
    },
    extraReducers: (builder) => {
        builder
            .addCase(fetchCourses.pending, (state) => {state.coursesLoadingStatus = 'loading'})
            .addCase(fetchCourses.fulfilled, (state, action) => {
                state.coursesLoadingStatus = 'idle';
                state.courses = action.payload
            })
            .addCase(fetchCourses.rejected, state => {
                state.coursesLoadingStatus = 'error';
            })
            .addDefaultCase(() => {})
    }
})

const {actions, reducer} = coursesSlice;

export default reducer;

export const {
    coursesFetching,
    coursesFetched,
    coursesFetchingError,
} = actions;
