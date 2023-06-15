"use client"
import React from 'react';
import FileList from '../../components/FileList'
import UploadFile from '../../components/UploadFile'


const App = () => {

    const handleLogout = () => {
        // Perform logout logic
        // Example: Clear authentication tokens, session, or user data
    };

    const uploadedFiles: File[] = [
        new File(['file1'], 'file1.jpg'),
        new File(['file2'], 'file2.pdf'),
        new File(['file3'], 'file3.txt'),
    ];

    return (
        <div className="flex justify-center items-center h-screen">
            <div className="w-80vw">
                <div className="container mx-auto py-10">
                    <h1 className="text-2xl font-bold mb-4">File Uploads</h1>
                    <FileList files={uploadedFiles} />
                </div>
                <div className="container mx-auto">
                    <button
                        className="bg-red-500 text-white px-4 py-2 rounded"
                        onClick={handleLogout}>
                        <a href="/">
                            Logout
                        </a>
                    </button>
                    <input type="file" />
                    <button
                        className="bg-green-500 text-white px-4 py-2 rounded"
                        onClick={handleLogout}>
                        <a href="/">
                            Upload
                        </a>
                    </button>
                </div>
            </div>
        </div>
    );
};

export default App;
