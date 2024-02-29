import './App.css'
import axios from 'axios';
import { useState, useEffect } from 'react';


function App() {

  const [people, setPeople] = useState<any[]>([]);

  useEffect(() => {
    (async () => {
      const res = await axios.get('http://127.0.0.1:8000/api')
      setPeople(res.data)
    })();

    return () => {
      // not really needed here.
    }
  }, [])
  if (people.length == [].length) return <div>Loading...</div>
  else return (
    people.map((person, index) => {
      return <p key={index}>{person.id} {person.name} {person.age}</p>
    })
  )
}

export default App
