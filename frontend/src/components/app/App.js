import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Provider } from 'react-redux';

import store from '../../store';
import MainPage from '../../pages/MainPage/MainPage';
import { Container } from "@mui/material";
import Lessons from "../coursesList/CoursesList";
import './App.scss';

function App() {
    return (
        <Router>
            <div className="app">
                <Provider store={store}>
                    <Container maxWidth='lg'>
                        <Routes>
                            <Route path="/" exact element={<MainPage/>}/>
                            <Route path="/category/:category_id" exact element={<MainPage/>}/>
                            <Route path="/lessons/:lesson_id" exact element={<MainPage/>}/>
                        </Routes>
                    </Container>
                </Provider>
            </div>
        </Router>
    );
}

export default App;
