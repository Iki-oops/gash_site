import { Container } from "@mui/material";

import LessonsList from "../../components/coursesList/CoursesList";
import SidebarInfo from "../../components/sidebarInfo/SidebarInfo";

const MainPage = () => {
    return (
        <>
            <div className="grid-70 left-content">
                <LessonsList/>
            </div>
            <SidebarInfo/>
        </>
    )
}

export default MainPage;
