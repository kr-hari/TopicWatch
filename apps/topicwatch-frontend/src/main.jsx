import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom'; // 👈 Add this line
import './index.css';
import App from './App.jsx';

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BrowserRouter>           {/* 👈 Wrap App inside this */}
      <App />
    </BrowserRouter>
  </StrictMode>,
);
// This code is the entry point for a React application.
// It uses React's StrictMode for highlighting potential problems in the application.
// The createRoot function from 'react-dom/client' is used to render the application into the DOM.
// The application is wrapped in a BrowserRouter component, which enables routing within the app.
// The './index.css' file is imported for global styles.
// The main App component is imported from './App.jsx' and rendered inside the root element of the HTML document.
// The createRoot function is used to create a root for the React application, and the render method is called to display the App component.
// The StrictMode component is a tool for highlighting potential problems in an application.
// It activates additional checks and warnings for its descendants.
// The BrowserRouter component is used to enable routing in the application, allowing for navigation between different views.
// The App component is the main component of the application, and it is rendered inside the root element with the ID 'root'.
// The code is structured to ensure that the application is rendered correctly and efficiently.
// The use of StrictMode and BrowserRouter helps in maintaining a clean and organized codebase.