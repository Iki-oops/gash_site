import { useEffect } from "react";
import { useDispatch, useSelector } from 'react-redux';

import { fetchCourses } from '../../reducers/coursesSlice'
import LessonPreview from "../coursePreview/CoursePreview"

const LessonsList = () => {
    const { courses, coursesLoadingStatus } = useSelector(state => state.courses)
    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(fetchCourses());
    }, [])

    return (
        <>
            {
                courses.map(({pk, ...props}) => {
                    return <LessonPreview key={pk} {...props}/>
                })
            }
        </>
        
    )
}

export default LessonsList;
