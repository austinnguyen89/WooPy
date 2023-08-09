import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Settings = () => {
    const [apiUrl, setApiUrl] = useState('');
    const [apiKey, setApiKey] = useState('');
    const [error, setError] = useState('');
    const [success, setSuccess] = useState('');

    // Function to load existing settings from the backend
    const loadSettings = () => {
        const settingsUrl = '/api/settings'; // Replace with your endpoint

        axios.get(settingsUrl)
            .then((response) => {
                setApiUrl(response.data.apiUrl);
                setApiKey(response.data.apiKey);
            })
            .catch((error) => {
                setError('An error occurred while loading settings');
                console.error(error);
            });
    };

    // Function to save settings to the backend
    const handleSave = () => {
        // Clear previous messages
        setError('');
        setSuccess('');

        // API endpoint for saving settings
        const settingsUrl = '/api/settings'; // Replace with your endpoint

        // Request payload
        const payload = {
            apiUrl: apiUrl,
            apiKey: apiKey,
        };

        // Make a PUT request to save the settings
        axios.put(settingsUrl, payload)
            .then((response) => {
                // Handle successful save
                setSuccess('Settings saved successfully');
            })
            .catch((error) => {
                // Handle request error
                setError('An error occurred while saving settings');
                console.error(error);
            });
    };

    // Load settings when the component mounts
    useEffect(() => {
        loadSettings();
    }, []);

    return (
        <div>
            <input type="text" placeholder="API URL" value={apiUrl} onChange={(e) => setApiUrl(e.target.value)} />
            <input type="text" placeholder="API Key" value={apiKey} onChange={(e) => setApiKey(e.target.value)} />
            <button onClick={handleSave}>Save</button>
            {error && <div className="error">{error}</div>}
            {success && <div className="success">{success}</div>}
        </div>
    );
};

export default Settings;
