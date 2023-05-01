import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [userInput, setUserInput] = useState({
    age: 0,
    height: 0,
    weight: 0,
    intenseDays: 0,
    intenseMinutes: 0,
    moderateDays: 0,
    moderateMinutes: 0,
  });

  const [workout, setWorkout] = useState(null);

  const handleChange = (e) => {
    setUserInput({ ...userInput, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post("http://127.0.0.1:5000/recommend", userInput);

      setWorkout(response.data);
    } catch (error) {
      console.error("Error fetching workout data:", error);
    }
  };
  
  return (
    <div className="App">
      <h1>SwolFit</h1>
      {!workout && (
        <form onSubmit={handleSubmit}>
          <label>
            Age:
            <input type="number" name="age" min="0" max="100" value={userInput.age} onChange={handleChange} />
          </label>
          <label>
            Height (cm):
            <input type="number" name="height" min = "1" step="0.1" value={userInput.height} onChange={handleChange} />
          </label>
          <label>
            Weight (kg):
            <input type="number" name="weight" min = "1" step="0.1" value={userInput.weight} onChange={handleChange} />
          </label>
          <label>
            Intense minutes:
            <input type="number" name="intenseMinutes" min="0" max="300" value={userInput.intenseMinutes} onChange={handleChange} />
          </label>
          <label>
          Intense days:
            <input type="number" name="intenseDays" min="0" max="7" value={userInput.intenseDays} onChange={handleChange} />
          </label>
          <label>
          Moderate minutes:
            <input type="number" name="moderateMinutes" min="0" max="300" value={userInput.moderateMinutes} onChange={handleChange} />
          </label>
          <label>
          Moderate days:
            <input type="number" name="moderateDays" min="0" max="7" value={userInput.moderateDays} onChange={handleChange} />
          </label>
          <button type="submit">Submit</button>
        </form>
      )}

{workout && (
  <div className="workout-container">
    <h2>Recommended Workout Plan</h2>
    {workout.workout_description.split("Day").map((day, index) => {
      if (index === 0) return null; // skip the empty string before the first "Day"
      const dayContent = `Day${day}`;
      return (
        <div key={index} className="workout-container">
          <pre>{dayContent}</pre>
        </div>
      );
    })}
  </div>
)}
    </div>
  );
}

export default App;
