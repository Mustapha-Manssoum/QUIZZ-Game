
import React, { useState } from "react";


const themes = ["History", "Geography", "Sports"];

export const ChooseThemes = (props) => {
  const [selectedThemes, setSelectedThemes] = useState([]);

  const handleChange = (e) => {
    const theme = e.target.value;
    if (selectedThemes.includes(theme)) {
      setSelectedThemes(selectedThemes.filter((t) => t !== theme));
    } else {
      setSelectedThemes([selectedThemes, theme]);
    }
  };

  return (
    <div>
      <header className="App-header" style={{display: 'flex', alignItems: 'center'}}>
        
      </header>
      <h3>Choose Themes for Your Quiz</h3>
      {themes.map((theme) => (
        <div key={theme}>
          <input
            type="checkbox"
            value={theme}
            onChange={handleChange}
            checked={selectedThemes.includes(theme)}
          />
          <label>{theme}</label>
        </div>
      )
      )}
      <button type="submit" onClick={() => props.onFormSwitch('Login')}>Start Quiz</button>
    </div>
  );
};

export default ChooseThemes;