import React, { useState } from 'react';
import { Form, Button, Container, Row, Col } from 'react-bootstrap'; // Importing Bootstrap components for styling

const Settings = () => {
    // State variables to hold the WooCommerce API Key and Secret
    const [apiKey, setApiKey] = useState('');
    const [apiSecret, setApiSecret] = useState('');

    // Function to handle saving settings
    const handleSave = () => {
        // Logic to save settings to the database
        // This part is currently empty and needs to be implemented
    };

    return (
        <Container className="settings-page"> {/* Container to center-align the form */}
            <Row className="justify-content-center"> {/* Row to create a responsive layout */}
                <Col md={6}> {/* Column to set the form width */}
                    <h1>Settings</h1>
                    <Form onSubmit={handleSave}> {/* Form component */}
                        <Form.Group controlId="apiKey">
                            <Form.Label>WooCommerce API Key:</Form.Label>
                            <Form.Control
                                type="text"
                                value={apiKey}
                                onChange={(e) => setApiKey(e.target.value)} // Updating the API Key state
                            />
                        </Form.Group>
                        <Form.Group controlId="apiSecret">
                            <Form.Label>WooCommerce API Secret:</Form.Label>
                            <Form.Control
                                type="text"
                                value={apiSecret}
                                onChange={(e) => setApiSecret(e.target.value)} // Updating the API Secret state
                            />
                        </Form.Group>
                        <Button variant="primary" type="submit"> {/* Button to submit the form */}
                            Save
                        </Button>
                    </Form>
                </Col>
            </Row>
        </Container>
    );
};

export default Settings;
