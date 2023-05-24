"use client"

import React, { useState } from 'react';

const UploadPage = () => {
    const [file, setFile] = useState<File | null>(null);

    const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const selectedFile = e.target.files && e.target.files[0];
        setFile(selectedFile);
    };

    const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        if (file) {
            // Handle file upload
            console.log(file);
        }
    };

    return (
        <div className="flex justify-center items-center h-screen">
            <div className="w-80vw">
                <div className="container mx-auto py-10">
                    <h1 className="text-2xl font-bold mb-4">Upload File</h1>
                    <form onSubmit={handleSubmit}>
                        <div className="mb-4">
                            <label htmlFor="file" className="block font-semibold mb-1">
                                Select a file:
                            </label>
                            <input
                                type="file"
                                id="file"
                                onChange={handleFileChange}
                                className="w-full px-4 py-2 border border-gray-300 rounded"
                            />
                        </div>
                        <button
                            type="submit"
                            className="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded"
                        >
                            Upload
                        </button>
                    </form>
                </div>
            </div>
        </div>
    );
};

export default UploadPage;
