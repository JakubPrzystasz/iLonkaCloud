import React from 'react';

interface UploadedFileProps {
  file: File;
}

const UploadedFile: React.FC<UploadedFileProps> = ({ file }) => {
  const formattedSize = (size: number) => {
    const kb = 1024;
    const mb = kb * 1024;
    const gb = mb * 1024;

    if (size >= gb) {
      return `${(size / gb).toFixed(2)} GB`;
    } else if (size >= mb) {
      return `${(size / mb).toFixed(2)} MB`;
    } else if (size >= kb) {
      return `${(size / kb).toFixed(2)} KB`;
    } else {
      return `${size} bytes`;
    }
  };

  const formattedUploadDate = (date: Date) => {
    return date.toLocaleString();
  };

  return (
    <div className="flex items-center py-2">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        className="h-6 w-6 mr-2"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth={2}
          d="M5 13l4 4L19 7"
        />
      </svg>
      <div className="flex-grow truncate">
        <p>{file.name}</p>
        <p className="text-gray-500 text-sm">
          Size: {formattedSize(file.size)}
        </p>
        <p className="text-gray-500 text-sm">
          Uploaded on: {formattedUploadDate(new Date(file.lastModified))}
        </p>
      </div>
    </div>
  );
};

export default UploadedFile;
