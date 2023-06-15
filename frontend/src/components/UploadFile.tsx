import React from 'react';

class UploadComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      selectedFile: null,
    };
  }

  handleFileChange = (e) => {
    const file = e.target.files[0];
    this.setState({ selectedFile: file });
  };

  render() {
    const { selectedFile } = this.state;

    return (
      <div>
        <input type="file" onChange={this.handleFileChange} />
        {selectedFile && <p>Selected file: {selectedFile.name}</p>}
      </div>
    );
  }
}

export default UploadComponent;
