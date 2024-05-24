import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import './Student.css'
const Student = () => {
    const [studentInfo, setStudentInfo] = useState(null);
    const { username } = useParams();

    useEffect(() => {
        const fetchStudentInfo = async () => {
            try {
                const authTokens = localStorage.getItem("authTokens");
                
                if (authTokens) {
                
                    const response = await fetch(`http://127.0.0.1:8000/api/StudentInfo/${username}`, {
                        method: "GET",
                        headers: {
                            "Content-Type": "application/json",
                        
                        },
                    });
                    const data = await response.json();
                
                    if (response.ok) {
                        setStudentInfo(data);
                        console.log(studentInfo)
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
    console.log(studentInfo);



    return (
        <div className='Student'>
            <div className='studentInfo'>
            {studentInfo ? (
                <div>
                    <h1 style={{ marginLeft:'100px'}}> Dear {studentInfo.student.name}</h1>
                    <hr style={{width:'1000px' , marginLeft:'100px'}}></hr>
                    <h5 style={{ marginLeft:'100px'}}> Your Assigned course :  {studentInfo.courses}</h5>
                
                </div>
            ) : (
                <p>Loading student information...</p>
            )}
        </div>
        </div>
    );
};

export default Student;
