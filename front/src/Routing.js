import React from 'react';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import Student from './components/Student';
import Teacher from './components/Teacher';
import App from './App';
import 'bootstrap/dist/css/bootstrap.min.css';

const router = createBrowserRouter([
    {
        path:'/',
        element:<App />
    },
    {
        path:'/Student/:username',
        element:<Student />
    },
    {
        path:'/Teacher/:username',
        element:<Teacher />
    }
]);

const Routing = () => {
    return (
        <div className=''>
            <RouterProvider router={router} />
        </div>
    );
};

export default Routing;
