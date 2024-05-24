import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import './Teacher.css'
const Teacher = () => {
    const [TeacherInfo, setTeacherInfo] = useState(null);
    const { username } = useParams();

    useEffect(() => {
        const fetchStudentInfo = async () => {
            try {
                const authTokens = localStorage.getItem("authTokens");
                
                if (authTokens) {
                
                    const response = await fetch(`http://127.0.0.1:8000/api/TeacherInfo/${username}`, {
                        method: "GET",
                        headers: {
                            "Content-Type": "application/json",
                        
                        },
                    });
                    const data = await response.json();
                
                    if (response.ok) {
                        setTeacherInfo(data);
                        console.log(TeacherInfo)
                    } else {
                        console.error("Failed to fetch student info:", response.statusText);
                    }
                } else {
                    console.error("Authentication token not found.");
                }
            } catch (error) {
                console.error("An error occurred during fetch:", error);
            }
        };

        fetchStudentInfo();
    }, [username]); 
    console.log(TeacherInfo);


    return (
        <div className='Teacher'>
            <div className='teacherInfo'> 
        {TeacherInfo ? (
            <div>
                <h1 style={{ marginLeft:'100px'}}>Respected {TeacherInfo.teacher.name}</h1>
                <hr style={{width:'1000px' , marginLeft:'100px'}}></hr>
                <h5 style={{ marginLeft:'100px'}}>Your Material: 
                            {TeacherInfo.file_url ? (
                                <a href={TeacherInfo.file_url} download style={{ marginLeft: '10px' }}>
                                    TATA Material
                                </a>
                            ) : (
                                "No file available"
                            )}</h5>
                {TeacherInfo.courses.map(courseData => (
                    <div key={courseData.course.id}>
                        <h5 style={{ marginLeft:'100px'}}>Your Course : {courseData.course.name}</h5>
                        <h5 style={{ marginLeft:'100px'}}>Your Students:</h5>
                        <ul >
                            {courseData.students.map(student => (
                                <li style={{ marginLeft:'100px'}} key={student}><h5>{student}</h5></li>
                            ))}
                        </ul>
                    </div>
                ))}
            </div>
        ) : (
            <p>Loading teacher information...</p>
        )}
    </div>
    </div>
    );
};

export default Teacher;
