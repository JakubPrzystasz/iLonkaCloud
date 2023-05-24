import React from 'react';
import UploadedFile from './UploadedFile';

interface FileListProps {
  files: File[];
}

const FileList: React.FC<FileListProps> = ({ files }) => {
  return (
    <div>
      {files.map((file, index) => (
        <UploadedFile key={index} file={file} />
      ))}
    </div>
  );
};

export default FileList;
