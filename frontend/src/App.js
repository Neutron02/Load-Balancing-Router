import React from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Link, Routes} from 'react-router-dom';
import Performance from './Performance';
const imageUrl = process.env.PUBLIC_URL + '/peepocry.png'; // Assuming the image is in the public folder

const HomePage = () => {
  return (
    <div className="container">
      <h1 className="title">Welcome to Frontend For The Router</h1>
    </div>
  );
};

function App() {
  return (
      <div className="container">
        <header className="header">
          <nav className="navbar">
            <Link to="/Home">Home</Link>
            <Link to="/Home/Performance">Performance</Link>
          </nav>
        </header>
        <Routes>
          <Route path="/Home" exact Component={HomePage} /> 
          <Route path="/Home/Performance" element={<Performance />} />
          {/* Catch all path */}
          <Route path="*" element={
            <div>
              <h1>Well you've navigated to the middle of nowhere</h1>
              <img src={imageUrl}></img>
            </div>
          } />
        </Routes>
      </div>
  );
}

export default App;
