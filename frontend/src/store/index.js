import { configureStore } from '@reduxjs/toolkit';

import configs from '../reducers/configsReducer';
import courses from '../reducers/coursesSlice';

const stringMiddleware = () => (next) => (action) => {
    if (typeof action === 'string') {
        return next({type: action})
    }
    return next(action)
};

const store = configureStore({
    reducer: {configs, courses},
    middleware: getDefaultMiddleware => getDefaultMiddleware().concat(stringMiddleware),
    devTools: process.env.NODE_ENV !== 'production',
})

export default store;
