import React, { useState } from 'react';

const Settings = () => {
    const [apiKey, setApiKey] = useState('');
    const [apiSecret, setApiSecret] = useState('');

    const handleSave = () => {
        // Logic to save settings to the database
    };

    return (
        <div className="settings-page">
            <h1>Settings</h1>
            <form onSubmit={handleSave}>
                <label>WooCommerce API Key:</label>
                <input type="text" value={apiKey} onChange={(e) => setApiKey(e.target.value)} />
                <label>WooCommerce API Secret:</label>
                <input type="text" value={apiSecret} onChange={(e) => setApiSecret(e.target.value)} />
                <button type="submit">Save</button>
            </form>
        </div>
    );
};

export default Settings;
