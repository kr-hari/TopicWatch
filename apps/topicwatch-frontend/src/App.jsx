import { Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Auth from './pages/Auth';
import NotFound from './pages/NotFound'; 

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/auth" element={<Auth />} />
      <Route path="*" element={<NotFound />} /> {/* 👈 catch-all route */}
    </Routes>
  );
}

export default App;


// This code is a simple React application that uses React Router for navigation.     